import sympy

#C = {C}_{0}\exp{{k}_{T}t}
#k = {A}_{0}\exp{\dfrac{{E}_{a}}{RT}}


#(32 °F − 32) × 5/9 + 273.15 = 273.15 K

def fahren_to_kelvin(x):
	return ((x − 32)*5.0/9.0 + 273.15)

def calc_k_constant(t):
	return (A_0*math.exp(E_a/(GAS_CONSTANT*t)));

if __name__ == "__main__":
	a = fahren_to_kelvin(200)
	b = fahren_to_kelvin(300)
	c = fahren_to_kelvin(400)
	d = fahren_to_kelvin(500)
	e = fahren_to_kelvin(600)

	k_a = calc_k_constant(a)
	k_b = calc_k_constant(b)
	k_c = calc_k_constant(c)
	k_d = calc_k_constant(d)
	k_e = calc_k_constant(e)
	
	C_0 = Symbol('{c}_{0}')
	t = Symbol('t') #where t is expressed in minutes
	C_a = C_0*sympy.exp(-k_a*t)
	C_b = C_0*sympy.exp(-k_b*t)
	C_c = C_0*sympy.exp(-k_c*t)
	C_d = C_0*sympy.exp(-k_d*t)
	C_e = C_0*sympy.exp(-k_e*t)

