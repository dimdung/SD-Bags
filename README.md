<html>
<boyd>
# Steps to Clone  Repos <br> 
<h3>Step # 1 - Create folder name called 'htech-project' and CD into 'htech-project' <br> </h3>
[sdimdung@htech007 ~]$ mkdir htech-project <br>
[sdimdung@htech007 ~]$ cd htech-project/ <br>
[sdimdung@htech007 htech-project]$ ls <br>
<h3>Step # 2 - Run ' git init' <br> </h3>
[sdimdung@htech007 htech-project]$ git init <br>
Initialized htech007 Git repository in /home/sdimdung/htech-project/.git/<br>
<h3>Step # 3 - Run the 'git clone' command alone with the  following url: </h3><br>
[sdimdung@htech007 htech-project]$ git clone https://github.com/dimdung/htech2015-master.git<br>
Initialized empty Git repository in /home/sdimdung/htech-project/htech2015-master/.git/<br>
remote: Counting objects: 31, done.<br>
remote: Compressing objects: 100% (25/25), done.<br>
remote: Total 31 (delta 4), reused 15 (delta 1), pack-reused 0<br>
Unpacking objects: 100% (31/31), done.<br>
[sdimdung@htech007 htech-project]$ <br>
<h3>Step # 4 - do the ' ls -l or ll' to dispay cloned repos locally </h3><br>
[sdimdung@sshjump htech-project]$ ll<br>
total 4<br>
drwx------. 5 sdimdung sdimdung 4096 Sep  2 00:15 htech2015-master<br>
[sdimdung@htech007 htech-project]$ cd htech2015-master/<br>
[sdimdung@htech007 htech2015-master]$ ll<br>
total 12<br>
drwx------. 2 sdimdung sdimdung 4096 Sep  2 00:15 ansible-playbook<br>
drwx------. 3 sdimdung sdimdung 4096 Sep  2 00:15 aws-training<br>
-rw-------. 1 sdimdung sdimdung   90 Sep  2 00:15 README.md<br>

</body>
</html>
