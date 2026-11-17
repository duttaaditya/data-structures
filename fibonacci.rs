use std::{io};

fn fibonacci(n:i64) -> i128 {
    let mut result = Vec::<i128>::new();
    if n <= 0 {
        result.push(0);

    }
    else if n == 1 {
        result.push(1);
    }
    else {
        result.push(0);
        result.push(1);
        for i in 2..n+1 {
            result.push(result[i as usize-1] + result[i as usize -2]);
        }
    }
    result[result.len() - 1]
}

fn main() {
    let mut input_text = String::new();
    io::stdin().read_line(&mut input_text).expect("Failed to read line");
    
    let n: i64 = input_text.trim().parse().expect("Invalid number");
    
    let result = fibonacci(n);
    println!("{}", result);
}