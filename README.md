Arbeitsspeicher wird unter Windows komplett mit Cache gefüllt, was zu Problemen führen kann.
Da DynCache von Microsoft mit den neuen Windows-Versionen zu fehlern führt (da angelblich dies kein thema sein soll und nicht auf neue Versionen geupdatet wurde) habe ich einen walkaround umgesetzt.
RamCacheCleaner prüft, wieviel Ram gesamt vorhanden ist und wenn der wirklich freie speicher unter 1gb oder 5% des gesamten Speichers liegt, wird die Hälfte des Standby freigegeben.

v2.0.0 umstellung von powershell auf python
v2.1.0 Bestehenden Ram zum ausrechnen genutzt
v2.1.1 Ram % und Bruchteilig anahnd des genutzten Standby freigeben
v2.1.2 .exe inkl. .icon erstellt

To-Do:
- in die Prüfung mit aufnehmen ob der Standby überhaupt größer als 1gb / 5% ist da ansonsten eine endlosschleife entstehen könnte (wenn das programm automatisiert gestartet wird)
