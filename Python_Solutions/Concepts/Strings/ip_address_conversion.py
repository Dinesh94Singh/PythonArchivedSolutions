"""
Write a program that converts an IP address in decimal to binary

Example input:
"1.2.3.4" => "00000001.00000010.00000011.00000100"
"0.0.0.0" => "00000000.00000000.00000000.00000000"
"""

def ip_address_conv(s):
    def convert_to_decimal(base10Number):
        binary = []
        while base10Number > 0:
            rem = base10Number % 2
            binary.insert(0, rem)
            base10Number = base10Number // 2
        if len(binary) != 8:
            for _ in range(8 - len(binary)):
                binary.insert(0, 0)
        return ''.join([str(x) for x in binary])

    temp = s.split('.')
    res = []

    for each in temp:
        if int(each) <= 255:
            res.append(convert_to_decimal(int(each)))
    return '.'.join(res)

ip_address_conv('0.0.0.0')
ip_address_conv('1.2.3.4')
ip_address_conv('255.255.255.255')
