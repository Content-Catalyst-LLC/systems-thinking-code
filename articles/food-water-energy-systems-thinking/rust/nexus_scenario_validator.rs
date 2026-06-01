fn main() {
    let mut groundwater: f64 = 1000.0;
    let recharge: f64 = 28.0;
    let withdrawal: f64 = 55.0 * 1.18;
    println!("year,groundwater,status");
    for year in 0..=30 {
        groundwater = (groundwater + recharge - withdrawal).max(0.0);
        let status = if groundwater < 250.0 { "depletion_warning" } else { "within_monitoring_range" };
        println!("{}, {:.3}, {}", year, groundwater, status);
    }
}
