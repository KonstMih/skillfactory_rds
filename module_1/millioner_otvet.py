# -*- coding: utf-8 -*-

import pandas as pd


# Таблицы данных из файла
data = pd.read_csv("data.csv")

# Таблице данных столбца прибыли по каждому фильму
data["pribil"] = data["revenue"] - data["budget"]

# Замена псевдонима режисёра McG на реальное имя
data["director"] = data["director"].apply(lambda x: "Joseph McGinty Nichol" if x == "McG" else x) 

# Таблице данных столбца с наименованием месяца в котором был выпущен фильм
data["mesac"] = data["release_date"].apply(lambda x: x.split("/")[0])

# Таблице данных столбца с количеством символов в названии фильма
data["kol_simvl"] = data["original_title"].apply(lambda x: len(x))

# Таблице данных столбца с количеством слов в названии фильма
data["kol_slov"] = data["original_title"].apply(lambda x: len(x.split(" ")))

# Таблицы с положительной прибылью
data_prib = data[data["pribil"] > 0]


def spisok_dannih(stolbec):
# Функция для формирования имеющихся в столбце данных
    spisok = []
    for i in data[stolbec].values:
        i = i.split("|")
        for k in i:
           if (k in spisok) == False:
               spisok.append(k)
    return spisok


def spisok_slov(stolbec):
# Функция для формирования имеющихся в столбце данных
    spisok = []
    for i in data[stolbec].values:
        i = i.split(" ")
        for k in i:
           if (k in spisok) == False:
               spisok.append(k)
    return spisok


# Список жаноров
zhanr = spisok_dannih("genres")

# Список режисёров
reshiser = spisok_dannih("director")

# Список актёров
akter = spisok_dannih("cast")

# Список студий
studiya = spisok_dannih("production_companies")

# Список годов выпуска фильмов
god = list(data["release_year"].unique())

# Список месяцев выпуска фильмов
mesac = data["mesac"].unique()

# Список слов используемых в названии фильмов
slova = spisok_slov("original_title")


def vopros_1():
    #Первый вопрос (правильный ответ 4 "The Warrior's Way")
    otvet_1_1 = data[["imdb_id", "original_title"]][data["budget"] == data["budget"].max()]
    otvet_1_2 = data["budget"].sort_values(ascending = False)
    return otvet_1_1["original_title"].values[0]


def vopros_2():
    # Второй вопрос  (правильный ответ 2 "Gods and Generals")
    otvet_2_1 = data[["imdb_id", "original_title"]][data["runtime"] == data["runtime"].max()]
    otvet_2_2 = data["runtime"].sort_values(ascending = False)
    return otvet_2_1["original_title"].values[0]


def vopros_3():
    # Третий вопрос  (правильный ответ 3 "Winnie the Pooh")
    otvet_3_1 = data[["imdb_id", "original_title"]][data["runtime"] == data["runtime"].min()]
    otvet_3_2 = data["runtime"].sort_values(ascending = True)
    return otvet_3_1["original_title"].values[0]


def vopros_4():
    # Четвёртый вопрос (правильный ответ 2 "110")
    otvet_4 = data["runtime"].mean()
    return round(otvet_4)


def vopros_5():
    # Пятый вопрос (правильный ответ 1 "106")
    otvet_5 = data["runtime"].median()
    return round(otvet_5)

def vopros_6():
    # Шестой вопрос (правильный ответ 5 "Avatar")
    otvet_6_1 = data[["imdb_id", "original_title"]][data["pribil"] == data["pribil"].max()]
    otvet_6_2 = data["pribil"].sort_values(ascending = False)
    return otvet_6_1["original_title"].values[0]


def vopros_7():
    # Седьмой вопрос (правильный ответ 2 "The Warrior's Way")
    otvet_7_1 = data[["imdb_id", "original_title"]][data["pribil"] == data["pribil"].min()]
    otvet_7_2 = data["pribil"].sort_values(ascending = True)
    return otvet_7_1["original_title"].values[0]


def vopros_8():
    # Восьмой вопрос (правильный ответ 1 "1478")
    otvet_8 = len(data_prib["pribil"].values)
    return otvet_8


def vopros_9():
    # Девятый вопрос (правильный ответ 4 "The Dark Knight")
    data_prib_9 = data[(data["release_year"] == 2008) & (data["pribil"] > 0)]
    otvet_9_1 = data_prib_9[["imdb_id", "original_title"]][data_prib_9["pribil"] == data_prib_9["pribil"].max()]
    otvet_9_2 = data_prib_9["pribil"].sort_values(ascending = False)
    return otvet_9_1["original_title"].values[0]


