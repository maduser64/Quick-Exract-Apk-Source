#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      SHarsha
#
# Created:     12-07-2015
# Copyright:   (c) SHarsha 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import subprocess

def main():
    #cmd = "java -jar E:/Blogs/Secure_apk/QuickExtractApkSource/tools/fernflower.jar E:/Blogs/Secure_apk/QuickExtractApkSource/output/jar/classes.jar E:/Blogs/Secure_apk/QuickExtractApkSource/output/decompiledByfernflower/"
    cmd = "java -version"
    #msg = subprocess.check_output(cmd, shell = True)
    os.system(cmd)

    FNULL = open(os.devnull, 'w')
    msg = subprocess.check_output(cmd,shell=True)
    print "check this: ",  type(msg)
    #subprocess.call(cmd,stdout=FNULL,stderr=subprocess.STDOUT,shell=True)

if __name__ == '__main__':
    main()
