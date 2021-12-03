import sympy
import random
from string import ascii_lowercase, ascii_uppercase

random = random.Random()

alpha = [i for i in ascii_uppercase + ascii_lowercase]
alpha_l = list(ascii_lowercase)
alpha_u = list(ascii_uppercase)

for l in [alpha, alpha_u, alpha_l]:
	try:
		l.remove("l")
		l.remove("o")
		l.remove("O")
		l.remove("I")
		l.remove("i")
	except ValueError:
		pass

digits = list(range(-26,26))
digits_nozero = list(range(-26,26))
digits_nozero.remove(0)
irrationals = [sympy.sqrt(3), sympy.sqrt(2), sympy.sqrt(5)]
rationals = [sympy.Rational(1/2), sympy.Rational(1/4), sympy.Rational(1/5)]


def get_int_coef(min=-6, max=6):
	l = list(range(min, max))
	if 0 in l: l.remove(0)
	return random.choice(l)


def get_irr_coef():
	return random.randint(1,6) * random.choice(irrationals)


def get_rat_coef(min=-6, max=6):
	return random.randint(min,max-1) + random.choice(rationals)


def get_coefficients(n, int=True, rat=False, irr=False, min=-10, max=10, unique=False):
	if unique and max-min < n: 
		raise Exception(f"It's impossible to generate {n} unique coeffs in range {min} to {max}")

	coeffs = []
	while len(coeffs) != n:
		random_coeffs = []

		if int: random_coeffs.extend([get_int_coef(min, max)] * 2) # chance of int is bigger
		if rat: random_coeffs.append(get_rat_coef(min, max))
		if irr: random_coeffs.append(get_irr_coef())

		c = random.choice(random_coeffs)

		if unique and c not in coeffs: coeffs.append(c)
		elif not unique: coeffs.append(c)

	return coeffs


def line_from_point_and_vector(A, u):
	x, y, t = sympy.symbols('x y t')
	m = (-u[1], u[0]) # used to get rid of parameter

	line_x = A[0] + t*u[0]
	line_y = A[1] + t*u[1]

	# get rid of t
	line = m[0]*x + m[1]*y - ((m[0] * line_x).expand() + (m[1] * line_y).expand())
	line = sympy.Eq(line, 0)

	return line.expand()


def line_from_two_points(A, B):
	u = (B[0] - A[0], B[1] - A[1])
	return line_from_point_and_vector(A, u)


def line_from_point_and_vector_parametric(A, u):
	mult = random.choice([random.randint(2,5), random.randint(-5,-2)]) 
	A = (A[0] + mult*u[0], A[1] + mult*u[1])

	return f"{sympy.latex(A)} + t{sympy.latex(u)}"


def line_from_two_points_parametric(A, B):
	u = (B[0] - A[0], B[1] - A[1])
	mult = random.choice([random.randint(2,5), random.randint(-5,-2)]) 
	A = (A[0] + mult*u[0], A[1] + mult*u[1])

	return f"{sympy.latex(A)} + t{sympy.latex(u)}"