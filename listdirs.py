import os
import time,datetime

for dir,subdir,file in os.walk (path):
   modified=os.path.getmtime(dir)
   print ("Modified on ", time.strftime('%m/%d/%Y', time.gmtime (modified)))
