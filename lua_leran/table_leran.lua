-- table

function print_table( t )
	print("")
	print("---------print table start--------")
	for k, v in pairs(t) do
		print(k, v)
	end
	print("----------print table end---------")
end

function print_table2( t )
	print("")
	print("---------print table start--------")
	for k, v in ipairs(t) do
		print(k, v)
	end
	print("----------print table end---------")
end

-- 定义table

local t = {
	x = 1,
	y = 2,
	11,
	22,
	[3] = 300,
	-- [4] = 300,
	[5] = 500,
	['z'] = 3,
}

print(t.x)
print(t.y)
print(t[1])
print(t[2])
print(t.z)
print(t['z'])
print(t[3])

for i = 1, #t do
	print(i, t[i])
end

local t = {
	color = 'blue',
	thinckness = 2,
	{x=0, y=0},
	{x=-1, y=5},
}

print(t)
print(t[1])
print(t.color)
print(t['thinckness'])

t[-1] = 5

print(t[-1])

local a = {}
a[1] = 1
a[1000] = 1000
a['a'] = 10000

for i = 1, #a do
	print(#a, i, a[i])
end

for k, v in pairs(a) do
	print(k, v)
end

for k, v in ipairs(a) do
	print(k, v)
end

print('********** table 标准库 ***********')

-- table 标准库

-- table.insert

t = {10, 20, 30}

table.insert(t, 1, 100)

for k, v in ipairs(t) do
	print(#t, k, v)
end

table.remove(t, 1)
print_table(t)

-- table.move(t, 1, #t, 3)
table.move(t, 2, #t, 1)
t[#a] = nil

print_table(t)

a = {}
a.a = a
print(1111111111111, a.a.a.a, #a.a.a.a)
print(a)

a.a.a.a = 3
-- print_table(a)
print(a.a)

local t = {1, 3, 5, 7, 9, a=2, b=4, c=6, d=8, f=10, 11, 13, 15, 17, 19}

print_table(t)
print_table2(t)