def installersdcardd():
    device = AdbDeviceUsb()
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