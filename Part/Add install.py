def addInstall(cmd):
    return "echo -n \"%sinstal\">>/sdcard/apk.txt;echo \"l%s\">>/sdcard/apk.txt;" % (cmd[0], cmd[1])