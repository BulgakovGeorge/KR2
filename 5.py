array = list(map(int, input().split()))
#Реверс списка, чтобы удобно пройтись от конца, так как нужно найти сумму ПОСЛЕДНЕГО набора чисел между нолями
array.reverse()
zero_counter = 0
summ = 0

for ind in range(len(array)):
	#Пропуск чисел до первого встреченного ноля, потому что они не учитываются
	if zero_counter == 0 and array[ind] != 0:
		continue

	#Выход из цикла, так как было найдено два ноля
	if zero_counter == 2:
		break

	#Подсчет количества нулей, чтобы в будущем выйти из цикла	
	if array[ind] == 0:
		zero_counter+=1
	else:
		summ+= array[ind]

print(summ)

