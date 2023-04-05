-- Tables are often used as structures (or objects) by using strings as keys. Because such use is very common, Lua features a special syntax for accessing such fields
--
point = {x = 10, y = 20}	-- Create new table
print(point["x"])
print(point.x)	-- has exactly the same meaning as line above
