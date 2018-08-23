names = ['alex','jack','peiqi',2,'rain','mack',2,'reach',2,'abc','def']

first_index = names.index(2)

new_list=names[first_index+1:]
second_index = new_list.index(2)
second_val = names[first_index+second_index+1]
print(new_list,first_index,second_index)
print("secongd_cal",second_val)