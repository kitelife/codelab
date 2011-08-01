(define (list-append p q)
 (if (null? p)
  q
  (cons (car p) (list-append (cdr p) q))))

(define (intsto n)
 (if (= n 0)
  null
  (list-append (intsto (- n 1)) (list n))))

(intsto 9)
