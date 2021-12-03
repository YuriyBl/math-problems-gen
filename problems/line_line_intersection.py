from enum import Enum
import sympy

from sympy.sets.sets import Intersection
from problems.helper import get_coefficients, line_from_point_and_vector, line_from_point_and_vector_parametric, random

class LLIIntersections(Enum):
	ZERO = 0
	ONE = 1
	RANDOM = 'Random'

class LLILineForm(Enum):
	RANDOM = 'Random'
	GENERIC = 'General'
	PARAMETRIC = 'Parametric'

LLIIntersectionsNoRandom = list(filter(lambda c: c != LLIIntersections.RANDOM, LLIIntersections))
LLILineFormNoRandom = list(filter(lambda c: c != LLILineForm.RANDOM, LLILineForm))


def make_line_line_intersection_2d(intersections, first_line_form, second_line_form):
	if not isinstance(intersections, LLIIntersections): raise TypeError("intersections must be LLIIntersections")
	if not isinstance(first_line_form, LLILineForm): raise TypeError("first_line_form must be LLILineForm")
	if not isinstance(second_line_form, LLILineForm): raise TypeError("second_line_form must be LLILineForm")

	if not intersections: intersections = LLIIntersections.RANDOM
	if not first_line_form: first_line_form = LLILineForm.RANDOM
	if not second_line_form: second_line_form = LLILineForm.RANDOM

	if intersections == LLIIntersections.RANDOM: intersections = random.choice(LLIIntersectionsNoRandom)
	if first_line_form == LLILineForm.RANDOM: first_line_form = random.choice(LLILineFormNoRandom)
	if second_line_form == LLILineForm.RANDOM: second_line_form = random.choice(LLILineFormNoRandom)


	if intersections == LLIIntersections.ONE:
		A = B = tuple(get_coefficients(2))
		u1 = tuple(get_coefficients(2))
		u2 = tuple(get_coefficients(2))
		while u2 == u1: u2 = tuple(get_coefficients(2))
		solution = (A)
	elif intersections == LLIIntersections.ZERO:
		A = tuple(get_coefficients(2))
		B = tuple(get_coefficients(2))
		while B == A: B = tuple(get_coefficients(2))
		u1 = tuple(get_coefficients(2))
		u2 = random.choice([u1, (-u1[0], -u1[1])])
		solution = (sympy.EmptySet)

	if first_line_form == LLILineForm.GENERIC:
		line_1 = line_from_point_and_vector(A, u1)
	elif first_line_form == LLILineForm.PARAMETRIC:
		line_1 = line_from_point_and_vector_parametric(A, u1)

	if second_line_form == LLILineForm.GENERIC:
		line_2 = line_from_point_and_vector(B, u2)
		line_2 = sympy.Eq(get_coefficients(1)[0] * line_2.args[0], 0)
	elif second_line_form == LLILineForm.PARAMETRIC:
		line_2 = line_from_point_and_vector_parametric(B, u2)


	return line_1, line_2, solution

