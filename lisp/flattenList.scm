(define (list-append p q)
 (if (null? p)
  q
  (cons (car p) (list-append (cdr p) q))))

(define (list-flatten p)
 (if (null? p)
  null
  (list-append (car p) (list-flatten (cdr p)))))

(define someList (list (list 1 2 3) (list 4 5 6) (list 7 8 9)))
(display (list-flatten someList))
(newline)

;Test the function of procedure cdr,because i forget it
(display (cdr someList))
(newline)

(define (deep-list-flatten p)
 (if (null? p)
  null
  (list-append (if (list? (car p))
				(deep-list-flatten (car p))
				(list (car p)))
   (deep-list-flatten (cdr p)))))

(display (deep-list-flatten someList))
(newline)
(set! someList (list (list 1 2) (list (list 3 '()) 4) (list 5 6)))
(display (deep-list-flatten someList))
(newline)
