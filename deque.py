from collections import deque
d= deque()
num = input()

for i in range(0,num):
    input_str = raw_input()
    command = input_str.split()
    if len(command)>1:
        eval('d.'+command[0]+'('+command[1]+')')
    else:
        eval('d.'+input_str+'()')
lst=''
for elem in d:
    lst = lst+' '+str(elem)
print lst.strip()
