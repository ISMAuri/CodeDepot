#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#crudo
crudo_dalto = 3.5
crudo_promedio_cursos = 5

#Diferencias de duracion
diferencia_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_max = round(100 - dalto_curso / otros_cursos_max * 100, 1)
diferencia_promedio = 100 - dalto_curso / otros_cursos_promedio * 100


print(f'El curso de dalto dura {diferencia_min}% menos que el minimo de duracion de los demas cursos.')
print(f'El curso de dalto dura {diferencia_max}% menos que el maximo de duracion de los demas cursos.')
print(f'El curso de dalto dura {diferencia_promedio}% menos que el promedio de duracion de los demas cursos.')

porcentaje_dalto = round(100 - dalto_curso / crudo_dalto * 100, 1)
porcentaje_promedio_cursos = 100 - otros_cursos_promedio / crudo_promedio_cursos * 100

print(f' El porcentaje de marterial inservible reducido en el curso de dalto es de un {porcentaje_dalto}%.')
print(f' El porcentaje de marterial inservible reducido en el promedio de cursos es de un {porcentaje_promedio_cursos}%.')

horas_de_dalto_a_otro =  round(otros_cursos_promedio / dalto_curso * 10, 1)
horas_de_otro_a_dalto =  round(dalto_curso / otros_cursos_promedio * 10, 1)

print(f' Ver 10 horas del curso de dalto equivale a ver {horas_de_dalto_a_otro} horas de otro curso.')
print(f' Ver 10 horas de otro curso equivale a ver {horas_de_otro_a_dalto} horas de dalto.')