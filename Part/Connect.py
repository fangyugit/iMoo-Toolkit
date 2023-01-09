def start():
    print('此版本为canary版本，专门为测试使用，包含大量测试功能，极不稳定，请斟酌后使用\n此软件的任何版本皆免费（包括re版，高级版），不做也不允许做商业用途\n此项目由ReX 组织下ReX Wear 项目的 ReX iMoo Team 团队合力开发，版权及著作权属于ReX群组，请勿用其作商业用途，一经发现，将严肃处理！\nQQ群158015384，论坛watch.rexwe.net')
    accept = input('是否同意上述条款(y/n):')
    if accept == 'y':
        os.system('start adb.exe ')
        os.system('adb shell dumpsys battery unplug')
        os.system('taskkill /T /F /IM adb.exe')
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
        mainp()

    else:
        sys.exit()