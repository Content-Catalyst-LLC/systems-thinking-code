#include <stdio.h>
double clamp(double value) { if (value < 0.0) return 0.0; if (value > 100.0) return 100.0; return value; }
double next_outcome(double outcome, double effort, double burden, double capacity) { return clamp(outcome + 0.2 * effort - 0.25 * burden + 0.1 * capacity); }
int main(void) { printf("Synthetic policy outcome: %.2f
", next_outcome(42.0, 35.0, 24.0, 55.0)); return 0; }
