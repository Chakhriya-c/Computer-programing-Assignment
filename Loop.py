num = int(input('Enter a number (-1) to terminate : '))
counter = 0
totel = 0
while num != -1:
    counter += 1
    totel += num
    answer = totel/counter
    num = int(input('Enter a number (-1) to terminate : '))
if num==-1:
    print('Total number entered is ',counter,' Average = ',answer)