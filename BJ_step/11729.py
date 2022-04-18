def hanoi_tower(n, start, end) :
    # 원판이 1개면 2단계인 그냥 원판을 end 포인트에 옮기기만 하면 됨
    if n == 1 :
        print(start, end)
        return
    
    # 1단계
    # 최종 end 포인트 탑이 아닌, 나머지 탑에 모든 원판들이 쌓아지도록 호출
    # 6-start-end ; start와 end 가 아닌 다른 막대
    hanoi_tower(n-1, start, 6-start-end) 
    # 2단계
    # 제일 큰 원판을 end 포인트 탑에 넣어줌
    print(start, end)
    # 3단계
    # 1단계에 옮겼던 원판들이 end 포인트 탑 위로 쌓아지도록 호출
    hanoi_tower(n-1, 6-start-end, end)
    
n = int(input())
print(2**n-1) # 최소로 움직이는 경우의 수
hanoi_tower(n, 1, 3) # 최종적으로 1에 n개의 원판이 3으로 옮겨져야 함