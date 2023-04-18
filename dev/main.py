from .simple import PowerNum

def num_to_power_of_two(num):
    print(num.val)
    num.power_of_two()
    print(num.val)

if __name__ == "__main__":
    num = PowerNum(2)
    num_to_power_of_two(num)
    