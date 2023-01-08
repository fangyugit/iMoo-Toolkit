import os

def file_creation(rout,name,format,msg):  # 路径，文件名，后缀名，内容

    full_path = rout + name + format
        file = open(full_path,'w')
            file.write(msg)
                file.close()

                # 转化获取的脚本目录为Python可用
                list = os.getcwd()
                list=list.replace("\\", "\\\\")
                list=list+"\\\\"

                file_creation(list,'mode','.dat','mode2')  # 创建数据文件

                mode = os.path.exists('mode.dat')  # 确认是否存在数据文件
                if mode == True:  # 如果存在数据文件
                    file_object = open('mode.dat', 'r')  # 文件对象

                        try:
                                output=file_object.read()  # 结果为str类型

                                    finally:
                                            file_object.close()


                                            else:   # 若没有数据文件