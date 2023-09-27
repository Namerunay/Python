my_list=[2,4,6,8,10]
for i in range(len(my_list)):
    my_list[i]=my_list[i]-1
    
number = int(input('Введите чило: '))
my_list.append(number)
print(my_list)