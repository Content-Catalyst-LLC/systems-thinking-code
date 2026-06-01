use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let topic = args.get(1).map(String::as_str).unwrap_or("organizational-learning");
    println!("Diagnostics scaffold for: {}", topic);
    println!("Use this CLI scaffold to add checks for workload, feedback, memory, and burnout indicators.");
}
