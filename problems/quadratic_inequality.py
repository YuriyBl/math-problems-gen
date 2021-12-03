import sympy
from problems.quadratic_equation import QELeftSideType, QELeftSideTypeNoRandom, QERightSideTypeNoRandom, QERightSideType, QERoots, make_quadratic_equation
from problems.helper import random

def make_quadratic_inequality(var='x', left_side_type=QELeftSideType.QUADRATIC_EXPANDED, right_side_type=QERightSideType.ZERO):
	if not isinstance(left_side_type, QELeftSideType): raise TypeError("left_side_type must be QELeftSideType")
	if not isinstance(right_side_type, QERightSideType): raise TypeError("right_side_type must be QERightSideType")

	if left_side_type == QELeftSideType.RANDOM: left_side_type = random.choice(QELeftSideTypeNoRandom)
	if right_side_type == QERightSideType.RANDOM: right_side_type = random.choice(QERightSideTypeNoRandom)

	eq, _ = make_quadratic_equation(var=var, roots=QERoots.TWO, left_side_type=left_side_type, right_side_type=right_side_type)

	ls, rs = eq.args
	sign = random.choice(['>', '>=', '<', '<='])
	poly = sympy.Poly(ls - rs)
	sol = sympy.solve_poly_inequality(poly, sign)
	sol = sympy.Union(*sol)

	if left_side_type == QELeftSideType.QUADRATIC_EXPANDED:
		ls = ls.expand()
	elif left_side_type == QELeftSideType.QUADRATIC_SHORT:
		ls = ls.factor()

	if right_side_type == QERightSideType.QUADRATIC_EXPANDED:
		rs = rs.expand()
	elif right_side_type == QERightSideType.QUADRATIC_SHORT:
		rs = rs.factor()

	return sympy.sympify(str(ls) + sign + str(rs)), sol
	