def vopros_10():
    # Десятый вопрос (правильный ответ 5 "The Lone Ranger")
    data_prib_10 = data[(data["release_year"] >= 2012) & (data["release_year"] <= 2014)]
    otvet_10_1 = data_prib_10[["imdb_id", "original_title"]][data_prib_10["pribil"] == data_prib_10["pribil"].min()]
    otvet_10_2 = data_prib_10["pribil"].sort_values(ascending = True)
    return otvet_10_1["original_title"].values[0]


def vopros_11():
    # Одиннадцатый вопрос (правильный ответ 3 "Drama")
    zhanr_popular_slovar = {}
    for i in zhanr:
        tab = data[data["genres"].str.contains(i)]
        kolichestvo = len(tab.values)
        zhanr_popular_slovar[i] = kolichestvo
    
    zhanr_popular = pd.Series(zhanr_popular_slovar)
    zhanr_popular = zhanr_popular.sort_values(ascending = False)
    otvet_11 = zhanr_popular.index[0]
    return otvet_11


def vopros_12():
    # Двенадцатый вопрос (правильный ответ 1 "Drama")
    zhanr_popular_slovar = {}
    
    for i in zhanr:
        tab = data_prib[data_prib["genres"].str.contains(i)]
        kolichestvo = len(tab.values)
        zhanr_popular_slovar[i] = kolichestvo
    
    zhanr_popular = pd.Series(zhanr_popular_slovar)
    zhanr_popular = zhanr_popular.sort_values(ascending = False)
    otvet_12 = zhanr_popular.index[0]
    return otvet_12


def vopros_13():
    # Тринадцатый вопрос (правильный ответ 1 "Steven Soderbergh")
    rezh_max_slovar = {}
    
    for i in reshiser:
        tab = data[data["director"].str.contains(i)]
        kolichestvo = len(tab.values)
        rezh_max_slovar[i] = kolichestvo
    
    rezh_max = pd.Series(rezh_max_slovar)
    rezh_max = rezh_max.sort_values(ascending = False)
    otvet_13 = rezh_max.index[0]
    return otvet_13


def vopros_14():
    # Четыранадцатый вопрос (правильный ответ 4 "Ridley Scott")
    rezh_max_slovar = {}
    
    for i in reshiser:
        tab = data_prib[data_prib["director"].str.contains(i)]
        kolichestvo = len(tab.values)
        rezh_max_slovar[i] = kolichestvo
    
    rezh_max = pd.Series(rezh_max_slovar)
    rezh_max = rezh_max.sort_values(ascending = False)
    otvet_14 = rezh_max.index[0]
    return otvet_14


def vopros_15():
    # Пятнадцатый вопрос (правильный ответ 5 "Peter Jackson")
    rezh_max_slovar = {}
    
    for i in reshiser:
        tab = data[data["director"].str.contains(i)]
        kolichestvo = tab["pribil"].sum()
        rezh_max_slovar[i] = kolichestvo
    
    rezh_max = pd.Series(rezh_max_slovar)
    rezh_max = rezh_max.sort_values(ascending = False)
    otvet_15 = rezh_max.index[0]
    return otvet_15


def vopros_16():
    # Шестнадцатый вопрос (правильный ответ 1 "Emma Watson")
    akt_max_slovar = {}
    
    for i in akter:
        tab = data[data["cast"].str.contains(i)]
        kolichestvo = tab["pribil"].sum()
        akt_max_slovar[i] = kolichestvo
    
    akt_max = pd.Series(akt_max_slovar)
    akt_max = akt_max.sort_values(ascending = False)
    otvet_16 = akt_max.index[0]
    return otvet_16


def vopros_17():
    # Семнадцатый вопрос (правильный ответ 3 "Kirsten Dunst")
    akt_max_slovar = {}
    data_2012 = data[data["release_year"] == 2012]
    
    for i in akter:
        tab = data_2012[data_2012["cast"].str.contains(i)]
        kolichestvo = tab["pribil"].sum()
        akt_max_slovar[i] = kolichestvo
    
    akt_max = pd.Series(akt_max_slovar)
    akt_max = akt_max.sort_values(ascending = True)
    otvet_17 = akt_max.index[0]
    return otvet_17


def vopros_18():
    # Восемнадцатый вопрос (правильный ответ 3 "Matt Damon")
    data_vbudg = data[data["budget"] > data["budget"].mean()]
    
    akt_max_slovar = {}
    
    for i in akter:
        tab = data_vbudg[data_vbudg["cast"].str.contains(i)]
        kolichestvo = len(tab.values)
        akt_max_slovar[i] = kolichestvo
    
    akt_max = pd.Series(akt_max_slovar)
    akt_max = akt_max.sort_values(ascending = False)
    otvet_18 = akt_max.index[0]
    return otvet_18


