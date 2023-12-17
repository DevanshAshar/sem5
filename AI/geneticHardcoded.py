import random
gene = ['01101', '11000', '01000', '10011']
def selection(gene):
    x=[]
    for i in gene:
        x.append(int(i,2))
    fx=[]
    for i in x:
        fx.append(i*i)
    fx_sum = sum(fx)
    fx_avg = fx_sum // len(fx)
    expected_count=[]
    for i in fx:
        expected_count.append(round((i / fx_avg), 4))
    actual_count=[]
    for i in expected_count:
        actual_count.append(round(i))
    mate_pool = []
    for i, j in zip(actual_count, gene): 
        if i:
            for c in range(i):
                mate_pool.append(j)
    return x, fx, fx_sum, fx_avg, expected_count, actual_count, mate_pool
def crossover(mate_pool):
    mate, crossover_points = [1,0,3,2],[4,4,2,2] #hardcoded
    new_poplu = [-1] * len(mate_pool)
    for i in mate:
        new_poplu[i] = mate_pool[i][:crossover_points[i]] + mate_pool[mate[i]][crossover_points[i]:]#mate_pool=01101 crossover_point=4  0110+  left wale ka jo bhi mate hai uska baaki ka part concat kardo
    x=[]
    for i in new_poplu:
        x.append(int(i, 2))
    fx=[]
    for i in x:
        fx.append(int(i) * int(i))
    return mate_pool, new_poplu, mate, crossover_points, x, fx
def GA(gene, iter, n):
    if iter == 0:
        return    
    x,fx, fx_sum,fx_avg,excepted_count,actual_count,mate_pool = selection(gene)
    if sum(actual_count)!=len(gene):
        print("Error dont know what to do at this situation ")
        return 
    print(f"\n------------------------------------------------- GENERATION {n} --------------------------------------------------")
    print("Initial Population\tX Value\t\tFitness Value( f(x) )\tProbability(Expected Count)\tActual Count")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{gene[i]}\t\t\t{x[i]}\t\t{fx[i]}\t\t\t{excepted_count[i]}\t\t\t\t{actual_count[i]}")
    mate_pool, new_poplu, mate, crossover_points, x, fx = crossover(mate_pool)
    print(f"\n----------------------------------------------- New Population {n} ------------------------------------------------")
    print("Mate Pool\tMate\t\tCrossover Points\tNew Population\t\tx value\t\tf(x)")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{mate_pool[i]}\t\t{mate[i]}\t\t{crossover_points[i]}\t\t\t{new_poplu[i]}\t\t\t{x[i]}\t\t{fx[i]}")
    GA(new_poplu, iter - 1, n + 1)
GA(gene, 3, 0)
