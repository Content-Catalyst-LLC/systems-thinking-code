fn main() {
    let mut susceptible = 99820.0_f64;
    let mut infected = 180.0_f64;
    let mut recovered = 0.0_f64;
    let population = 100000.0_f64;
    let beta = 0.39_f64;
    let gamma = 0.20_f64;
    let prevention = 0.42_f64;

    for _week in 0..=52 {
        let effective_beta = beta * (1.0 - prevention);
        let mut new_infections = effective_beta * susceptible * infected / population;
        if new_infections > susceptible { new_infections = susceptible; }
        let mut recoveries = gamma * infected;
        if recoveries > infected { recoveries = infected; }
        susceptible -= new_infections;
        infected += new_infections - recoveries;
        recovered += recoveries;
    }

    if susceptible < -0.001 || infected < -0.001 || recovered < -0.001 {
        panic!("Invalid negative population stock");
    }
    println!("Final infected: {:.3}; recovered: {:.3}", infected, recovered);
}
