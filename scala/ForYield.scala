object ForYield {
  def main(args: Array[String]) {
    val argList = args.toList
    val res = for (a <- argList) yield a.toUpperCase
    println("Arguments: " + res.toString)
  }
}
