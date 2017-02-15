def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    power = 0
    diff = 0
    while base ** power < num:
        diff  = abs(base**power-num)
        power += 1
    if diff != 0:
	    laterdiff = abs(base**power-num)
	    if laterdiff < diff:
		    return power
	    else:
		    return power-1
    else:
	    return power

print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
