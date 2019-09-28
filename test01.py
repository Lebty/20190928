l1=['a','b','c']
l2=[1, 2, 3, 4, 5]
l3=['가','나','다','라']

sum=l1+l2+l3

print("{}".format(sum))

for i in range(len(sum)+1):
    if i == len(l1):
        print()
    if i == len(l1)+len(l2):
        print()
    if i == len(l1)+len(l2)+len(l3):
        print()
    if i < len(sum):
        print("{}".format(sum[i]))
    else:
        print("{}".format(sum))

