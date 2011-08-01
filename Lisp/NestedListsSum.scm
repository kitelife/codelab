(define (list-sum p)
 (if (null? p)
  0
  (+ (car p) (list-sum (cdr p)))))

(define (nested-list-sum p)
 (if (null? p)
  0
  (+ (list-sum (car p))
   (nested-list-sum (cdr p)))))

(define someList (list (list 1 2 3) (list 4 5 6)))
(display "nested-list-sum:")
(display (nested-list-sum someList))
(newline)

(define (deep-list-sum p)
 (if (null? p)
  0
  (+ (if (list? (car p))
	  (deep-list-sum (car p))
	  (car p))
   (deep-list-sum (cdr p)))))

(define otherList (list (list (list 1 2) 3) (list (list (list 4) 5 ) 6)))
(display "deep-list-sum:")
(display (deep-list-sum otherList))
(newline)
