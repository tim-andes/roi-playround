import adjusted_growth_rate
import roi_no_contributions

# Adjusted rate / real_rate
@pytest.mark.parametrize("growth_rate, inflation_rate, expected",
                         [(0, 0, 0),
                          (.1, .03, 0.06796),
                          (.05, .03, .01942),
                          (1, .5, 0.33333)])
def test_real_rate(growth_rate, inflation_rate, expected):
    assert adjusted_growth_rate.real_rate(growth_rate, inflation_rate) == expected  

# ROI, no contributions
@pytest.mark.parametrize("starting_principal, years_invested, compound_frequency,"
                        "real_rate, expected",
                        [
                        (0, 0, 0, 0, 0),
                        (10000, 10, 1, .01942, 12121),
                        (220000, 25, 1, .06796, 1138406)
])
def test_roi(starting_principal, years_invested, compound_frequency, real_rate,
             expected):
    assert roi_no_contributions.roi(starting_principal, years_invested,
                              compound_frequency, real_rate) == expected
