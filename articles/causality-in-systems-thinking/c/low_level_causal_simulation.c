#include <stdio.h>

static double threshold_response(double stress, double threshold) {
    if (stress < threshold) {
        return 0.25 * stress;
    }
    return 0.25 * threshold + 1.15 * (stress - threshold);
}

int main(void) {
    printf("stress,response\n");
    for (int stress = 40; stress <= 100; stress += 5) {
        printf("%d,%.2f\n", stress, threshold_response((double)stress, 70.0));
    }
    return 0;
}
