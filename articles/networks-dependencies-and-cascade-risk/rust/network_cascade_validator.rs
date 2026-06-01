fn main() {
    let loads = [0.70_f64, 0.55, 0.30, 0.20];
    let threshold = 0.50_f64;
    let failures = loads.iter().filter(|load| **load > threshold).count();
    println!("validated dependency loads; failures above threshold: {}", failures);
}
