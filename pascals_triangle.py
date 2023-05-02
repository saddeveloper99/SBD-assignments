'''
        line1 = [1]
      line2 = [1, 1]
     line3 = [1, 2, 1]
   line4 = [1, 3, 3, 1]
  line5 = [1, 4, 6, 4, 1]
line6 = [1, 5, 10, 10, 5, 1]

n = n번째 줄
n번째 줄의 원소의 개수도 n


'''
# n번째 라인의 i번째 원소 > n-1번째 파스칼[i-1] + n-1번째 파스칼[i]
# 예상되는 문제점 : 그럼 인덱스가 모자라면, indexerror?
# try except로 [1]을 배열에 추가하면?   

# 막상 해보니 초기값을 줘서 IndexError는 발생하지 않음.
# 그냥 마지막에 1만 추가해주면 된다.

# [1] + [구해야 하는 부분] + [1]이므로
# 구해야 하는 부분은 n-2개 > range를 하나 적게
# 처음 1은 배열에 초기값으로 주고, 마지막 1은 for문이 끝난 뒤 더해준다.

def pascal_line(n):
    if n == 1:
        return [1]
    if n > 1:
        row = [1]
        prev_pascal = pascal_line(n-1)
        for i in range(1, len(prev_pascal)):
            row.append(prev_pascal[i-1] + prev_pascal[i])
        row.append(1)
        return row


def pascal_tri(n):
    for i in range(1, n+1):
        print(pascal_line(i))


pascal_tri(7)
print(pascal_line(8))