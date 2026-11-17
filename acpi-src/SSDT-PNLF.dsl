/* Backlight for WhateverXe. _UID 19 (0x13) selects the WEX 16-bit PWM profile. */
DefinitionBlock ("", "SSDT", 2, "LAT54", "PNLF", 0x00002000)
{
    External (_SB_.PC00.GFX0, DeviceObj)

    Scope (\_SB.PC00.GFX0)
    {
        Device (PNLF)
        {
            Name (_HID, EisaId ("APP0002"))
            Name (_CID, "backlight")
            Name (_UID, 0x13)
            Method (_STA, 0, NotSerialized)
            {
                If (_OSI ("Darwin")) { Return (0x0B) }
                Return (Zero)
            }
        }
    }
}
