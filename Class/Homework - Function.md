# Homework 05

#### 2019-01-08

1. List는 for문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다. 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

```python
def print_list(my_list):
	for item in my_list:
		print(item)

my_list = ['리스트요소1','리스트요소2','리스트요소3']

print_list(my_list)
```



2. 위에 작성한 코드를 인덱스(index)값과 함께 출력하는 코드로 변경하시오.

```python
def print_list(my_list):
	for index, item in enumerate(my_list):
		print(index, item)
        
print_list(my_list)
```



3. 딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.
   - key: for key in my_dict.keys()
   - value: for value in my_dict.values()
   - key 와 value: for key, value in my_dict.items()



4. result에 저장된 값은?

def my_func(a, b):

​	c = a + b

​	print(c)

result = my_func(1, 5)

> 위를 실행하면 6이 나온다.