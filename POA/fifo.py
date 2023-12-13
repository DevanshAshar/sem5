def fifo(capacity,pages):
    pg=[]
    faults=0
    for page in pages:
        if page not in pg:
            if len(pg)==capacity:
                pg.pop(0)
            pg.append(page)
            print(f"{pg} Fault")
            faults+=1
        else:
            print(f"{pg} Page HIT")
    return faults
totalFaults=fifo(capacity=3,pages=[4 , 7, 6, 1, 7, 6, 1, 2, 7, 2])
print(f"Total Faults={totalFaults}")
