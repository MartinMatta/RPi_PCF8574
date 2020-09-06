import smbus
import time

class PCF8574:

    def __init__(self, addr, rev=1):
        self._bus = smbus.SMBus(rev)
        self._addr = addr
        self._pin_state = [0, 0, 0, 0,
                   0, 0, 0, 0]
        self._bus.write_byte(self._addr, 0x0)

    def write(self, pin, state):
        data = 0;
        self._pin_state[pin] = state

        for i, state in enumerate(self._pin_state):
            if state == 1:
                data = data +  2**i

        data = int(hex(data), 16)

        self._bus.write_byte(self._addr, data)

        return hex(data)

    def read(self, pin):
        data = self._bus.read_byte(self._addr)
        data = format(data, "0>8b")
        pin += 1
        return int(data[-pin])



pcf8574 = PCF8574(0x20)

pcf8574.write(0, 1)
pcf8574.write(3, 1)

time.sleep(2)

print(pcf8574.read(6))
print(pcf8574.read(7))

pcf8574.write(0, 0)
pcf8574.write(3, 0)
