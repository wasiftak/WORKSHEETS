S1={10,20,30,40,50,60}
S2={40,50,60,70,80,90}
S1.update([55,66])
print(S1)

S1.remove(10)
S1.remove(30)

S1.union(S2)

S1.intersection(S2)

S1.difference(S2)