"""
Данная программа угадывает натуральное число, задуманное пользователем в заданном диапазоне (от 1 до 100). 
Максимальное количество попыток, которое требуется программе, равно 7.
Данная программа является интерактивной.
В программу по возможности были включены элементы, изученные в разделе (Юнит 0).
"""

#------------------------------------------------------------------------------
# Переменные и функции, используемые в модуле
#------------------------------------------------------------------------------


import re 																		# Модуль для формирования регулярного выражения

obrazec_chisla = re.compile('\d+')												# Регулярное выражение для опрежделения формы задуманного числа (натуральное число)
ghelanie = True																	# Переменная для отслеживания наличия у игрока или программы желания продолжать игру
terpenie = 3																	# Счётчик терпения уменьшается каждый раз на 1, если игрок не справляется с заданием

# Функция для подсчёта среднего значения в диапазоне угадываемых чисел
def srednee(niz, verh):
	a = niz + verh
	b = a / 2
	if a % 2 == 0:
		sred = int(b)
	else:
		sred = int(b) + 1
	return sred

# Функция для отработки реакции на неверный или ложный ответ
def reakciya():
	global terpenie
	if terpenie == 3:
		terpenie -= 1
		print("Наверное вы не переключили раскладку клавиатуры на русский язык. ", end = 2 * "\n")
	elif terpenie == 2:
		terpenie -= 1
		print("Читайте внимательно вопрос. ", end = 2 * "\n")
	elif terpenie == 1:
		terpenie -= 1
		print("Неужели это слишком сложно для вас? ", end = 2 * "\n")
	elif terpenie == 0:
		terpenie -= 1
		print("Вы не справились.")
		input("Прощайте!!! ")

#------------------------------------------------------------------------------
# Тело программы
#------------------------------------------------------------------------------

while ghelanie == True:
	niz = 0					# Нижний предел диапазона угадываемых чисел
	verh = 100				# Верхний предел диапазона угадываемых чисел

	"""
	Цикл для ввода числа. Он проверяет являются ли вводимые данные числом.
	Если да, то находится ли число в пределах от 1 до 100. 
	"""
	
	while True:
		chislo = input("Введите натуральное число от 1 до 100: ")

		# Число или нет
		if obrazec_chisla.fullmatch(chislo) == None:
			print("Введите НАТУРАЛЬНОЕ ЧИСЛО! ", end = 2 * "\n")
			terpenie -= 1
			if terpenie == -1:
					ghelanie = False
					print("Думаю, что это слишком сложно для вас. ", end = 2 * "\n")
					input("Прощайте!!! ")
					break

		# Число в пределах от 1 до 100 или нет
		elif obrazec_chisla.fullmatch(chislo) != None:
			if int(chislo) < 1 or int(chislo) > 100:
				print("Чиcло должно быть от 1 до 100! ", end = 2 * "\n")
				terpenie -= 1
				if terpenie == -1:
						ghelanie = False
						print("Думаю, что это слишком сложно для вас. ", end = 2 * "\n")
						input("Прощайте!!! ")
						break
			elif int(chislo) > 0 or int(chislo) <= 100:
				chislo = int(chislo)
				break

	"""
	Цикл для обработки числа. Пытается угадать число, а также проверяет игрока на обман. 
	"""
	while ghelanie == True:
		dogadka = input("Ваше число равно {0} ? (да/нет): ".format(str(srednee(niz, verh))))

		# 1. Условие угаданного числа, но игрок это отрицает
		if chislo == srednee(niz, verh) and dogadka.lower() == "нет":
			somnenie = input("Вы уверены? (да/нет): ")

			# 1.1 Игрок настаивает
			if somnenie.lower() == "да":
				ghelanie = False
				input("Вы меня обманываете, игра закончена! ")
				break
			# 1.1 Игрок признаётся
			elif somnenie.lower() == "нет":
				print("Не пытайтесь меня обмануть! ", end = 2 * "\n")
				terpenie -= 1

		# 2. Условие угаданного числа, и игрок с этим согласен
		elif chislo == srednee(niz, verh) and dogadka.lower() == "да":
			print("Отлично! ")

			povtor = input("Сыграем ещё раз? (да/нет): ")		# Предложение сыграть ещё

			# 2.1 Согласие сыграть ещё
			if povtor.lower() == "да":
				print("Погнали! ", end = 2 * "\n")
				break
			# 2.2 Отказ сыграть ещё
			elif povtor.lower() == "нет":
				ghelanie = False
				input("Что же, до скорой встречи! ")
				break

		# 3. Условие неугаданного числа, но игрок это отрицает
		elif chislo != srednee(niz, verh) and dogadka.lower() == "да":
			
			somnenie = input("Вы уверены? (да/нет): ")		# Сомнение по поводу ответа

			# 3.1 Игрок настаивает
			if somnenie.lower() == "да":
				print("Попробуйте загадать число ещё раз, только на этот раз не забудьте его. ")
				print()
				break

			# 3.2 Игрок признаётся
			elif somnenie.lower() == "нет":
				print("Будьте внимательнее. ")

		# 4. Условие неугаданного числа, и игрок с этим согласен	
		elif chislo != srednee(niz, verh) and dogadka.lower() == "нет":
			
			sravnenie = input("Ваше число больше или меньше " + str(srednee(niz, verh)) + "? (больше/меньше): ")		# Сомнение по поводу ответа

			# 4.1 Игрок не может верно оценить величину задуманного числа
			if (chislo < srednee(niz, verh) and sravnenie.lower() == "больше") or (chislo > srednee(niz, verh) and sravnenie.lower() == "меньше"):
				print("Вам следует повторить школьную программу. ")
				input("До свидания. ")
				ghelanie = False

			# 4.2 Задуманное число меньше
			elif chislo < srednee(niz, verh) and sravnenie.lower() == "меньше":
				verh = srednee(niz, verh)											# Обновление верхнего предела
			
			# 4.3 Задуманное число больше
			elif chislo > srednee(niz, verh) and sravnenie.lower() == "больше":
				niz = srednee(niz, verh)											# Обновление нижнего предела
			
			# 4.4 Другой ответ
			else:
				reakciya()
				if terpenie == -1:
					ghelanie = False

		# 5. Другой  ответ
		else:
			reakciya()
			if terpenie == -1:
				ghelanie = False
				break