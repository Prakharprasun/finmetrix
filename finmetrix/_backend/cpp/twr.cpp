// finmetrix/_backend/cpp/twr.cpp
#include "twr.hpp"

namespace finmetrix {

double twr(const std::vector<double>& returns) {
    // Python guarantees: non-empty, finite, valid values
    // C++ assumes this contract is upheld

    double result = 1.0;
    for (double r : returns) {
        result *= (1.0 + r);
    }
    return result - 1.0;
}

}  // namespace finmetrix