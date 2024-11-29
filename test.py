import random
import collections

if __name__ == '__main__':
    grupos = collections.defaultdict(list)
    for a in range(int(input("grupos M "))):
        grupos[a] = []
    print(list(grupos.keys()))
    for _ in range(int(input("persona N "))):
        persona = input()
        i = random.choice([x for x in list(grupos.keys()) if len(grupos[x])<3])
        grupos[i].append(persona)
    print(grupos)