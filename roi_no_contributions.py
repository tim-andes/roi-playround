import adjusted_growth_rate

def roi(starting_principal, years_invested, compound_frequency, real_growth_rate):
	"""
	Calculate return on investment, excluding monthly contributions.

	:param starting_principal: Starting capital
	:param years_invested: Number of years monies will be invested
	:param compound_frequency: Frequency that interest compounds (1 for anually)
	:param real_rate: Rate of growth adjusted for inflation
	:return: Final balance after year over year growth
	"""
	if compound_frequency == 0: # handle 0 division error
		compound_frequency = 1

	final_balance = (1 + real_rate / compound_frequency)
	final_balance **= (years_invested * compound_frequency)
	final_balance *= starting_principal
	final_balance = round(final_balance)

	return final_balance
  
  if __name__ == "__main__":
    real_growth_rate = adjusted_growth_rate.real_growth_rate(growth_rate, inflation_rate)
    roi(starting_principal, years_invested, compound_frequency, real_growth_rate)
