Arbeitsspeicher wird unter Windows komplett mit Cache gefüllt, was zu Problemen führen kann.
Da DynCache von Microsoft mit den neuen Windows-Versionen zu fehlern führt (da angelblich dies kein thema sein soll und nicht auf neue Versionen geupdatet wurde) habe ich einen walkaround umgesetzt.
RamCacheCleaner prüft, wieviel Ram gesamt vorhanden ist und wenn der wirklich freie speicher unter 1gb oder 5% des gesamten Speichers liegt, wird die Hälfte des Standby freigegeben.

## Versionen
![Static Badge](https://img.shields.io/badge/v2.x.x-green?style=for-the-badge)

![Static Badge](https://img.shields.io/badge/v2.0.0-green?style=social&label=umstellung%20von%20powershell%20auf%20python)

![Static Badge](https://img.shields.io/badge/v2.1.0-green?style=social&label=Bestehenden%20Ram%20zum%20ausrechnen%20genutzt)

![Static Badge](https://img.shields.io/badge/v2.1.1-green?style=social&label=Ram%20%25%20und%20Bruchteilig%20anahnd%20des%20genutzten%20Standby%20freigeben)

![Static Badge](https://img.shields.io/badge/v2.1.2-green?style=social&label=.exe%20inkl.%20.icon%20erstellt)

## To-Do
- in die Prüfung mit aufnehmen ob der Standby überhaupt größer als 1gb / 5% ist da ansonsten eine endlosschleife entstehen könnte (wenn das programm automatisiert gestartet wird)
