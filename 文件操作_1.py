
old_str = '111'
new_str = '123'

f = open('1.txt','r+',encoding='utf-8')
data = f.read()
f.seek(0)
data.replace(old_str,new_str)
for line in f:
    if old_str in  line:
        line = data.replace(old_str,new_str)


    f.write(line)

f.close()