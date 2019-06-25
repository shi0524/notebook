-- 函数

-- 多返回值(接收个数)

function func_1( )
	return 1, 2, 3
end

print(func_1())

a, b = func_1()

print(a, b)

a, b, c, d = func_1()
print(a, b, c, d)

-- 可变长参数 ... 表示函数的参数是可变长的
-- 表达式 {...} 的结果是可编程参数组成的列表

function func_add( ... )
	local s = 0
	for _, v in ipairs({...}) do
		s = s + v
	end
	return s
end

print(func_add(3, 2, 4))


-- table.pack
-- 像表达式{...}一样保存了所有的参数， 还保存了参数个数的额外参数n

function func_nonils( ... )
	local arg = table.pack(...)
	for i = 1, arg.n do
		if arg[i] == nil then
			return false
		end
	end
	return true
end

print('========================')
print(func_nonils(1,2,3,nil))

-- select 
-- 拥有一个参数 selector
-- selector 是数值n,函数返回第n个参数后的所有参数
-- selector 是 "#" ,返回额外参数的总数

require('print_table')

local t = {'a', 'b', 'c', 'd', 'e'}
print('========================')

print(select(2,table.unpack(t)))
print('========================')

-- print_table(select(2, t))


-- print_table(select(2, t))


