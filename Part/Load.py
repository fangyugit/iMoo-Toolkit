if __name__ == "__main__":
    Ver = '3.6.0'  # 当前版本
    list = os.getcwd()
    list = list.replace("\\", "\\\\")
    list = list + "\\\\"  # list变量为PY直接可用的路径，意义为程序所在文件夹
    file_name = os.path.basename(__file__)  # file_name变量为当前程序文件名
    print('测试网络连接中***')
    exit_code = os.system('ping toscode.gitee.com')  #测试网络连接
    os.system('cls')
    if exit_code == 0:  # 网络连接成功
        print('服务器连接成功')
        os.system('cls')
        mode = os.path.exists('mode.dat')
        if mode == True:
            file_object = open('mode.dat', 'r')  # 文件对象
            try:
                output = file_object.read()  # 结果为str类型
            finally:
                file_object.close()

            if output == 'update':  # 如果为更新模式  #预留的更新子程序接口，还没写
                print(output)  # 占位用的，记得删

            if output == 'Normal-startup':  # 如果为正常启动模式
                start()


        else:
            file_creation(list, 'mode', '.dat', 'Normal-startup')  # 写入正常启动
            start()  # 启动主程序

    else:
        print('False')
        print('服务器连接失败，切换为单机模式')
        os.system('cls')
        start()