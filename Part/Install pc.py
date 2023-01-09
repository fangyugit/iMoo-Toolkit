def installerpc():
    device = AdbDeviceUsb()
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