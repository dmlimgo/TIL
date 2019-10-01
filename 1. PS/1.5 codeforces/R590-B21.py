n, k = map(int, input().split())
arr = list(map(int, input().split()))
msg = []
msg_len = 0
dic = {}
for q in arr:
    try:
        if dic[q]:
            pass
        else:
            dic[q] = 1
            msg = [q] + msg
            msg_len += 1
            if msg_len > k:
                dic[msg.pop()] = 0
                msg_len -= 1    
    except KeyError:
        dic[q] = 1
        msg = [q] + msg
        msg_len += 1
        if msg_len > k:
            dic[msg.pop()] = 0
            msg_len -= 1
print(msg_len)
for i in range(msg_len):
    print(msg[i], end=" ")