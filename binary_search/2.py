import sys
n = int(input())
n_list = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(input())
m_list = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색 소스코드 (반복문 사용)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간 인덱스 반환
        if array[mid] == target:
            return mid
		# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽으로
        elif array[mid] > target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽으로
        else:
            start = mid + 1
    return None

n_list.sort()

for i in m_list:
    res = binary_search(n_list, i, 0, n-1)
    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')