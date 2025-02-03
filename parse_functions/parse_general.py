

def parse_general(row_index,line_1,line):
    if line_1[0] == 'DELAY_ms':
        line_1[1] = int(line_1[1]) // 1000
    write_word = f'SendKey({line[1][3:].title()},{line_1[1]},1)'
    row_index += 2
    print('normal_write_word', write_word)
    return row_index, write_word