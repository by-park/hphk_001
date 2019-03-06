# 기존의 일급 객체 함수 사용법
print(list(map(int, ["1", "2"])))

# 일급 객체 함수 직접 만들어보기
# my_map(함수, 리스트):
def my_map(func, input_list):    
    # 0. 빈 리스트를 만들고
    # 1. 인자로 받은 리스트를 돌면서
    # 2. 인자로 받은 함수를 각각의 요소에 적용한 값을
    #    빈 리스트에 넣어서
    # 3. 빈 리스트를 리턴한다.
    new_list = []
    for item in input_list:
        new_list.append(func(item))
    return new_list
    
    # list comprehesion 버전
    # return [func(x) for x in input_list]

print(my_map(int, ["1", "2", "3"]))
print(my_map(str, [1, 2, 3]))

# filter 함수 사용법
def is_even(num):
    return num % 2 == 0
print(list(filter(is_even, [1, 2, 3, 4])))

# my_filter(참, 거짓을 리턴해주는 함수, 리스트)
def my_filter(func, input_list):
    empty_list = []
    for item in input_list:
        if func(item):
            empty_list.append(item)
    return empty_list

    # list comprehension 버전
    # return [x for x in input_list if func(x)]

print(my_filter(is_even, [1, 2, 3, 4, 5]))

# 람다 사용법
print(my_filter(lambda num: num % 2 ==0, [1, 2, 3, 4, 5]))