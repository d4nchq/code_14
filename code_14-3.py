import matplotlib.pyplot as plt

#дані про кількість пасажирів у кожній категорії ваги багажу.
categories = ['< 5 кг', '5-25 кг', '> 25 кг']
passenger_counts = [3, 5, 2]  #наприклад, кількість пасажирів у кожній категорії.

#побудова кругової діаграми.
plt.figure(figsize=(8, 8))
plt.pie(passenger_counts, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'salmon'])

#додавання легенди та назви.
plt.title('Розподіл пасажирів за вагою багажу')
plt.axis('equal')  #зробити діаграму круглою.
plt.show()