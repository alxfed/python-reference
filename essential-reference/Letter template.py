#стр. 214

"""
Шаблон письма, в котором присутствуют переменные элементы
"""

form = """\
Уважаемый {name},
Пожалуйста, верните обратно {item} или заплатите {amount:0.2f}.
                                                  Искренне ваш,

                                                Joe Python User
"""
print(form.format(name='Мистер Буш', item='блендер', amount=50.0))
