def solution(sequence):
    n = len(sequence)
    a, b = [0]*n, [0]*n
    for i in range(n):
        a[i] = max(0,a[i-1])+sequence[i]*(-1)**i
        b[i] = max(0,b[i-1])+sequence[i]*(-1)**(i+1)
    return max(max(a),max(b))