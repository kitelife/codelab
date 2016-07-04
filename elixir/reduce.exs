defmodule MReduce do
    def reduce([], value, _) do
        value
    end

    def reduce([head|tail], value, func) do
        reduce(tail, func.(value, head), func)
    end
end

IO.puts MReduce.reduce([1, 10, 500], 0, &(&1+&2))
IO.puts MReduce.reduce([], 0, &(&1+&2))
