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

##### 

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

