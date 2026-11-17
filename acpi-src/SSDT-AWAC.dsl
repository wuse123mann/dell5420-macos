/*
 * Disable AWAC (\_SB.AWAC) and enable legacy RTC (\_SB.PC00.LPCB.RTC) on macOS.
 * The DSDT already defines \_SB._INI, so STAS is set at table-load time instead of in a new _INI.
 */
DefinitionBlock ("", "SSDT", 2, "LAT54", "AWAC", 0x00002000)
{
    External (STAS, FieldUnitObj)

    If (_OSI ("Darwin"))
    {
        STAS = One
    }
}
