# global imports
import sys
import os
import datetime
import shutil
import zipfile
import subprocess

# local imports


'''
todo : change in command for OS X
'''
class QuickExtract:
    def __init__(self,rootPath):
        print "object created!"

        self.rootFol = rootPath
        self.apkFol = self.rootFol + "/apk"
        self.archive = self.rootFol + "/archives"
        self.mainFol = self.rootFol + "/main"
        self.outputFol = self.rootFol + "/output"
        self.toolsFol = self.rootFol + "/tools"
        self.filesFol = self.rootFol + "/main/files"
        self.tmpFol = self.rootFol + "/main/tmp"
        self.unZipped = self.rootFol + "/main/tmp/unZipped"
        self.dex2jar = self.rootFol + "/main/tmp/dex2jar"

        self.apk = "" #dynamically added
        self.tools_dex2jar = ""
        self.tools_fernFlower = ""
        self.tools_proCyon = ""


    def healthCheck(self):
        print "check health"
        healthStatus = True
        '''
        more to add..
        check java installed
        check dex2jar, fern and pro folders

        '''
        if not self.archiveLastReport():
            sys.exit()
        self.apk = self.checkApkDir()
        if not self.apk:
            sys.exit()
        if not self.checkTmpDir():
            sys.exit()
        if not self.checkOutDir():
            sys.exit()

        self.tools_dex2jar = self.toolsFol + "/dex2jar-0.0.9.9.zip"
        self.tools_fernFlower = self.toolsFol + "/fernflower.jar"
        self.tools_proCyon = self.toolsFol + "/procyon.jar"
        return healthStatus

    def archiveLastReport(self):
        health = True
        try:
            dt = datetime.datetime.now().strftime("%Y.%B.%d_%H.%M.%S")
            shutil.copytree(self.outputFol,self.archive+"/Output_"+str(dt))
            shutil.rmtree(self.outputFol)
        except Exception as err:
            health = False
            print "couldn't create last report archive..\n", err
        return health

    def checkApkDir(self):
        print "apk fol health check.."
        apkPath = None
        health = True
        if not len(os.listdir(self.apkFol)):
            print "please keep the apk file to be decompiled in apk folder and restart."
            health = False
        elif len(os.listdir(self.apkFol))>1:
            print "apk directory should contain only one apk file to be decompiled."
            health = False
        elif not os.listdir(self.apkFol)[0].endswith('.apk'):
            print "its not the apk file in the directpry apk"
            health = False
        if health:
            apkPath = self.apkFol +'/'+ os.listdir(self.apkFol)[0]
        return apkPath

    def checkTmpDir(self):
        print "checking the tmp folder.."
        health = True
        try:
            if os.path.exists(self.tmpFol):
                shutil.rmtree(self.tmpFol)
        except Exception as err:
            print "error while deleting the tmp dir"
            health = False
        try:
            if not os.path.exists(self.tmpFol):
                os.makedirs(self.tmpFol)
        except Exception as err:
            health = False
            print "error while creating tmp folder."
        return health

    def checkOutDir(self):
        health = True
        try:
            if os.path.exists(self.outputFol):
                shutil.rmtree(self.outputFol)
        except Exception as err:
            print "error while deleting the output dir"
            health = False
        try:
            os.makedirs(self.outputFol)
            os.makedirs(self.outputFol+'/jar')
            os.makedirs(self.outputFol+'/decmpiledByProcyon')
            os.makedirs(self.outputFol+'/decompiledByfernflower')
        except Exception as err:
            health = False
            print "couldn't create output dirs"
        return health


    def getApk(self):
        print "getting app from apk folder."
        '''
        move the code to apk folder check
        '''
        #self.apk = self.apkFol +'/'+ os.listdir(self.apkFol)[0]

    def unZipApk(self):
        #print "apk path = ", self.apk
        print "unzipping and placing in tmp folder.."
        with zipfile.ZipFile(self.apk, "r") as zf:
            zf.extractall(self.unZipped)

    def getJar(self):
        print "getting jar file from classes dex.."
        with zipfile.ZipFile(self.tools_dex2jar, "r") as zf:
            zf.extractall(self.tmpFol)

        src = "E:/Blogs/Secure_apk/QuickExtractApkSource/main/tmp/dex2jar-0.0.9.9"
        os.rename(src, self.dex2jar)

        cmd = self.dex2jar + "/d2j-dex2jar.bat "+ self.unZipped + "/classes.dex"
        #print cmd
        os.chdir(self.outputFol+'/jar')
        #subprocess.call(cmd)
        self.executeCmd(cmd)
        os.chdir(self.mainFol)
        os.rename(self.outputFol+'/jar/classes-dex2jar.jar',self.outputFol+"/jar/classes.jar")
        #shutil.move(self.mainFol+"/classes-dex2jar.jar",self.outputFol+"/jar/classes.jar")


    def getSourceCode(self):
        print "extracting java sourec code from jar.."
        print "1) procyon exctraction in progress.. "
        cmd = "java -jar "+self.toolsFol+"/procyon.jar -jar "+\
                            self.outputFol+"/jar/classes.jar -o "+self.outputFol+"/decmpiledByProcyon"
        self.executeCmd(cmd)
        print "2) fernflower extraction in progress.."
        cmd = "java -jar "+self.toolsFol+"/fernflower.jar "+\
                            self.outputFol+"/jar/classes.jar "+self.outputFol+"/decompiledByfernflower"
        #print cmd
        self.executeCmd(cmd)
        with zipfile.ZipFile(self.outputFol+"/decompiledByfernflower/classes.jar", "r") as zf:
            zf.extractall(self.outputFol+"/decompiledByfernflower")
        os.remove(self.outputFol+"/decompiledByfernflower/classes.jar")

    def executeCmd(self,cmd):
        msg = None
        FNULL = open(os.devnull, 'w')
        try:
            subprocess.call(cmd,stdout=FNULL,stderr=subprocess.STDOUT,shell=True)
        except Exception as err:
            print "error whle trying to execute :",cmd
            print "\nError : ", err

if __name__=='__main__':

    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')).replace('\\','/')
    #print rootPath

    extractObj = QuickExtract(rootPath)
    if extractObj.healthCheck():    #delete& create tmp folder. ; check for single apk etc..
        print "Good to start.."
    else:
        print "Something went wrong..! :("
        sys.exit()
    extractObj.getApk()
    extractObj.unZipApk()
    extractObj.getJar()
    extractObj.getSourceCode()

    #extractObj.moveToOutDir()

