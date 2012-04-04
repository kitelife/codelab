-- Although Lua does not have a built-in concept of classes,
-- they can be implementd using two language features: first-class functions and tables.
-- By placing functions and related data into a table, an object is formed
--
-- Inheritance(both single and multiple) can be implemented via the metatable mechanism,
-- telling the object to lookup nonexistent methods and fields in parent object(s).
--
-- Lua provides some syntactic sugar to facilitate object orientation. To declare member functions inside a prototype table, one can use function table:func(args), which is equivalent to function table.func(self, args). Calling class methods also make use of the colon: object:func(args) is equvialent to object.func(object, args).
--
Vector = {}	-- Create a table to hold the class methods
function Vector:new(x,y,z)	-- The constructor
	local object = {x = x, y = y, z = z}
	setmetatable(object,{__index = Vector})	-- Inheritance
	return object
end

function Vector:magnitude()	-- Another member function
	-- Reference the implicit object using self
	return math.sqrt(self.x^2 + self.y^2 + self.z^2)
end

vec = Vector:new(0, 1, 0)	-- Create a vector
print(vec:magnitude())	-- Call a member function using ":"
print(vec.x)	-- Access a member variable using "."
