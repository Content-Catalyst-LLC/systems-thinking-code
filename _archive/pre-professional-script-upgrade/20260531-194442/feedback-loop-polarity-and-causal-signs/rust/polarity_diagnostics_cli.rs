use std::process;

fn loop_polarity(signs: &[i32]) -> &'static str {
    let product: i32 = signs.iter().product();
    if product > 0 { "reinforcing" } else { "balancing" }
}

fn main() {
    let signs = vec![1, -1, -1];
    println!("Loop polarity: {}", loop_polarity(&signs));
    process::exit(0);
}
