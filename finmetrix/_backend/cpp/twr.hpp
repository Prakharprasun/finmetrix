// finmetrix/_backend/cpp/twr.hpp
#ifndef FINMETRIX_TWR_HPP
#define FINMETRIX_TWR_HPP

#include <vector>

namespace finmetrix {

/**
 * Compute time-weighted return.
 *
 * Assumes input is already validated by Python layer.
 * Returns compound return: ∏(1 + r_i) - 1
 */
double twr(const std::vector<double>& returns);

}  // namespace finmetrix

#endif  // FINMETRIX_TWR_HPP