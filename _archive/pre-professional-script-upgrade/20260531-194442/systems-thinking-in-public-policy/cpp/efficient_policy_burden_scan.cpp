#include <iostream>
int main() {
  double learning = 28, compliance = 36, psychological = 31, digital = 22, appeal = 27;
  std::cout << "Synthetic burden index: " << (learning + compliance + psychological + digital + appeal) / 5.0 << std::endl;
  return 0;
}
