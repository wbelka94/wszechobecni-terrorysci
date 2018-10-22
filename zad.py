import itertools
import random

n = 10000  # liczba osob
p = 0.1  # prawdopodobienstwo nocowania w hotelu
h = 100  # liczba hoteli
d = 100  # liczba dni

m = {} #slownik par ?
histogram = {}
suspectsPersons = set()
suspectsPairs = set()
suspectsPersonsAndDays = 0
for di in range(d):                                         # iterujemy po dniach
    hs = {}  # hotel state                                    lista osob w hotelu
    for ni in range(n):                                     # iterujemy po osobach
        if random.random() < p:                             # sprawdzamy czy di dnia ni osoba poszla do hotelu
            nh = random.randint(0, h)                       # losujemy numerek hotelu do którego idzie
            hs[nh] = hs.get(nh, []) + [ni]                  # dopisujemy ta osobe do listy osob w hotelu
    for v in hs.values():                                   # iterujemy po hotelach
        for pair in list(itertools.combinations(v, 2)):     # iterujemy po wszystkich parach w v hotelu
            m[pair] = m.get(pair, 0) + 1                    # zwiekszamy licznik spotkania sie konkretnej pary

for k,v in m.items():
    histogram[v] = histogram.get(v, 0) + 1
    if v >= 2:
        suspectsPersonsAndDays += v*(v-1)/2
        suspectsPersons.add(k[0])
        suspectsPersons.add(k[1])
        suspectsPairs.add(k)

print('Histogram', histogram)
print('Liczbna podejrzanych par:', len(suspectsPairs))
print('Liczba podejrzanych osób:', len(suspectsPersons))
print('Liczba podejrzanych par "osób i dni":', (int)(suspectsPersonsAndDays))