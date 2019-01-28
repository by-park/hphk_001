# Workshop 08

## 2019-01-24



Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 '나만의 영어 단어장' 페이지를 만들어 보세요.



```python
from flask import Flask
app = Flask(__name__)

dictionary = {'apple':'사과'}

@app.route("/hello/<name>")
def hello(name):
    if name in dictionary.keys():
	    return str(name)+"은(는) "+str(dictionary[name]) + "!"
    else:
        return str(name)+"은(는) 나만의 단어장에 없는 단어입니다!"
```

