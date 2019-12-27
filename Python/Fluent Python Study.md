## 파이썬 심화

> 191223 전문가를위한 파이썬 읽기 시작

### 1. 파이썬 데이터 모델

> 아래와 같이 파이썬을 이용한 카드 모델을 구성할 수 있다.

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

###### 1.1 namedtuple

- collections의 namedtuple을 사용해 tuple에 의미를 부여할 수 있다.

  ```bash
  >>> beer_card = Card('7', 'diamonds')
  >>> beer_card
  Card(rank='7', suit='diamonds')
  ```

###### 1.2 private? 변수

- _변수명을 사용해 private하게 선언할 수 있다. `from module import *` 사용시 호출되는 것을 막을 수 있다.  하지만 완전한 private는 아니므로 직접 호출은 가능하다.

  ```bash
  >>> deck = FrenchDeck()
  >>> deck._cards[2]
  Card(rank='4', suit='spades')
  ```

###### 1.3 특별메소드

- 기본적인 언어 구조체를 사용할 수 있게 해준다. 직접 구현해야 하는 함수들을 특별메소드를 이용해 구현하면 파이썬 언어의 구조체와 같이 사용할 수 있다.

  ```bash
  >>> len(deck)
  52
  >>> deck[2]
  Card(rank='4', suit='spades')
  ```

  

