(define (biggestInThree x y z) 
  (if (> x y)
      (if (> y z)
          x
          (if (> x z)
              x
              z))
      (if (> y z)
          y
          z)
        ))
(biggestInThree 1000 100 100)