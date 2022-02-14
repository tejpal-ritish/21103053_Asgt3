#wap to count the number of occurences of characters in a string

string1=input('Enter a string -> ')
list1=[]
count=dict()
for i in string1:      
    list1.append(i) 
for j in list1:        
    if j in count:          
        count[j]+=1    
    else:
        count[j]=1
print(count)        
