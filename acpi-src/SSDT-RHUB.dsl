/* USB reset: hide \_SB.PC00.XHCI.RHUB on macOS so ports enumerate from the controller. */
DefinitionBlock ("", "SSDT", 2, "LAT54", "RHUB", 0x00002000)
{
    External (_SB_.PC00.XHCI.RHUB, DeviceObj)

    Scope (\_SB.PC00.XHCI.RHUB)
    {
        Method (_STA, 0, NotSerialized)
        {
            If (_OSI ("Darwin")) { Return (Zero) }
            Return (0x0F)
        }
    }
}
