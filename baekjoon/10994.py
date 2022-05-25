n = int(input())

'''
1 + 4*(n-1) == 4*n-3
1 + 2*(n-1) ==  2*n-1 ; 정가운데
'''
arr = [[' ']*(4*n-3) for _ in range(4*n-3)]
mid = 1 + 2*(n-1)
arr[mid-1][mid-1] = '*'

def draw(num):
    if num == 1:
        return
    else:
        top = left = mid - 2*(num-1) -1
        bottom = right = mid + 2*(num-1) -1
        for i in range(4*n-3): # 행
            for j in range(4*n-3): # 열
                if i == top or i == bottom:
                    if left<=j<=right:
                        arr[i][j] = '*'
                if j == left or j == right:
                    if top<=i<=bottom:
                        arr[i][j] = '*'
        draw(num-1)
draw(n)

for a in arr:
    print(''.join(a))