a=[]
for i in range (1,6):
    num=int(input("Enter the value :"+ str(i+1))) 
    a.append(num)
    
sum=0
for i in a:
    sum=sum+i
    print(sum)
