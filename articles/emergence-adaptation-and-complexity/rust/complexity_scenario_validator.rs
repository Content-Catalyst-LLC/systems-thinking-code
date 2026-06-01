fn clamp01(x: f64) -> f64 {
    if x < 0.0 { 0.0 } else if x > 1.0 { 1.0 } else { x }
}

fn main() {
    let agents = 40usize;
    let mut states: Vec<f64> = (0..agents).map(|i| ((i * 17) % 100) as f64 / 100.0).collect();
    for _ in 0..20 {
        let mut next = states.clone();
        for i in 0..agents {
            let left = states[(i + agents - 1) % agents];
            let right = states[(i + 1) % agents];
            let local = (left + right) / 2.0;
            next[i] = clamp01(states[i] + 0.18 * (local - states[i]));
        }
        states = next;
    }
    let mean: f64 = states.iter().sum::<f64>() / agents as f64;
    println!("Rust complexity validator final mean: {:.4}", mean);
}
