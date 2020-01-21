## Python Sequence

> Fluent Python 2장 공부

- Sequence란?
  
- 값이 연속적으로 이어진 자료형
  
- 파이썬 표준 라이브러리는 C로 구현된 시퀀스형을 제공한다.

  - 컨테이너 시퀀스
    - list, tuple, collections.deque
    - 객체에 대한 참조를 담고 있다.

  - 균일 시퀀스
    - str, bytes, bytearray, memoryview, array.array
    - 각 항목의 값을 직접 담는다. 컨테이너 시퀀스보다 메모리를 적게 사용하지만, 문자, 바이트, 숫자 등 기본적인 자료형만 저장할 수 있다.

  - 가변 시퀀스
    - list, bytearray, array.array, collections.deque, memoryview
  - 불변 시퀀스
    - tuple, str, bytes

- 지능형 리스트(list comprehension)를 사용하여 가독성 높은 코드를 작성하자.

  ```python
  >>> colors = ['black', 'white']
  >>> sizes = ['S', 'M', 'L']
  >>> tshirts = [(color, size) for color in colors
              				 for size in sizes]
  [('black', 'S'), ('white', 'S'), ('black', 'M'), ...]
  ```

#### 제너레이터 표현식

> 지능형 리스트와 동일한 구문을 사용하지만, 대괄호 대신 괄호를 사용한다.
>
> 리스트를 생성하는 것이 아닌 하나의 항목씩 생성해서 사용하므로 메모리를 적게 사용한다.
>
> 메모리에 유지할 필요가 없는 데이터를 생성할 때 사용할 수 있다.
>
> 위의 지능형 리스트로 작성한 코드와 비교해보자.

```python
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
>>>     print(tshirt)
black S
black M
black L
white S
white M
white L
```



#### 튜플 언패킹

> 반복형 언패킹(iterable unpacking)이라는 용어가 점점 인기를 끌고 있다.

```python
lax_coordinates = (33.9425, -118.408056)
latitue, longitude = lax_coordinates # 튜플 언패킹
```

> *을 붙여 튜플을 언패킹할 수도 있다.

```python
>>> t = (20, 8)
>>> divmod(*t)
(2, 4)
```

> 전통적으로 _는 gettext.gettext() 함수에 대한 별명으로 사용되었으므로, 상황에 따라 _를 더미변수로 사용하지 않아야 할 수도 있다.



#### 초과 항목을 위한 * 사용

> *는 단 하나의 변수에만 적용할 수 있다.

```python
>>> a, *body, c, d = range(5)
>>> print(a, body, c, d)
0 [1, 2] 3 4
```

```python
>>> a, *body, *c, d = range(5)
>>> print(a, body, c, d)
...
SyntaxError: two starred expressions in assignment
```



#### 명명된 튜플(namedtuple())

> 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수

```python
>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
>>> print(tokyo.population)
>>> print(tokyo.coordinates)
>>> print(tokyo[1])
36.933
(35.689722, 139.691667)
JP
```

- `_fields` , `_make(iterable)` , `_asdict()` 속성

```python
# _fields
>>> print(City._fields)
('name', 'country', 'population', 'coordinates')

# _make()
>>> LatLong = namedtuple('LatLong', 'lat long')
>>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
>>> delhi = City._make(delhi_data)

# _asdict()
>>> print(delhi._asdict())
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
```



#### 리스트와 튜플에서 볼 수 있는 메서드

