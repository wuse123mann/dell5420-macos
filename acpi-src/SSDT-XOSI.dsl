/*
 * XOSI for Dell Latitude 5420: on macOS answer _OSI like Windows 10 so OSYS = 0x07DF.
 * Needed for the I2C touchpad: with OSYS < 0x07DC the DSDT gives TPD0 an APIC interrupt
 * and disables the GPIO pad (SRXO) instead of the GpioInt that VoodooI2C uses.
 * Pairs with the ACPI patch _OSI -> XOSI (DSDT only).
 */
DefinitionBlock ("", "SSDT", 2, "LAT54", "XOSI", 0x00002000)
{
    Method (XOSI, 1, NotSerialized)
    {
        Local0 = Package ()
        {
            "Windows 2001",
            "Windows 2001 SP1",
            "Windows 2001 SP2",
            "Windows 2001.1",
            "Windows 2006",
            "Windows 2006 SP1",
            "Windows 2009",
            "Windows 2012",
            "Windows 2013",
            "Windows 2015"
        }
        If (_OSI ("Darwin"))
        {
            Return ((Ones != Match (Local0, MEQ, Arg0, MTR, Zero, Zero)))
        }

        Return (_OSI (Arg0))
    }
}
