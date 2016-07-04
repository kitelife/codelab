defmodule MSum do
    def sum([], total), do: total
    def sum([head|tail], total), do: sum(tail, total+head)
end
