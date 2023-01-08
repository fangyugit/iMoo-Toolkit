import os

def file_creation(rout,name,format,msg):  # 路径，文件名，后缀名，内容
    full_path = rout + name + format
    file = open(full_path,'w')
    file.write(msg)
    file.close()

def read(nam):  # 文件名（包括后缀）
    file_object = open(nam, 'r')  # 文件对象
    try:
        all_the_text = file_object.read()  # 结果为str类型
    finally:
        file_object.close()

list = os.getcwd()
list=list.replace("\\", "\\\\")
list=list+"\\\\"

file_creation(list,'mode','.dat','mode2')
mode = os.path.exists('mode.dat')
if mode == True:
    print(mode)



