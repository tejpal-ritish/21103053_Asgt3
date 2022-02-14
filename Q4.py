#Q4. wap to calculate the grade based on the points input by user

def grade_calc():
    point=int(input('Enter your grade point -> '))
    if point>10 or point<4:
        print('Invalid input. Try again')
        point = grade_calc()
    return point
grade=grade_calc()
if grade==4:
    print("Your Grade is 'D' and your performance has been 'Poor'")
elif grade==5:
    print("Your Grade is 'C' and your performance has been 'Below Average'")
elif grade==6:
    print("Your Grade is 'C+' and your performance has been 'Average'")
elif grade==7:
    print("Your Grade is 'B' and your performance has been 'Good'")
elif grade==8:
    print("Your Grade is 'B+' and and your performance has been 'Very Good'")
elif grade==9:
    print("Your Grade is 'A' and your performance has been 'Excellent'")
elif grade==10:
    print("Your Grade is 'A+' and your performance has been 'Outstanding'")
