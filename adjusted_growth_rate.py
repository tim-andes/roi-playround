def real_growth_rate(growth_rate, inflation_rate):
	"""
	Calculate the real investment growth rate after adjusting for inflation.
	
	:param growth_rate: Growth rate of investment
	:param inflation_rate: Rate of inflation
	:return: Adjusted growth rate after inflation
	"""
	real_rate = ((1 + growth_rate) / (1 + inflation_rate)) - 1
	real_rate = round(real_rate, 5)
	return real_rate
  
if __name__ == "__main__":
	real_growth_rate(growth_rate, inflation_rate)
