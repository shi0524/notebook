require("print_table")
-- 控制结构

-- if then else end

local a = -1
if a < 0 then a=0 end

print(a)

local b = 100

function test_max(a, b)
	if a < b then return b else return a
	end
end

print(test_max(101, 13))


-- while do

local i = 5

while i > 0 do
	print(i)
	i = i -1
end

-- repeat until
-- 重复执行循环体，直到条件为真时结束
-- 区别于 while 先执行循环体，再判断条件，故至少会执行一次


function test_repeat(a)
	local n = 10
	repeat a = a*a
		n = n - 1
	until a >= 100000 or a < 0.00001 or n <= 0
	return a
end
print(test_repeat(10))
print(test_repeat(1))
print(test_repeat(0.9))


-- for
-- for 语句有两种形式： 数值型for 和 泛型for

-- 数值型 for 语法
-- for var = exp1, exp2, exp3 do
-- 	something
-- end

for i=1, 10 do
	print(i)
end

for i=3, 30, 3 do
	print(i)
end

-- 泛型for
-- 泛型for遍历迭代函数返回的所有值

local test_table ={3,5,10,[1]=1,a=1}
print(test_table)
print_table(test_table)
local t = {1, 3, 5, 7, 9, a=2, b=4, c=6, d=8, f=10, 11, 13, 15, 17, 19}
print(t)


local test_table ={[1]=4,3,5,10,[1]=1,a=1}
print(test_table)
print_table(test_table)
local test_table ={["a"]=1,a=3}
test_table["a"] = 4
test_table.a = 9


print_table(test_table)







