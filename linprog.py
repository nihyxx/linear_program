# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from scipy.optimize import linprog

if __name__ == "__main__":
    obj = [1, 1, 1, 1]
    lhs = [[2,-8,0,-10],[-5,-2,0,0],[-3,5,-10,2]]
    rhs = [-50,-100,-25]

    optimization = linprog(c=obj, A_ub=lhs, b_ub=rhs)

    print(optimization)


