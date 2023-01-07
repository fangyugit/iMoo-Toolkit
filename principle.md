# principle

#### Incoming file
adb push com.***.***.apk /sdcard/    or    curl --output /sdcard/load.apk http:// or https:// or ftp://***.***.***/****.apk

#### Connecting devices
adb shell

#### Get create code
pm install-create

#### To be installed
pm install-write [create] install /sdcard/com.***.***.apk

#### Confirm installation
pm install-commit [create]