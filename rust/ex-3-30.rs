use std::ops::Add;

#[derive(Debug)]
struct Point {
  x: i32,
  y: i32
}

impl Add for Point {
  type Output = Point;
  fn add(self, other: Point) -> Point {
    Point {
      x: self.x + other.x,
      y: self.y + other.y
    }
  }
}

fn main() {
  println!("{:?}", Point{x: 1, y: 0} + Point{x: 2, y: 3});
}