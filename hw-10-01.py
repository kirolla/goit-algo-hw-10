import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість "Лимонаду"
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')  # Кількість "Фруктового соку"

# Функція цілі (Максимізація виробництва)
model += lemonade + fruit_juice, "Total Production"

# Додавання обмежень
model += 2 * lemonade + fruit_juice <= 100  # Обмеження на воду
model += lemonade <= 50  # Обмеження на цукор
model += lemonade <= 30  # Обмеження на лимонний сік
model += 2 * fruit_juice <= 40  # Обмеження на фруктове пюре
model += fruit_juice <= 100  # Додаткове обмеження (не вказано у завданні)

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Кількість виробленого Лимонаду:", lemonade.varValue)
print("Кількість виробленого Фруктового соку:", fruit_juice.varValue)
