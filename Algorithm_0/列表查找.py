import time

def get_time(f):
    def inner(*arg,**kwarg):
        s_time = time.time()
        res = f(*arg,**kwarg)
        e_time = time.time()
        print('耗时：{%.5f}秒' %(e_time - s_time))
        return res
    return inner


li = [1,2,3,4,5,96,55,45]


#顺序查找，线性查找
@get_time
def linear_search(list,val):
    for ind,dest in enumerate(list):
        if dest== val:
            return ind
    else:
        return None

# print(linear_search(li,55))


#二分查找，前提是有序
@get_time
def dehalf_search(list,val):
    lt = list.sort()
    left = 0
    right = len(li)-1
    while left<=right:#区间内还有候选值
        mid = (left+right)//2 #总是向下整取
        if list[mid] == val:
            return mid
        elif list[mid]>val:
            right = mid-1
        else: #mid<val
            left = mid+1
        print(left, right, mid)
    else:
        return None

print(dehalf_search(li,55))