fn clamp(x: f64) -> f64 {
    if x < 0.0 { 0.0 } else if x > 100.0 { 100.0 } else { x }
}

fn main() {
    let mut congestion = 48.0;
    let mut affordability = 46.0;
    let mut infrastructure = 64.0;
    let mut displacement = 38.0;
    for _year in 0..=30 {
        congestion = clamp(congestion + 0.55 + displacement * 0.008 - affordability * 0.004);
        affordability = clamp(affordability + 0.45 - congestion * 0.010 - displacement * 0.006);
        infrastructure = clamp(infrastructure + 0.60 - 1.00 - congestion * 0.008);
        displacement = clamp(displacement + congestion * 0.005 - affordability * 0.004);
    }
    let resilience = clamp((100.0 - congestion) * 0.25 + affordability * 0.25 + infrastructure * 0.30 + (100.0 - displacement) * 0.20);
    println!("Urban validator: congestion={:.2} affordability={:.2} infrastructure={:.2} displacement={:.2} resilience={:.2}", congestion, affordability, infrastructure, displacement, resilience);
}
