#Q2. wap a program to calculate the next date of the input date


def date_calc():                                                #function is run in loop to give user option to rectify error in input if any
    month_30=[4,6,9,11]
    month_31=[1,3,5,7,8,10]
    feb=[2]
    dec=[12]
    while(True):                                                #checking if date entered is according to given constraints 
        day=int(input("Enter today's date -> "))
        if 1<=day<=31:
            break
        else:
            print('Invalid input. Try again')
    while(True):                                                #checking if month entered is according to given constraints
        month=int(input('Enter the current month -> '))
        if 1<=month<=12:
            break
        else:
            print('Invalid input. Try again')
    while(True):                                                #checking if year entered is according to given constraints
        year=int(input('Enter the current year -> '))
        if 1800<=year<=2025:
            break
        else:
            print('Invalid input. Try again')
    if month in month_31 :                                      #checking if month has 31 days 
        if day==31:
            day=1
            month+=1
            print(day,"/",month,"/",year)
        elif day<31:
            day+=1
            print(day,"/",month,"/",year)
        else:
            print('Invalid input. Try again')
            date_calc()
    
    elif month in month_30 :
        if day==30:
            day=1
            month+=1  
            print(day,"/",month,"/",year)   
        elif day<30:
            day+=1
            print(day,"/",month,"/",year)
        else:
            print('Invalid input. Try again') 
            date_calc()      
    elif month in feb:
        if year%4==0:                                           #checking if input year is leap year  
            if day==29:
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif day<29:
                day+=1
                print(day,"/",month,"/",year)
            else:
                print('Invalid input. Try again')
                date_calc()
        else:                                                   #when input year is not leap year
            if day==28:
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif day<28:
                day+=1
                print(day,"/",month,"/",year)
            else:
                print('Invalid input. Try again')
                date_calc()
    elif month in dec:                                          #checking if the input date is the last date in the input year
        if day==31:
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif day<31:
            day+=1;
            print(day,"/",month,"/",year)
        else:
            print('Invalid input. Try again')
            date_calc()
        
    else:                                                       #some other error by the user
        print('Invalid input. Try again')
        date_calc()
date_calc()
