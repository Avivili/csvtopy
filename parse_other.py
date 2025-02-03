

def parse_other(row_index,line):
    if line[0] in ['DELAY_ms', 'DELAY_Sec']:
        if line[0] == 'DELAY_ms':
            line[1] = int(line[1]) // 1000
        write_word = f'time.sleep({line[1]})'
    else:
        write_word = '#unknown' + ''.join([str(k) for k in line]).strip('nan')
    print('other_write_word', write_word)
    row_index += 1
    return row_index,write_word