import os

t_w = os.get_terminal_size().columns
#os.get_terminal_size()


givinStr = input('Enter a string: ')
print(givinStr.center(t_w).title())
print(givinStr.ljust(t_w).title())
print(givinStr.rjust(t_w).title())
