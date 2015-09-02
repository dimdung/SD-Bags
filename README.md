# Steps to Clone  Repos
Step # 1 - Create folder name called 'htech-project' and CD into 'htech-project'
[sdimdung@htech007 ~]$ mkdir htech-project
[sdimdung@htech007 ~]$ cd htech-project/
[sdimdung@htech007 htech-project]$ ls
Step # 2 - Run ' git init' 
[sdimdung@htech007 htech-project]$ git init
Initialized htech007 Git repository in /home/sdimdung/htech-project/.git/
Step # 3 - Run the 'git clone' command alone with the  following url:
[sdimdung@htech007 htech-project]$ git clone https://github.com/dimdung/htech2015-master.git
Initialized empty Git repository in /home/sdimdung/htech-project/htech2015-master/.git/
remote: Counting objects: 31, done.
remote: Compressing objects: 100% (25/25), done.
remote: Total 31 (delta 4), reused 15 (delta 1), pack-reused 0
Unpacking objects: 100% (31/31), done.
[sdimdung@htech007 htech-project]$ 
Step # 4 - do the ' ls -l or ll' to dispay cloned repos locally 
[sdimdung@sshjump htech-project]$ ll
total 4
drwx------. 5 sdimdung sdimdung 4096 Sep  2 00:15 htech2015-master
[sdimdung@htech007 htech-project]$ cd htech2015-master/
[sdimdung@htech007 htech2015-master]$ ll
total 12
drwx------. 2 sdimdung sdimdung 4096 Sep  2 00:15 ansible-playbook
drwx------. 3 sdimdung sdimdung 4096 Sep  2 00:15 aws-training
-rw-------. 1 sdimdung sdimdung   90 Sep  2 00:15 README.md
