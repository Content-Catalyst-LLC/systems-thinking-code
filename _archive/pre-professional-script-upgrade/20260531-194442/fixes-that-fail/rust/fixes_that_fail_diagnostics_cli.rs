use std::env;

fn dependency_ratio(fix: f64, repair: f64, capacity: f64) -> f64 {
    fix / (repair + capacity).max(0.001)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let fix = args.get(1).and_then(|v| v.parse::<f64>().ok()).unwrap_or(0.8);
    let repair = args.get(2).and_then(|v| v.parse::<f64>().ok()).unwrap_or(0.2);
    let capacity = args.get(3).and_then(|v| v.parse::<f64>().ok()).unwrap_or(0.7);
    let ratio = dependency_ratio(fix, repair, capacity);
    println!("dependency_ratio={:.3}", ratio);
    if ratio >= 1.0 {
        println!("risk_flag=dependency_risk");
    } else {
        println!("risk_flag=lower_dependency");
    }
}
