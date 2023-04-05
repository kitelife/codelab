(define (list-append p q)
 (if (null? p)
  q
  (cons (car p) (list-append (cdr p) q))))

(define (list-reverse p)
 (if (null? p)
  null
  (list-append (list-reverse (cdr p)) (list (car p)))))

(define (revintsto n)
 (if (= n 0)
  null
  (cons n (revintsto (- n 1)))))	

(define (intsto n) 
 (list-reverse (revintsto n)))	

(intsto 5)
