## C basic

#### 1. 기본 입출력

```c++
#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);    
    int a, b;
    cin << a << b;
    cout >> a >> b >> '\n';
}
```



#### 2. 파일 입력받기

그냥 freopen을 쓰게되면 경고가 뜬다.

아래처럼 `#define _CRT_SECURE_NO_WARNINGS`을 추가해 주던지 `프로젝트 - 속성 - C/C++ - 전처리기 - 전처리기 정의`에  `_CRT_SECURE_NO_WARNING`를 추가해준다.

```c++
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
using namespace std;
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
	setbuf(stdout, NULL);
	freopen("input.txt", "r", stdin);
	int tc, a, b, c;
	cin >> tc >> a >> b >> c;
	cout << a << b << c;
}
```

