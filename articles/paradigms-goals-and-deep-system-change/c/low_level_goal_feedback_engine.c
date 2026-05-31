/* Low-level goal-feedback engine scaffold.
   Compile with: cc low_level_goal_feedback_engine.c -o goal_feedback_engine
*/

#include <stdio.h>

static double clamp(double x) {
    if (x < 0.0) return 0.0;
    if (x > 1.0) return 1.0;
    return x;
}

int main(void) {
    double state = 0.25;
    double goal = 0.80;
    double correction = 0.30;

    for (int t = 0; t < 12; ++t) {
        double error = goal - state;
        state = clamp(state + correction * error);
        printf("%d,%.3f\n", t, state);
    }
    return 0;
}
