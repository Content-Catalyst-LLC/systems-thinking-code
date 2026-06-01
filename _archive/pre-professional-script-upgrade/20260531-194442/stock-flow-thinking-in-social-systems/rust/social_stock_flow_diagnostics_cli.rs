use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 4 {
        eprintln!("Usage: social_stock_flow_diagnostics_cli <stock> <inflow> <outflow>");
        std::process::exit(1);
    }
    let stock: f64 = args[1].parse().expect("stock must be numeric");
    let inflow: f64 = args[2].parse().expect("inflow must be numeric");
    let outflow: f64 = args[3].parse().expect("outflow must be numeric");
    let next = (stock + inflow - outflow).max(0.0);
    println!("next_stock={:.2}", next);
    if inflow > outflow {
        println!("trajectory=repair_or_accumulation");
    } else if inflow < outflow {
        println!("trajectory=depletion");
    } else {
        println!("trajectory=stable");
    }
}
