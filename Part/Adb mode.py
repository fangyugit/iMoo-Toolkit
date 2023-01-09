def adbmode():
    device = AdbDeviceUsb()
    while True:
        sc = input('shell:')
        if sc == 'exit':
            sys.exit(1)

        if sc =='':
            adbmode()

        else:
            device.shell(sc)
            adbmode()