def vopros_19():
    # Девятнадцатый вопрос (правильный ответ 2 "Action")
    data_niholas = data[data["cast"].str.contains("Nicolas Cage")]
    
    zhanr_popular_slovar = {}
    
    for i in zhanr:
        tab = data_niholas[data_niholas["genres"].str.contains(i)]
        kolichestvo = len(tab.values)
        zhanr_popular_slovar[i] = kolichestvo
    
    zhanr_popular = pd.Series(zhanr_popular_slovar)
    zhanr_popular = zhanr_popular.sort_values(ascending = False)
    otvet_19 = zhanr_popular.index[0]
    return otvet_19


def vopros_20():
    # Двадцатый вопрос (правильный ответ 1 "Universal")
    stud_max_slovar = {}
    
    for i in studiya:
        tab = data[data["production_companies"].str.contains(i)]
        kolichestvo = len(tab.values)
        stud_max_slovar[i] = kolichestvo
    
    stud_max = pd.Series(stud_max_slovar)
    stud_max = stud_max.sort_values(ascending = False)
    otvet_20 = stud_max.index[0]
    return otvet_20


def vopros_21():
    # Двадцать первый вопрос (правильный ответ 1 "Universal")
    data_2015 = data[data["release_year"] == 2015]
    stud_max_slovar = {}
    
    for i in studiya:
        tab = data_2015[data_2015["production_companies"].str.contains(i)]
        kolichestvo = len(tab.values)
        stud_max_slovar[i] = kolichestvo
    
    stud_max = pd.Series(stud_max_slovar)
    stud_max = stud_max.sort_values(ascending = False)
    otvet_21 = stud_max.index[0]
    return otvet_21


def vopros_22():
    # Двадцать второй вопрос (правильный ответ 3 "Columbia Pictures")
    data_comedy = data[data["genres"] == "Comedy"]
    stud_max_slovar = {}
    
    for i in studiya:
        tab = data_comedy[data_comedy["production_companies"].str.contains(i)]
        kolichestvo = tab["pribil"].sum()
        stud_max_slovar[i] = kolichestvo
    
    stud_max = pd.Series(stud_max_slovar)
    stud_max = stud_max.sort_values(ascending = False)
    otvet_22 = stud_max.index[0]
    return otvet_22


def vopros_23():
    # Двадцать третий вопрос (правильный ответ 3 "Columbia Pictures")
    data_2012 = data[data["release_year"] == 2012]
    stud_max_slovar = {}
    
    for i in studiya:
        tab = data_2012[data_2012["production_companies"].str.contains(i)]
        kolichestvo = tab["pribil"].sum()
        stud_max_slovar[i] = kolichestvo
    
    stud_max = pd.Series(stud_max_slovar)
    stud_max = stud_max.sort_values(ascending = False)
    otvet_23 = stud_max.index[0]
    return otvet_23


def vopros_24():
    # Двадцать четвёртый вопрос (правильный ответ 1 "K-19: The Widowmaker")
    data_paramount = data[data["production_companies"].str.contains("Paramount Pictures")]
    otvet_24_1 = data_paramount[["imdb_id", "original_title"]][data_paramount["pribil"] == data_paramount["pribil"].min()]
    otvet_24_2 = data_paramount["pribil"].sort_values(ascending = True)
    return otvet_24_1["original_title"].values[0]


def vopros_25():
    # Двадцать пятый вопрос (правильный ответ 5 "2015")
    god_max_slovar = {}
    
    for i in god:
        tab = data[data["release_year"] == i]
        kolichestvo = tab["pribil"].sum()
        god_max_slovar[i] = kolichestvo
    
    god_max = pd.Series(god_max_slovar)
    god_max = god_max.sort_values(ascending = False)
    otvet_25 = god_max.index[0]
    return otvet_25


def vopros_26():
    # Двадцать шестой вопрос (правильный ответ "2011")
    data_Warner = data[data["production_companies"] == 'Warner Bros.']
    
    god_max_slovar = {}
    
    for i in god:
        tab = data_Warner[data_Warner["release_year"] == i]
        kolichestvo = tab["pribil"].sum()
        god_max_slovar[i] = kolichestvo
    
    god_max = pd.Series(god_max_slovar)
    god_max = god_max.sort_values(ascending = False)
    otvet_26 = god_max.index[0]
    return otvet_26


