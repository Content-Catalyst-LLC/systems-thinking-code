#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

static double abs_value(double value) {
    return value < 0 ? -value : value;
}

int main(void) {
    double state = 46.0;
    double goal = 70.0;

    printf("period,system_state,error_signal,control_action\n");
    for (int period = 0; period <= 36; period++) {
        double error_signal = goal - state;
        double control_action = clamp(abs_value(error_signal) * 0.42, 0.0, 100.0);
        double direction = error_signal >= 0 ? 1.0 : -1.0;
        printf("%d,%.3f,%.3f,%.3f\n", period, state, error_signal, control_action);
        state = clamp(state + direction * control_action * 0.18 - 1.2, 0.0, 100.0);
    }

    return 0;
}
