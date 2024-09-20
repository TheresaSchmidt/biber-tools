# Theresa Schmidt, 2024
"""
Ergänzt die Vor- und Nachnamen der SuS in der Ergebnistabelle des Biberwettbewerbs.

Benötigte Dateien:
	- Klassenliste(n) im csv-Format 
		- mit den folgenden Spalten: "Nummer", "Nachname", "Vorname"
			- Spaltenüberschriften erforderlich!
			- Reihenfolge der Spalten egal
		- mit Trennzeichen ";"
		- z.B. eine Zeile: "42;Schmidt;Theresa"
	- Ergebnistabelle im csv-Format 
		- mit den folgenden Spalten: "Teamchef Benutzername", "Teamchef Vorname", "Teamchef Nachname", "Teammitglied 1 Benutzername", "Teammitglied 1 Vorname", "Teammitglied 1 Nachname"
		- mit Trennzeichen ";"
		- Benutzername im folgenden Format: gas-<Klasse>-<Nummer>, wobei Nummer der Nummer in der Klassenliste entspricht und Klasse dem Dateinamen der jeweiligen Klassenlistendatei
		- Tipp: Tabelle vorher nach Namen sortieren, dass die Einträge ohne Namen ganz oben oder ganz unten stehen  - dann findet man sie nachher leichter, wenn man sie z.B.irgendwie einfärben möchte.

Rückgabe:
	- Datei <Ergebnistabelle>_vollständig.csv
"""
import csv


# Quelldateien
klassenlisten = ["7a.csv", "7b.csv", "7c.csv", "7d.csv", "7e.csv"]#, "10Montag.csv", "10Do.csv"]
ergebnisdatei = "Ergebnisse_2023.csv"

# Rückgabedatei
rueckdatei = ergebnisdatei[:-4] + "_vollständig.csv"



# Klassenlisten einlesen
names_dict = dict() # mapping von Nutzername zu (Vorname, Nachname)

for klassenliste in klassenlisten:
	klasse = klassenliste[:-4]
	with open(klassenliste, "r") as f:
		k_reader = csv.DictReader(f, delimiter=";")
		for row in k_reader:
			# Nutzername zusammensetzen aus "gas", Klasse und Nummer
			nutzername = "gas-" + klasse + "-" + row["Nummer"]
			# Zeileninformation für Benutzername speichern
			names_dict[nutzername] = row



# Ergebnisse einlesen und neue Ergbenisdatei schreiben

# CSV-Reader für Originaldatei definieren
with open(ergebnisdatei, "r") as e:
	e_reader = csv.DictReader(e, delimiter=";")

	# CSV-Writer für Rückgabedatei definieren
	with open(rueckdatei, "w", newline="") as r:
		r_writer = csv.DictWriter(r, e_reader.fieldnames, delimiter=";")
		r_writer.writeheader()

		# jede Zeile in e überprüfen
		for row in e_reader:
			
			# Teamchef
			if row["Teamchef Benutzername"] and not row["Teamchef Vorname"]:
				#print("Chef ergänzen", row, "\n\n")
				row["Teamchef Vorname"] = names_dict[row["Teamchef Benutzername"]]["Vorname"]
				row["Teamchef Nachname"] = names_dict[row["Teamchef Benutzername"]]["Nachname"]
			
			# Teampartner ("Teammitglied 1")
			if row["Teammitglied 1 Benutzername"] and not row["Teammitglied 1 Vorname"]:
				#print("1 ergänzen", row, "\n\n")
				row["Teammitglied 1 Vorname"] = names_dict[row["Teammitglied 1 Benutzername"]]["Vorname"]
				row["Teammitglied 1 Nachname"] = names_dict[row["Teammitglied 1 Benutzername"]]["Nachname"]
			
			# TODO: die Namen, die schon in e stehen, überprüfen

			# ausgebesserte Zeile schreiben
			r_writer.writerow(row)
