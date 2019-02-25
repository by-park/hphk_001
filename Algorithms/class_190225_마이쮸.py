candy = 20
Q = [0] * (candy*candy) # 인덱스 문제
candynum = [1] * (candy*candy) 
front = -1
rear = 0
student = 0 # 입장하는 학생
#Q[front+1] =student + 1 # 1번 학생이 처음에 들어감

print("마이쮸 증정식을 시작합니다")
print("==================")

while candy > 0:
#for student in range(candy):
    if front == -1: # 교실에 학생이 아직 안 들어왔으면
        print("첫 번째 학생 입장!")
        front += 1
        Q[front] = student + 1 # 0번째에 1 학생 들어옴
        candy -= candynum[Q[front]-1] # 1학생이 받아야하는 수 1개를 받아감
        candynum[Q[front]-1] += 1 # 다음 번에는 2개를 받아야함
        print("{}번 학생이 {}를 받아가서 {}가 남았습니다".format(student+1, candynum[Q[front]-1]-1, candy))
        rear += 1 # 1번이 들어와서 뒤에 한 칸 더 생겨야함
    
    # 교실에 학생이 있는 경우
    # 맨 앞에 서있는 애가 마이쮸를 또 받아감

    print(Q)
    
    front += 1
    Q[front] = Q[front-1] # 증가한 자리에 또 들어옴
    candy -= candynum[Q[front]-1] # 1학생이 받아야하는 수 2개를 받아감
    candynum[Q[front]-1] += 1 # 다음 번에는 3개를 받아야함
    print("{}번 학생이 {}를 받아가서 {}가 남았습니다".format(Q[front], candynum[Q[front]-1]-1, candy))
    
    # 받은 후 개수 체크
    if candy < 1:
        print(Q[front])
        break

    print(Q)
    
    # 맨 앞에 서있는 애가 맨 뒤로 감
    print("{}번 학생은 뒤로 가서 줄을 섭니다.".format(Q[front]))
    rear += 1
    Q[rear] = Q[front]
    front += 1 # 1이 거기서 나옴

    print(Q)
    # 새로운 학생이 들어옴
    student += 1
    print("{}번 학생 입장합니다.".format(student+1))
    rear += 1
    Q[rear] = student +1
