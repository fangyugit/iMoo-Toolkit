import os

def file_creation(rout,name,format,msg):  # 路径，文件名，后缀名，内容
    full_path = rout + name + format
    file = open(full_path,'w')
    file.write(msg)
    file.close()

list = os.getcwd()
list=list.replace("\\", "\\\\")
list=list+"\\\\"

file_creation(list,'mode','.dat','mode2')
mode = os.path.exists('mode.dat')
if mode == True:
    file_object = open('mode.dat', 'r')  # 文件对象
    try:
        output=file_object.read()  # 结果为str类型
    finally:
        file_object.close()