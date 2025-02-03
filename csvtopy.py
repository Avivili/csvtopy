import os
import pandas as pd
from parse_functions.parse_loop import parse_loop
from parse_functions.parse_other import  parse_other
from parse_functions.parse_ifelse import parse_ifelse
from parse_functions.parse_general import parse_general

def parse_csv(path,py_path):
    # text=os.path.
    data=pd.read_csv(path)
    col_0 = data.loc[:,'CMD_TITLE'] #csv文件第一列
    col_1 = data.loc[:,'param1']#csv文件第二列
    f_name=os.path.join(py_path,file_name(path))
    row_index = 0
    py_func_name=py_func_define(path)
    with open(f_name,'w') as f:
        f.write(py_func_name)
        while row_index<len(data):
            row_index,write_word=write_words(row_index,path,data,col_0,col_1)
            f.write(f'    {write_word}\n')


def write_words(row_index,path,data,col_0,col_1):

    line = data.loc[row_index].tolist()# line为csv 当前读取的数据行
    if row_index != len(data)-1:
        line_1 = data.loc[row_index + 1].tolist()# line_1为csv 当前读取的数据行的下一行
    print(line)


    if line[0] == 'LOOP_Begin':#csv 中提取loop begin/end 循环，line[0]为当前行第一个单元格数据
        col_0_l = col_0.tolist()#csv文件第一列转化为列表，方便读取数据
        print(col_0_l)
        row_index,write_word=parse_loop(row_index, col_0, col_1, col_0_l,line)

    elif line[0] == 'IF_Begin': #csv 中包含ifelse循环进行提取
        row_index,write_word=parse_ifelse(row_index,col_0, data)
    elif line[0] == 'IR_SendKey' and line_1[0] in ['DELAY_ms', 'DELAY_Sec']:
        row_index,write_word=parse_general(row_index, line_1, line)#csv 中包含一次性key值发送

    else:
        row_index,write_word=parse_other(row_index, line)#csv 其他类型键值块检测
    return row_index,write_word

def py_func_define(path):
    func_name=file_name(path).strip('.py')#命名函数名称为脚本名称
    func_name_def=f'def {func_name}():\n'#定义函数名字
    return func_name_def

def file_name(path):
    file=os.path.split(path)
    f_name=file[1].replace('.csv','.py')#利用csv文件名命名py文件
    return f_name


if __name__=='__main__':
    csv_path=r'D:\software\python\selenium_python\case\script\script_csv'
    py_path=r'D:\software\python\selenium_python\case\script\script_py'
    csv_paths=[os.path.join(csv_path,file) for file in os.listdir(csv_path)]
    print(csv_paths)
    for csv_path in csv_paths:
        parse_csv(csv_path,py_path)