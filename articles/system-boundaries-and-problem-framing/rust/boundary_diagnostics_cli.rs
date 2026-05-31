// Boundary diagnostics CLI scaffold.
// Compile with: rustc boundary_diagnostics_cli.rs -o boundary_diagnostics_cli

use std::env;

fn diagnose(inclusion_ratio: f64, external_cost_ratio: f64) -> &'static str {
    if inclusion_ratio < 0.5 && external_cost_ratio > 1.0 {
        "High boundary risk: excluded stakeholders and large externalized costs."
    } else if inclusion_ratio < 0.5 {
        "Moderate boundary risk: stakeholder inclusion is weak."
    } else if external_cost_ratio > 1.0 {
        "Moderate boundary risk: externalized costs are large."
    } else {
        "Lower boundary risk in this simplified diagnostic."
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let inclusion_ratio = args.get(1).and_then(|x| x.parse::<f64>().ok()).unwrap_or(0.43);
    let external_cost_ratio = args.get(2).and_then(|x| x.parse::<f64>().ok()).unwrap_or(1.75);

    println!("{}", diagnose(inclusion_ratio, external_cost_ratio));
}
