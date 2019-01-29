# 데이터베이스 ORM

## 2019-01-29



flask_sqlalchmy라는 모듈을 사용해서 데이터베이스를 ORM으로 변형할 것이다. 객체를 다루도록 해서 완전히 파이썬 코드로만 데이터베이스를 조작할 수 있다. 

플라스크 서버에서 데이터베이스 ORM에 접근하고 수정할 수 있도록 하기 위하여 다음과 같이 코드를 작성하였다.



_app.py_

```python
# app.py
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Flask 클래스의 인스턴스
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app) # app과 orm이 하나가 된다.

class Quest(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String, nullable=False)

db.create_all()

@app.route('/')
def index():
    # DB에 저장된 모든 질문들을 불러온다. (quest들의 묶음)
    quests = Quest.query.all() # query를 날려서 데이터베이스에 담긴 모든 애들을 데려온다.
    return render_template('index.html', quests = quests)

@app.route('/ask')
def ask():
    # 데이터베이스에 저장
    q = request.args.get('question')
    # INSERT INTO questions (id, content) VALUES (1, 사용자가 입력한 값)
    # ORM을 통해 DB에 데이터를 저장하는 방법
    quest = Quest(content = q)    
    db.session.add(quest) # 추가하고
    db.session.commit() # 실제로 데이터 베이스에 기록 (깃에서도 save에 가깝다 실제로 저장)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    # 특정 데이터 레코드 (한 행)를 지워준다.
    # DELETE FROM questions WHERE id == 1
    q = Quest.query.get(id) # id == 1인 객체가 q에 들어가있음
    # = Quest.query.filter_by(id=id).first()
    db.session.delete(q)
    db.session.commit()
    return redirect('/')
```



_index.html_

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
    <h1>익명 질문 앱</h1>
    <p>익명으로 질문하세요.</p>
    <form action="/ask"> <!--ask라는 route로 넘어갈 것이다-->
        <input type="text" name="question"></input>
        <input type="submit" value="submit"></input>
    </form>
    <!--quests(리스트)안에 담긴 모든 질문 객체들을 보여준다-->
    {% for q in quests %}
        <p>{{ q.id }} : {{ q.content }}<a href="/delete/{{ q.id }}">[삭제]</a></p>
    {% endfor %}
</body>
</html>
```

