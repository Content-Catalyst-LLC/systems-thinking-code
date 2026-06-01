use std::env;

fn resilience_score(system_capacity: f64, dependency_stress: f64, resilience_buffer: f64, coordination_quality: f64) -> f64 {
    (system_capacity + resilience_buffer + coordination_quality - dependency_stress) / 3.0
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let system_capacity = args.get(1).and_then(|v| v.parse::<f64>().ok()).unwrap_or(56.0);
    let dependency_stress = args.get(2).and_then(|v| v.parse::<f64>().ok()).unwrap_or(58.0);
    let resilience_buffer = args.get(3).and_then(|v| v.parse::<f64>().ok()).unwrap_or(32.0);
    let coordination_quality = args.get(4).and_then(|v| v.parse::<f64>().ok()).unwrap_or(46.0);

    let score = resilience_score(system_capacity, dependency_stress, resilience_buffer, coordination_quality);
    println!("resilience_score={:.2}", score);

    if score >= 35.0 {
        println!("status=moderate_resilience");
    } else if score >= 25.0 {
        println!("status=fragility_warning");
    } else {
        println!("status=high_fragility");
    }
}
