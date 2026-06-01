#include <algorithm>
#include <iostream>
int main() { double backlog = std::max(0.0, 100.0 + 8.0 - 45.0 * 0.15); std::cout << "Synthetic backlog after delay: " << backlog << std::endl; return 0; }
