/*
 * DIAGNOSE variant of SSDT-BRT6 (types b when BRT6 runs). Brightness Fn keys for Dell Latitude 5420.
 * Dell's EC event (_Q66 -> SMEE -> EV6) calls \_SB.PC00.GFX0.BRT6, which only notifies the LCD device.
 * On macOS this sends the Dell brightness scan codes (e0 06 up / e0 05 down) straight to the
 * PS/2 keyboard (VoodooPS2Keyboard), which macOS turns into brightness keys.
 * Requires the ACPI patch BRT6 -> BRTX (method definition in DSDT) and SSDT-XOSI.
 */
DefinitionBlock ("", "SSDT", 2, "LAT54", "BRT6D", 0x00000001)
{
    External (_SB_.PC00.GFX0, DeviceObj)
    External (_SB_.PC00.GFX0.BRTX, MethodObj)
    External (_SB_.PC00.LPCB.PS2K, DeviceObj)

    Scope (\_SB.PC00.GFX0)
    {
        Method (BRT6, 2, NotSerialized)
        {
            If (_OSI ("Darwin"))
            {
                Notify (\_SB.PC00.LPCB.PS2K, 0x0330)  // DIAG: b = BRT6 reached
                If ((Arg0 == One))
                {
                    Notify (\_SB.PC00.LPCB.PS2K, 0x0406)
                }

                If ((Arg0 & 0x02))
                {
                    Notify (\_SB.PC00.LPCB.PS2K, 0x0405)
                }
            }
            Else
            {
                \_SB.PC00.GFX0.BRTX (Arg0, Arg1)
            }
        }
    }
}
