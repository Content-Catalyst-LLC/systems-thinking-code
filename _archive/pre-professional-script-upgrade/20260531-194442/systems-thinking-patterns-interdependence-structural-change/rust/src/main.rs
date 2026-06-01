fn simulate_stock(initial: f64, inflow: f64, outflow: f64, steps: usize) -> Vec<f64> {
    let mut values = vec![initial];

    for _ in 1..steps {
        let next = (values[values.len() - 1] + inflow - outflow).max(0.0);
        values.push(next);
    }

    values
}

fn main() {
    let stock_values = simulate_stock(50.0, 5.0, 3.5, 20);

    println!("Systems Thinking CLI: stock-flow simulation");

    for (time, value) in stock_values.iter().enumerate() {
        println!("time={}, stock={:.2}", time, value);
    }
}
