#include <stdio.h>

static double max_double(double a, double b) {
    return a > b ? a : b;
}

int main(void) {
    double pressure = 80.0;
    double capacity = 55.0;
    double dependency = 0.30;

    printf("period,pressure,capacity,dependency\n");

    for (int period = 0; period < 10; ++period) {
        double relief = 34.0 - 2.0 * period;
        double repair = 10.0 + 3.0 * period;

        if (relief < 8.0) {
            relief = 8.0;
        }

        capacity = max_double(0.0, capacity + 0.6 * repair - 0.2 * relief);
        dependency = max_double(0.0, dependency + 0.012 * relief - 0.013 * repair);
        pressure = max_double(0.0, pressure + 4.0 - 0.3 * relief - 0.2 * capacity);

        printf("%d,%.2f,%.2f,%.3f\n", period, pressure, capacity, dependency);
    }

    return 0;
}
