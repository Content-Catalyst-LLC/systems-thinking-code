fn main() {
    let administrative_burden = 0.71;
    let trust_stock = 0.48;
    let coordination_density = 0.36;
    let institutional_capacity = 0.52;
    let public_value = 0.49;
    let score = (1.0 - administrative_burden) * 0.20 + trust_stock * 0.20 + coordination_density * 0.18 + institutional_capacity * 0.20 + public_value * 0.22;
    println!("governance_system_score={:.3}", score);
}
