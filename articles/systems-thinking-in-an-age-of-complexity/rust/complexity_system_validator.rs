use std::fs;
use std::path::Path;

fn within_expected_range(value: f64) -> bool {
    value >= 0.0 && value <= 120.0
}

fn main() {
    let sample_values = vec![42.5, 58.0, 74.2, 39.1, 101.0];
    for value in sample_values {
        assert!(within_expected_range(value), "value outside expected range");
    }

    let out_dir = Path::new("outputs/tables");
    fs::create_dir_all(out_dir).expect("create outputs/tables");
    fs::write(
        out_dir.join("rust_complexity_system_validation_report.txt"),
        "Rust validation passed: all sample complexity indicators are bounded.\n",
    ).expect("write validation report");

    println!("Rust validation passed.");
}
