from pynput.keyboard import Listener
import platform
import getpass
import os
from shutil import copyfile
import shutil
import webbrowser
import sys

userName = getpass.getuser()
system = platform.system()

parentDirWindows = ""
pathProgramPython = "/home/"+userName+"/.fastexec/"
directory="fastexec"
nameFile="fastexec.py"
nameCompile="fastexec.py"

sentence = ""
version = "Version=1.7"

def checkVersion():
    fileExec = "/home/"+userName+"/.config/autostart/fastexec.desktop"
    path = os.path.join(pathProgramPython) 
    if os.path.isfile(fileExec):
        config = open(fileExec, 'r').read()
        arConfig = config.split("\n")
        sameVersion = version in arConfig
        if(sameVersion == False):
            os.remove(fileExec)
            shutil.rmtree(path)

def operatingSystem():
    checkVersion()
    path = os.path.join(pathProgramPython, directory) 
    if(verifyScriptExists() == False):
        os.mkdir(pathProgramPython)
        copyfile(nameFile, pathProgramPython+"/"+nameCompile)
        # os.remove(nameFile)
    
    reboot(system)

def verifyScriptExists():
    pathFile = os.path.join(pathProgramPython,nameCompile)
    if os.path.isfile(pathFile):
        return True
    
    return False

def reboot(systemName):
    fileExec = "/home/"+userName+"/.config/autostart/fastexec.desktop"
    if os.path.isfile(fileExec) == False:
        pathFile = os.path.join(pathProgramPython,nameCompile)
        textFile ="[Desktop Entry]\nType=Application\n"+version+"\nExec=python3 "+pathFile+"\nX-GNOME-Autostart-enabled=true\nNoDisplay=false\nHidden=false\nName[en_US]=fastexec\nName[pt_BR]=fastexec\nComment[en_US]=No description\nX-GNOME-Autostart-Delay=3"

        f = open(fileExec, "a")
        f.write(textFile)
        f.close()



def clearSentence():
    global sentence
    sentence = ""

def fastExec(key):
    global sentence
    keydata = str(key)    
    # python == 2
    if(sys.hexversion == 34017776): 
        keyWithOutQuotationMarks = str(key).replace("'", "")    
        key = keyWithOutQuotationMarks.replace('u', '', 1)
    else:
        key =str(key).replace("'", "")

    split = keydata.split('.')
    size = len(split)
    
    if(size == 2):
        clearSentence()
    else:
        sentence = sentence+key

    if(len(sentence) >= 100):
        sentence =""
    
    if(sentence == 'opsigaderr'):
        webbrowser.get('firefox').open_new_tab('sigaderr.aderr.com.br')
        sentence =""
    if(sentence == 'opsidap'):
        webbrowser.get('firefox').open_new_tab('http://sidap.sedap.pb.gov.br')
        sentence =""
    if(sentence == 'oppecus'):
        webbrowser.get('firefox').open_new_tab('http://pecus.ipeweb.com.br/password')
        sentence =""
    if(sentence == 'opjira'):
        webbrowser.get('firefox').open_new_tab('sigaderr.aderr.com.br:8080')
        sentence =""
    if(sentence == 'opbitbucket'):
        webbrowser.get('firefox').open_new_tab('sigaderr.aderr.com.br:7990')
        sentence =""
    if(sentence == 'opgales'):
        webbrowser.get('firefox').open_new_tab('http://jira.sidap.sedap.pb.gov.br')
        sentence =""
    if(sentence == 'opsidaam'):
        webbrowser.get('firefox').open_new_tab('http://sidaam.adaf.am.gov.br')
        sentence =""
    if(sentence == 'opyoutube'):
        webbrowser.get('firefox').open_new_tab('https://www.youtube.com')
        sentence =""
        
operatingSystem()
with Listener(on_press=fastExec) as listener:
    listener.join()