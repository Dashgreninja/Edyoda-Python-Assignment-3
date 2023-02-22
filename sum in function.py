def sum_list(x):
    sum=0
    for i in x:
        sum=sum+i
    return sum
l=[]
n=int(input('Enter no. of elements : '))
for i in range(n):
    l.append(int(input('Enter number : ')))
print('sum of no.s is : ',sum_list(l))
