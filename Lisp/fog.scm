(define fog (lambda (f g x)(g (f x)))) ;lambda相当于生成一个匿名函数
(define fcompose
  (lambda (f g) (lambda (x) (g (f x)))))

(define (square x) (* x x))
(define (cube x) (* x (* x x)))
(define (inc x) (+ x 1))

(fog square cube 2)
(fog inc square 2)
(fog (lambda (x) (+ x 1)) square 2)

(fcompose inc inc)
((fcompose inc inc) 1)
((fcompose inc square) 2)
((fcompose square inc ) 2)
;Exercise 4.1
(fcompose (lambda (x) (* x 2)) (lambda (x) (/ x 2)))
((fcompose (lambda (x) (* x 2)) (lambda (x) (/ x 2))) 150)
((fcompose (fcompose inc inc) inc) 2)
;Exercise 4.2
;Suppose we define self-compose as a procedure that composes a procedure with itself:
(define (self-compose f) (fcompose f f))
(((fcompose self-compose self-compose) inc) 1)
;Exercise 4.3
(define (fcompose3 f g h) (lambda (x)(h (g (f x)))))
((fcompose3 abs inc square) -5)
;
(define (fcompose3 f g h) (fcompose (fcompose f g) h))
((fcompose3 abs inc square) -5)
;Exercise 4.4
(define add +)
(define (f2compose f g) (lambda (x y) (g (f x y))))
((f2compose add abs) 3 -5)
