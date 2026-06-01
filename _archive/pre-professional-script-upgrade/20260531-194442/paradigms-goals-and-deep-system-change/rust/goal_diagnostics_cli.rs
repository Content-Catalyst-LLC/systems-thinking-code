// Goal diagnostics CLI scaffold.
// Compile with: rustc goal_diagnostics_cli.rs -o goal_diagnostics_cli

fn classify_gap(explicit_goal: &str, operating_goal: &str) -> &'static str {
    if explicit_goal == operating_goal {
        "aligned"
    } else {
        "goal gap: investigate incentives, metrics, and power"
    }
}

fn main() {
    let explicit_goal = "dignified_access";
    let operating_goal = "risk_avoidance";
    println!("{}", classify_gap(explicit_goal, operating_goal));
}
