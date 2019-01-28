# Homework 10

## 2019-01-21

1. CSS는 무엇의 약자인가?

(2) cascading style sheets



2. 다음 중 맞으면 T, 틀리면 F를 기입하시오.

- HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. (T)
- 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. (T)
- 자식요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다.(F)



3. 크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데, 이를 예방하기 위해 HTML  최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

> rem



4. 다음 예제를 통해 "후손 셀렉터"와 "자식 셀렉터"의 차이를 설명하시오.

```html
/*후손 셀렉터*/
div p{
color: crimson;
}
/*자식 셀렉터*/
div > p{
color:crimson;
}
```

> 후손 셀렉터는 자식, 손자, 그 이후의 모든 후손을 포함한다. div 이내에 있는 p  요소는 모두 crimson색으로 지정이 된다. 자식 셀렉터는 특정 요소의 직계 자식만 선택하는 선택자이다. div 이내에 있는 직계 자식 p만 crimson 색으로 표시 된다. [출처](https://aboooks.tistory.com/286)