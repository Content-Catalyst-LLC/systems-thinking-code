fn main() {
    let high_advantage = 84.0_f64;
    let low_advantage = 25.0_f64;
    let gap = high_advantage - low_advantage;
    println!("advantage_gap={:.2}", gap);
    if gap > 40.0 {
        println!("diagnostic=high cumulative-advantage risk");
    }
}
