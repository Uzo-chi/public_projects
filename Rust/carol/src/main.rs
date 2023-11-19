fn main() {
    for day in 1..13 {
        if day == 1 {
            println!("On the 1st day of Christmas, my true love sent to me\n{}\n", carol(day));
        } else if day == 2 {
            println!("On the 2nd day of Christmas, my true love sent to me");
            for days in (1..day+1).rev() {
                if days == 2 {
                    println!("{} and", carol(days));
                } else {
                    println!("{}", carol(days));
                }
            }
            println!("");
        } else if day == 3 {
            println!("On the 3rd day of Christmas, my true love sent to me");
            for days in (1..day+1).rev() {
                if days == 2 {
                    println!("{} and", carol(days));
                } else {
                    println!("{}", carol(days));
                }
            }
            println!("");
        } else {
            println!("On the {}th day of Christmas, my true love sent to me", day);
            for days in (1..day+1).rev() {
                if days == 2 {
                    println!("{} and", carol(days));
                } else {
                    println!("{}", carol(days));
                }
            }
            println!("");
        }
    }
}

fn carol(d:u64) -> &'static str {
    if d == 1 {
        return "a patridge in a pear tree";
    } else if d == 2 {
        return "two turtle doves";
    } else if d == 3 {
        return "three french hens";
    } else if d == 4 {
        return "four calling birds";
    } else if d == 5 {
        return "five golden rings";
    } else if d == 6 {
        return "six geese a-laying";
    } else if d == 7 {
        return "seven swans a-swimming";
    } else if d == 8 {
        return "eight maids a-milking";
    } else if d == 9 {
        return "nine ladies dancing";
    } else if d == 10 {
        return "ten lords a-leaping";
    } else if d == 11 {
        return "eleven pipers piping";
    } else if d == 12 {
        return "twelve drummers drumming";
    } else {
        return "Nothing, bruh!";
    }
}