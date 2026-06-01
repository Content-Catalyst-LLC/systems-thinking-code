#include <stdio.h>

int main(void) {
    double backlog = 120.0;
    double capacity = 55.0;

    printf("period,incoming,completed,backlog,capacity\n");

    for (int period = 1; period <= 18; period++) {
        double incoming = 11.0 + period * 0.25;
        double completed = capacity / 6.0 - backlog / 150.0;
        if (completed < 5.0) {
            completed = 5.0;
        }
        backlog = backlog + incoming - completed;
        capacity = capacity - backlog / 500.0 + 0.5;

        printf("%d,%.2f,%.2f,%.2f,%.2f\n", period, incoming, completed, backlog, capacity);
    }

    return 0;
}