> `append()`, `pop()`등 몇가지 제외

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = (7, 8, 9)
d = ('x', 'y', 'z')
```

| 메서드                 | 리스트 | 튜플 | 코드                 | 결과                             |
| ---------------------- | ------ | ---- | -------------------- | -------------------------------- |
| `s.__add__(b)`         | O      | O    | `c + d`              | `[7, 8, 9, 'x', 'y', 'z']`       |
| `s.__iadd__(b)`        | O      |      | `a += b`             | `[1, 2, 3, 'a', 'b', 'c']`       |
| `s.clear()`            | O      |      | `a.clear()`          | `[]`                             |
| `s.__contains__(e)`    | O      | O    | `5 in c`             | `False`                          |
| `s.copy()`             | O      |      | `a.copy()`           | `[1, 2, 3]`                      |
| `s.count(e)`           | O      | O    | `c.count(7)`         | `1`                              |
| `s.__delitem__(pos)`   | O      |      | `del a[2]`           | `[1, 2]`                         |
| `s.extend(iter)`       | O      |      | `a.extend((-1, -2))` | `[1, 2, 3, -1, -2]`              |
|                        |        |      | `a.append((-1, -2))` | `[1, 2, 3, (-1, -2)]`            |
| `s.__getitem__(pos)`   | O      | O    | `c[1]`               | `8`                              |
| `s.__getnewargs__()`   |        | O    | 아직                 | 모르겠음                         |
| `s.index(e)`           | O      | O    | `c.index(9)`         | `2`                              |
| `s.insert(pos, e)`     | O      |      | `a.insert(1, 5)`     | `[1, 5, 2, 3]`                   |
| `s.__iter__()`         | O      | O    | `it = iter(c)`       |                                  |
|                        |        |      | `next(it)`           | `7`                              |
|                        |        |      | `next(it)`           | `8`                              |
| `s.__reversed__()`     | O      | O(?) | `it = reversed(c)`   |                                  |
|                        |        |      | `next(it)`           | `9`                              |
|                        |        |      | `next(it)`           | `8`                              |
| `s.__len__()`          | O      | O    | `len(c)`             | `3`                              |
| `s.__mul__(time)`      | O      | O    | `c * 3`              | `[7, 8, 9, 7, 8, 9, 7, 8, 9]`    |
| `s.__imul__(time)`     | O      |      | `a *= 3`             | `[1, 2, 3, 1, 2, 3, 1, 2, 3]`    |
| `s.__rmul__(time)`     | O      | O    | `3 * c`              | 역순으로도 동작하도록하는 메서드 |
| `s.__setitem__(pos,e)` | O      |      | `a[1] = 5`           | `[1, 5, 3]`                      |



#### 슬라이싱

- `a:b:c` 표기법은 `[]` 안에서만 사용할 수 있고, `slice(a, b, c)` 객체를 생성한다.
  - `seq[start:stop:step]` 은 `seq.__getitem__(slice(start, stop, step))`을 호출한다.

- 슬라이싱 활용 예제

```python
invoice = """
0.....6.............................36........46...52....
1909  Pimoroni PiBrella             $17.50    3    $52.50
1489  6mm Tactile Switch x20         $4.95    2     $9.90
1510  Panavise Jr. - PV-201         $28.00    1    $28.00
1601  PiFTF Mini Kit 320x240        $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 36)
UNIT_PRICE = slice(36, 46)
QUANTITY = slice(46, 51)
ITEM_TOTAL = slice(51, None)
line_items = invoice.split('\n')[2:-1]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
```

- 슬라이스로 객체의 값 변화하기

```python
>>> l = list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[3::2] = [11, 22, 33, 44] # 갯수가 맞아야 함
[0, 1, 2, 11, 4, 22, 6, 33, 8, 44]
>>> l[2:5] = [100] # iterable한 형태이어야 함
[0, 1, 100, 22, 6, 33, 8, 44]
>>> del l[::3]
[1, 100, 6, 33, 44]
```



#### 시퀀스에 덧셈, 곱셈하기

- 덧셈 및 곱셈 연산자는 언제나 객체를 새로 만들고, 피연산자를 변경하지 않는다.



#### 리스트의 리스트 만들기 (참조에 관한 이야기)

> 내포된 리스트를 가진 리스트를 만드는 방법에 대해 생각해보자

- 아래의 두가지 표현법은 서로 다르게 동작한다

```python
board_a = [['_'] * 3 for i in range(3)]
board_b = [['_'] * 3] * 3
```

```python
# board_a = [['_'] * 3 for i in range(3)]
board_a = []
for i in range(3):
	row = ['_'] * 3    
    board_a.append(row)
```

```python
# board_b = [['_'] * 3] * 3
board_b = []
row = ['_'] * 3
for i in range(3):
    board_b.append(row)
```



#### 시퀀스의 복합 할당

> `a += b`는 `__iadd__()` 메서드를 호출하여 `a`의 값을 변경한다. (`__iadd__()`가 구현되지 않은경우 `__add__()`를 호출한다.)
>
> `a = a + b`는 `__add__()` 메서드를 호출하여 객체를 새로 생성한 후 `a`에 할당한다.



#### bisect 모듈

> 파이썬에서 제공하는 이진탐색 모듈이다.
>
> `bisect(sequence, x, lo, hi)` 의 형태로 사용하며 이미 정렬된 시퀀스에서 x가 들어가야할 위치에 대한 작업을 한다. `lo`와 `hi`로 범위를 지정해 줄 수 있으며, 시퀀스를 변형시키지 않는다.

- `bisect.bisect_left(seq, x, lo=0, hi=len(seq))`

  x의 위치가 경계(시퀀스 내부의 값과 일치한 경우)보다 왼쪽에 위치한다.

- `bisect.bisect_right(seq, x, lo=0, hi=len(seq))`

  x의 위치가 경계보다 오른쪽에 위치한다.

- `bisect.bisect(seq, x, lo=0, hi=len(seq))`

  `bisect.bisect_right()`와 같이 동작한다.

- `bisect.insort(seq, x, lo=0, hi=len(seq))`

  `seq` 의 정렬을 유지한 채로 `x`를 `seq`에 삽입한다.

- 간단한 예제

```python
>>> import bisect
>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
>>>     index = bisect.bisect(breakpoints, score)
>>>     return grades[index]
>>> [grade(score) for score in [33, 55, 60, 75, 80, 100]]
['F', 'F', 'D', 'C', 'B', 'A']
```

