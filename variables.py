def generate_cnf(states, characters, rules):
    clauses = []
    var_map = {}
    counter = 1

    # transitions
    for i in states:
        for j in states:
            for c in characters:
                var_map[f"t_{i},{c},{j}"] = counter
                counter += 1

    # paths
    for i in states:
        for j in states:
            for (l, r) in rules:
                var_map[f"p_{i},{r},{j}"] = counter
                counter += 1

    # clauses
    for (l, r) in rules:
        for i in states:
            for j in states:
                if f"t_{i},{l},{j}" in var_map and f"p_{i},{r},{j}" in var_map:
                    t_var = var_map[f"t_{i},{l},{j}"]
                    p_var = var_map[f"p_{i},{r},{j}"]
                    clauses.append([-t_var, p_var])

    return clauses, var_map

states = range(3)
characters = ['a', 'b']
rules = [('a', 'aa'), ('ab', 'ba'), ('b', 'bb')]

clauses, var_map = generate_cnf(states, characters, rules)

num_vars = len(var_map)
num_clauses = len(clauses)
print(f"p cnf {num_vars} {num_clauses}")
for clause in clauses:
    print(" ".join(map(str, clause)) + " 0")

print("\nVariable mapping:")
for var, id in var_map.items():
    print(f"{id}: {var}")

