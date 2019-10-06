import os


def get_list(message):
    flag = ''
    name_list = []
    while flag != '0':
        flag = input(message)
        if flag != '0':
            name_list.append(flag.strip())
    return name_list


def get_all_path(open_file_path, suffix_list):
    path_list = []
    root_dir = open_file_path
    file_list = os.listdir(root_dir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(file_list)):
        com_path = os.path.join(root_dir, file_list[i])
        if os.path.isfile(com_path) and os.path.splitext(com_path)[1] in suffix_list:
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path, suffix_list))
    return path_list


def merge(root_path_list, suffix_list, file_name):
    path = []
    for i in range(0, len(root_path_list)):
        path.extend(get_all_path(root_path_list[i], suffix_list))
    with open(file_name, 'w') as write_file_obj:
        for i in range(0, len(path)):
            with open(path[i], encoding='utf-8') as read_file_obj:
                contents = read_file_obj.read()
                write_file_obj.write(os.path.split(path[i])[1] + "\n")
                write_file_obj.write(contents.strip() + "\n\n")


root_path_list = get_list(r"请输入代码存放根目录绝对路径，输入0表示结束：")
suffix_list = get_list("请输入代码文件后缀名，输入0表示结束：")
file_name = input("请输入合并后的文件名：")
merge(root_path_list, suffix_list, file_name)
