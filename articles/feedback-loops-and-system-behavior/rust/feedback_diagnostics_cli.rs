use std::env;

fn classify_loop(negative_links: i32) -> &'static str {
    if negative_links % 2 == 0 { "reinforcing" } else { "balancing" }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let negative_links = args.get(1)
        .and_then(|s| s.parse::<i32>().ok())
        .unwrap_or(0);

    println!("negative_links,loop_type");
    println!("{},{}", negative_links, classify_loop(negative_links));
}
