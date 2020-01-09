## Python Print Expression

> {} 를 이용한 출력방식에 대한 내용
>
>  https://docs.python.org/ko/3/tutorial/inputoutput.html 

```PYTHON
>>> name = 'Jack'
>>> age = 10
```

#### 

| 표현 | 예제        | 결과           |
| ---- | ----------- | -------------- |
| `:`  | `{name:10}` | `Jack      10` |
| `!a` | `{name!a}`  | `'Jack'10`     |
| `!s` | `{name!s}`  | `Jack10`       |
| `!r` | `{name!r}`  | `'Jack'10`     |
|      |             |                |



- `:` 뒤에 정수를 전달하면 해당 필드의 최소 문자 폭이 된다.

```python
>>> print(f'{name:10}{age}')
Jack      10
```

- `!a`는 `ascii()`를, `!s`는 `str()`를, `!r` 은 `repr()`를 적용한다.

```python
>>> print(f'{name!a}{age}')
>>> print(f'{name!s}{age}')
>>> print(f'{name!r}{age}')
'Jack'10
Jack10
'Jack'10
```

- 두개를 같이 쓸 수도 있다.

```python
>>> print(f'{name:10}{age}')
>>> print(f'{name!r:10}{age}')
Jack      10
'Jack'    10
```







```python
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:^9.4f} | {:^9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))
```

위 코드의 결과물은 다음과 같다.

```bash
                |   lat.    |   long.
Tokyo           |  35.6897  | 139.6917
Delhi NCR       |  28.6139  |  77.2089
Mexico City     |  19.4333  | -99.1333
New York-Newark |  40.8086  | -74.0204
Sao Paulo       | -23.5478  | -46.6358
```

