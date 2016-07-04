defmodule MMax do

    def compare(first, second) when first >= second do
        first
    end

    def compare(first, second) when first < second do
        second
    end

    def reduce([], value, _) do
        value
    end

    def reduce([head|tail], value, func) when value === false do
        reduce(tail, head, func)
    end

    def reduce([head|tail], value, func) when value !== false do
        reduce(tail, func.(head, value), func)
    end
end

IO.puts MMax.reduce([], false, &(MMax.compare/2))
IO.puts MMax.reduce([1], false, &(MMax.compare/2))
IO.puts MMax.reduce([10, 1, 5], false, &(MMax.compare/2))
