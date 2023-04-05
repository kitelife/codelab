#[derive(Debug, PartialEq)]
struct Point<T> {
  x: T,
  y: T
}

impl<T> Point<T> {
  fn new(x: T, y: T) -> Self {
    Point{x: x, y: y}
  }
}

fn main() {
  let point1 = Point::new(1, 2);
  let point2 = Point::new("1", "2");
  assert_eq!(point1, Point{x: 1, y: 2});
  assert_eq!(point2, Point{x: "1", y: "2"});
  println!("{:?}", point1);
  println!("{:?}", point2);
}