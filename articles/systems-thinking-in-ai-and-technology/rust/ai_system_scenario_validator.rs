fn clamp(v: f64) -> f64 { v.max(0.0).min(100.0) }

fn main() {
    let mut risk = 34.0;
    let mut governance = 49.0;
    println!("period,risk,governance");
    for period in 0..=12 {
        println!("{}, {:.3}, {:.3}", period, risk, governance);
        risk = clamp(risk + 2.0 - governance * 0.03);
        governance = clamp(governance + 1.2);
    }
}
