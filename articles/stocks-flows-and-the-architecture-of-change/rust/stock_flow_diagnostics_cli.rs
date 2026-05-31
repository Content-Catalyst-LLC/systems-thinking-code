use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let inflow: f64 = args.get(1).and_then(|v| v.parse().ok()).unwrap_or(4.0);
    let outflow: f64 = args.get(2).and_then(|v| v.parse().ok()).unwrap_or(5.0);
    let net = inflow - outflow;
    let direction = if net > 0.0 { "accumulating" } else if net < 0.0 { "depleting" } else { "stable" };
    println!("net_flow={:.3}, direction={}", net, direction);
}
