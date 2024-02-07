a=[1,2,3,4,5]
for i in range(5):
    a.pop(a[i+1])
print(a)