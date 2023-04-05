trait Page {
  fn set_page(&mut self, p: i32) {
    println!("Page: {}", p);
  }
}

trait PerPage {
  fn set_perpage(&self, num: i32) {
    println!("Per Page: {}", num);
  }
}

#[derive(Debug)]
struct MyPaginate{page: i32}

impl Page for MyPaginate {
  fn set_page(&mut self, p: i32) {
    self.page = p;
  }
}

impl PerPage for MyPaginate {}

fn main() {
  let mut my_paginate = MyPaginate{page: 1};
  println!("Before set_page: {:?}", my_paginate);
  my_paginate.set_page(2);
  println!("After set_page: {:?}", my_paginate);
  my_paginate.set_perpage(100);
}