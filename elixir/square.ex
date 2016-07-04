defmodule MSquare do
    def square([]), do: []
    def square([head|tail]), do: [head*head | square(tail)]
end
