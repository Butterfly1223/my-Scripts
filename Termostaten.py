#!/usr/bin/python3

NuTemp = input('Hur många grader är det just nu? ')

if NuTemp <= '24':
 print(f'Slå på värmen, det är {NuTemp} grader')
elif NuTemp >= '25':
 print(f'Stäng av värmen, det är {NuTemp} grader')

