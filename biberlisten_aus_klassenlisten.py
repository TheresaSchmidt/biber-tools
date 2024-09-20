# Theresa Schmidt, 2024
"""
Erstellt eine Teilnehmerliste für die Anmeldung beim Informatikbiber.

Benötigte Dateien:
	- Klassenliste(n) im csv-Format
		- mit den folgenden Spalten: "Nummer", "Nachname", "Vorname", (optional: "Geschlecht")
			- Spaltenüberschriften erforderlich!
			- Reihenfolge der Spalten egal
		- mit Trennzeichen ";"
		- z.B. eine Zeile: "42;Schmidt;Theresa"

Erzeugt (oder ergänzt!) Datei:
	- Nutzerdaten im csv-Format 
		- default-Dateiname: "Nutzerdaten.csv"
		- mit den folgenden Spalten: Klassen-/Kursname, Stufe, Vorname, Nachname, Benutzername, Passwort, Geschlecht, Schnupper-Biber, Informatik-Biber
			- keine Spaltenüberschriften
		- mit Trennzeichen ";"
		- Benutzername im folgenden Format: <Schule>-<Klasse>-<Nummer>, wobei Nummer der Nummer in der Klassenliste entspricht
		- Sollte bereits eine Datei mit dem selben Namen existieren, werden die bereits vorhandenen Daten beibehalten und die neuen unten angefügt.

Bedienung:
	- Voraussetzung: Python muss installiert sein
	- Klassenlistendateien, Klassennamen und Jahrgangsstufe in Zeile #todo 26 eintragen
		- für Klassenlistendateien die Dateipfade angeben
		- wenn im selben Ordner wie dieses Script gespeichert, genügen die Dateinamen
	- Schulname eintragen
	- ggf. anonymen Modus aktivieren (Zeile #todo 37)
		- Im anonymen Modus werden nur die automatisch erzeugten Nutzernamen in die Ergebnisdatei übernommen, nicht aber die echten Namen der SuS.
		- Sinnvoll, wenn keine Einverständniserklärungen zur Datenverarbeitung von den Eltern vorliegen
	- Script über Kommandozeile aufrufen 

"""



###########################################
##############  Parameter  ################
###########################################

klassen = [("nr-nachname-vorname-7e2.csv", "7E2", 7)] # Klassenlisten, Klassennamen, Jahrgangsstufen
schulname = "gar"
anonym = True # Auf True setzen, falls echte Namen der SuS nicht gedruckt werden sollen.

# Rückgabedatei
rueckdatei = "Nutzerdaten.csv"






######################################
##############  Code  ################
######################################

import csv


# Schleife über alle Klassen
for klassenliste,klasse,stufe in klassen:

	# Ergebnisdatei im ergänzenden Schreibmodus öffnen
	with open(rueckdatei, "a") as r:

		# jeweilige Klassenliste einlesen
		with open(klassenliste, "r") as f:
			k_reader = csv.DictReader(f, delimiter=";")

			# Schleife über alle SuS der Klasse
			for row in k_reader:

				# Nutzername zusammensetzen aus Schulname, Klasse und Nummer
				print(row)
				nutzername = schulname + "-" + klasse.lower() + "-" + row["Nummer"]

				# Platzhalter für Geschlecht eintragen, falls keine Angabe
				if not "Geschlecht" in row.keys():
					row["Geschlecht"] = ""

				# Zeileninformation für Nutzer in Ergebnisdatei schreiben
				# Spalten: Klassen-/Kursname, Stufe, Vorname, Nachname, Benutzername, Passwort, Geschlecht, Schnupper-Biber, Informatik-Biber
				# Trennzeichen: ";"
				if anonym:
					r.write(";".join([klasse, str(stufe), "", "", nutzername, "", row["Geschlecht"], "", ""]))
				else:
					r.write(";".join([klasse, str(stufe), row["Vorname"], row["Nachname"], nutzername, "", row["Geschlecht"], "", ""]))
				r.write("\n")

