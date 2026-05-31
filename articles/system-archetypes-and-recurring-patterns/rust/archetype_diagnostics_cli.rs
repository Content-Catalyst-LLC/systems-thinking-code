use std::env;

fn classify_hint(term: &str) -> &'static str {
    let text = term.to_lowercase();
    if text.contains("growth") || text.contains("constraint") {
        "Candidate archetype: Limits to Growth"
    } else if text.contains("quick") || text.contains("fix") || text.contains("delayed") {
        "Candidate archetype: Fixes That Fail"
    } else if text.contains("burden") || text.contains("dependency") {
        "Candidate archetype: Shifting the Burden"
    } else if text.contains("goal") || text.contains("standard") {
        "Candidate archetype: Eroding Goals"
    } else if text.contains("resource") || text.contains("commons") {
        "Candidate archetype: Tragedy of the Commons"
    } else {
        "Candidate archetype unclear: map behavior over time and feedback loops"
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let term = if args.len() > 1 { args[1..].join(" ") } else { String::from("backlog quick fix delayed consequence") };
    println!("{}", classify_hint(&term));
}
