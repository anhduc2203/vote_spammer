import os
import signal
import subprocess

class Proxy:
    process = None

    def start_proxy(self):
        cmd =  ["tor"]
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

