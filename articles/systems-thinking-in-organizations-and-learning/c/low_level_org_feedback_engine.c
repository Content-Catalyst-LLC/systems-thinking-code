#include <stdio.h>

int main(void) {
    double observed = 0.68;
    double distortion = 0.25;
    double received = observed * (1.0 - distortion);
    printf("received_signal=%.3f\n", received);
    return 0;
}
