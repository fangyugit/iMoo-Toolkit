def com():
    device = AdbDeviceUsb()
    os.system('cls')
    print("正在打开串口，将为您打开调试设置")
    device.shell('am start com.xtc.selftest/.ui.ControllerActivity')
    input('请在手表上下拉页面，并勾选“打开串口”选项,并在回车后自动重启手表')
    device.shell('reboot')
    input('请您在手表重启完成后连接电脑，并重新打开程序')
    sys.exit(1)