import string
from openpyxl import Workbook, load_workbook

def number_to_col(n: int):
		
	alphabet = string.ascii_uppercase

	if n>26: return alphabet[n//26]+alphabet[n%26]
	else   : return alphabet[n]


def insert_fichier(path: str, data):
	wb = load_workbook(filename=path)
	ws = wb.active

	data_items = data.items()

	data_keys = list(data)

	taille_data = len(data_items)

	list_data = [] # Création de la liste qui contiendra les données

	for i in range(len(data_items)):
		list_data.append(data[data_keys[i]])

	print(list_data)	

	max_column = ws.max_column

	for row in range(len(list_data)):
		for col in range(len(list_data)):
			n = number_to_col(col)
			ws.cell(row=row+1, column=max_column+1, value=list_data[row])

	wb.save(filename=path)
	wb.close()



def creer_fichier(path: str):
	new_workbook = Workbook()

	ws = new_workbook.active

	ws["A1"] = "OF"
	ws["A2"] = "Symbole"
	ws["A3"] = "Client"
	ws["A4"] = "Défaut"
	ws["A5"] = "A trier"
	ws["A6"] = "Bonnes"
	ws["A7"] = "Mauvaises"
	ws["A8"] = "Date"
	ws["A9"] = "Est trié?"

	new_workbook.save(path)
