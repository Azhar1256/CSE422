import numpy as np


def crossover(p1, p2, r_cross):
    c1, c2 = p1.copy(), p2.copy()

    if np.random.rand() < r_cross:
        pt = np.random.randint(0, len(p1))

        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]


def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):

        if np.random.rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]


def selection(pop, scores, k=3):
    selection_ix = np.random.randint(len(pop))
    for ix in np.random.randint(0, len(pop), k - 1):
        selection_ix = ix
    return pop[selection_ix]


def fitness(parent, run, target):
    sum = 0
    for x in range(len(parent)):
        sum = sum + parent[x] * run[x]
    return abs(target - sum)


def genetic_algorithm(fitness, n_bits, n_iter, n_pop, r_cross, r_mut, target, run):
    pop = [np.random.randint(0, 2, n_bits).tolist() for _ in range(n_pop)]

    best, best_eval = 0, fitness(pop[0], run, target)

    for gen in range(n_iter):

        scores = [fitness(c, run, target) for c in pop]

        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]

        selected = [selection(pop, scores) for _ in range(n_pop)]

        children = list()
        for i in range(0, n_pop, 2):
            p1, p2 = selected[i], selected[i + 1]
            for c in crossover(p1, p2, r_cross):
                mutation(c, r_mut)
                children.append(c)
        pop = children
    if best_eval == 0:
        return [1, best]
    else:
        return [0, best]


    

#input

n_bits,target=[int(x) for x in input().split()]

name=[]
run=[]
for _ in range(n_bits):
  x,y=input().split()
  y=int(y)
  name.append(x)
  run.append(y)

x=genetic_algorithm(fitness,n_bits,2**n_bits,20,.5,1.0/n_bits,target,run)
if x[0]==1:
  print(name)
  print(''.join(map(str, x[1])))
else:
  print(name)
  print(-1)
