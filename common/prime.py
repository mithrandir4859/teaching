for число_которое_мы_проверяем in range(2, 50):  # допустим дошли до число 17
    число_оказалось_простым = True  # правда, истина
    for делитель in range(2, число_которое_мы_проверяем):
        if число_которое_мы_проверяем % делитель == 0:
            print(str(число_которое_мы_проверяем) + ' делится на ' + str(делитель))
            число_оказалось_простым = False  # ложь, ложно
            break
        else:
            print(str(число_которое_мы_проверяем) + ' НЕ делится на ' + str(делитель))
    if число_оказалось_простым:
        print(str(число_которое_мы_проверяем) + ' ПРОСТОЕ')
    print()
