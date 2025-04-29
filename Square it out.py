num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
sq=[]
even=[]
odd=[]
def odd_even(num1,num2):
    for i in range(num1,num2+1):
        j=i**2
        sq.append(j)
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)

odd_even(num1,num2)
print(sq)
print("List of even numbers: ",even)
print("List of odd numbers: ",odd)
        







