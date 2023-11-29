class calcu:
    def __init__(self, string):
        self.a, self.t, self.b = string.split(" ")
        
    
    def result(self):
        a = self.a
        b = self.b
        if self.t == "+":
            return int(a) + int(b)
        elif self.t == "-":
            return int(a) + int(b)
        elif self.t == "/":
            return int(int(a) / int(b))
        elif self.t == "*":
            return int(a) * int(b)
        else:
            return False

input_string = input()
if not calcu(input_string).result():
    print("False")
print(f"{input_string} = {calcu(input_string).result()}")