/* Low-level growth constraint engine scaffold. */
#include <stdio.h>

int main(void) {
    double scale = 100.0;
    double rate = 0.13;
    double capacity = 260.0;
    for (int year = 0; year <= 25; ++year) {
        printf("%d,%.3f,%.3f\n", year, scale, scale / capacity);
        scale += rate * scale * (1.0 - scale / capacity);
    }
    return 0;
}
