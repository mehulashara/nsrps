#!/usr/bin/env python
import psutil,sys,datetime,time
def main():
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
			if proc.name() == "nsrd.exe" or proc.name() == "nsrsnmd.exe" or proc.name() == "nsrctld.exe" or proc.name() == "nsrindexd.exe" or proc.name() == "nsrmmdbd.exe" or proc.name == "nsrdispd.exe" or proc.name() == "nsrlogd.exe" or proc.name() == "nsrvmwsd.exe" or proc.name() == "nsrjobd.exe" or proc.name() == "nsrexecd.exe" or  proc.name() == "nsrvproxy_save" or proc.name() == "nsrdisp_nwbg.exe" or proc.name() == "nsrlmc" or proc.name() == "nsrclone.exe" or proc.name == "nsrrecopy.exe" or proc.name == "nsrworkflow.exe" or proc.name == "nsrvproxy_save.exe" or proc.name == "nsrvproxy_recover.exe":
#				print(pinfo)
				memp = pinfo['memory_percent'] and round(pinfo['memory_percent'], 1)
				array.append( pinfo['pid'])
				array.append(pinfo['cpu_percent'])
				array.append(memp)
				array.append(pinfo['name'])
				#print templ % ( pinfo['pid'], pinfo['cpu_percent'], memp, pinfo['name'].strip() or '?' )
	
	for i in range(0, len(array)):
		if ( i % 4 == 0 ):	
			print (localtime, "PID", array[i], end =" ")
		else:
			if ( i % 4 == 1 ):	print ("is using CPU%:", array[i], end =" ")
			else:
				if ( i % 4 == 2 ): print ("MEM%:", array[i], end =" ")
				else:
					if  ( i % 4 == 3 ): print (array[i])
				 
if __name__ == '__main__':
	main()