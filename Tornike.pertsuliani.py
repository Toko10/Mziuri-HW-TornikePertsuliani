with open("Titanic67") as file1:
    female_Count = 0
    male_Count = 0
    total_Count = 0
    didnt_survive_fem = 0
    didnt_survive_ma = 0
    Pclass_1_count = 0
    Pclass_2_count = 0
    Pclass_3_count = 0
    Pclass_Fare_1 = 0
    Pclass_Fare_2 = 0
    Pclass_Fare_3 = 0
    total_age = 0
    for line in file1:
        gender = line.strip().split(',')
        if gender[4] == "female":
            female_Count += 1
            if gender[1] == "1":
                didnt_survive_fem += 1
        elif gender[4] == "male":
            male_Count += 1
            if gender[1] == "1":
                didnt_survive_ma += 1
        if gender[2] == "1":
            Pclass_1_count += 1
            Pclass_Fare_1 += float(gender[9])
        elif gender[2] == "2":
            Pclass_2_count += 1
            Pclass_Fare_2 += float(gender[9])
        elif gender[2] == "3":
            Pclass_3_count += 1
            Pclass_Fare_3 += float(gender[9])
        if gender[5] == '':
            continue
        else:
            total_age += float(gender[5])
    total_Count = male_Count + female_Count
    male_percentage = male_Count * 100 / total_Count
    female_percentage = female_Count * 100 / total_Count
    female_percentage_didnt_survive = didnt_survive_fem * 100 / total_Count
    male_percentage_didnt_survive = didnt_survive_ma * 100 / total_Count
    Pclass_Percentage_1 = Pclass_1_count * 100 / total_Count
    Pclass_Percentage_2 = Pclass_2_count * 100 / total_Count
    Pclass_Percentage_3 = Pclass_3_count * 100 / total_Count
    print("males: ", male_Count)
    print("females: ", female_Count)
    print("males: ", male_percentage, "%")
    print("females: ", female_percentage, "%")
    print("males who didnt survive: ", male_percentage_didnt_survive, "%")
    print("females who didnt survive: ", female_percentage_didnt_survive, "%")
    print("Pclass 1: ", Pclass_Percentage_1, "%")
    print("Pclass 2: ", Pclass_Percentage_2, "%")
    print("Pclass 3: ", Pclass_Percentage_3, "%")
    print("1 Pclass avg Fare: ", Pclass_Fare_1 / Pclass_1_count)
    print("2 Pclass avg Fare: ", Pclass_Fare_2 / Pclass_2_count)
    print("3 Pclass avg Fare: ", Pclass_Fare_3 / Pclass_3_count)
    print("total age: ", total_age) #gamovitane mgzavrebis total age TM

# TEORIA
# N1
# r
# a
# w
# N2
# axal fails sheqmnis
# N3
# Tuples shecvla ar shegvidzlia da listshi shegvidzlia davamatot da wavshalot
# N4
# dictionaryshi aris key da listshi aris indexebi
