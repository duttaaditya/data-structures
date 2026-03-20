use std::io;

fn gcd(a:i64,b:i64) -> i64 {    
    let x = a;
    let y = b;
    
    if (x!=0) && y!=0 {
        if x > y {
            gcd(x%y,y)
        } else {
            gcd(x,y%x)
        }
    }
    else if x==0 {
        y
    }
    else {
        x
    }    
}

fn main() {
    let mut input_text = String::new();
    io::stdin().read_line(&mut input_text).expect("Failed to read line");
    
    let mut iter = input_text.split_whitespace();
    let a: i64 = iter.next().expect("Missing first number").parse().expect("Invalid number");
    let b: i64 = iter.next().expect("Missing second number").parse().expect("Invalid number");
    
    let result = gcd(a, b);
    println!("{}", result);
}   