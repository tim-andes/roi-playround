import roi_playground

# Adjusted rate / real_rate
@pytest.mark.parametrize("growth_rate, inflation_rate, expected",
                         [(.05, .03, .01942),
                          (.1, .03, 0.06796),
                          (0, 0, 0),
                          (1, .5, 0.33333)])
def test_real_rate(growth_rate, inflation_rate, expected):
    assert roi_playground.real_rate(growth_rate, inflation_rate) == expected
