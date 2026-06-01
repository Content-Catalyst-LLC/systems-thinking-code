use std::collections::HashMap;

fn main() {
    let edges = vec![
        ("Public Trust", "Cooperation", 1),
        ("Cooperation", "Service Performance", 1),
        ("Service Performance", "Public Trust", 1),
    ];
    let mut outgoing: HashMap<&str, usize> = HashMap::new();
    for (source, _target, _sign) in edges {
        *outgoing.entry(source).or_insert(0) += 1;
    }
    println!("Causal loop diagnostics scaffold");
    for (node, count) in outgoing {
        println!("{} has {} outgoing edge(s)", node, count);
    }
}
