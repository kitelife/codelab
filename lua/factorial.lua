-- The factorial is an example of a recursive function
--
function factorial(n)
	if n == 0 then
		return 1
	else
		return n * factorial(n - 1)
	end
end

print("factorial(10):"..factorial(10))
