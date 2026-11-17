# Changelog

| Datum | Änderung | Grund |
| --- | --- | --- |
| 26.10.2026 | Erste EFI: OpenCore 1.0.8, WhateverXe 0.6.0, MacBookPro16,2, Ice-Lake-CPUID | |
| 26.10.2026 | OpenHfsPlus → HfsPlus.efi | Installer hing beim Laden der Kernel-Collection |
| 27.10.2026 | SSDTs neu aus dem ACPI-Dump, MmioWhitelist, APFS -1 | alte SSDT-AWAC kollidierte mit `\_SB._INI` |
| 27.10.2026 | **`AppleXcpmExtraMsrs = true`** | Hänger bei `EXITBS:START` ohne Ladebalken (Tiger Lake) |
| 27.10.2026 | IntelMausi, AirportItlwm statt itlwm | WLAN/LAN im Installer |
| 28.10.2026 | Betriebs-EFI: RELEASE, ohne Verbose; WhateverXe 0.6.1 | |
| 28.10.2026 | SimpleHDA 1.0.0 + AppleALC | Tahoe hat kein AppleHDA mehr |
| 09.11.2026 | WhateverXe 0.8.0 | Kext 0.8.0 braucht Grafik-Paket 0.4.x, sonst schwarzer Bildschirm |
| 11.11.2026 | VoodooI2C Nightly + SSDT-XOSI | Touchpad lief nur als PS/2-Maus (Tiger-Lake-I2C fehlte in 2.9.1) |
| 11.11.2026 | SSDT-BRT6 + Patch `BRT6`→`BRTX` | Fn-Helligkeitstasten |
| 11.11.2026 | XOSI-Patch auf exakte Muster | einfaches `_OSI`-Ersetzen beschädigte `\_SB_.OSID` und blockierte die Helligkeitstasten |
| 12.11.2026 | UTBMap.kext aus ACPI | 16 Ports > Limit 15, Bluetooth als intern |
| 12.11.2026 | OpenLinuxBoot + ext4, `LauncherOption Full` | Ubuntu im Menü |
| 12.11.2026 | OpenCanopy, GoldenGate, eigenes Linux-Symbol, schwarzer Hintergrund | |
| 12.11.2026 | itlwm, SMCDellSensors, btrfs entfernt (59 → 43 MB) | EFI-Partition zu klein |
| 12.11.2026 | `PickerAttributes 151 → 147` | Linux stand als „Other OS“ im Menü |
| 17.11.2026 | Fn-Helligkeitstasten und Bluetooth bestätigt | |
| 17.11.2026 | Einfrieren der Bluetooth-Einstellungen nicht mehr aufgetreten, aus „Bekannte Probleme“ entfernt | |
| 17.11.2026 | SMBIOS im Repo durch neu erzeugte Werte ersetzt | echte Seriennummer nicht im Repo |
