import pulp

# Create a problem variable:
problem = pulp.LpProblem("Maximize_Beverage_Production", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')  # Units of Lemonade to produce
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')  # Units of Fruit Juice to produce

# Objective Function
problem += x + y, "Total_Production"

# Constraints
problem += 2 * x + 1 * y <= 100, "Water_Constraint"
problem += 1 * x <= 50, "Sugar_Constraint"
problem += 1 * x <= 30, "Lemon_Juice_Constraint"
problem += 2 * y <= 40, "Fruit_Puree_Constraint"

# Solve the problem
problem.solve()

# Print the results
print("Production Plan:")
print(f"Lemonade: {x.varValue} units")
print(f"Fruit Juice: {y.varValue} units")
print(f"Total Production: {pulp.value(problem.objective)} units")