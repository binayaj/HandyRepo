import os
import time,datetime
path="/var/"
for dir,subdir,file in os.walk (path):
   modified=os.path.getmtime(dir)
   print ("Modified on ", time.strftime('%m/%d/%Y', time.gmtime (modified)))
#accessed=os.path.getatime(file)
print ("Modified on this ", time.strftime('%m/%d/%Y', time.gmtime (modified)))
#print ("Accessed on ", time.strftime('%m/%d/%Y', time.gmtime (accessed)))
