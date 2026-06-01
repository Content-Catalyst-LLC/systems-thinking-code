/* Professional stock-flow kernel for Mental Models and the Limits of Linear Reasoning */
#include <stdio.h>
static double clamp(double x, double lo, double hi) { if (x < lo) return lo; if (x > hi) return hi; return x; }
int main(void) {
    double stock = 74, capacity = 46, burden = 52;
    printf("year,stock,capacity,burden,risk\n");
    for (int year = 0; year <= 30; ++year) {
        double pressure = 5.0 + 2.4 * year * 0.45;
        burden = clamp(burden + pressure * 0.08 - 1.2 * 0.35, 0.0, 100.0);
        capacity = clamp(capacity + 1.2 - burden * 0.015, 0.0, 100.0);
        stock = clamp(stock + stock * 0.024 - pressure - burden * 0.035 + capacity * 0.025, 0.0, 120.0);
        double risk = clamp(100.0 - (0.45 * stock + 0.35 * capacity - 0.20 * burden), 0.0, 100.0);
        printf("%d,%.2f,%.2f,%.2f,%.2f\n", year, stock, capacity, burden, risk);
    }
    return 0;
}
