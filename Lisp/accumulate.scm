;Exercise 4.7
(define (accumulate f base)
  (lambda (n)
    (if (< n 1)
        base
        (f n ((accumulate f base) (- n 1))))))
((accumulate + 0) 100)