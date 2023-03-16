str='The Lyrics is not that poor'
pos_not = str.find("not")
pos_poor = str.find("poor")
print("not pos -", pos_not)
print("poor pos -", pos_poor)
if pos_not < pos_poor:
    print(str[:pos_not]+"good")
