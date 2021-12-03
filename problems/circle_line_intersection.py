import sympy
from enum import Enum
from problems.helper import get_coefficients, line_from_point_and_vector, line_from_point_and_vector_parametric, line_from_two_points, line_from_two_points_parametric, random

class CLIIntersections(Enum):
	ZERO = 0
	ONE = 1
	TWO = 2
	RANDOM = 'Random'

class CLILineForm(Enum):
	GENERAL = 'General'
	PARAM = 'Param'

CLIIntersectionsNoRandom = list(filter(lambda c: c != CLIIntersections.RANDOM, CLIIntersections))


def make_circle_line_intersection(intersections=CLIIntersections.TWO):
	if not intersections: intersections = CLIIntersections.RANDOM
	if not isinstance(intersections, CLIIntersections): raise TypeError("intersections must be CLIIntersections")
	if intersections == CLIIntersections.RANDOM: intersections = random.choice(CLIIntersectionsNoRandom)

	if intersections == CLIIntersections.ONE:
		'''
		A			- intersection point
		O 		- circle center
		u 		- line vector
		'''
		[A_x, A_y] = get_coefficients(2)
		r = sympy.sqrt(A_x**2 + A_y**2)

		[O_x, O_y] = get_coefficients(2)
		u = (-A_y, A_x)
		A = (A_x + O_x, A_y + O_y)

		x, y = sympy.symbols('x y')
		circle = sympy.Eq((x-O_x)**2 + (y-O_y)**2, r**2)

		line = line_from_point_and_vector(A, u)
		line_parametric = line_from_point_and_vector_parametric(A, u)
		solution = (A)

	elif intersections == CLIIntersections.TWO:
		'''
		A, B 	- intersection points
		O 		- circle center
		'''
		[A_x, A_y] = get_coefficients(2)
		[B_x, B_y] = random.choice([(A_y, A_x), (A_y, -A_x), (-A_y, A_x), (-A_y, -A_x)])
		r = sympy.sqrt(A_x**2 + A_y**2)

		[O_x, O_y] = get_coefficients(2)
		A = (A_x + O_x, A_y + O_y)
		B = (B_x + O_x, B_y + O_y)

		x, y = sympy.symbols('x y')
		circle = sympy.Eq((x-O_x)**2 + (y-O_y)**2, r**2)

		line = line_from_two_points(A, B)
		line_parametric = line_from_two_points_parametric(A, B)
		solution = (A, B)
	elif intersections == CLIIntersections.ZERO:
		'''
		A			- point on circle
		B			- point outside of the circle
		O 		- circle center
		u 		- line vector
		'''
		[A_x, A_y] = get_coefficients(2)
		r = sympy.sqrt(A_x**2 + A_y**2)

		[O_x, O_y] = get_coefficients(2)
		u = (-A_y, A_x)
		A = (A_x + O_x, A_y + O_y)
		mult = random.randint(2, 5)
		B = (A[0]*mult, A[1]*mult)

		x, y = sympy.symbols('x y')
		circle = sympy.Eq((x-O_x)**2 + (y-O_y)**2, r**2)

		line = line_from_point_and_vector(B, u)
		line_parametric = line_from_point_and_vector_parametric(B, u)
		solution = (sympy.EmptySet)

	return circle, line, line_parametric, solution



