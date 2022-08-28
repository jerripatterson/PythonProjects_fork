import os


my_str='python'
my_new_str='python scripting'
my_str3='string operation'
x='python is easy and it is popular'
#print(my_str.center(20))
#print(f"{my_str.center(20)}\n{my_new_str.center(20)}\n{my_str3.center(20)}")
#print(my_str.zfill(10))
#x.count('is')
print(x.ljust(80))
y=os.get_terminal_size()
print(y)
