num = []
sum=0
n =  int(input("Enter number of elements: "))
i=0
while i<n:
  num.append(int(input("Enter a number: ")))
  sum = sum + num[i]
  i=i+1
print("The sum is %d" %(sum))
