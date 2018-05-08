from RPiMCP23S17.MCP23S17 import MCP23S17
import time

mcp1 = MCP23S17(bus=0x00, ce=0x00, deviceID=0x00)
mcp1.open()

for x in range(16):
    mcp1.setDirection(x, mcp1.DIR_OUTPUT)

print "Starting blinky on all pins (CTRL+C to quit)"
mcp1.writeGPIO(0x0000)

for y in range(100):
    for x in range(16):
        mcp1.digitalWrite(x, MCP23S17.LEVEL_HIGH)
        time.sleep(0.25)

    for x in range(16):
        mcp1.digitalWrite(x, MCP23S17.LEVEL_LOW)
        time.sleep(0.25)

    # the lines below essentially have the same effect as the lines above

    mcp1.writeGPIO(0xFFFF)
    time.sleep(0.25)

    mcp1.writeGPIO(0x0000)
    time.sleep(0.25)

# Turn off leds as we exit...

mcp1.writeGPIO(0x0000)
print "bye bye..."
