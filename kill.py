def kill_all():
	for proc in psutil.process_iter(['pid', 'name', 'username']):
	    try:
	        if((proc.info['username'] == None)): #If username is None then process will not be Killed
	            print('skipped :',proc.info['pid'])
	        elif((proc.info['name'] == None)):# Ignore this one
	            print('skipped :',proc.info['pid'])
	        elif('conhost.exe' in proc.info['name']):# Important file for windows
	            print('skipped 2 :',proc.info['pid'])
	        elif('python.exe' in proc.info['name']):# Python is Important
	            print('skipped 2 :',proc.info['pid'])
	        elif('cmd.exe' in proc.info['name']):# Running this script on what?
	            print('skipped 2 :',proc.info['pid'])	            
	        elif(psutil.users()[0][0] not in proc.info['username']):# Ignore this one too
	            print('skipped :',proc.info['pid'])
	        else:
	            print(proc.info)
	            print('killed')
	            proc.kill()
	    except Exception as e:
	            print(e)
	            pass
kill_all()
