"""
Функции, используемые в прогргамме
"""

def srednee(niz, verh):
	# Функция для подсчёта среднего значения в диапазоне угадываемых чисел
	a = niz + verh
	b = a / 2
	if a % 2 == 0:
		sred = int(b)
	else:
		sred = int(b) + 1
	return sred


def reakciya():
	# Функция для отработки реакции на неверный или ложный ответ
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