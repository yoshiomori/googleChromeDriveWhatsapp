import re

regex = re.compile(r'(?P<semana>\w+) (?P<dia>\d+)/November (?P<horario>\d+):.+')

semana_dict = dict(
    sunday=0,
    monday=1,
    tuesday=2,
    wednesday=3,
    thursday=4,
    friday=5,
    saturday=6
)


def read():
    c_aux = [[dict() for _ in range(7)] for _ in range(24)]
    with open('online.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            m = regex.match(line)
            if m:
                d = m.groupdict()
                semana = d.get('semana')
                semana = semana.lower()
                semana_aux = semana_dict.get(semana)
                if not semana_aux:
                    print(semana)
                semana = semana_aux
                dia = d.get('dia')
                horario = d.get('horario')
                horario = int(horario)
                print(f'{semana} {dia} {horario}')
                c_aux[horario][semana].setdefault(dia, 0)
                c_aux[horario][semana][dia] += 1

    c = [[0] * 7 for _ in range(24)]
    for i, row in enumerate(c_aux):
        for j, e in enumerate(row):
            if e:
                c[i][j] = sum(e.values()) / len(e)
    return c


if __name__ == '__main__':
    for r in read():
        print(r)
