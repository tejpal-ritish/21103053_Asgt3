#Q5. wap to print the figure given in question

inp="ABCDEFGHIJK"
control=1
while control<7:
    print(" "*(control-1),inp[0:11-((control-1)*2)])
    control+=1
