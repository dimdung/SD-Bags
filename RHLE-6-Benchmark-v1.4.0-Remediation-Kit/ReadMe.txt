This archive contains a shell script for configuring Red Hat Enterprise Linux 6 according to the CIS Benchmark.  It was tested against the CIS Red Hat Enterprise Linux 6 Benchmark v1.4.0 as assessed by CIS-CAT v3.0.15.

To execute the script pass a single parameter for the profile desired:

# sh CIS_Red_Hat_Enterprise_Linux_6_Benchmark_v1.4.0.sh "Level 1"

or 

# sh CIS_Red_Hat_Enterprise_Linux_6_Benchmark_v1.4.0.sh "Level 2"

If no parameter is passed the script will default to "Level 1".



In addition to non cis-cat assessed items, the following are not configured by this script:

1.1.1, 1.1.5, 1.1.6, 1.1.7, 1.1.8, 1.1.9: Partioning is not modified, mount options will be set if partition exists.

1.4.1, 1.4.2, 1.4.3: Modification of SELinux settings can prevent system boot, should be completed manually.

1.4.6: Investigation and remediation must be completed manually

1.5.3: Bootloader password must be set by end user.

3.6: NTP server must be set by end user.

3.16: Remediation depends on MTA in use.

5.1.4: Automated parsing of rsyslog.conf can falsely identify non-logfiles for remediation, should be completed manually.

5.1.5: Remote log server must be set by end user.

6.2.13: SSH Access limits must be set by end user.

9.1.11, 9.1.12: Apropriate user/group must be set by end user.

9.2.1: Appropriate password must be set by end user.

9.2.5: Proper UID 0 account may have been remnamed, should be completed manually.

9.2.6: root PATH must be set by end user.

9.2.7, 9.2.8, 9.2.9, 9.2.10: User file/folder permissions/existence should be updated manually.

9.2.11: Groups should be deleted from passwd or added to group by end user.

9.2.12: Proper home directories must be assigned by end user.

9.2.13: Directory ownership should be updated manually.

9.2.14, 9.2.15: Duplicate IDs must be remediated by end user.

9.2.16, 9.2.17: Duplicate names must be remediated by end user.

9.2.18, 9.2.19: User file/folder permissions/existence should be updated manually.