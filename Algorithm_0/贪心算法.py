# 找钱问题
#  t = [100, 50, 20, 5, 1]
def change(t, n):
    m = [0 for _ in range(len(t))]  # 对应的张数
    for i, money in enumerate(t):
        m[i] = n // money  # 找的张数
        n = n % money  # 找完还要找多少钱
        return m, n


print(change([100, 50, 20, 5, 1], 376))

# 背包问题-分数背包
goods = [(60, 10), (100, 20), (120, 30)]  # （价值，重量）
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


# 分包问题
def fractional_package(goods, w):
    m = [0 for _ in range(len(goods))]  # 这是按照排序后的顺序
    total = 0  # 拿走的总价值
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1  # 拿走了全部的
            w -= weight
            total += prize
        else:
            m[i] = w / weight
            w = 0  # 背包被全部占满了
            total += m[i] * prize
            break
    return m, total


print(fractional_package(goods, 50))

# 拼接数字最大问题
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    if x + y < y + x:
        return 1  # y会挪到x前面
    elif x + y > y + x:
        return -1  # y不会挪到x前面
    else:
        return 0


def number_join(li):
    li_str = list(map(str, li))
    li_str.sort(key=cmp_to_key(xy_cmp))  # 升序排序，函数决定要不要转换位置
    print(li_str)
    return ''.join(li_str)  # 返回列表的拼接，以字符串形式返回


print(number_join(li))

# 活动安排
from functools import cmp_to_key

# （开始时间，结束时间）
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
activities.sort(key=lambda x: x[1])  # 按照结束时间进行升序排序


def activitie_selection(a):
    res = [a[0]]  # 最先结束的肯定在里面
    # 依次看后面的，没有冲突继续添加
    for i in range(1, len(a)):
        # 当前活动的开始时间大于等于最后一个入选活动的结束时间
        # 此时满足条件的一定也是相同开始时间结束最早的，前面已经按照结束时间升序排序
        if a[i][0] >= res[-1][1]:
            res.append(a[i])  # 不冲突，将这个活动添加进来
    return res


print(activitie_selection(activities))
