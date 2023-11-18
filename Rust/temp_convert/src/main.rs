use std::io;

fn main() {
    let input = io::stdin();
    let mut choice = String::new();
    let mut conv = String::new();

    println!("Would you like to convert to Celsius or Fahrenheit? (Enter c/f):");
    input.read_line(&mut choice).expect("Not a string!");
    let choice:char = choice.trim().parse().expect("This isn't a character!");

    println!("Enter temperature (make sure it's a decimal):");
    input.read_line(&mut conv).expect("Not a string!");
    let conv:f64 = conv.trim().parse().expect("This isn't a decimal!");

    if choice == 'c' {
        let a = f_to_c(conv);
        println!("That would be {} degrees Celsius!", a);
    } else if choice == 'f' {
        let a = c_to_f(conv);
        println!("That would be {} degrees Fahrenheit!", a);
    } else {
        println!("Feeling rebellious?");
    }
}

fn c_to_f(n:f64) -> f64 {
    ((9.0/5.0) * n) + 32.0
}

fn f_to_c(n:f64) -> f64 {
    (5.0/9.0) * (n - 32.0)
}