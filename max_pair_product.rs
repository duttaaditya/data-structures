use std::io;

fn max_pair_product() -> i64 {
    let mut input_text = String::new();
    io::stdin().read_line(&mut input_text).expect("Failed to read line");
    let arr = input_text.split_whitespace().filter_map(|s| s.parse::<i64>().ok()).collect::<Vec<i64>>();
    println!("{:?}", arr);
    let mut max1 = -1;
    let mut id1 = 0;
    for i in 0..arr.len() {
        if arr[i] > max1 {
            id1 = i;
            max1 = arr[id1];
        };
    };
    let mut max2 = -1;
    for i in 0..arr.len() {
        if i != id1 && arr[i] > max2 {
            max2 = arr[i];
        };
    };
    return max1 * max2;

}

fn main() {
    let result = max_pair_product();
    println!("{}", result);
}