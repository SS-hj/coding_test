import heapq
def solution(plans):
    answer = []
    arr = []
    temp = []
    for n, s, p in plans:
        h, m = map(int,s.split(":"))
        heapq.heappush(arr, (h*60+m, int(p), n))
    now = arr[0][0]
    while arr:
        # 이전에 못다한 과제 temp가 있고, 아직 다음 과제 시작 시간 전인 경우
        if temp and now < arr[0][0]:
            playtime, name = temp.pop()
            # 남은 과제를 다 마무리 할 수 있는 경우
            if now+playtime <= arr[0][0]:
                answer.append(name)
                now += playtime
            # 현재 과제를 마무리 못하는 경우
            else:
                # 가능한 진행할 수 있는 과제시간
                m = arr[0][0]-now
                temp.append((playtime-m, name))
                now += m
        # 새로운 과제를 시작해야하는 경우
        else:
            start, playtime, name = heapq.heappop(arr)
            now = start
            # 마지막 새로운 과제였을 경우
            if not arr:
                answer.append(name)
            # 남은 과제를 다 마무리 할 수 있는 경우
            elif now+playtime <= arr[0][0]:
                answer.append(name)
                now += playtime
            # 현재 과제를 마무리 못하는 경우
            else:
                # 가능한 진행할 수 있는 과제시간
                m = arr[0][0]-now
                temp.append((playtime-m, name))
                now += m
    while temp:
        answer.append(temp.pop()[1])
    return answer