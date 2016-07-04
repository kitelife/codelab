defmodule MCaesar do
    @z_value 122
    defp _checkValue(beforeAdd, afterAdd) when afterAdd > @z_value do
        beforeAdd
    end

    defp _checkValue(_, afterAdd) when afterAdd <= @z_value do
        afterAdd
    end

    def caesar([], _) do
        []
    end

    def caesar([head|tail], n) do
        [_checkValue(head, head+n) | caesar(tail, n)]
    end
end

IO.puts MCaesar.caesar('ryvkvez', 1)
IO.puts MCaesar.caesar('', 10)
