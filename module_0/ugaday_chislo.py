import numpy as np

def game_core():
    """Поиск задуманного числа с помощью бинарного поиска"""
    
    def srednee(niz, verh):
        """Функция для подсчёта среднего значения 
        в диапазоне угадываемых чисел"""
        a = niz + verh
        b = a / 2
        if a % 2 == 0:
            sred = int(b)
        else:
            sred = int(b) + 1
        return sred
    
    # Нижний предел диапазона угадываемых чисел
    niz = 0	

	# Верхний предел диапазона угадываемых чисел	              		
    verh = 100 

    # Вариант ответа
    number = srednee(niz, verh)  

    # Количество попыток                  
    count = 1  

    # Задуманное число                         
    predict = np.random.randint(1,101)
    
    # Реализация бинарного поиска
    while predict != number:
        
        # Задуманное число больше варианта ответа
        if predict > srednee(niz, verh):
            niz = srednee(niz, verh)
         
        # Задуманное число меньше варианта ответа    
        elif predict < srednee(niz, verh):
            verh = srednee(niz, verh)
        
        # обновление задуманного числа, и обновление счётчика попыток
        number = srednee(niz, verh)
        count += 1
        
    # Функция возврвщает количество попыток
    return(count)


def sred_kol_poptk():
    """Поиск среднего количества попыток угадать число 
    (во всём диапазоне задуманных чисел)"""
    
    def srednee(niz, verh):
        """Функция для подсчёта среднего значения попыток"""
        a = niz + verh
        b = a / 2
        if a % 2 == 0:
            sred = int(b)
        else:
            sred = int(b) + 1
        return sred
    
    # Пустой массив хранения количества попыток для 
    # всех возможных вариантов задуманного числа
    spisok_poptk = []
 
    # Формирование списка со всеми возможными вариантами загаданного числа 
    for i in range(1, 101):
        count = 1
        niz = 0					
        verh = 100
        number = 50
        count = 1
        
        # Реализация бинарного поиска
        while i != number:
            
            # Задуманное число больше варианта ответа
            if i > srednee(niz, verh):
                niz = srednee(niz, verh)
                
            # Задуманное число меньше варианта ответа       
            elif i < srednee(niz, verh):
                verh = srednee(niz, verh)
                
            # обновление задуманного числа, и обновление счётчика попыток   
            number = srednee(niz, verh)
            count += 1
        
        # Заполнение списка со всеми возможными вариантами загаданного числа
        spisok_poptk.append(count)
    
    # Вычислинение среднего числа требуемых попыток
    sred_poptk = sum(spisok_poptk)/100
    sred_poptk = int(sred_poptk)+1
    
    # Функция возврвщает среднее количество попыток
    return(sred_poptk)
        
     