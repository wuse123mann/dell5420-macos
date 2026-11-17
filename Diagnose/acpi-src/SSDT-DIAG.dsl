/*
 * DIAGNOSE ONLY - Dell Latitude 5420 brightness keys.
 * Types a marker letter (via VoodooPS2Keyboard) each time a firmware step runs on macOS:
 *   q = EC event _Q66 fired
 *   s = SMEE (Dell SMI event dispatcher) reached
 *   d = OSID >= 0x20 inside SMEE (brightness branch allowed)
 * Requires ACPI patches _Q66 -> XQ66 and SMEE -> XMEE.
 */
DefinitionBlock ("", "SSDT", 2, "LAT54", "DIAG", 0x00000001)
{
    External (_SB_.PC00.LPCB.ECDV, DeviceObj)
    External (_SB_.PC00.LPCB.ECDV.XQ66, MethodObj)
    External (_SB_.PC00.LPCB.PS2K, DeviceObj)
    External (_SB_.OSID, MethodObj)
    External (XMEE, MethodObj)

    Scope (\_SB.PC00.LPCB.ECDV)
    {
        Method (_Q66, 0, NotSerialized)
        {
            If (_OSI ("Darwin"))
            {
                Notify (\_SB.PC00.LPCB.PS2K, 0x0310)
            }

            \_SB.PC00.LPCB.ECDV.XQ66 ()
        }
    }

    Method (SMEE, 1, NotSerialized)
    {
        If (_OSI ("Darwin"))
        {
            Notify (\_SB.PC00.LPCB.PS2K, 0x031F)
            If ((\_SB.OSID () >= 0x20))
            {
                Notify (\_SB.PC00.LPCB.PS2K, 0x0320)
            }
        }

        \XMEE (Arg0)
    }
}
