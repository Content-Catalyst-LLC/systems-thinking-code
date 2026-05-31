use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let delay: f64 = args.get(1).and_then(|v| v.parse().ok()).unwrap_or(6.0);
    let repair: f64 = args.get(2).and_then(|v| v.parse().ok()).unwrap_or(0.08);
    let score = (0.68 - 0.035 * delay + 1.2 * repair - 1.4 * 0.05).clamp(0.0, 1.0);
    println!("delay={:.2}, repair={:.3}, resilience_score={:.3}", delay, repair, score);
}
