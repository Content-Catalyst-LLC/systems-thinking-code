use std::env;

fn classify_margin(margin: f64) -> &'static str {
    if margin >= 0.05 {
        "resilient"
    } else if margin >= 0.0 {
        "fragile"
    } else {
        "at-risk"
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let capacity_growth: f64 = args.get(1).and_then(|v| v.parse().ok()).unwrap_or(0.03);
    let demand_growth: f64 = args.get(2).and_then(|v| v.parse().ok()).unwrap_or(0.04);
    let margin = capacity_growth - demand_growth;
    println!("capacity_growth={:.3}", capacity_growth);
    println!("demand_growth={:.3}", demand_growth);
    println!("robustness_margin={:.3}", margin);
    println!("classification={}", classify_margin(margin));
}
