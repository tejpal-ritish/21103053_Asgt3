#Q7. wap to print the fibonacci series upto the length input by user

length=int(input('Enter the length of the series -> '))
if length==1:
    output=[1]
else:
    output=[1,1]
    while len(output)<length:
        output.append(output[-1]+output[-2])
print('The fibonacci series for the length input by you is ',output)
avg=0
for i in range(length):
    avg+=output[i]
print('The average of the series is ',avg/length)
