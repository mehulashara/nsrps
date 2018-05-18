Linux nsps.zip - Contains executable for linux with shell script to run the executable. 

Executable has logging to a new file /nsr/logs/nsrps.log

#Sample output:

05/18/2018 05:42:23 PM PID 26170 is using CPU%: 0.0 MEM%: 0.2 nsrexecd
05/18/2018 05:42:23 PM PID 26192 is using CPU%: 0.0 MEM%: 0.0 nsrctld
05/18/2018 05:42:23 PM PID 26300 is using CPU%: 0.0 MEM%: 12.3 nsrd
05/18/2018 05:42:23 PM PID 26455 is using CPU%: 0.0 MEM%: 0.0 nsrlogd
05/18/2018 05:42:23 PM PID 26479 is using CPU%: 0.0 MEM%: 0.1 nsrmmdbd
05/18/2018 05:42:23 PM PID 26485 is using CPU%: 0.0 MEM%: 0.0 nsrindexd
05/18/2018 05:42:23 PM PID 26502 is using CPU%: 0.0 MEM%: 0.0 nsrdispd
05/18/2018 05:42:23 PM PID 26512 is using CPU%: 0.0 MEM%: 0.2 nsrjobd
05/18/2018 05:42:23 PM PID 26588 is using CPU%: 0.0 MEM%: 0.0 nsrvmwsd
05/18/2018 05:42:23 PM PID 26599 is using CPU%: 0.0 MEM%: 0.1 nsrsnmd

Program will check for:

  if proc.name() == "nsrd" or proc.name() == "nsrsnmd" or proc.name() == "nsrctld" or proc.name() == "nsrindexd" or proc.name() == "nsrmmdbd" or proc.name() == "nsrdispd" or proc.name() == "nsrlogd" or proc.name() == "nsrvmwsd" or proc.name() == "nsrjobd" or proc.name() == "nsrexecd" or proc.name() == "nsrvproxy_save" or proc.name() == "nsrdisp_nwbg" or proc.name() == "nsrlmc" or proc.name() == "nsrclone" or proc.name == "nsrrecopy" or proc.name == "nsrworkflow" or proc.name == "nsrvproxy_save" or proc.name == "nsrvproxy_recover":

# more processes can be added

Windows file does not have logging at moment:

C:\Users\Administrator\Desktop\scripts\win2>python nsrps_win.py
05/18/2018 07:16:06 PM PID 1876 is using CPU%: 0.0 MEM%: 0.4 nsrexecd.exe
05/18/2018 07:16:06 PM PID 2664 is using CPU%: 0.0 MEM%: 0.2 nsrctld.exe
05/18/2018 07:16:06 PM PID 2916 is using CPU%: 0.0 MEM%: 0.6 nsrd.exe
05/18/2018 07:16:06 PM PID 4496 is using CPU%: 0.0 MEM%: 0.5 nsrmmdbd.exe
05/18/2018 07:16:06 PM PID 4580 is using CPU%: 0.0 MEM%: 0.2 nsrindexd.exe
05/18/2018 07:16:06 PM PID 4764 is using CPU%: 0.0 MEM%: 0.6 nsrjobd.exe
05/18/2018 07:16:06 PM PID 4816 is using CPU%: 0.0 MEM%: 0.3 nsrdisp_nwbg.exe
05/18/2018 07:16:06 PM PID 4828 is using CPU%: 0.0 MEM%: 0.2 nsrlogd.exe
05/18/2018 07:16:06 PM PID 4860 is using CPU%: 0.0 MEM%: 0.6 nsrsnmd.exe
05/18/2018 07:16:06 PM PID 4948 is using CPU%: 0.0 MEM%: 0.3 nsrvmwsd.exe
