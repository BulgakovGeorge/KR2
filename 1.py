string = input()
cel_string = ''
cel_count = 0
drob_string = ''
drob_count = 0

dot_was_found = False

for char in string:
	if char == '.':
		dot_was_found = True
		continue

	#Проверка на то, что мы работаем в целой части или дробной
	if dot_was_found == False:
		cel_string += char
		cel_count +=1 

	else:
		drob_string += char
		drob_count +=1

if dot_was_found == False:
	print("Строка не явлвяется десятичным числом с целой и дробной частью")
else:
	print("Целая часть:\n",cel_string,"Количество символом -",cel_count)
	print("Дробная часть:\n",drob_string,"Количество символом -",drob_count)