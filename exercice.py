#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
pi = math.pi

def square_root(a: float) -> float:
    a **= 1/2
    return a


def square(a: float) -> float:
    a **= 2
    return a


def average(a: float, b: float, c: float) -> float:
    moyenne = (a + b + c)/3
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_total = (math.radians(angle_degs + (angle_mins/60) + (angle_secs/3600)))

    return angle_total



def to_degrees(angle_radian = float) -> tuple:
    degrees = math.degrees(angle_radian)
    minutes = (degrees - math.floor(degrees)) * 60
    seconds = (minutes - math.floor(minutes)) * 60
    return math.floor(degrees), math.floor(minutes), seconds

def to_celsius(temperature: float) -> float:
    temperature = ((temperature - 32) / 1.8)
    return temperature


def to_farenheit(temperature: float) -> float:
    temperature = ((temperature * 1.8) + 32)
    return temperature


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
