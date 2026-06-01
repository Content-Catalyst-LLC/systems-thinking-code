fn main() {
    let memory_score = 0.48;
    let feedback_closure = 0.34;
    let authority_connection = 0.42;
    let system_learning = memory_score * feedback_closure * authority_connection;
    println!("system_learning_index={:.3}", system_learning);
}
