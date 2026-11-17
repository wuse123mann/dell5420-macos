# Komponenten

## OpenCore und Treiber

| Datei | Version | Quelle |
| --- | --- | --- |
| OpenCore.efi, BOOTx64.efi, OpenRuntime, OpenCanopy, OpenLinuxBoot, ResetNvramEntry, ToggleSipEntry, OpenShell | 1.0.8 RELEASE | https://github.com/acidanthera/OpenCorePkg |
| HfsPlus.efi, ext4_x64.efi, Theme `Acidanthera/GoldenGate`, Fonts, Labels | OcBinaryData | https://github.com/acidanthera/OcBinaryData |
| `Resources/Image/Acidanthera/GoldenGate/Linux.icns` | eigenes Design | `tools/make_linux_icon.py` |

## Kexts (Ladereihenfolge)

| Kext | Version | Quelle |
| --- | --- | --- |
| Lilu | 1.7.2 | https://github.com/acidanthera/Lilu |
| VirtualSMC, SMCBatteryManager, SMCProcessor | 1.3.8 | https://github.com/acidanthera/VirtualSMC |
| WhateverXe | 0.8.0 | https://github.com/b00t0x/WhateverXe |
| AMFIPass (Mod) | 1.4.1 | https://github.com/b00t0x/WhateverXe-Graphics (extras) |
| AppleALC | 1.9.8 | https://github.com/acidanthera/AppleALC |
| SimpleHDA | 1.0.0 | https://github.com/laobamac/SimpleHDA |
| RestrictEvents | 1.1.6 | https://github.com/acidanthera/RestrictEvents |
| NVMeFix | 1.1.3 | https://github.com/acidanthera/NVMeFix |
| ECEnabler | 1.0.6 | https://github.com/1Revenger1/ECEnabler |
| BrightnessKeys | 1.0.3 | https://github.com/acidanthera/BrightnessKeys |
| USBToolBox | 1.2.0 | https://github.com/USBToolBox/kext |
| UTBMap | eigene Map | aus ACPI erzeugt, 12 Ports, XHCI `8086:A0ED` |
| VoodooPS2Controller (+ Keyboard, Mouse, Trackpad) | 2.3.7 | https://github.com/acidanthera/VoodooPS2 |
| VoodooI2C (+ GPIO, Services, VoodooInput), VoodooI2CHID | Nightly `0271bbd` (10.11.2026) | https://github.com/dortania/build-repo |
| IntelMausi | 1.0.8 | https://github.com/acidanthera/IntelMausi |
| AirportItlwm (Tahoe) | 2.4.0-alpha | laobamac, über https://github.com/JulioNectar/Hackintosh-XPS13Plus-IrisXe-Tahoe |
| IntelBluetoothFirmware, IntelBTPatcher | 2.5.1 | wie oben |
| BlueToolFixup | 2.7.3 | wie oben |

## USB-Map (UTBMap.kext)

| Port | Index | Typ | Gerät |
| --- | --- | --- | --- |
| HS01, HS02 | 1, 2 | USB-C (9) | USB-2-Teil der USB-C-Buchsen |
| HS03 + SS01 | 3, 13 | USB-A (3) | USB-A 1 |
| HS04 + SS02 | 4, 14 | USB-A (3) | USB-A 2 |
| HS06 | 6 | intern | Webcam |
| HS10 | 10 | intern | Bluetooth |
| HS05, HS07–HS09 | 5, 7–9 | intern | reserviert |

Nicht gemappt: USR1/USR2, SS03/SS04 (laut ACPI unbenutzt).

## Nach der Installation (nicht im Repo)

| Paket | Version | Quelle |
| --- | --- | --- |
| WhateverXe-Graphics | 0.4.1 (zu WhateverXe 0.8.0) | https://github.com/b00t0x/WhateverXe-Graphics/releases |
| SimpleHDA-HAL | 1.0.0 | https://github.com/laobamac/SimpleHDA/releases |
| USBToolBox (Windows) | 0.2 | https://github.com/USBToolBox/tool/releases |

Die Lizenzen der einzelnen Komponenten gelten unverändert. HfsPlus.efi und SimpleHDA enthalten Apple-Code.
