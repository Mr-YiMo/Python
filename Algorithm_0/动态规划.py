# 斐波那契数列：递归
def fibonacci(n):
    if n == 1 or n == 2:  # 终止条件
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # 前进


print(fibonacci(5))


# f5 = f4 +f3 A操作：计算前两项
# f4 = f3 +f2 B操作：A操作中的f4计算前两项
# f3 = f2 +f1 C操作：A操作中的f3计算前两项
# f3 = f2 +f1 D操作：B操作中的f3计算前亮相 - 重复计算
# f2 = 1
# f1 = 1


def fibonacci_no_recurision(n):
    f = [0, 1, 1]

    if n <= 1:
        return 1

    for i in range(n - 2):
        num = f[-1] + f[-2]  # 每一项都等于前两项之和
        f.append(num)

    return f[-1]


print(fibonacci_no_recurision(100))

# 钢条切割问题
price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod_recurision(p, n):
    if n == 0:
        return p[0]
    else:
        res = 0
        for i in range(1, n + 1):  # 左边切割，右边不切割。右开导致+1
            # 依次比较n的最优值和组合(i+(n-i))= n的最优值那个大，大的返回
            res = max(res, p[i] + cut_rod_recurision(p, n - i))
    return res


print(cut_rod_recurision(price, 7))


def cut_rod_no_recurision(p, n):
    great = [0]  # 保存最优解
    for i in range(1, n + 1):
        res = 0
        # 计算i之前所有的最优解
        for j in range(1, i + 1):  # 遍历所有的组合
            res = max(res, p[j] + great[i - j])
        great.append(res)  # 保存最优解
        print(great)
    return great[n]


print(cut_rod_no_recurision(price, 10))


def cut_solution(p, n):
    great = [0]  # 保存最优解
    solution = [0]  # 左边的长度
    for i in range(1, n + 1):
        # 计算i之前所有的最优解
        maxV = 0  # 价格最大值
        leave = 0  # 最大价值时左边不切割的长度
        for j in range(1, i + 1):  # 遍历所有的组合
            if maxV <= (p[j] + great[i - j]):
                maxV = (p[j] + great[i - j])
                leave = j
        great.append(maxV)  # 保存最优解
        solution.append(leave)  # 保存当前最优解的左边长度
    return great[n], (solution[n], n - solution[n])


print(cut_solution(price, 10))


# 最长公共子序列


def MaxLength_CommonChildArray(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 下表是从1开始的，判断最后一个字母是否相同
            if x[i - 1] == y[j - 1]:
                #
                c[i][j] = c[i - 1][j - 1] + 1  # 从左上方过来的值
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


def MaxLength_CommonChildArray_Print(x, y):
    # 输出
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 记录当前的箭头: 1-斜箭头  2-上箭头  3-左箭头
    arrow = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 下表是从1开始的，判断最后一个字母是否相同
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1  # 从左上方过来的值
                arrow[i][j] = 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                arrow[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                arrow[i][j] = 3

    return c[m][n], arrow


def lcs_print(x, y):
    c, b = MaxLength_CommonChildArray_Print(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自上方
            i -= 1
        else:  # 来自左方
            j -= 1
    return "".join(reversed(res))

i = 'ABCBDAB'
j = 'BDCABA'

print(lcs_print(i, j))
