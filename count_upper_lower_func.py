def count_UandL(x):
    Upper=0
    Lower=0
    for i in x:
        if i.isupper():
            Upper+=1
        elif i.islower():
            Lower+=1
    return ('No. of Upper case characters : ',Upper),('No. of Lower case characters : ',Lower)

n=input('enter text : ')
print(count_UandL(n))