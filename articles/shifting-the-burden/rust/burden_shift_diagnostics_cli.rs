// Simple CLI scaffold for shifting-the-burden diagnostics.
#[derive(Debug)]
struct Diagnostic {
    symptom_pressure: f64,
    symptomatic_reliance: f64,
    fundamental_capacity: f64,
}

impl Diagnostic {
    fn dependency_ratio(&self) -> f64 {
        if self.fundamental_capacity <= 0.0 {
            return f64::INFINITY;
        }
        self.symptomatic_reliance / self.fundamental_capacity
    }

    fn risk_label(&self) -> &'static str {
        let ratio = self.dependency_ratio();
        if ratio >= 0.8 {
            "high dependency"
        } else if ratio >= 0.5 {
            "moderate dependency"
        } else {
            "lower dependency"
        }
    }
}

fn main() {
    let diagnostic = Diagnostic {
        symptom_pressure: 82.0,
        symptomatic_reliance: 46.0,
        fundamental_capacity: 56.0,
    };

    println!("Shifting the Burden Diagnostic");
    println!("symptom_pressure: {:.1}", diagnostic.symptom_pressure);
    println!("dependency_ratio: {:.2}", diagnostic.dependency_ratio());
    println!("risk_label: {}", diagnostic.risk_label());
}
