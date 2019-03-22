## NUGU Develop

> 공식문서
>
> C9에서 보면 됌.

Intents - 의도설정

Entity Type -> 

Actions - 동작설정

요청 -> NUGU -> 

intents의 단어를 Entity Type에서 키워드를 묶어서 관리. (미세먼지, 미먼, 황사, PM10)

즉, Entity들이 모여서 Intent의 단어가 됌.



### api 서버 개발

Backend proxy

Intent에 해당하는 Action을 던져주는데 그 Action이 dust(미세먼지 기능).

POST/dust로 던짐 그걸 Django에서 def dust로 받아서 만들어주면 됌.



Django에서 처리한걸 다시 반환할 때

'resultCode : OK'이어야 함

'output: 값'이어야 하는데 json으로 반환해 줘야함.

settings에 APPEND_SLASH 설정이랑 csrf토큰 주석처리 꼭 해야함.

(이미 다른 토큰으로 확인을 하기 떄문)

urls에 path'dust' URL 닫지 말아야함(설정해줬으니)

JsonResponse를 임포트해서 return 해주면 됌 딕셔너리형태로

result = request.POST or {} 하면 딕셔너리를 받으니

result['output'] = {'status':dust..} 와 같이 값을 받을 수 있음.

```html
{
'output' : {
		'input': 55,
		'jdkfajl', 'alskdjflk',
		'location', '강남'
		},
'resultCode':'OK'
}
```

이런식으로..