def vopros_27():
    # Двадцать седьмой вопрос (правильный ответ 4 "9 месяц - Сентябрь")
    mesac = data["mesac"].unique()
    
    mesac_max_slovar = {}
    
    for i in mesac:
        tab = data[data["mesac"] == i]
        kolichestvo = len(tab.values)
        mesac_max_slovar[i] = kolichestvo
    
    mesac_max = pd.Series(mesac_max_slovar)
    mesac_max = mesac_max.sort_values(ascending = False)
    otvet_27 = mesac_max.index[0]
    return otvet_27


def vopros_28():
    # Двадцать восьмой вопрос (правильный ответ 2 "450")
    mesac = data["mesac"].unique()
    tab = data[(data["mesac"] == "6") | (data["mesac"] == "7") | (data["mesac"] == "8")]
    otvet_28 = len(tab.values)
    return otvet_28


def vopros_29():
    # Двадцать девятый вопрос (правильный ответ 5 "Peter Jackson")
    zima = data[(data["mesac"] == "1") | (data["mesac"] == "2") | (data["mesac"] == "12")]
    
    rezh_max_slovar = {}
    
    for i in reshiser:
        tab = zima[zima["director"].str.contains(i)]
        kolichestvo = len(tab.values)
        rezh_max_slovar[i] = kolichestvo
    
    rezh_max = pd.Series(rezh_max_slovar)
    rezh_max = rezh_max.sort_values(ascending = False)
    otvet_29 = rezh_max.index[0]
    return otvet_29


def vopros_30():
    # Тридцатый вопрос (правильный ответ 2 "6 месяц - Июнь")
    slovar = {}
    sv = data.pivot_table(values = "pribil", index = "mesac", columns = "release_year",
                          aggfunc = "sum", fill_value = 0)
    
    for i in god:
         kol = sv[i].sort_values(ascending = False).index[0]
         slovar[i] = kol
    
    max_mes = pd.Series(slovar)
    max_mes = max_mes.sort_values(ascending = False)
    otvet_30_2 = max_mes.value_counts()
    return otvet_30_2.index[0]


def vopros_31():
    # Тридцать первый вопрос (правильный ответ 5 'Four By Two Productions')
    simvl_title_slovar = {}
    
    for i in studiya:
        tab = data[data["production_companies"].str.contains(i)]
        kolichestvo = tab["kol_simvl"].mean()
        simvl_title_slovar[i] = kolichestvo
    
    simvl_title = pd.Series(simvl_title_slovar)
    simvl_title = simvl_title.sort_values(ascending = False)
    otvet_31 = simvl_title.index[0]
    return otvet_31


def vopros_32():
    # Тридцать второй вопрос (правильный ответ 5 'Four By Two Productions')
    slovo_title_slovar = {}
    
    for i in studiya:
        tab = data[data["production_companies"].str.contains(i)]
        kolichestvo = tab["kol_slov"].mean()
        slovo_title_slovar[i] = kolichestvo
    
    slovo_title = pd.Series(slovo_title_slovar)
    slovo_title = slovo_title.sort_values(ascending = False)
    otvet_32 = slovo_title.index[0]
    return otvet_32


def vopros_33():
    # Тридцать третий вопрос (правильный ответ 3 "2477")
    otvet_33 = len(slova)
    return otvet_33


def vopros_34():
    # Тридцать четвёртый вопрос (правильный ответ "фильмы которые входят в список")
    top_1_proc = data[data["vote_average"] >= data["vote_average"].quantile(0.99)]
    spisok_top_1_proc = list(top_1_proc["original_title"])
    spisok_top_1_proc.sort()
    return spisok_top_1_proc


def vopros_35():
    # Тридцать пятый вопрос (правильный ответ 5 "Daniel Radcliffe, Rupert Grint")
    pari_aktr_spisk = []
    for n in data["cast"].values:
        n = n.split("|")
        for i in range(len(n)-1):
            for k in range(i+1, len(n)):
                para = set()
                para.add(n[i])
                para.add(n[k])
                pari_aktr_spisk.append(para)
    
    pari_aktr = pd.Series(pari_aktr_spisk)
    pari_aktr = pari_aktr.apply(lambda x: str(x))
    otvet_35 = pari_aktr.value_counts()
    return otvet_35.index[2]


def vopros_36():
    # Тридцать шестой вопрос (правильный ответ "Christopher Nolan")
    slovar = {}
    for i in reshiser:
        data_i = data[data["director"].str.contains(i)]
        vsego = len(data_i.values)
        data_i_prib = data_i[data_i["pribil"] > 0]
        prib = len(data_i_prib.values)
        slovar[i] = prib / vsego
    
    slovar = pd.Series(slovar)
    slovar = slovar.sort_values(ascending = False)
    return slovar




