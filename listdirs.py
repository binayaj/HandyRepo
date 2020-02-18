import os,sys
import time,datetime
if ( (len (sys.argv)==2) and os.path.isdir(sys.argv[1])):
    for dir,subdir,file in os.walk (sys.argv[1]):
        modified=os.path.getmtime(dir)
        print ('{0},{1} '.format(dir,time.strftime('%m/%d/%Y', time.gmtime (modified) ) )) 
else:
   print ("Usage: listdir.py dirname")
