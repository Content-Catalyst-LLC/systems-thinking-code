use std::fs;
use std::path::Path;

fn within_0_100(value: f64) -> bool {
    value >= 0.0 && value <= 100.0
}

fn main() {
    let sample_scores = vec![42.5, 58.0, 74.2, 39.1];
    for score in sample_scores {
        assert!(within_0_100(score), "score outside 0-100 range");
    }

    let out_dir = Path::new("outputs/tables");
    fs::create_dir_all(out_dir).expect("create outputs/tables");
    fs::write(
        out_dir.join("rust_validation_report.txt"),
        "Rust validation passed: all sample infrastructure scores are bounded.\n",
    ).expect("write validation report");

    println!("Rust validation passed.");
}
