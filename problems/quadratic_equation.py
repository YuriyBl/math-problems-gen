import sympy
from enum import Enum
from problems.helper import get_coefficients, random

class QERoots(Enum):
	ZERO = 0
	ONE = 1
	TWO = 2
	RANDOM = 'Random'

class QELeftSideType(Enum):
	RANDOM = 'Random'
	QUADRATIC_EXPANDED = 'Quadratic expanded'
	QUADRATIC_SHORT = 'Quadratic short'

class QERightSideType(Enum):
	RANDOM = 'Random'
	ZERO = 'Zero'
	QUADRATIC_EXPANDED = 'Quadratic expanded'
	QUADRATIC_SHORT = 'Quadratic short'

QERootsNoRandom = list(filter(lambda c: c != QERoots.RANDOM, QERoots))
QELeftSideTypeNoRandom = list(filter(lambda c: c != QELeftSideType.RANDOM, QELeftSideType))
QERightSideTypeNoRandom = list(filter(lambda c: c != QERightSideType.RANDOM, QERightSideType))

def make_quadratic_equation(var='x', roots=QERoots.TWO, left_side_type=QELeftSideType.QUADRATIC_EXPANDED, right_side_type=QERightSideType.ZERO):
	'''
	roots: number of roots (0, 1 ,2 (DEFUALT), 3 (random))
	'''
	if isinstance(var, str): var = sympy.Symbol(var)

	if not isinstance(roots, QERoots): raise TypeError("Roots must be QERoots")
	if not isinstance(left_side_type, QELeftSideType): raise TypeError("left_side_type must be QELeftSideType")
	if not isinstance(right_side_type, QERightSideType): raise TypeError("right_side_type must be QERightSideType")
		
	if roots == QERoots.RANDOM: roots = random.choice(QERootsNoRandom)
	if left_side_type == QELeftSideType.RANDOM: left_side_type = random.choice(QELeftSideTypeNoRandom)
	if right_side_type == QERightSideType.RANDOM: right_side_type = random.choice(QERightSideTypeNoRandom)

	if roots == QERoots.TWO:
		a = random.choice([-2, -1, 1, 2])
		x1, x2 = get_coefficients(2, unique=True)
		ls = a*(var - x1) * (var - x2)
		sols = [x1, x2]
	elif roots == QERoots.ONE:
		a = random.choice([-2, -1, 1, 2])
		[x1] = get_coefficients(1)
		ls = a*(var - x1) * (var - x1)
		sols = x1
	elif roots == QERoots.ZERO:
		[b] = get_coefficients(1)
		c = random.randint(b**2+4, b**2 + 10) // 4  # b**2 < 4c
		ls = var**2 + b*var + c
		sols = sympy.EmptySet

	if right_side_type == QERightSideType.ZERO:
		rs = 0
	else:
		ls_new = sympy.Integer(0)
		rs = sympy.Integer(0)
		for p in ls.expand().args:
			coef = random.choice([-2, 0, 1, 2])
			ls_new += p+(coef*p)
			rs += (coef*p)
		ls = ls_new

	if left_side_type == QELeftSideType.QUADRATIC_EXPANDED:
		ls = ls.expand()
	elif left_side_type == QELeftSideType.QUADRATIC_SHORT:
		ls = ls.factor()

	if right_side_type == QERightSideType.QUADRATIC_EXPANDED:
		rs = rs.expand()
	elif right_side_type == QERightSideType.QUADRATIC_SHORT:
		rs = rs.factor()

	eq = sympy.Eq(ls, rs)
	return eq, sols