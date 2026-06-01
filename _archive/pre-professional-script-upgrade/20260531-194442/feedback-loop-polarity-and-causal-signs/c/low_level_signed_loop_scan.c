#include <stdio.h>

int main(void) {
    int signs[] = {1, -1, -1};
    int product = 1;
    for (int i = 0; i < 3; i++) {
        product *= signs[i];
    }
    printf("%s\n", product > 0 ? "reinforcing" : "balancing");
    return 0;
}
