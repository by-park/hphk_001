import numpy as np
array = np.random.randint(25, size=(5, 5))
array = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
# 행
total_sum = 0
for i in range(5):
    # 열
    for j in range(5):
        left = abs(array[i][j] - array[i][j-1]) if j >= 1 else 0
        right = abs(array[i][j] - array[i][j+1]) if j <= 3 else 0
        up = abs(array[i][j] - array[i-1][j]) if i >= 1 else 0
        down = abs(array[i][j] - array[i+1][j]) if i <= 3 else 0
        total_sum += left+right+up+down
print(total_sum)

# 선생님 코드

def calAbs(y,x):
    if y-x > 0: return y-x
    else: return x-y

def isWall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]

            # 0~4까지니까 그 외에는 벽이다. 패딩은 하면 안 됨 절대값 차이 필요해서
            if isWall(testX, testY) == False:
                sum += calAbs(arr[x][y], arr[testX][testY])

print("sum = %d" %sum)
