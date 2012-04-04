-- Tables are always passed by reference
--
a_table = {x = 10}
print(a_table["x"])
b_table = a_table
b_table["x"] = 20
print(b_table["x"])
print(a_table["x"])

-- We can insert/remove values/indexes from tables, as well.

local myTable = {"a", "b"}
print(unpack(myTable))

table.insert(myTable, "c")
print(unpack(myTable))

table.remove(myTable, 2)
print(unpack(myTable))
