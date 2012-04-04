-- By using a table to store related functions, it can act as a namespace
--
Point = {}
Point.new = function (x, y)
	return {x=x, y=y}
end
Point.set_x = function (point, x)
	point.x = x
end

Point= Point.new(10, 20)
print(Point.x..","..Point.y)
--Point.set_x(Point, 30)
--print(Point.x)
