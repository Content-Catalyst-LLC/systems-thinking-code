#include <stdio.h>
double next_stock(double stock, double regeneration, double extraction, double degradation) { double value = stock + regeneration - extraction - degradation; return value < 0.0 ? 0.0 : value; }
int main(void) { printf("Synthetic next stock: %.2f
", next_stock(100.0, 4.0, 2.5, 0.6)); return 0; }
