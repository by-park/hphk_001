# Homework 09

## 2019-01-21

1. HTML은 무엇의 약자인가?

   (3) HyperText Markup Language


2. 다음 중 맞으면 T, 틀리면 F를 기입하시오.

- 웹 표준을 만드는 곳은 Mozilla 재단이다. (x)
- 표(table)을 만들 때에는 반드시 <th> 태그를 사용해야 한다. (x)
- 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. (o)
- 인용문을 가리키는 태그는 <blockquote>이다. (o)



3. 보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된 시맨틱 (semantic) 태그를 모두 선택하시오.

[div, header, h1, section, footer, a, form, span]

> section, article, aside, header, footer, nav 이므로 위의 목록 중에서는 header, section, footer가 해당한다.

4. 아래 이미지와 같은 로그인 화면을 생성하는 html 코드를 작성하시오.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div>
        ID: <input type="text" value="user" />
    </div>
    <div>
    PWD: <input type="text" value="****" />
    <button type="submit">로그인</button>
    </div>
</body>
</html>
```

