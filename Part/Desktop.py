def back():
    device = AdbDeviceUsb()
    os.system('cls')
    device.shell('input keyevent KEYCODE_HOME')
    sys.exit(1)