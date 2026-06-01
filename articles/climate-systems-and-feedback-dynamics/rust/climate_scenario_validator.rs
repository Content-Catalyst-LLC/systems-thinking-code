// Dependency-light climate scenario validator.
// Compile with: rustc rust/climate_scenario_validator.rs -o outputs/climate_scenario_validator

fn forcing(co2: f64) -> f64 {
    5.35 * (co2 / 280.0).ln()
}

fn main() {
    let mut co2 = 420.0;
    let mut emissions = 40.0;
    let mut temp = 1.2;
    let mut heat = 0.0;
    let feedback = 1.28;
    for _year in 0..=80 {
        emissions *= 0.96;
        co2 += (emissions / 7.8) * 0.55;
        let f = forcing(co2);
        heat += f * 0.035;
        let target = 0.78 * f * feedback;
        temp += 0.10 * (target - temp) + heat * 0.006;
    }
    println!("Final synthetic CO2 ppm: {:.2}", co2);
    println!("Final synthetic temperature anomaly: {:.3} C", temp);
    if co2 <= 0.0 || temp.is_nan() {
        std::process::exit(1);
    }
}
