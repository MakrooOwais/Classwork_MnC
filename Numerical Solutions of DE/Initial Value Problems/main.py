from sympy import var, simplify
from sympy.utilities.lambdify import lambdify
from forward_euler import ForwardEuler
from backward_euler import BackwardEuler
from rk_method import RungeKuttaMethod
from milne_pc_method import MilnePreCorr
from modified_euler import ModFEM


menu = """1. Forward Euler Method (FEM)
2. Backward Euler Method (BEM)
3. RK Method (RKM)
4. Milne Predictor-Corrector Method (MPC)
5. Modified Euler Method (MEM)
Enter Q to quit.

Select a Method:"""


methods = {
    "FEM": ForwardEuler,
    "BEM": BackwardEuler,
    "RKM": RungeKuttaMethod,
    "MPC": MilnePreCorr,
    "MEM": ModFEM,
    "Q": quit
}

print(menu)
method = input().upper()

while method not in methods.keys():
    print("Please enter a valid code.")
    try:
        method = input().upper()
    except:
        continue

if method == "RKM":
    method = methods[method](int(input("Enter the order of the method: ")))
else:
    method = methods[method]()

x = var("x")
y = var("y")

user_input = input("Enter f(x, y): ")
expr = simplify(user_input)
f = lambdify((x, y), expr)

param = dict()
print("Please enter")
for x in method.param.keys():
    if x not in param.keys():
        param[x] = None
    while param[x] == None:
        try:
            if x == "error":
                param[x] = float(input(x + ": ") or 1e-3)

                break
            else:
                param[x] = float(input(x + ": "))

        except:
            print("Please enter a float.")

method.set_param(**param)
print(method.solve(f))
