#include <stdio.h>

int main(void) {
    double dependency_stress = 30.0;
    double resilience_buffer = 50.0;

    printf("period,dependency_stress,resilience_buffer\n");

    for (int period = 1; period <= 18; period++) {
        double stress_inflow = 4.0 + 0.03 * dependency_stress;
        double stress_outflow = 0.10 * resilience_buffer;
        dependency_stress = dependency_stress + stress_inflow - stress_outflow;

        double buffer_recovery = 2.5;
        double buffer_depletion = 0.05 * dependency_stress;
        resilience_buffer = resilience_buffer + buffer_recovery - buffer_depletion;

        if (dependency_stress < 0.0) dependency_stress = 0.0;
        if (resilience_buffer < 0.0) resilience_buffer = 0.0;

        printf("%d,%.2f,%.2f\n", period, dependency_stress, resilience_buffer);
    }

    return 0;
}
