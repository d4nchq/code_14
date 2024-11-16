import pandas as pd
import matplotlib.pyplot as plt

#зчитування даних з CSV файлу.
data = pd.read_csv('data.csv')

#видалення всіх рядків, які містять нечислові значення у стовпці 'Time'.
data = data[pd.to_numeric(data['Time'], errors='coerce').notna()]

#перетворення стовпця 'Time' у тип int.
data['Time'] = data['Time'].astype(int)

#фільтрація даних для двох країн.
country1 = "Ukraine"
country2 = "United States"
data_country1 = data[data['Country Name'] == country1]
data_country2 = data[data['Country Name'] == country2]

#витягання років та значень показника.
years_country1 = data_country1['Time']
values_country1 = pd.to_numeric(data_country1['Value'], errors='coerce')
years_country2 = data_country2['Time']
values_country2 = pd.to_numeric(data_country2['Value'], errors='coerce')

#побудова лінійного графіка.
plt.figure(figsize=(10, 6))
plt.plot(years_country1, values_country1, label=country1, color="blue", linewidth=2)
plt.plot(years_country2, values_country2, label=country2, color="green", linewidth=2)

#налаштування графіка.
plt.title('Динаміка показника для двох країн', fontsize=15)
plt.xlabel('Рік', fontsize=12, color='red')
plt.ylabel('Значення показника', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()

#стовпчаста діаграма для однієї з країн.
country_input = input("Введіть назву країни для побудови стовпчастої діаграми: ")
if country_input == country1:
    years = years_country1
    values = values_country1
elif country_input == country2:
    years = years_country2
    values = values_country2
else:
    print("Країна не знайдена у файлі.")
    years, values = None, None

if years is not None and values is not None:
    plt.figure(figsize=(10, 6))
    plt.bar(years, values, color="orange" if country_input == country1 else "purple")
    plt.title(f'Стовпчаста діаграма для {country_input}', fontsize=15)
    plt.xlabel('Рік', fontsize=12, color='red')
    plt.ylabel('Значення показника', fontsize=12, color='red')
    plt.grid(True)
    plt.show()
