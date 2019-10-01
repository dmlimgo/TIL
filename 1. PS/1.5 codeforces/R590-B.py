n, k = map(int, input().split())
arr = list(map(int, input().split()))
msg = []
msg_len = 0
for q in arr:
    if q not in msg:
        msg = [q] + msg
        msg_len += 1
        if msg_len > k:
            msg.pop()
            msg_len -= 1
print(msg_len)
for i in range(msg_len):
    print(msg[i], end=" ")