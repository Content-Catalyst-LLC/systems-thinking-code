fn sustainability_pressure(resource_use: f64, capacity: f64) -> f64 {
    if resource_use > capacity { resource_use - capacity } else { 0.0 }
}
fn main() { println!("Synthetic overshoot diagnostic: {:.2}", sustainability_pressure(112.0, 101.0)); }
