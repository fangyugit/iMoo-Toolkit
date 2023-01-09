def dpisize():
    device = AdbDeviceUsb()
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