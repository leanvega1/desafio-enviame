import sys
import math


delivery_range_days = {
    0: 0,
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 3,
}

def delivery_days(n):
    range = math.ceil(n / 100)
    return get_range(range)

def get_range(range):
    if delivery_range_days.get(range) is None:
        delivery_range_days[range] = get_range(range-1) + get_range(range-2)
    return delivery_range_days.get(range)

def main():
    km = int(sys.argv[1])
    days = delivery_days(km)
    print(f"Se entrega en {days} día{'s' if days != 1 else ''}")

if __name__ == "__main__":
    main()
