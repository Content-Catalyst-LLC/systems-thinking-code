fn clamp(x: f64, low: f64, high: f64) -> f64 {
    if x < low { low } else if x > high { high } else { x }
}

fn main() {
    let mut engagement = 55.0;
    let mut risk = 22.0;
    let mut trust = 72.0;
    for _ in 0..36 {
        engagement = clamp(engagement + 3.0 - risk * 0.02, 0.0, 100.0);
        risk = clamp(risk + engagement * 0.035 - trust * 0.025, 0.0, 100.0);
        trust = clamp(trust - risk * 0.05 + 1.1, 0.0, 100.0);
    }
    println!("platform scenario validator: engagement={:.3} risk={:.3} trust={:.3}", engagement, risk, trust);
}
