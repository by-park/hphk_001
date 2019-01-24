# workshop05

#### 2019-01-08

1. Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ' a', 'nan', '토마토' 모두 palindrome에 해당합니다. 따라서, 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

```python
def palindrome(word):
	if word == word[::-1]:
		print(True)
	else:
		print(False)
```



선생님 답

```python
def is_palindrome(word):
    list_word = list(word)
    for i in range(len(list_word)//2):
        if list_word[i] != list_word[-i-1]: # i=0, 0과-1비교, i=1, 1과-2비교
            return False
    return True

print(is_palindrome('level'))
print(is_palindrome('apple'))
```

