# Question 1.
def calculate(min, max, step):
    sum = 0
    for i in range(min,max+1,step):
        sum += i
    print(sum)

    
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

#=============================================================
# Question 2.
def avg(data):
    length = len(data["employees"])
    num = 0
    total = 0
    
    for i in range(0,length):
        if(data["employees"][i]["manager"] == False):
            total += data["employees"][i]["salary"]
            num += 1
    print(total/num)
            
        
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

#=============================================================
# Question 3.
def func(a):
    def mult(b,c):
        print(a + (b*c))
    return mult


func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#=============================================================
# Question 4.
def maxProduct(nums):
    inf = float('Inf')
    maxlist = [-inf,-inf]       # maxlist = [-inf,max(nums)]
    minlist = [inf,inf]         # minlist = [min(nums),inf]
    
    for i in range(0,len(nums)):
        #找最大兩個值
        if(maxlist[1] <= nums[i]):        # 比最大的大
            maxlist.pop(0)
            maxlist.append(nums[i])
        elif(maxlist[0] < nums[i]):       # 比第二大的大,但比最大的小
            maxlist.pop(0)
            maxlist.insert(0,nums[i])
    
        #找最小兩個值
        if(nums[i] <= minlist[0]):        # 比最小的小
            minlist.pop()
            minlist.insert(0,nums[i])
        elif(nums[i] < minlist[1]):       # 比第二小的小,但比最小的大
            minlist.pop()
            minlist.append(nums[i])
            
    prod1 = maxlist[0] * maxlist[1]
    prod2 = minlist[0] * minlist[1]
    if (prod1 > prod2):
        print(prod1)
    else:
        print(prod2)

        
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

#=============================================================
# Question 5.
def twoSum(nums, target):
    solve = []
    length = len(nums)

    for i in range(0,length):
        diff = target - nums[i]
        if(diff in nums):                       # 搜尋 list會增加時間複雜度 → list 一個坑一個蘿蔔
            solve.extend([i,nums.index(diff)])
            return solve

    
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#--------------------------------------------------------------
# Questuin 5.改
def twoSum(nums,target):
    solve = {nums[0]:0}
    length = len(nums)
    
    for i in range(1,length):
        diff = target - nums[i]
        if(diff in solve):              # 用dict搜尋可降低時間複雜度
            return [solve[diff],i]
        else:
            solve[nums[i]] = i

            
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#=============================================================
# Question 6.
def maxZeros(nums):
    cnt = 0
    length = len(nums)
    cntList = []
    
    for i in range(0,length):
        if (nums[i] == 0):
            cnt += 1
            cntList.append(cnt)
        else:
            cnt = 0
            cntList.append(cnt)

    print(max(cntList))         # 用 max會在搜尋一次 cntList此列表中的元素，增加時間複雜度
#     print(cntList)
    
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3

#--------------------------------------------------------------
# Question 6. 改
def maxZeros(nums):
    cnt = 0
    cntMax = 0                #設一個跟cnt比大小的值，來儲存cnt最大值的時候
    length = len(nums)
    
    for i in range(0,length):
        if(nums[i] == 0):
            cnt += 1
            if(cnt > cntMax):
                cntMax = cnt
        else:
            cnt = 0

    print(cntMax)


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3