## C basic

#### 1. 기본 입출력

```c
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



