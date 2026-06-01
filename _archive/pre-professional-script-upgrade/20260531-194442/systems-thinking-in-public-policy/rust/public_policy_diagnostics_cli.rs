fn policy_impact(benefits: f64, burdens: f64, risks: f64) -> f64 {
    benefits - burdens - risks
}
fn main() {
    println!("Synthetic net policy impact: {:.2}", policy_impact(48.0, 62.0, 31.0));
}
