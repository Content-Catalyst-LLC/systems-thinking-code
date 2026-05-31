#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::map<std::string, std::vector<std::string>> nested;
    nested["Governance System"] = {"Public Agency"};
    nested["Public Agency"] = {"Service Team", "Frontline Worker"};
    nested["Socio-Ecological Region"] = {"Regional Infrastructure Network"};

    for (const auto& pair : nested) {
        std::cout << pair.first << ": ";
        for (const auto& child : pair.second) {
            std::cout << child << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
