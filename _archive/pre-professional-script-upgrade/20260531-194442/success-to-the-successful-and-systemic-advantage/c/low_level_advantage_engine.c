#include <stdio.h>
int main(void) {
    double advantage = 30.0;
    for (int t = 0; t < 12; ++t) {
        advantage = advantage + 0.04 * advantage + 1.5;
    }
    printf("final_advantage=%.2f\n", advantage);
    return 0;
}
