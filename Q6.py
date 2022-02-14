#Q6. wap to make a dictionary containing names and SIDs and perform operations on it

sid=int(input('Enter SID -> '))
name=input('Enter name -> ')
students={sid:name}

while True:
    option=input('Do you want to enter more records (Y/N) -> ').upper()
    if option=='Y':
        sid=int(input('Enter SID -> '))
        name=input('Enter name -> ')
        students[sid]=name
    elif option=='N':
        break
    else:
        print('Invalid input')

print('Part A) -> ',students,'\n')
print('Part B) -> ',{k:v for k,v in sorted(students.items(), key=lambda x:x[1])},'\n')
print('Part C) -> ',{k:v for k,v in sorted(students.items())},'\n')
sid=int(input('Enter SID to search for recorded name -> \n'))
print('Part D) -> ',students[sid],'\n')
