"""На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.

Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.

Формат выходных данных
Программа должна вывести возраст собаки в человеческих годах.

Примечание. В течение первых двух лет собачий год равен 10.510.5 человеческим годам. После этого каждый год собаки равен 4 человеческим годам."""
a = float(input())
if a <= 2:
    print(a * 10.5)
elif a > 2:
    print( 2 * 10.5 + (a -2) * 4)