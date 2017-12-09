import os
import signal
import subprocess

class Proxy:
    process = None
    conf = None
    
    def __init__(self):
        my_dir = os.path.dirname(__file__)
        self.conf = os.path.join(my_dir, '../.torrc')

    def start_proxy(self):
        cmd =  'tor -f ' + self.conf
        self.process = subprocess.Popen(cmd,
                    stdout=subprocess.PIPE,
                    universal_newlines=True,
                    shell=True,
                    preexec_fn=os.setsid
                )
        for stdout_line in iter(self.process.stdout.readline, ""):
            yield stdout_line
        self.process.stdout.close()
        return_code = self.process.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)

    def kill_proxy(self):
        os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
    
    def init_conf(self):
        f = open(self.conf, 'w')
        f.write('ExcludeExitNodes ')
        f.close()

    def block_node(self, node, purge=False):
        if not os.path.exists(self.conf):
            self.init_conf()
        f = open(self.conf, 'a')
        f.write(node)
        f.write(", ")
        f.close()
    
    def purge_blocked_nodes(self):
        self.init_conf()
