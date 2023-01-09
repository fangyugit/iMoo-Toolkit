def mainp():
    os.system('cls')

    print(' \n请选择模式 \n1.批量安装手表/sdcard/目录下名称为1，2，3...的apk.\n2.安装手表中的apk(自定义路径).\n3.解锁push.\n4.安装web或本地的apk\n5.scrcpy投屏\n6.冻结系统及系统软件更新\n7.在QMMI安装软件\n8.修改分辨率，DPI\nexit.强制返回桌面\nabout.关于')
    device = AdbDeviceUsb()
    mode = input('请输入:')
    if mode == '1':
        installersdcard()
        
    if mode == '2':
        installersdcardd()
    
    if mode == '3':
        com()

    if mode == '4':
        installerpc()

    if mode == '5':
        scrcpy()

    if mode == '6':
        disable()

    if mode == '7':
        qmmi()

    if mode == '8':
        dpisize()
        
    if mode == 'exit':
        back()

    if mode == 'adbtest':
        adbmode()

    if mode == 'bartest':
        progress_bartest()
        sys.exit(1)
        
    if mode == 'about':
        os.system('cls')
        input('此项目由ReX 组织下ReX Wear 项目的 ReX iMoo Team 团队合力开发，版权及著作权属于ReX群组，请勿用其作商业用途，一经发现，将严肃处理！\nQQ群158015384，论坛watch.rexwe.net')
        sys.exit(1)
        
    if mode == '114514':
        os.system('cls')
        input('药不能停！')
        sys.exit(1)

    if mode == 'Re':
        os.system('cls')
        input('阔耐的Re诶，是我的')
        sys.exit(1)

    else:
        os.system('cls')
        print('\n没有此选项')
        mainp()