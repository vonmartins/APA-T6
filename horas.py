"""
Autor: Marti DOminguez Rivero
Descripción: Este fichero contiene la función `normalizaHoras`, que analiza un fichero
de texto en busca de expresiones horarias y las normaliza al formato estándar HH:MM.
Las expresiones incorrectas se dejan tal cual.
"""
import re

def normalizaHoras(ficText, ficNorm):
    """
    Lee un fichero de texto, analiza las expresiones horarias y escribe un nuevo fichero
    con las expresiones normalizadas en formato HH:MM.

    Las expresiones incorrectas se dejan tal cual.

    Ejemplo:
    Entrada:
        La llegada del tren está prevista a las 18:30
        Tenía su clase entre las 8h y las 10h30m
        Se acaba a las 4 y media de la tarde
    Salida:
        La llegada del tren está prevista a las 18:30
        Tenía su clase entre las 08:00 y las 10:30
        Se acaba a las 16:30
    """
    patrones = [
        (re.compile(r'(\d{1,2}):(\d{2})'), lambda m: f'{int(m.group(1)):02}:{int(m.group(2)):02}'),
        (re.compile(r'(\d{1,2})h(\d{1,2})m'), lambda m: f'{int(m.group(1)):02}:{int(m.group(2)):02}'),
        (re.compile(r'(\d{1,2})h'), lambda m: f'{int(m.group(1)):02}:00'),
        (re.compile(r'(\d{1,2}) y media de la tarde'), lambda m: f'{int(m.group(1)) + 12}:30'),
        (re.compile(r'(\d{1,2}) y cuarto de la tarde'), lambda m: f'{int(m.group(1)) + 12}:15'),
        (re.compile(r'(\d{1,2}) menos cuarto de la tarde'), lambda m: f'{int(m.group(1)) + 11}:45'),
        (re.compile(r'(\d{1,2})h de la mañana'), lambda m: f'{int(m.group(1)):02}:00'),
        (re.compile(r'12 de la noche'), lambda m: '00:00'),
    ]

    with open(ficText, 'r', encoding='utf-8') as entrada, open(ficNorm, 'w', encoding='utf-8') as salida:
        for linea in entrada:
            original = linea
            for patron, reemplazo in patrones:
                linea = patron.sub(reemplazo, linea)
            salida.write(linea)


if __name__ == "__main__":
    normalizaHoras('horas.txt', 'horas_normalizadas.txt')