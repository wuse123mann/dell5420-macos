# Diagnose Helligkeitstasten (nur falls die Tasten mit der neuen EFI weiterhin nicht gehen)

1. `SSDT-DIAG.aml` und `SSDT-BRT6D.aml` nach `EFI/OC/ACPI/` kopieren.
2. Die aktuelle `EFI/OC/config.plist` sichern (z. B. `config-normal.plist`), dann `config-diagnose.plist` nach `EFI/OC/config.plist` kopieren.
3. Neu starten, TextEdit öffnen, ins leere Dokument klicken.
4. Mehrmals Fn + Helligkeit heller/dunkler drücken. Danach einmal das Netzteil ab- und wieder anstecken.
5. Mir die getippten Buchstaben schicken:
   - `q` = die Firmware meldet ein Ereignis (EC _Q66)
   - `s` = Dells Ereignis-Verteiler (SMEE) läuft
   - `d` = die Helligkeits-Abfrage ist freigegeben
   - `b` = BRT6 wird aufgerufen, Tasten werden weitergeleitet
6. Danach die gesicherte `config-normal.plist` zurück nach `config.plist` kopieren.
