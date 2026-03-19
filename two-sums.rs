use std::io;

fn two_sums() -> i64 {
    let mut input_text = String::new();
    io::stdin().read_line(&mut input_text).expect("Failed to read line");
    
    let mut iter = input_text.split_whitespace();
    let a: i64 = iter.next().expect("Missing first number").parse().expect("Invalid number");
    let b: i64 = iter.next().expect("Missing second number").parse().expect("Invalid number");
    
    a + b
}

fn main() {
    let result = two_sums();
    println!("{}", result);
}