fn classify_regime(resilience: f64, pressure: f64) -> &'static str {
    let margin = resilience - pressure;
    if margin <= 0.0 { "shifted" }
    else if margin <= 10.0 { "near_threshold" }
    else { "recoverable" }
}

fn main() {
    let mut resilience = 78.0;
    let mut pressure = 35.0;
    for year in 0..=20 {
        pressure += 2.3;
        resilience = (resilience + 1.3 - 2.1 - pressure * 0.02).clamp(0.0, 100.0);
        println!("{year:02} resilience={:.2} pressure={:.2} regime={}", resilience, pressure, classify_regime(resilience, pressure));
    }
}
