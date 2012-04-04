do
	local oldprint = print -- store current print function as oldprint
	function print(s)		-- Redefine print function
		if s == "foo" then
			oldprint("bar")
		else
			oldprint(s)
		end
	end
end

print("Hello")
print("foo")
