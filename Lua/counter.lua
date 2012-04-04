function create_a_counter()
	local count = 0
	return function()
		count = count + 1
		return count
	end
end

counter = create_a_counter()

print(counter())
print(counter())
print(counter())
print(counter())
