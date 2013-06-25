object Persons {
  
  var persons = List(
    new Person("Bob", 17),
    new Person("John", 40),
    new Person("Richard", 68)
  )

  class Person(val name: String, val age: Int)

  def olderThan20 (xs: Seq[Person]): Iterator[String] = 
    olderThan20(xs.elements)

  def olderThan20(xs: Iterator[Person]): Iterator[String] = {
    for (p <- xs if p.age > 20) yield p.name
  }
}

object Numeric {
  
  def divisors(n: Int): List[Int] = 
    for (i <- List.range(1, n+1) if n % i == 0) yield i

  def isPrime(n: Int) = divisors(n).length == 2

  def findNums(n: Int): Iterable[(Int, Int)] = {
    for (i <- 1 until n;
         j <- 1 until (i-1);
         if isPrime(i + j)) yield (i, j)
  }

  def sum(xs: List[Double]): Double = 
    xs.foldLeft(0.0) { (x, y) => x + y}

  def scalProd(xs: List[Double], ys: List[Double]) = 
    sum(for((x, y) <- xs zip ys) yield x * y)

  def removeDuplicates[A](xs: List[A]): List[A] = 
    if (xs.isEmpty)
      xs
    else
      xs.head :: removeDuplicates(for (x <-xs.tail if x != xs.head) yield x)
}

object Fors {
  
  def main(args: Array[String]) {
    import Persons._

    print("Persons over 20:")
    olderThan20(persons) foreach {x => print(" " + x)}
    println

    import Numeric._

    println("divisors(34) = " + divisors(34))

    print("findNums(15) =")
    findNums(15) foreach { x => print(" " + x) }
    println

    val xs = List(3.5, 5.0, 4.5)
    println("average(" + xs + ") = " + sum(xs) / xs.length)

    val ys = List(2.0, 1.0, 3.0)
    println("scalProd(" + xs + ", " + ys + ") = " + scalProd(xs, ys))
  }
}
