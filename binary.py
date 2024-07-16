def binary_to_decimal(binary):

    binary.reverse()

    for i in range(len(binary)):
        binary[i] = int(binary[i])
        binary[i] = binary[i]*(2**i)

    number = 0

    for bits in binary:
        number += bits

    print(number)

def decimal_to_binary(decimal):
    binary_list = []
    
    while decimal > 0:
        binary_list.append(str(int(decimal % 2)))
        decimal = int(decimal / 2)

    binary_list.reverse()
    print(''.join(binary_list))

# binary_to_decimal(binary = list(input("Enter bits: ")))
while True:
    decimal_to_binary(decimal = int(input("Enter number: ")))