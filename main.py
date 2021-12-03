import sympy
from problems.circle_line_intersection import CLIIntersections, make_circle_line_intersection
from problems.helper import get_coefficients, line_from_point_and_vector_parametric, alpha_u
from problems.line_line_intersection import LLIIntersections, LLILineForm, make_line_line_intersection_2d
from problems.quadratic_equation import QELeftSideType, QERightSideType, QERoots, make_quadratic_equation
from problems.quadratic_inequality import make_quadratic_inequality

quadratic_equation, solution = make_quadratic_equation(roots=QERoots.TWO, left_side_type=QELeftSideType.RANDOM, right_side_type=QERightSideType.RANDOM)
print(f"$$ {sympy.latex(quadratic_equation)} $$")
print(f"$$ {sympy.latex(solution)} $$")

print()

quadratic_inequality, solution = make_quadratic_inequality(left_side_type=QELeftSideType.RANDOM, right_side_type=QERightSideType.RANDOM)
print(f"$$ {sympy.latex(quadratic_inequality)} $$")
print(f"$$ {sympy.latex(solution)} $$")

print()

circle, line, line_parametric, solution = make_circle_line_intersection(CLIIntersections.ONE)
print(f"$$ k : {sympy.latex(circle)} $$")
print(f"$$ l : {sympy.latex(line)} $$")
print(f"$$ l : {line_parametric} $$")
solution_points = []
for i in range(len(solution)):
	if (solution[i] == sympy.EmptySet): solution_points.append(sympy.latex(solution[i]))
	solution_points.append(f"{alpha_u[i]}={sympy.latex(solution[i])}")
print(f"$$ solution: {alpha_u[i]}={sympy.latex(solution[i])} $$")

print()

line_1, line_2, solution = make_line_line_intersection_2d(intersections=LLIIntersections.ZERO, first_line_form=LLILineForm.GENERIC, second_line_form=LLILineForm.GENERIC)
print(f"$$ m : {sympy.latex(line_1)} $$")
print(f"$$ n : {sympy.latex(line_2)} $$")
print(f"$$ solution: A={sympy.latex(solution)} $$")