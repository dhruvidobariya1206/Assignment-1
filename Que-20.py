# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
cnt={}
# print(type(cnt))
for i in my_list:
    if(i in cnt):
        cnt[i] +=1
    else:
        cnt[i]=1
print(cnt)