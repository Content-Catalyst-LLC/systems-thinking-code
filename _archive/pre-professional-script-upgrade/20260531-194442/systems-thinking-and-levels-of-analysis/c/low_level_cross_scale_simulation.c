#include <stdio.h>

int main(void) {
    double micro_burden = 60.0;
    double meso_capacity = 65.0;
    double macro_stress = 70.0;

    printf("period,micro_burden,meso_capacity,macro_stress\n");
    for (int t = 1; t <= 12; t++) {
        micro_burden = micro_burden + 0.05 * macro_stress - 0.03 * meso_capacity;
        meso_capacity = meso_capacity + 0.02 * (100.0 - micro_burden) - 0.01 * macro_stress;
        macro_stress = macro_stress + 0.5 - 0.01 * meso_capacity;
        printf("%d,%.2f,%.2f,%.2f\n", t, micro_burden, meso_capacity, macro_stress);
    }

    return 0;
}
