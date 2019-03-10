def test():
    global i
    if i == 30:
        print('done')
        return 0
    else:
        print(i,'def')
        i += 1
        return 1
i = 0
while test(): continue

for i in range(99,-1,-1):
    print(i)