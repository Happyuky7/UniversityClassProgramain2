import pandas as pd

# Crear el DataFrame a partir de los datos proporcionados
data = {
    'year': [1949]*12 + [1950]*12 + [1951]*12 + [1952]*12 + [1953]*12 + [1954]*12 + [1955]*12 + [1956]*12 + [1957]*12 + [1958]*12 + [1959]*12 + [1960]*12,
    'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']*12,
    'passengers': [112, 118, 132, 129, 121, 135, 148, 148, 136, 119, 104, 118, 115, 126, 141, 135, 125, 149, 170, 170, 158, 133, 114, 140, 145, 150, 178, 163, 172, 178, 199, 199, 184, 162, 146, 166, 171, 180, 193, 181, 183, 218, 230, 242, 209, 191, 172, 194, 196, 196, 236, 235, 229, 243, 264, 272, 237, 211, 180, 201, 204, 188, 235, 227, 234, 264, 302, 293, 259, 229, 203, 229, 242, 233, 267, 269, 270, 315, 364, 347, 312, 274, 237, 278, 284, 277, 317, 313, 318, 374, 413, 405, 355, 306, 271, 306, 315, 301, 356, 348, 355, 422, 465, 467, 404, 347, 305, 336, 340, 318, 362, 348, 363, 435, 491, 505, 404, 359, 310, 337, 360, 342, 406, 396, 420, 472, 548, 559, 463, 407, 362, 405, 417, 391, 419, 461, 472, 535, 622, 606, 508, 461, 390, 432]
}

df = pd.DataFrame(data)

# Agrupar por año y calcular la suma de pasajeros por año
yearly_totals = df.groupby('year')['passengers'].sum()

# Identificar los años con aumento en el número de pasajeros
years_with_increase = yearly_totals.index[yearly_totals.diff() > 0]

# Calcular el promedio de años con aumento
average_years_with_increase = len(years_with_increase) / (yearly_totals.index[-1] - yearly_totals.index[0] + 1) * 100

print("Años con aumento en el número de pasajeros:", years_with_increase.tolist())
print("Promedio de años con aumento (%):", average_years_with_increase)
