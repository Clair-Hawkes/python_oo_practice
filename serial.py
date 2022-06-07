class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start):
        '''Create machine from a start number'''
        self.start = start
        self.next = start

    def generate(self):
        '''On each call return the the next sequential number:'''
        self.next += 1
        return self.next -1

    def reset(self):
        '''On call resets the current number back to
        the original start number:'''
        self.next = self.start









