;simple list map function
(define (list-map f p)
 (if (null? p)
  null
  (cons 
   (square (car p))
   (list-map f (cdr p)))))

;map the deep nested list
(define (deep-list-map func p)
 (if (null? p)
  null
  (cons (if (list? (car p))
		 (deep-list-map func (car p))
		 (func (car p)))
   (deep-list-map func (cdr p)))))

(define (double x) 
 (+ x 2))

(define someList (list (list 1 2) (list 3 (list 4 5))))
(display someList)
(newline)
(display (deep-list-map double someList))
(newline)
(display (deep-list-map (lambda (x) (* x 2)) someList))
(newline)
