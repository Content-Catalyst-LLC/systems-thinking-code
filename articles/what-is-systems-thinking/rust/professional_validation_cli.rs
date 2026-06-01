// Professional validation CLI for What Is Systems Thinking
use std::fs; use std::path::Path;
fn main() {
    let path = Path::new("outputs/tables/professional_timeseries.csv");
    if !path.exists() { eprintln!("Missing {}. Run python/run_professional_workflow.py first.", path.display()); std::process::exit(1); }
    let content = fs::read_to_string(path).expect("Unable to read timeseries CSV");
    let mut row_count = 0usize; let mut high_risk_count = 0usize; let mut header: Vec<&str> = Vec::new();
    for (i, line) in content.lines().enumerate() {
        if i == 0 { header = line.split(',').collect(); continue; }
        row_count += 1; let cols: Vec<&str> = line.split(',').collect();
        if let Some(pos) = header.iter().position(|c| *c == "risk_index") { if let Some(value) = cols.get(pos) { if value.parse::<f64>().unwrap_or(0.0) > 70.0 { high_risk_count += 1; } } }
    }
    println!("article_slug,what-is-systems-thinking"); println!("row_count,{}", row_count); println!("high_risk_rows,{}", high_risk_count);
    if row_count == 0 { std::process::exit(1); }
}
