defmodule MSum2 do

    def sum(list), do: _sum(list, 0)

    # 私有方法
    defp _sum([], total), do: total
    defp _sum([head|tail], total), do: _sum(tail, total+head)
end
