#include <iostream>
#include <string>

extern "C" {
    const char* get_audit_value(double mass) {
        double bsf_yield = mass * 0.20;
        double usd_value = bsf_yield * 2.50;
        static std::string result;
        result = "BSF Yield: " + std::to_string(bsf_yield) + "kg | Value: $" + std::to_string(usd_value);
        return result.c_str();
    }
}

int main() {
    std::cout << get_audit_value(10.0) << std::endl;
    return 0;
}
