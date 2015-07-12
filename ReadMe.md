1) About

It is an automated solution for decompiling an apk for java source code. You just need to get the apk to be decompiled and start the process.
What the tool does is, first it will take the apk and unzip it for the classes.dex file. Convert the dex file into a jar file using the famous tool called 'dex2jar.jar'. Then using java decompilers the obtained jar is decompiled for the source code. The java decompilers used are fernflower and procyon.

2) Directory structure.

 'main' directory contains the python code to be executed; sourceExractor.py
 'apk' folder where you need to drop the apk to decompile. Please drop only one apk file at a time.
 'output' directory is where you can find the decompiled items. The jar file as well as the java source code.
 'tools' folder contains all the tools used. Namely dex2jar.jar, fernflower.jar, pycyon.jar.
 'archives' contains the previous run output folders.
 In output folder the source code decompiled by different java decompilers can be found.
 
3) System requirements 

Python 2.7.x 
Java 7 or above.
Please keep the above two executables in OS path.

4) How to use ?

Place the apk file in the 'apk' directory.
Run sourceExractor.py located in the 'main' directory. (Command : python sourceExractor.py)
Find the decompiled jar as well as java files in the 'output' directory.

Note : Tool should not be used for any illegal purpose. Its just for learning sake, and if you are an android developer you can check to what extant your source code can be seen for others using the apk file. You can also consider protecting your source code using ProGaurd. 

Please send your bug reports/ features to : shsmysore@gmail.com

Thank U! :)




 
