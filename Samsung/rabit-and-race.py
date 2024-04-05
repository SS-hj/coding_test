import heapq

direct = [-1,1,-1,1]

class Race:
    def __init__(self,n,m,p,pid_list,d_list):
        self.n, self.m = n, m
        # d[pid] = d_pid
        self.dist = dict(zip(pid_list, d_list))
        # score[pid] = score_pid
        self.score = dict(zip(pid_list,[0]*p))
        # info = [총 점프 횟수, 현재 행 번호 + 열 번호, 행 번호, 열 번호, 고유번호] heapq
        self.info = []
        for i in range(p):
            heapq.heappush(self.info, [0,2,1,1,pid_list[i]])
    def move(self, k, s):
        check = {} # dict[pid] = (행번호+열번호, 행번호, 열번호, pid 고유번호)
        record = [] # [pid, r+c 점수]
        total_score = 0
        for _ in range(k):
            total_jump, sum_rc, r, c, pid = heapq.heappop(self.info)
            temp = []
            for i in range(4):
                if i<2: # 상하 (n-1)*2의 나머지로 이동
                    d = self.dist[pid]%((self.n-1)*2)
                    nr, nc = r+direct[i]*d, c
                    while nr<=0 or nr>self.n:
                        if nr>self.n:
                            nr = self.n*2 - nr
                        elif nr<=0:
                            nr = nr*-1 +2
                else:   # 좌우 (m-1)*2의 나머지로 이동
                    d = self.dist[pid]%((self.m-1)*2)
                    nr, nc = r, c+direct[i]*d
                    while nc<=0 or nc>self.m:
                        if nc>self.m:
                            nc = self.m*2 - nc
                        elif nc<=0:
                            nc = nc*-1 +2
                temp.append([nr+nc, nr, nc])
            # 4 방향 중 (행번호+열번호,행번호, 열번호) 큰 순으로 가장 높은 칸으로 이동
            sum_rc, r, c = max(temp)
            heapq.heappush(self.info, [total_jump+1, sum_rc, r, c, pid])
            check[pid] = [sum_rc, r, c, pid]
            record.append([pid,sum_rc])
            total_score += sum_rc
        
        # total score 한번에 더함
        for pid in self.score:
            self.score[pid] += total_score
        # k번동안 움직인 토끼들은 해당 점수 인덱싱해서 빼줌
        for pid, sum_rc in record:
            self.score[pid] -= sum_rc
        # (행번호+열번호,행번호, 열번호, pid 고유번호) 큰 토끼 += S 점  (단, k번동안 한번이라도 뽑혔던 토끼로)
        _, _, _, pid = max(check.values())
        self.score[pid] += s
        
    def change_dist(self, pid, L):
        # 고유번호가 pid_t 인 토끼의 이동거리를 L배
        self.dist[pid] *= L
        
    def best_rabbit(self):
        # 가장 높은 점수 출력
        print(max(self.score.values()))

q = int(input())
for _ in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 100:
        n, m, p = temp[1], temp[2], temp[3]
        pid_list = []
        d_list = []
        for i in range(p):
            pid_list.append(temp[4+(2*i)])
            d_list.append(temp[5+(2*i)])
        race = Race(n,m,p,pid_list,d_list)
    elif temp[0] == 200:
        race.move(temp[1], temp[2])
    elif temp[0] == 300:
        race.change_dist(temp[1], temp[2])
    else:
        race.best_rabbit()