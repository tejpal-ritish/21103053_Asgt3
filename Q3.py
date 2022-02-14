#Q3. wap to print the squares of numbers input by user in list form

in_list=input('Enter the numbers (int) that you want to square -> ')
control=in_list.split()
for i in range(len(control)):
    control[i]=int(control[i])                  #to convert string to int 
out_list=[(control[i],control[i]**2) for i in range(len(control))]
print(out_list)
