def main():
    celsius = float(input("Temperature in Celsius: "))
    fahrenheit = convert(celsius)
    print(f"{fahrenheit:.1f}")

def convert(celsius):
    return (celsius * 9 / 5) + 32

main()