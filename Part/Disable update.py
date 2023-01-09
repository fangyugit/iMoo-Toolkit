def disable():
    device = AdbDeviceUsb()
    device.shell('pm disable-user com.xtc.appupdate')
    device.shell('pm disable-user com.xtc.systemupdate_i11')
    sys.exit(1)