defmodule Outer do
    defmodule Inner do
        def inner_func do
            "inner_func"
        end
    end

    def outer_func do
        Inner.inner_func
    end
end

IO.puts Outer.outer_func
IO.puts Outer.Inner.inner_func
