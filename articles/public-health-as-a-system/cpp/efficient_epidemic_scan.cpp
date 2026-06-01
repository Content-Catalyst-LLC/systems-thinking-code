#include <algorithm>
#include <iostream>

int main() {
    double susceptible = 99820.0;
    double infected = 180.0;
    double recovered = 0.0;
    const double population = 100000.0;
    const double beta = 0.39;
    const double gamma = 0.20;
    const double prevention = 0.42;

    for (int week = 0; week <= 52; ++week) {
        double effective_beta = beta * (1.0 - prevention);
        double new_infections = std::min(susceptible, effective_beta * susceptible * infected / population);
        double recoveries = std::min(infected, gamma * infected);
        susceptible -= new_infections;
        infected += new_infections - recoveries;
        recovered += recoveries;
    }

    std::cout << "Final infected: " << infected << "; recovered: " << recovered << "\n";
    return 0;
}
