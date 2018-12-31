# Exercise questions

[TOC]

---

### 1. 짝수 홀수 저장

```python
# 1~100까지 숫자를
# even이라는 list를 만들어서 짝수만 저장
# odd라는 list를 만들어서 홀수만 저장
```

```python
hundred = range(1,101)
even=[]
odd=[]
for x in hundred:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(list(hundred))
print(even)
print(odd)
```

