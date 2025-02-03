
def parse_ifelse(row_index,col_0,data):
    for k_word in col_0[row_index:]:
        if k_word == 'IF_End':
            inx = col_0.tolist()[row_index:].index('IF_End') + row_index
            write_word = ''
            for j in range(row_index, inx + 1):
                one_word = ''.join(str(i) for i in data.iloc[j, :].tolist())
                if 'nan' in one_word:
                    one_word = one_word.strip('nan')
                write_word += '#' + one_word + '\n    '
                print('ifelse_write_word', write_word)
            row_index = inx + 1
            break
    return row_index,write_word