import heapq
import sys
input = sys.stdin.readline

N = int(input())
# 중간값보다 작은 값들은 leftHeap(최대힙)에, 큰 값은 rightHeap(최소힙)에 저장
# leftHeap에서 pop을 했을 때 바로 중간값을 구할 수 있도록
rightHeap = []
leftHeap = []
lenMin, lenMax = 0,0
for i in range(N):
    num = int(input())
    if lenMin==lenMax:
        heapq.heappush(leftHeap, -num)
        lenMax += 1
    else:
        heapq.heappush(rightHeap, num)
        lenMin += 1
    # leftHeap의 최대값이 rightHeap의 최소값보다 크다면, leftHeap에 중간값보다 큰 값이 들어가게 되므로
    # leftHeap의 최대값과 rightHeap의 최소값 교체
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        a = -heapq.heappop(rightHeap)
        b = -heapq.heappop(leftHeap)
        heapq.heappush(leftHeap, a)
        heapq.heappush(rightHeap, b)
    print(-leftHeap[0])