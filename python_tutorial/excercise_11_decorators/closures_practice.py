#function returning function(closure) practice
def to_power(x):
    def calculate_power(n):
        return n**x
    return calculate_power
cube=to_power(3)
print(cube(4))

square=to_power(2)
print(square(3))
