## Python Sequence

> Fluent Python 2장 공부



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