import os
import re
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
device = AdbDeviceUsb()
device.connect(rsa_keys=[PythonRSASigner(pub=pubkey, priv=privkey)])

inputMsg = input('$ ')
device.shell("rm /sdcard/apk.apk")
if inputMsg.startswith("http://") or inputMsg.startswith("https://") or inputMsg.startswith("ftp://"):
    command = 'curl --output /sdcard/apk.apk ' + inputMsg
    device.shell(command)

else:
    if inputMsg.startswith('"') and inputMsg.endswith('"'):
        inputMsg = inputMsg[1:-1]
    if not os.path.isfile(inputMsg):
        raise FileNotFoundError("此文件不存在.")
    device.push(inputMsg, "/sdcard/apk.apk")


create = device.shell('pm install-create')
create = re.findall(r'\d+',create)
create = create[0]

device.shell('pm install-write ' + create + ' install /sdcard/apk.apk')
device.shell('pm install-commit ' + create)