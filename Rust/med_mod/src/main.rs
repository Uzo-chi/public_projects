use std::{io, collections::Hashmap};

fn main() {
    let mut size = String::new();
    let input = io::stdin();
    let integers = Vec::new();

    println!("How many integers are we talking?:");
    input.read_line(&mut size).expect("Could not read value");
    let size:usize = size.trim().parse().expect("Not an unsigned integer");

    for s in 0..size {
        
    }
}
