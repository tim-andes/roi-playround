def real_rate(growth_rate, inflation_rate):
	"""
	
	:param growth_rate: Growth rate of investment
	:param inflation_rate: Rate of inflation
	:return: Adjusted growth rate after inflation
	"""
	real_rate = ((1 + growth_rate) / (1 + inflation_rate)) - 1
	return round(real_rate, 5)
  
if __name__ == "__main__":
	real_rate(growth_rate, inflation_rate)
