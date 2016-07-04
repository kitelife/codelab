defmodule MSum3 do
    def sum([]), do: 0
    def sum([head|tail]), do: head + sum(tail)
end

IO.puts MSum3.sum []
IO.puts MSum3.sum [1, 100, 2]
