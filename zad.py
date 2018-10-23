import itertools
import random


def simulate():
    m = {}
    histogram = {}
    suspects_persons = set()
    suspects_pairs = set()
    suspects_persons_and_days = 0
    for di in range(d):
        hs = {}
        for ni in range(n):
            if random.random() < p:
                nh = random.randint(0, h)
                hs[nh] = hs.get(nh, []) + [ni]
        for v in hs.values():
            for pair in list(itertools.combinations(v, 2)):
                m[pair] = m.get(pair, 0) + 1

    for k, v in m.items():
        histogram[v] = histogram.get(v, 0) + 1
        if v >= 2:
            suspects_persons_and_days += v * (v - 1) / 2
            suspects_persons.add(k[0])
            suspects_persons.add(k[1])
            suspects_pairs.add(k)

    return {
        "histogram": histogram,
        "pp": len(suspects_pairs),
        "po": len(suspects_persons),
        "ppod": int(suspects_persons_and_days),
    }


n = int(input("Podaj liczbę osób (n):"))  # 10 000
p = float(input("Podaj prawdopodobieństwo przenocowania w hotelu (p):"))  # 0.1
h = int(input("Podaj liczbę hoteli (hn):"))  # 100
d = int(input("Podaj liczbę dni (dn):"))  # 100
x = int(input("Podaj liczbę przebiegów (x):"))

results = []
for _ in range(x):
    results.append(simulate())

sumResults = {}
for item in results:
    sumResults['pp'] = sumResults.get('pp', 0) + item['pp']
    sumResults['po'] = sumResults.get('po', 0) + item['po']
    sumResults['ppod'] = sumResults.get('ppod', 0) + item['ppod']

print('Histogram', results[0]['histogram'])
print('Liczbna podejrzanych par:', int(sumResults['pp'] / x))
print('Liczba podejrzanych osób:', int(sumResults['po'] / x))
print('Liczba podejrzanych par "osób i dni":', int(sumResults['ppod'] / x))