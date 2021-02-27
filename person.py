class Person:
    name = None
    def __init__(self, addr, conn):
        self.addr = addr
        self.conn = conn

    def set_name(self, name):
        self.name = name

    def __eq__(self, other):
        if self.addr != other.addr:
            return False
        else:
            return True