// Minimal Rust CLI scaffold for leverage diagnostics.
fn main() {
    let leverage_points = vec![
        ("Reduce administrative burden", "rule", 0.82),
        ("Community feedback loop", "information_flow", 0.88),
        ("Preventive maintenance", "stock_flow", 0.74),
    ];
    for (name, level, score) in leverage_points {
        println!("{name} | {level} | leverage_score={score}");
    }
}
