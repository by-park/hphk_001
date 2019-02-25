candy = 20
Q = [0] * (candy*candy) # 인덱스 문제
candynum = [1] * (candy*candy) 
front = -1
rear = 0
student = 1 # 입장하는 학생
#Q[front+1] =student + 1 # 1번 학생이 처음에 들어감

print("마이쮸 증정식을 시작합니다")
print("==================")

while candy > 0:
#for student in range(candy):
    if front == -1: # 교실에 학생이 아직 안 들어왔으면 & 1번 학생까지는 여기에 해당
        ("첫 학생 입장!")
        front += 1
        Q[front] = student # 0번째에 1 학생 들어옴
        candy -= candynum[Q[front]-1] # 1학생이 받아야하는 수 1개를 받아감
        candynum[Q[front]-1] += 1 # 다음 번에는 2개를 받아야함
        print("{}번 학생이 {}를 받아가서 {}가 남았습니다".format(student, candynum[Q[front]-1]-1, candy))
    
    # 새로운 학생이 들어옴
    student += 1 # 1번 들어옴
    print("{}번 학생 입장합니다.".format(student))
    rear += 1
    Q[rear] = student

    # 맨 앞에 서있는 사람이 마이쮸 받아감    
    candy -= candynum[Q[front]-1] # 1학생이 받아야하는 수 2개를 받아감
    candynum[Q[front]-1] += 1 # 다음 번에는 3개를 받아야함
    print("{}번 학생이 {}를 받아가서 {}가 남았습니다".format(Q[front], candynum[Q[front]-1]-1, candy))
    
    # 받은 후 개수 체크
    if candy < 1:
        print(Q[front])
        break
    
    # 맨 앞에 서있는 애가 맨 뒤로 감
    print("{}번 학생은 뒤로 가서 줄을 섭니다.".format(Q[front]))
    rear += 1
    Q[rear] = Q[front]
    front += 1 # 1이 거기서 나옴

# for문으로 잘 못 생각한거
# index -1 로 써야하는 거 그렇게 안 쓴거
# student 변수 이후에는 que에 있는 것을 사용했어야하는데 자꾸 student 변수를 사용한 것
