defmodule MMapSum do
    def mapsum(list, func) do
        MMap.map(list, func)
            |> MSum2.sum
    end
end

IO.puts MMapSum.mapsum([], &(&1+10))
IO.puts MMapSum.mapsum([1, 2, 3], &(&1+10))
IO.puts MMapSum.mapsum([1, 2, 3], &(&1*&1))
