use std::io;

fn main() {
    let input = io::stdin();
    let mut term = String::new();

    println!("How many numbers from the fibonacci sequence?:");
    input.read_line(&mut term).expect("Not a string!");
    let term:u64 = term.trim().parse().expect("Not a real integer!");

    println!("Fibonacci ({}) => {}", term, fibo(term));
}

fn fibo(n:u64) -> u64 {
    if n <= 0 {
        return 0;
    } else if n == 1 {
        return 1;
    }   fibo(n - 1) + fibo(n - 2)
}