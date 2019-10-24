require('print_table')


-- os.time()
-- 获取当前时间戳
local t
t = os.time()
print('t:',t)

-- os.date()
-- 将一个表示日期和时间的数字转换为某些高级的表示形式
-- 要么是日期表，要么是字符串

-- os.date 可以使用格式化字符串“*t”, 生成一个日期表
local d1
d1 = os.date("*t", t)
print(d1)
print_table(d1)

-- os.date 根据指定的时间和日期信息对特定的指示符进行替换对应结果的字符串

print(os.date("%Y-%m-%d %H:%M:%S", t))	-- 2019-07-04 10:59:11
print(os.date('%Y-%j', t))				-- 2019-185	2019年的第185天
print(os.date('%c', t))					-- Thu Jul  4 11:11:45 2019


--[[
%a		星期几的简写（例如：Wed）
%A 		星期几的全名（例如：Wednesday）
%b 		月份的简写（例如：Sep）
%B 		月份的全名（例如：September）
%c 		日期和时间（例如：Thu Jul  4 11:10:39 2019)
%d 		一个月的第几天（16）[01-31]
%H 		24小时制中的小时数（23）[00-23]
%I 		12小时制中的小时数（11）[01-12]
%j 		一年中的第几天（185）[001-366]
%m 		月份（07）[01-12]
%M 		分钟（11）[01-59]
%p 		'am' 或 'pm'
%S 		描述（11）[00-60]
%w 		星期（3）[0-6=Sunday-Saturday]
%W 		一年中的第几周（37）[00-53]
%x		日期（例如：07/04/19）
%X 		时间（例如：11:35:27）
%y 		两位数年份（19）[00-99]
%Y 		完整的年份（2019）
%z		时区（例如：+0800, 东八区）
]]--

local y_t = os.time({year=2020, month=12, day=31})
print(os.date('%Y-%m-%d %H:%M:%S', y_t))
print(os.date('%Y-%j', y_t))
print(os.date('%x %X'))
print(os.date('%z', y_t))


