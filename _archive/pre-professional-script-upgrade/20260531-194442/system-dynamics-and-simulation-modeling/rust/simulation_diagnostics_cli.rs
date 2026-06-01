use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let scenario = args.get(1).cloned().unwrap_or_else(|| "baseline".to_string());
    println!("System dynamics diagnostics scaffold");
    println!("Scenario: {}", scenario);
    println!("Suggested checks: nonnegative stocks, bounded trust, delay sensitivity, scenario robustness.");
}
