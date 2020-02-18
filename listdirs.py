# Gets timestamp of all sub directories

import os,sys
import time,datetime
if ( (len (sys.argv)==2) and os.path.isdir(sys.argv[1])):
    filename="/tmp/"+str(time.time()).split(".")[0]+".csv"
    if not os.path.exists (filename):
        with open (filename,'w') as fp:
         for dir,subdir,file in os.walk (sys.argv[1]):
             modified=os.path.getmtime(dir)
             fp.write ('{0},{1}\n '.format(dir,time.strftime('%m/%d/%Y', time.gmtime (modified) ) )) 
         fp.close()
    else:

           print ("Output file already exists")
else:
   print ("Usage: listdir.py dirname")
print ("Results saved to {}".format(filename))
