import datetime
import os
import re

regex = re.compile(r'(?P<semana>\w+) (?P<dia>\d\d/\d\d/\d\d\d\d) (?P<horario>\d+):.+')

semana_dict = dict(
    sunday=0,
    monday=1,
    tuesday=2,
    wednesday=3,
    thursday=4,
    friday=5,
    saturday=6
)


def read(mode='mean'):
    c_aux = [[dict() for _ in range(7)] for _ in range(24)]
    size = os.path.getsize('online.txt')
    with open('online.txt') as f:
        while True:
            line = f.readline()
            print(f'\rCarregando... {f.tell()}/{size}', end='')
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
                c_aux[horario][semana].setdefault(dia, 0)
                c_aux[horario][semana][dia] += 1

    c = [[0] * 7 for _ in range(24)]
    if mode == 'mean':
        for i, row in enumerate(c_aux):
            for j, e in enumerate(row):
                if e:
                    c[i][j] = sum(e.values()) / len(e)
    elif mode == 'last7days':
        for i, row in enumerate(c_aux):
            for j, e in enumerate(row):
                for d in e:
                    if datetime.date.today() - datetime.datetime.strptime(d, '%d/%m/%Y').date() < datetime.timedelta(7):
                        c[i][j] = e[d]
    return c


if __name__ == '__main__':
    for r in read():
        print(r)
