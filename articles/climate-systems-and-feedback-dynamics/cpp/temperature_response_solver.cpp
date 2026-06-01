#include <cmath>
#include <iostream>

static double forcing(double co2) {
    return 5.35 * std::log(co2 / 280.0);
}

int main() {
    double co2 = 420.0;
    double emissions = 40.0;
    double temp = 1.2;
    double heat = 0.0;
    double feedback = 1.28;
    for (int year = 0; year <= 80; ++year) {
        emissions *= 0.96;
        co2 += (emissions / 7.8) * 0.55;
        double f = forcing(co2);
        heat += f * 0.035;
        double target = 0.78 * f * feedback;
        temp += 0.10 * (target - temp) + heat * 0.006;
    }
    std::cout << "Final synthetic CO2 ppm: " << co2 << "\n";
    std::cout << "Final synthetic temperature anomaly: " << temp << " C\n";
    return 0;
}
