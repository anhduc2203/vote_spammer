# vote_spammer

### What are you spamming?

* Without being too specific, my friend entered a competition, and moving on to the next stage would require them to be in the top 100 contestants.
* Their rank was determined by number of "votes" for their entry. At the time of writing, there are ~4, 000 contestants.
* Every vote is electronic (through a web form)
* Every vote is counted per IP Address, and is limited to 1 vote per day per IP address. 
* Changing IPs _should_ get us another vote in the same day _(spoiler: it does)_

### Why
* I wanted to see if I can find a way to break the voting system
* I didn't want to study for my finals

### The Goal
* Currently spot #1 belongs to a dude with ~19,000 votes. There's no way to beat that without a juicy botnet. (I have a hard time believing most of those votes are legit)
* The mark to beat is 2300 votes since that's contestant 100's count

### How? 
* We're setting up a SOCKS5 proxy via Tor and rotating keys for every request. 
* This is extremely unethical since bogs down the entire chain. 
* It's also kinda slow

### Is achieving the goal possible? 
* It's extremely unlikely.
* Contest ends on the 17th, we entered on the 8th ==> 9 days to top 2000 votes
* 2000/9  ==> ~223 votes per day to even stand a chance at cracking top spot 
* We also need to consider that every day we will see a rise in other contestant's votes

### Is it worth it? 
* I successfully procrastinated for 5 hours, so yeah, pretty darn worth it 
* I also got the script to work, which is cool too

## Updates:

#### Update 1: Dec 21, 2017
* Turns out the contest closes on the 24th, so we have extra time to spam!
* We successfully reached the goal of 2000 votes, and surpassed it by an insane margin. 
* Currently sitting at 4300+ votes
* We managed to get our contestant into the top 100 as well! Great success

#### Update 2: Dec 22, 2017
* Late night slammin through some code, snow gently burrying this quiet town, black sabbath blaring full blast through the headphones
* It seems I've reached a sort of "soft limit" 
* The rate at which I'm spamming votes seems to match my competition's 
* This means that the usual amount of daily spam does not advance our spot! It only keeps us from falling behind! 
* Luckily for us, this limit is in the sweet range of spots 90-100 
* For the last two days I go to bed with spot 94 in my grasp and wake up with spot 100 sliming its way into my life again 
* I'm extremely happy to say I surpassed my goal by an incredibly large margin (likely due to beyond-poor estimates)

#### Update 3: Jan 5, 2018
* I waited until the new year to post this update so that I can include the status of our contestant
* I was able to setup openvpn with PrivateInternetAccess and get whole new load of IPS 
* The new system was able to push past the soft limit 
* Contestant finished in the top ~80 (vague in order to discourage doxxing) 
* Unfortunately, the organizers did not feel the submission was worthy of the next round

### Final Thoughts
* The spammer worked as planned, and I'm super happy with the results
* We successfully beat 4000+ other contestants! 
* It's still pretty unethical ¯\_(ツ)_/¯
