;Exercise 4.5
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
(define (choose n k)
  (/ (factorial n) (* (factorial (- n k)) (factorial k))))
(choose 52 5)