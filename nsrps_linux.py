#!/usr/bin/env python
import psutil,sys,datetime,time,resource,subprocess
from subprocess import call
def main():
	orig_stdout = sys.stdout
	f= open('/nsr/logs/nsrps.log','a+')
	sys.stdout = f
	templ = "%-10s %5s %10s  %10s"
	attrs = ['name', 'pid', 'memory_percent', 'cpu_percent']
	#print(templ % ("PID", "%CPU", "%MEM", "NAME"))
	localtime = datetime.datetime.today().strftime('%m/%d/%Y %I:%M:%S %p')
	array = []
	for proc in psutil.process_iter():
    	 try:
          pinfo = proc.as_dict(attrs, ad_value='')
    	 except psutil.NoSuchProcess:
         	pass
         else:
	   if proc.name() == "nsrd" or proc.name() == "nsrsnmd" or proc.name() == "nsrctld" or proc.name() == "nsrindexd" or proc.name() == "nsrmmdbd" or proc.name() == "nsrdispd" or proc.name() == "nsrlogd" or proc.name() == "nsrvmwsd" or proc.name() == "nsrjobd" or proc.name() == "nsrexecd" or proc.name() == "nsrvproxy_save" or proc.name() == "nsrdisp_nwbg" or proc.name() == "nsrlmc" or proc.name() == "nsrclone" or proc.name == "nsrrecopy" or proc.name == "nsrworkflow" or proc.name == "nsrvproxy_save" or proc.name == "nsrvproxy_recover": 
        	#print pinfo
		memp = pinfo['memory_percent'] and round(pinfo['memory_percent'], 1)
		array.append( pinfo['pid'])
		array.append(pinfo['cpu_percent'])
		array.append(memp)
		array.append(pinfo['name'])
		#print templ % (pinfo['pid'], pinfo['cpu_percent'], memp, pinfo['name'].strip() or '?')
	
	for i in range(0, len(array)):
		#if (i == 0 or i==4 or i==8 or i==12 or i==16 ):	print localtime,
		#if  ( i % 4 == 3 ):   print pid[i]
		if ( i % 4 == 0 ):	print localtime,"PID", array[i],
		else:
		 if ( i % 4 == 1 ):	print "is using CPU%:", array[i],
		 else:
        		if  ( i % 4 == 2 ):	print "MEM%:", array[i],
			else:
        		 if  ( i % 4 == 3 ):   print array[i]
	#%% Set the maximum size (in bytes) of a core file that the current process can create to unlimited
	resource.setrlimit(resource.RLIMIT_CORE,(resource.RLIM_INFINITY, resource.RLIM_INFINITY))
	#print localtime, "Please run command: ulimit -c unlimited which is recommended for proper generation of core files"
	sys.stdout = orig_stdout
	f.close()

if __name__ == '__main__':
    main()
