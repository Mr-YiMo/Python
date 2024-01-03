import random
import sys

sys.setrecursionlimit(100000)


# 冒泡排序，一共会走N-1趟，复杂度n^2
def bubble_sort(arr):
    for i in range(len(arr) - 1):  # 趟数
        counter = False
        for j in range(len(arr) - i - 1):  # 每一趟需要对比的次数
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter = True
        # 上一趟没有发生数据交换认为已经排序完成，
        if counter is False:
            break


array = [random.randint(0, 1000) for i in range(10)]
print(array)
bubble_sort(array)
print(array)


# 选择排序：每次取最小的放到新的列表中，新开内存，时间复杂度O(N^2)
def select_sort(arr):
    print("选择排序：")
    arr_new = []  # 缺点一：多占了内存
    for i in range(len(arr)):
        min_val = min(arr)  # 缺点二：不是O(1)的操作
        arr_new.append(min_val)
        arr.remove(min_val)  # 缺点二：不是O(1)的操作，时间复杂度会增加
    return arr_new


# 选择排序优化：不新开内存，时间复杂度O(N^2)
def select_sort_upgrade(arr):
    print("选择排序-升级版：")
    for i in range(len(arr) - 1):  # 第几趟
        min_loc = i  # 假设最小数为无序区的第一个数
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_loc]:
                min_loc = j
        arr[i], arr[min_loc] = arr[min_loc], arr[i]


array = [random.randint(0, 1000) for i in range(10)]
print(array)
print(select_sort(array))  # 原本array里面的值全部被remove

array = [random.randint(0, 1000) for i in range(10)]
print(array)
select_sort_upgrade(array)
print(array)


# 插入排序：类似于打牌中插牌的过程,O(n^2)
def insert_sort(arr):
    print("插入排序：")
    for i in range(1, len(arr)):  # i表示摸到的牌的下标，手里已经有一张
        temp = arr[i]
        j = i - 1  # 手里的牌的下标
        print('摸到的牌：', arr[i],'手里的牌', arr[j])
        while arr[j] > temp and j >= 0:  # 当j为0的时候代表第一张牌的位置，移动之后就结束
            arr[j + 1] = arr[j]  # 手里的牌依次往右挪
            j -= 1  # 把j往左移
            print('移动', arr)
        arr[j + 1] = temp  # 将抽到的牌插入右移后空出来的位置


array = [random.randint(0, 1000) for i in range(10)]
print(array)
insert_sort(array)
print(array)


# 快速排序：递归，时间复杂度nlog(n),每一层是logn，一共有a层，可以视为n，实际a比n小；最坏的情况是n^2,可以先随机化再排序
def partition(li, left, right):
    temp = li[left]  # 先抽第一张
    while left < right:  # 判断双指针，递归的结束条件
        # 先从后往前
        while li[right] >= temp and left < right:  # 从后往前找，找比temp小的数,使用left<right来确保当所有数比第一张大时，内存不溢出
            right -= 1  # 再往左看一个
        li[left] = li[right]  # 如果数组内所有的数都比li[left]大或者找到了，把右边的值写到左边
        print("右边找完：", li)
        # 再从前往后
        while li[left] <= temp and left < right:  # 从前往后找，找比temp大的数,使用left<right来确保当所有数比第一张大时，内存不溢出
            left += 1
        li[right] = li[left]  # 如果数组内所有的数都比li[right]小或者找到了，把左边的值写到右边
        print("左边找完：", li)

    # 执行完后保证左边的全部比temp小，右边全部比temp大，然后继续下一张牌【】这张牌还是第一张
    li[left] = temp  # 把原来的值写到空白的地方
    return left  # 返回middle的值


def quick_sort(li, left, right):
    if left < right:  # 至少有两个元素
        mid = partition(li, left, right)  # 被分成两部分，继续递归调用来排序这两部分(这两部分可能不相等)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print("快速排序：")
quick_sort(li, 0, len(li) - 1)
print("找完：", li)


# 堆排序

# 向下调整一次：默认已经是按照大根堆的形式建立了堆 时间复杂度：n*log(n)
def shift(li, Top, Low):
    # Top:堆顶的位置下标
    # Low:最有一个没有检查的位置下标
    i = Top  # 另存堆顶的下标
    j = 2 * i + 1  # 先看左孩子的下标
    tmp = li[i]  # 另存堆顶
    while j <= Low:  # 只要孩子节点存在，不超过最后一个节点的下标
        if j + 1 <= Low and li[j + 1] > li[j]:  # 如果右孩子比左孩子大，并且右孩子存在
            j = j + 1  # j放在右孩子上
        if li[j] > tmp:
            li[i] = li[j]  # 互换位置
            # 更新下标，继续下一层
            i = j
            j = 2 * i + 1
        else:  # tmp更大
            li[i] = tmp  # 放到某一级领导的节点上面
            break
    else:  # 没有孩子节点了
        li[i] = tmp  # 放到某一级领导的节点上面


def heap_sort(li):
    # 第一步：利用向下调整建堆，农村包围城市
    n = len(li)
    for i in range(((n - 1) - 1) // 2, -1, -1):
        shift(li, i, n - 1)

    # 建堆完成，挨个出数，先出省长
    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个位置
        li[0], li[i] = li[i], li[0]
        shift(li, 0, i - 1)  # i-1是新的最后元素的下标

    # 完成


array = [random.randint(0, 100) for i in range(10)]
print("堆排序", array)
heap_sort(array)
print("序完成", array)

# import heapq
# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# heapq.heapify(array)  # 建堆
# for i in range(len(array)):
#     print(heapq.heappop(array), end=',')  # 每次拿出最小的值，重新存到新列表中就可以了


# 归并排序：将一个大数组划分为两部分，然后依次进行合并，合并过程中再进行比较排序下，时间复杂度nlog(n)：logn层二叉树，每层n

# 一次归并：两段列表都是有序的
def merge(li, low, mid, high):
    i = low  # 第一个数下标
    j = mid + 1  # 第二个数下标
    ltmp = []  # 临时列表
    while i <= mid and j <= high:  # 左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1  # 更新i的下标
        else:
            ltmp.append(li[j])
            j += 1  # 更新i的下标
    # 执行完后，两部分有一部分没数了，将剩下的继续存到ltmp中
    while i <= mid:
        ltmp.append(li[i])
        i += 1

    while j <= high:
        ltmp.append(li[j])
        j +=1
    # 重新写回
    li[low:high + 1] = ltmp

li  = [2,4,5,7,1,3,6,8]
merge(li,0,3,7)
print(li)

# 递归归并
def merge_sort(li, low, high):
    if low < high:  # 至少有两个数,递归的终止条件
        mid = (low + high) // 2
        merge_sort(li, low, mid)  # 递归左边,直到一个数就是一个分组，然后返回依次归并，归并的过程中排序
        merge_sort(li, mid + 1, high)  # 递归右边
        merge(li, low, mid, high) #合并

array = [random.randint(0, 100) for i in range(10)]
print('归并排序', array)
merge_sort(array,0,len(array)-1)
print('排序完成', array)
