"""
10진수 -> 2, 8, 16진수 문자열로 변환
2진수      bin( 정수 )
8진수      oct( 정수 )
16진수    hex( 정수 )
----------------------------------------
x진수 -> 10진수 변환

형식 : int( 정수, 진수 ) // 진수에 해당하는 정수 문자열

ex) int( 12345, 7 ) -> 7진수를 10진수로 변환
"""
bina = bin(1024)
octa = oct(1024)
hexa = hex(1024)
print(bina, octa, hexa)

print(type(bina))
print(type(int(bina, 2)))

print(int(bina, 2))
print(int(octa, 8))
print(int(hexa, 16))
