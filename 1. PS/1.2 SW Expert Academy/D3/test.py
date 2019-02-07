arr = [1,2,3,4,5]
for i in range(5):
    for j in range(i,5):
        print(i,j+1,sum(arr[i:j+1]))