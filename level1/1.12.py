N = int(input())


for _ in range(N):
    first, second, number_to_convert = input().split()

    if first == "2" and second == "10":
        print(int("0b"+number_to_convert, 2))
    elif first == "10" and second == "2":
        print(bin(int(number_to_convert))[2:].upper())
    elif first == "16" and second == "10":
        print(int("0x"+number_to_convert, 16))
    elif first == "10" and second == "16":
        print(hex(int(number_to_convert))[2:].upper())
    elif first == "2" and second == "16":
        print(hex(int("0b"+number_to_convert, 2))[2:].upper())
    elif first == "16" and second == "2":
        print(bin(int("0x"+number_to_convert, 16))[2:].upper())
    elif first == "8" and second == "10":
        print(int("0o"+number_to_convert, 8))
    elif first == "10" and second == "8":
        print(oct(int(number_to_convert))[2:].upper())
    elif first == "2" and second == "8":
        print(oct(int("0b"+number_to_convert, 2))[2:].upper())
    elif first == "8" and second == "2":
        print(bin(int("0o"+number_to_convert, 8))[2:])
    elif first == "8" and second == "16":
        print(hex(int("0o"+number_to_convert, 8))[2:])
    elif first == "16" and second == "8":
        print(oct(int("0x"+number_to_convert, 16))[2:])