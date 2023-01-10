lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: #sig可以去掉txt開頭的隱藏暗碼造成的空格
    for line in f:
        lines.append(line.strip())#strip可以拿掉換行

for line in lines:
    s = line.split(' ')
    time = s[0][:5] #陣列的第一組字申，獲取第1個到5個的字
    name = s[0][5:] #陣列的第一組字申，獲取第5個到結尾的字
    #print(time)
    print(name)