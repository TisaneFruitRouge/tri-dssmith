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

	max_rows = ws.max_row

	for row in range(len(list_data)):
		for col in range(len(list_data)):
			n = number_to_col(col)
			value = list_data[col]

			if col==8:
				value = "Oui" if value==True else "Non"

			ws.cell(row=max_rows+1, column=col+1, value=value)


	wb.save(filename=path)
	wb.close()



def creer_fichier(path: str):
	new_workbook = Workbook()

	ws = new_workbook.active

	ws["A1"] = "OF"
	ws["B1"] = "Symbole"
	ws["C1"] = "Client"
	ws["D1"] = "Défaut"
	ws["E1"] = "A trier"
	ws["F1"] = "Bonnes"
	ws["G1"] = "Mauvaises"
	ws["H1"] = "Date"
	ws["I1"] = "Est trié?"

	new_workbook.save(path)

