A = [1,2,3,4]
B = []
C = []


def hanoi(n, A, B, C):
    if n == 1:  # 终止条件
        C.append(A.pop())
        return
    else:
        hanoi(n - 1, A, C, B)  # 将A经过C移动到B
        print(n,A,B,C)
        C.append(A.pop())  # 此时A还剩下最大的盘子，将这个盘子移动到C
        hanoi(n - 1, B, A, C)  # 将B通过A移动到最后一根C


hanoi(len(A), A, B, C)  # 递归调用
print(A, B, C)