(define (double x) (+ x x))
(define (square1 x) (* x x))
(define (square2 x)
  (exp (double (log x))))

(square1 1000)
(square2 1000)