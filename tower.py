import time

class Tower:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
    
    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A =", self.A)
        print("Items in Tower A\n")

    def move(self, from_peg, to_peg, from_name, to_name):
        if from_peg:
            disk = from_peg.pop()
            to_peg.append(disk)
            time.sleep(1)
            print(f"Move disk {disk} from {from_name} to {to_name}")
            print("A =", self.A, "  B =", self.B, "  C =", self.C)
        else:
            print("No disk to move.")

    def pass1(self):
        self.move(self.A, self.C, 'A', 'C')

    def pass2(self):
        self.move(self.A, self.B, 'A', 'B')

    def pass3(self):
        self.move(self.C, self.B, 'C', 'B')

    def pass4(self):
        self.move(self.A, self.C, 'A', 'C')

    def pass5(self):
        self.move(self.B, self.A, 'B', 'A')

    def pass6(self):
        self.move(self.B, self.C, 'B', 'C')

    def pass7(self):
        self.move(self.A, self.C, 'A', 'C')

# Example usage:
obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

