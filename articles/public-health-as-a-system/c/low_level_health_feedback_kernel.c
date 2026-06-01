#include <stdio.h>

int main(void) {
    double susceptible = 99820.0;
    double infected = 180.0;
    double recovered = 0.0;
    double population = 100000.0;
    double beta = 0.39;
    double gamma = 0.20;
    double prevention = 0.42;

    for (int week = 0; week <= 52; week++) {
        double effective_beta = beta * (1.0 - prevention);
        double new_infections = effective_beta * susceptible * infected / population;
        if (new_infections > susceptible) new_infections = susceptible;
        double recoveries = gamma * infected;
        if (recoveries > infected) recoveries = infected;
        susceptible -= new_infections;
        infected += new_infections - recoveries;
        recovered += recoveries;
    }

    printf("Final infected: %.3f; recovered: %.3f\n", infected, recovered);
    return 0;
}
