import os
import sys
import time
from adb_shell.adb_device import AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

pubkey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAivSgL4SgvC9U+TDvVO7C06QFZCmmdSb/aXAT6xGsUAODjrdTFmHCqwNyDKX5u8XTLeX7GWromjr9IVPOs4DQ/A5ECxXFfDcpFIy/lMuNm9tU2Qu5+eKBWsY4wmR6m8pzU3gQ8r4MEeifwQwJNANrXPWOimfibwTmCSsC7wAMlbj/OThbkVinXcBaxDZVvg7mEwKuyhmM99+MnXtK1uMcpLiVGBRKkzvsZYE9RVMtWLEsM8N5bEixBh8hBbF+yjnImsqyTtrH59UKWPzhV99C2dkGqER+2G1fcMJdu8JzxY7Td6OcwrOTThjIX3QXiu7A7oOj9rrgOAjHDJBWz852bwIDAQAB"
privkey = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCK9KAvhKC8L1T5
MO9U7sLTpAVkKaZ1Jv9pcBPrEaxQA4OOt1MWYcKrA3IMpfm7xdMt5fsZauiaOv0h
U86zgND8DkQLFcV8NykUjL+Uy42b21TZC7n54oFaxjjCZHqbynNTeBDyvgwR6J/B
DAk0A2tc9Y6KZ+JvBOYJKwLvAAyVuP85OFuRWKddwFrENlW+DuYTAq7KGYz334yd
e0rW4xykuJUYFEqTO+xlgT1FUy1YsSwzw3lsSLEGHyEFsX7KOciayrJO2sfn1QpY
/OFX30LZ2QaoRH7YbV9wwl27wnPFjtN3o5zCs5NOGMhfdBeK7sDug6P2uuA4CMcM
kFbPznZvAgMBAAECggEAVoG0t+B5sK5G2Fv+o4GBCQEz2geT+ZstpxZ/T/jQrX+C
h3bZ4zU5W/3pIraxopSlxA1JJanI5TuUGwtxw46OjFzVP5FuQMaWbJSzMI8Iud7y
E62ZOlgo77o3281yB0siQPSemIB4Qy3vRt+XWypFzLmS49eIwFTsYQjF6sS9EPgP
9ktjpc+XAczHuY/HU+uKDJXZl2lTmTAoNIHHobhD72pYp6jFS/6PvNVkAA+Vke0O
9kdaRQf/tZJINs+jNEJILu5jOSqcY47NDY8U8cqF89EI3dZquxjFalrQlRY+RtOQ
ZDUSENgOQz7p+8mbRbZUrqnl5eXLZuOGt+2kGiMnAQKBgQDCzRIHQt9yogt/jhnF
epCu7mDIA8XfEYZrjzsMwbbdTJqTc5VIrO5k0HOrOAaAOznUHs/6VBU2eHpqb1yy
gopACN+LSAQkDf0JuoEMzuwYtK54DQzg4L7ApC0MyKC5pIGexSGO7mRRsf2kZlW9
XOQ4pRaVKsyPCeaVwmslwnvhUwKBgQC2nCqVdBmnEjiC05RtGmomU53Y1l8OD0jb
Wq/nHwMNGZVsJWQFYimdsok/mIVcyrn/tz7jNUzy1p2zHelqeT63C0BfMuyXUDx9
uwTzP94iUzPQXskhxd2ZworoPcfa4BYYcDcFj2CHgyBHJMRBlooQye/XFIqemnaj
KbD2X8ym9QKBgDl0BCoyFfcYRe3j+kPdJ0kAs3iqbDSjVZLplo/nnkhcrIZqo4/g
uRrww/yutHQjg6XFRK/fFraPCAPWPm/DwoSqWUwZ/Gap3YR+BkvBx65ts7tilfbJ
Mllc0pCfp4+5LiWmnIQsWVgi990B9a249PKj9ioeimBxmhl3UuS7HJBTAoGAbOK1
qaQu36ZHuAq9SEkl3nChgHhi+Zk3kkSC+sdNJHSK2o95EpSzx+p7WEZzzx66xbXY
c9aGaY57PiCp2+kr8i1tVtagqKEZUMdBbmI47DK8hJTgTZkUR+jutwiPsP1Jb40J
4fDaWDNh/cn4lDtVXCltL8x505S7BROJB3+cIjkCgYA4mxy7lFIvgk+M115pdcNu
1TVxaVJeNAxKiblpDModNsAtIX2E78LLT05Sioh0WWN3BHZ2HNDSnzzCQTWEmtmq
o64nX0MTTAeuJ2vWhKDMxnUvWfX23KHiKz6cyOLFrnk8Wd2cboMWrdxo6fjRs2cK
em2l8OC1Ejqj6oZaabPWFA==
-----END PRIVATE KEY-----
"""


def restart_program():
    print(' \n开始重新运行程序...\n ')
    os.system('cls')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def progress_bar():
  for i in range(1, 101):
    print("\r", end="")
    print("Reboot: {}%: ".format(i), "▋" * (i // 1), end="")
    sys.stdout.flush()
    time.sleep(0.7)


def addInstall(cmd):
    return "echo -n \"%sinstal\">>/sdcard/apk.txt;echo \"l%s\">>/sdcard/apk.txt;" % (cmd[0], cmd[1])

def adbmode():
    while True:
        sc = input('shell:')
        if sc == 'exit':
            sys.exit(1)

        if sc =='':
            adbmode()

        else:
            device.shell(sc)
            adbmode()


def start():
    adbmode()

def progress_bartest():
  os.system('cls')
  namef=input('firstname:')
  namel=input('lastname:')
  tim=input('time:')
  inf=input('fill:')
  info=input('f/s:')
  info=int(info)
  tim=int(tim)
  namef = namef+"  {}%: "
  namel = " "+namel
  for i in range(1, 101):
      print("\r", end="")
      print(namef.format(i), inf * (i // info), end=namel)
      sys.stdout.flush()
      time.sleep(tim)

#def k2415rootmode_test():
#    os.system('cls')
#    key=input('key:')

#    if key == '':
#        os.system('cls')
#        #rootmode()

#    else:
#        os.system('cls')
#        input('测试功能，暂不开放')
#        sys.exit(1)

def dpisize():
    print('1.查看分辨率\n2.修改分辨率\n3.查看DPI\n4.修改DPI\n5.恢复原始分辨率\n6.恢复原始DPI')
    moded=input('选择模式:')
    os.system('cls')
    if moded =='1':
      out=device.shell('wm size')
      input(out)
      dpisize()

    if moded =='2':
        out = device.shell('wm size')
        out = '当前分辨率'+out
        print(out)
        infot=input('横向分辨率修改为:')
        infol=input('纵向分辨率修改为:')
        info=infot+'x'+infol
        info='wm size '+info
        device.shell(info)
        out=device.shell('wm size')
        input(out)
        dpisize()

    if moded == '3':
        out=device.shell('wm density')
        input(out)
        dpisize()

    if moded == '4':
        out = device.shell('wm density')
        out = '当前DPI' + out
        print(out)
        info=input('DPI修改为：')
        info='wm density '+info
        device.shell(info)
        out=device.shell('wm density')
        input(out)
        dpisize()

    if moded == '5':
        device.shell('wm size reset')
        out = device.shell('wm size')
        out = '恢复完成，当前分辨率' + out
        input(out)
        dpisize()

    if moded == '6':
        device.shell('wm density reset')
        out = device.shell('wm density')
        out = '恢复完成，当前DPI' + out
        input(out)
        dpisize()

    else:
        print('没有此选项')
        os.system('cls')
        dpisize()

def mainp():
    os.system('cls')
    print(' \n请选择模式 \n1.批量安装手表/sdcard/目录下名称为1，2，3...的apk.\n2.安装手表中的apk(自定义路径).\n3.解锁push.\n4.安装web或本地的apk\n5.scrcpy投屏\n6.冻结系统及系统软件更新\n7.在QMMI安装软件\n8.修改分辨率，DPI\nexit.强制返回桌面\nabout.关于')
    device = AdbDeviceUsb()
    mode = input('请输入:')
    if mode == '1':
        os.system('cls')
        inputMsg = input(" \n请将软件放置于/sdcard/，改名为1.apk，2.apk.... \n并输入软件安装包数量:")
        inputMs = int(inputMsg)

        for shit in range(inputMs):
            shits = str(shit + 1)
            try:
                print(" \n正在创建安装会话.")
                device.shell("rm /sdcard/apk.txt")
                response = device.shell(addInstall(["pm ", "-create"]) + "sh /sdcard/apk.txt")
                if not response.startswith("Success"):
                    raise Exception(response)
                sessionID = int(response.split("[", 1)[1].split("]", 1)[0])

                print("正在安装软件, 可能需要一些时间.")
                device.shell("rm /sdcard/apk.txt")
                in1 = "-write %d force /sdcard/" + shits + ".apk"
                response = device.streaming_shell(addInstall(["pm ", in1 % sessionID]) + addInstall(
                    ["pm ", "-commit %d" % sessionID]) + "sh /sdcard/apk.txt", read_timeout_s=100)
                for line in response:
                    print(line, end="")
                device.shell("rm /sdcard/apk.txt")

                print("该安装进程结束.\n ")

            except BaseException as err:
                exceptionName = type(err).__name__
                exceptionInfo = str(err)
                print("安装失败, 错误信息: \n%s: %s" % (exceptionName, exceptionInfo))
        finish = input("安装结束.")
        sys.exit(0)
    if mode == '4':
        os.system('cls')
        print(" \n软件位置可输入apk下载链接或是本地文件路径.\n该模式会一直循环执行，直到关闭程序.\n")
        while True:
            try:
                device.shell("rm /sdcard/apk.txt")
                device.shell("rm /sdcard/apk.apk")
                inputMsg = input("请输入软件位置或拖载: ")
                if inputMsg.startswith('"') and inputMsg.endswith('"'):
                    inputMsg = inputMsg[1:-1]
                if inputMsg.startswith("http://") or inputMsg.startswith("https://") or inputMsg.startswith("ftp://"):
                    print("正在加载软件.")
                    response = device.streaming_shell("curl --output /sdcard/apk.apk %s" % inputMsg)
                    for line in response:
                        print(line)
                else:
                    if not os.path.isfile(inputMsg):
                        raise FileNotFoundError("此文件不存在.")
                    device.push(inputMsg, "/sdcard/apk.apk")

                print(" \n正在创建安装会话.")
                device.shell("rm /sdcard/apk.txt")
                response = device.shell(addInstall(["pm ", "-create"]) + "sh /sdcard/apk.txt")
                if not response.startswith("Success"):
                    raise Exception(response)
                sessionID = int(response.split("[", 1)[1].split("]", 1)[0])

                print("正在安装软件, 可能需要一些时间，请勿关闭窗口.")
                device.shell("rm /sdcard/apk.txt")
                response = device.streaming_shell(
                    addInstall(["pm ", "-write %d force /sdcard/apk.apk" % sessionID]) + addInstall(
                        ["pm ", "-commit %d" % sessionID]) + "sh /sdcard/apk.txt", read_timeout_s=100)
                for line in response:
                    print(line, end="")
                device.shell("rm /sdcard/apk.txt")
                device.shell("rm /sdcard/apk.apk")
                print("安装结束,若上句为Success则安装成功，若为Failure则失败,将开始下一次循环.")
            except BaseException as err:
                exceptionName = type(err).__name__
                exceptionInfo = str(err)
                print("安装失败, 错误信息: \n%s: %s" % (exceptionName, exceptionInfo))
                if exceptionName == 'UsbReadFailedError' and exceptionInfo.endswith('LIBUSB_ERROR_TIMEOUT [-7]'):
                    print("您的手表可能没有打开串口，将为您打开调试设置，")
                    device.shell('am start com.xtc.selftest/.ui.ControllerActivity')
                    exitsetting = input('请在手表上下拉页面，并勾选“打开串口”选项,并在回车后自动重启手表')
                    device.shell('reboot')
                    rebootwatch = input('请您在手表重启完成后连接电脑，并重新打开程序')
                    sys.exit(1)
    if mode == '2':
        os.system('cls')
        while True:

            inputapk = input(" \n请输入软件的路径:")
            try:
                print(" \n正在创建安装会话.")
                device.shell("rm /sdcard/apk.txt")
                response = device.shell(addInstall(["pm ", "-create"]) + "sh /sdcard/apk.txt")
                if not response.startswith("Success"):
                    raise Exception(response)
                sessionID = int(response.split("[", 1)[1].split("]", 1)[0])

                print("正在安装软件, 可能需要一些时间.")
                device.shell("rm /sdcard/apk.txt")
                in1 = "-write %d force " + inputapk
                response = device.streaming_shell(addInstall(["pm ", in1 % sessionID]) + addInstall(
                    ["pm ", "-commit %d" % sessionID]) + "sh /sdcard/apk.txt", erad_timeout_s=100)
                for line in response:
                    print(line, end="")
                device.shell("rm /sdcard/apk.txt")

                print("该安装进程结束.\n ")

            except BaseException as err:
                exceptionName = type(err).__name__
                exceptionInfo = str(err)
                print("安装失败, 错误信息: \n%s: %s" % (exceptionName, exceptionInfo))

    if mode == '114514':
        os.system('cls')
        input('药不能停！')
        sys.exit(1)

    if mode == 'Re':
        os.system('cls')
        input('阔耐的Re诶，是我的')
        sys.exit(1)

    if mode == '3':
        os.system('cls')
        print("正在打开串口，将为您打开调试设置")
        device.shell('am start com.xtc.selftest/.ui.ControllerActivity')
        exitsetting = input('请在手表上下拉页面，并勾选“打开串口”选项,并在回车后自动重启手表')
        device.shell('reboot')
        rebootwatch = input('请您在手表重启完成后连接电脑，并重新打开程序')
        sys.exit(1)

    if mode == 'about':
        os.system('cls')
        input('此项目由ReX 组织下ReX Wear 项目的 ReX iMoo Team 团队合力开发，版权及著作权属于ReX群组，请勿用其作商业用途，一经发现，将严肃处理！\nQQ群158015384，论坛watch.rexwe.net')
        sys.exit(1)

    if mode == '5':
        os.system('cls')
        input('投屏软件来自github开源项目，不可与此软件同时使用')
        os.system('start scrcpy.exe')
        sys.exit(1)

    if mode == '6':
        device.shell('pm disable-user com.xtc.appupdate')
        device.shell('pm disable-user com.xtc.systemupdate_i11')
        sys.exit(1)

    if mode == '7':
        check = device.shell('pm list packages com.qualcomm.qti.qmmi')
        check = check[0:-1]
        if check == 'package:com.qualcomm.qti.qmmi':
            input('回车后自动进入手表QMMI')
            device.shell('am start com.qualcomm.qti.qmmi/.framework.MainActivity')
            os.system('cls')
            input('请依次点击重启，选择重启到QMMI，并确认，完成后请回车')
            os.system('cls')
            progress_bar()
            device = AdbDeviceUsb()
            device.connect(rsa_keys=[PythonRSASigner(pub=pubkey, priv=privkey)])
            os.system('cls')
            print(" \n软件位置可输入apk下载链接或是本地文件路径.\n该模式会一直循环执行，直到关闭程序.\n")
            while True:
                try:
                    device.shell("rm /sdcard/apk.txt")
                    device.shell("rm /sdcard/apk.apk")
                    inputMsg = input("请输入软件位置或拖载: ")
                    if inputMsg.startswith('"') and inputMsg.endswith('"'):
                        inputMsg = inputMsg[1:-1]
                    if inputMsg.startswith("http://") or inputMsg.startswith("https://") or inputMsg.startswith(
                            "ftp://"):
                        print("正在加载软件.")
                        response = device.streaming_shell("curl --output /sdcard/apk.apk %s" % inputMsg)
                        for line in response:
                            print(line)
                    else:
                        if not os.path.isfile(inputMsg):
                            raise FileNotFoundError("此文件不存在.")
                        device.push(inputMsg, "/sdcard/apk.apk")

                    print(" \n正在创建安装会话.")
                    device.shell("rm /sdcard/apk.txt")
                    response = device.shell(addInstall(["pm ", "-create"]) + "sh /sdcard/apk.txt")
                    if not response.startswith("Success"):
                        raise Exception(response)
                    sessionID = int(response.split("[", 1)[1].split("]", 1)[0])

                    print("正在安装软件, 可能需要一些时间，请勿关闭窗口.")
                    device.shell("rm /sdcard/apk.txt")
                    response = device.streaming_shell(
                        addInstall(["pm ", "-write %d force /sdcard/apk.apk" % sessionID]) + addInstall(
                            ["pm ", "-commit %d" % sessionID]) + "sh /sdcard/apk.txt", read_timeout_s=100)
                    for line in response:
                        print(line, end="")
                    device.shell("rm /sdcard/apk.txt")
                    device.shell("rm /sdcard/apk.apk")
                    print("安装结束,若上句为Success则安装成功，若为Failure则失败,将开始下一次循环.")
                    os.system('cls')
                except BaseException as err:
                    exceptionName = type(err).__name__
                    exceptionInfo = str(err)
                    print("安装失败, 错误信息: \n%s: %s" % (exceptionName, exceptionInfo))
                    if exceptionName == 'UsbReadFailedError' and exceptionInfo.endswith('LIBUSB_ERROR_TIMEOUT [-7]'):
                        print("您的手表可能没有打开串口，将为您打开调试设置，")
                        device.shell('am start com.xtc.selftest/.ui.ControllerActivity')
                        exitsetting = input('请在手表上下拉页面，并勾选“打开串口”选项,并在回车后自动重启手表')
                        device.shell('reboot')
                        rebootwatch = input('请您在手表重启完成后连接电脑，并重新打开程序')
                        sys.exit(1)

            device.shell('adb shell input keyevent KEYCODE_HOME')

        else:
            os.system('cls')
            print('您的手表未安装QMMI，请安装后重新运行此模式')
            restart_program()

    if mode == 'exit':
        os.system('cls')
        device.shell('input keyevent KEYCODE_HOME')
        sys.exit(1)

    if mode == 'adbtest':
        os.system('cls')
        start()

    if mode == 'bartest':
        progress_bartest()
        sys.exit(1)

#    if mode == 'root_dev':
#        k2415rootmode_test()

    if mode == '8':
        dpisize()

    else:
        os.system('cls')
        print('\n没有此选项')
        mainp()


if __name__ == "__main__":
    print('此版本为canary版本，专门为测试使用，包含大量测试功能，极不稳定，请斟酌后使用\n此软件的任何版本皆免费（包括re版，高级版），不做也不允许做商业用途\n此项目由ReX 组织下ReX Wear 项目的 ReX iMoo Team 团队合力开发，版权及著作权属于ReX群组，请勿用其作商业用途，一经发现，将严肃处理！回车则默认\nQQ群158015384，论坛watch.rexwe.net')
    accept=input('是否同意上述条款(y/n):')
    if accept == 'y':

    # 连接小天才电话手表.
        print("正在连接手表.")
        os.system('cls')
        try:
            device = AdbDeviceUsb()
            device.connect(rsa_keys=[PythonRSASigner(pub=pubkey, priv=privkey)])
        except BaseException as err:
            exceptionName = type(err).__name__
            exceptionInfo = str(err)
            if exceptionInfo == 'LIBUSB_ERROR_ACCESS [-3]':
                  os.system('taskkill /T /F /IM adb.exe')
                  device = AdbDeviceUsb()
                  device.connect(rsa_keys=[PythonRSASigner(pub=pubkey, priv=privkey)])

            elif exceptionInfo == 'No device available, or it is in the wrong configuration.':
                  print("您未连接设备，请连接后重新打开此软件")
                  input("按回车键退出.")
                  sys.exit(1)
            else:
                  print("连接失败, 错误信息: \n%s: %s" % (exceptionName, exceptionInfo))
                  input("按回车键退出.")
                  sys.exit(1)

        print("连接成功")
        os.system('start adb.exe ')
        os.system('adb shell dumpsys battery unplug')
        os.system('taskkill /T /F /IM adb.exe')
        device.shell('dumpsys battery unplug')
        mainp()

    else:
        sys.exit(1)