

def parse_loop(row_index,col_0,col_1,col_0_l,line):
    for k_word in col_0_l[row_index:]:#从当前行向后搜索Loop_end关键字
        if k_word == 'L_Stop':
            inx = col_0_l[row_index:].index('L_Stop') + row_index #获取loop_end行号
            #print('index...', inx)
            for j in range(row_index, inx + 1):#将loop 中的csv命令转化为python代码
                if col_0[j] == 'IK_SendKey' and col_0[j + 1] in ['DELAY_ms', 'DELAY_Sec']:
                    if col_0[j + 1] == 'DELAY_ms':#将ms转化为s
                        col_1[j + 1] = int(col_1[j + 1]) // 1000
                    #如下转化为python代码格式为SendKey("key名称，发key间隔，发key次数")
                    write_word = f'SendKey({col_1[j][3:].title()},{col_1[j + 1]},{line[1]})'

                    print('loop_write_word', write_word)
                    j += 1#发key名称一行+间隔时间一行，总共两行，下次循环需要多加一行
            row_index = inx + 1
            break
    return row_index,write_word