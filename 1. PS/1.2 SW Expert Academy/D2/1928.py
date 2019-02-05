T = int(input())
for tc in range(T):
    sen = input()
    new_sen = ''
    for i in sen:
        if i >= 'A' and i <= 'Z':
            dc = bin(ord(i) - 65).lstrip('0b')
            if len(dc) < 6:
                dc = '0' * (6 - len(dc)) + dc
            new_sen += dc
        elif i >= 'a' and i <= 'z':
            dc = bin(ord(i) - 71).lstrip('0b')
            if len(dc) < 6:
                dc = '0' * (6 - len(dc)) + dc
            new_sen += dc
        elif i >= '0' and i <= '9':
            dc = bin(ord(i) + 4).lstrip('0b')
            if len(dc) < 6:
                dc = '0' * (6 - len(dc)) + dc
            new_sen += dc
    print(f'#{tc+1}', end=' ')
    result = ''
    for i in range(len(new_sen) // 8):
        result += chr(int(new_sen[8*i:8*i+8], 2))
    print(result)

# TGlm -> 19063738 -> 010011000110100101100110
# ->01001100 01101001 01100110
# ->76 105 102
#
# Lif -> 76 105 102 -> 010011 000110 100101 100110 -> TGlm