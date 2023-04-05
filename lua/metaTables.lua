-- Extensible sematics is a key feature of Lua, and the metatable concept allows Lua's tables to be customized in powerful and unique ways. The following example demonstrates an "infinite" table.
--
fibs = {1, 1} -- Initial values for fibs[1] and fibs[2]
setmetatable(fibs,{
__index = function(name, n)	-- Call this function if fibs[n] does not exist.
	name[n] = name[n-1] + name[n-2]
	return name[n]
end
})

print(fibs[2])
print(fibs[3])
print(fibs[10])

-- Another example, with the __call metamethod to create a Object-Oriented Programming feel
--
newPerson = {}	-- Creates a new table called 'newPerson'

setmetatable(newPerson, {
__call = function(table, name, age)	-- Turns the newPerson table into a functable
	local person = {Name = name, Age = age}	-- Creates a local variable which has all the properties of the person you create later on
	return person
end
})

Bill = newPerson("Bill Raizer", 21)	-- create a new person
print(Bill.Name, Bill.Age)
