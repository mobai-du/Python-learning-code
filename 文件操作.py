


f_name = '1.txt'
f_new_name = '%s.new'%f_name

old_str = '111'
new_str = '123'

f = open(f_name,'r',encoding='utf-8')
f_new =open(f_new_name,'w',encoding='utf-8')

for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)

    f_new.write(line)

f.close()
f_new.close()

