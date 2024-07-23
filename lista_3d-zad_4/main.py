"""Napisz generator, który zwraca wartości funkcji trygonometrycznych sin(x),
cos(x) i tan(x) dla kolejnych wartości x z podanego zakresu."""

import math

def trig_generator(start, end, step=1):

    for x in range(start, end, step):
        # Convert x to radians
        x_rad = math.radians(x)

        # Calculate sin(x), cos(x), and tan(x)
        sin_x = math.sin(x_rad)
        cos_x = math.cos(x_rad)
        tan_x = math.tan(x_rad)

        # Yield the values as a tuple
        yield (x, sin_x, cos_x, tan_x)

def main(start=0, end=360, step=1):
    print(f"Start...")
    for x, sin_x, cos_x, tan_x in trig_generator(start, end, step):
        print(f"x: {x}, sin(x): {sin_x}, cos(x): {cos_x}, tan(x): {tan_x}")


if __name__ == "__main__":
    main()