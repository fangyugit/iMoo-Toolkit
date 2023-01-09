def file_creation(rout,name,format,msg):  # 路径，文件名，后缀名，内容
    full_path = rout + name + format
    file = open(full_path,'w')
    file.write(msg)
    file.close()