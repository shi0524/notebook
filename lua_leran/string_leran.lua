-- lua sting
-- ":" 冒号操作符， 可以像调用字符串的一个方法那样调用字符串标准库中的所有函数


s = 'Hello world! '
-- 求字符串长度
-- string.len(s) 等价于 #s 	也可写成 s:len()
print(string.len(s))
print(s:len())
print(#s)

-- 重复字符串s n次
-- sting.rep(s, n)	也可写成	s:rep(n)

print(string.rep(s, 3))
print(s:rep(3))
-- print(string.rep("a", 2^20))	-- 创建一个1MB大小的字符串

-- 字符串翻转
-- string.reverse()		s:reverse()
print(string.reverse(s))
print(s:reverse())

-- 字符串转换成小写\大写
-- string.lower()
-- string.upper()

print(string.lower(s))
print(string.upper(s))

-- 字符串 提取（切片）,不改变源字符串
-- string.sub()
print(string.sub(s, 1, 5))
print(string.sub(s, 1, -5))
print(string.sub(s, -7, -5))

-- ASCII码转换
-- string.char(49)				接收零个和多个整数作为参数，然后将每个整数转换成对应的字符
-- string.byte(s, i)			返回字符串s中的第i个字符的内部数值表示
-- string.byte(s, i, j)			返回字符串s中的第i个到第j个字符的内部数值表示
print(string.char(49, 52, 99))
print(string.byte(s,2))
print(string.byte(s,2,-1))


-- 字符串格式化
-- string.format()
-- d: 十进制整数
-- x: 十六进制整数
-- f: 浮点数
-- s: 字符串

print(string.format("x = %d y = %d", 10, 20))
print(string.format("x = %x", 200))
print(string.format("x = 0x%X", 200))
print(string.format("x = %f", 200))
tag, title = "h1", "a title"
print(string.format("<%s> %s<%s>", tag, title, tag))
print(string.format("x = %.2f", 200))

-- 字符串查找
-- find
print(string.find(s, "ll"))		-- 3 4
print(string.find(s, "l l"))	-- nil


-- utf8 相关操作

print(utf8.len('12'))
print(utf8.len("人"))
print(string.len("人"))

s = [==[argebgmbps]==]
print(s)



