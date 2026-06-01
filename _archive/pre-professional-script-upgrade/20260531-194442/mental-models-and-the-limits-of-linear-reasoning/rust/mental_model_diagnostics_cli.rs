fn main() {
    let linear_score = 0.86;
    let feedback_score = 0.24;
    let boundary_score = 0.31;
    let power_score = 0.28;
    let systemic_quality = (feedback_score + boundary_score + power_score + (1.0 - linear_score)) / 4.0;
    println!("mental_model_systemic_quality={:.3}", systemic_quality);
}
