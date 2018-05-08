import spidev
import sys
import time

IODIRA   = 0x00
IODIRB   = 0x01
IPOLA    = 0x02
IPOLB    = 0x03
GPINTENA = 0x04
GPINTENB = 0x05
DEFVALA  = 0x06
DEFVALB  = 0x07
INTCONA  = 0x08
INTCONB  = 0x09
IOCONA   = 0x0a
IOCONB   = 0x0b
GPPUA    = 0x0c
GPPUB    = 0x0d
INTFA    = 0x0e
INTFB    = 0x0f
INTCAPA  = 0x10
INTCAPB  = 0x11
GPIOA    = 0x12
GPIOB    = 0x13
OLATA    = 0x14
OLATB    = 0x15

def writeReg(spi, reg, val):
  cmd = 0x40	# Write command, address 000
  spi.xfer([cmd, reg, val])

def setup23s17():
  spi = spidev.SpiDev()
  spi.open(0,0)
  spi.max_speed_hz=1000000

  writeReg(spi, IODIRA, 0) # all port A pins output
  writeReg(spi, IODIRB, 0) # all port B pins output

  return spi

if __name__ == '__main__':
  spi = setup23s17()

  try:
    for i in range(0, 1000):
      writeReg(spi, OLATA, 0xff)
      writeReg(spi, OLATB, 0xff)
      print "On"
      time.sleep(0.25)
      writeReg(spi, OLATA, 0)
      writeReg(spi, OLATB, 0)
      print "Off"
      time.sleep(0.25)

  except KeyboardInterrupt:
    spi.close()
    sys.exit(0)
