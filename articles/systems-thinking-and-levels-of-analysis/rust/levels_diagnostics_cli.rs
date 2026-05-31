use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let level = args.get(1).cloned().unwrap_or_else(|| "cross-scale".to_string());

    println!("Systems Thinking Levels Diagnostics");
    println!("Selected level: {}", level);
    println!("Diagnostic prompts:");
    println!("- Where is the problem experienced?");
    println!("- Where is it generated?");
    println!("- Where is authority located?");
    println!("- Where does feedback fail to travel?");
}
