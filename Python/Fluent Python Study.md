## 파이썬 심화

> 191223 전문가를위한 파이썬 읽기 시작

### 1. 파이썬 데이터 모델

##### 1.1 파이썬 카드 한 벌

> 아래와 같이 파이썬을 이용한 카드 모델을 구성할 수 있다.

- namedtuple을 사용해 tuple에 의미를 부여했다.
- _변수명은 private하게 선언한 것이다. `from module import *` 사용시 호출되는 것을 막을 수 있다. 하지만 직접 호출시에는 호출이 되므로 "weak internal use indicator"라고 부르기도 한다.

```python
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

