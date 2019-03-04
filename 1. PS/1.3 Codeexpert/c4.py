R = int(input())
sum = 0
for r in range(1, R):
    sum += int((R**2-r**2)**0.5)
print(sum*4)