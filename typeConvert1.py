# Büyük kümeden küçük kümeye geçişte veri kaybına dikkat edilir.
# Küçük kümeden büyük kümeye geçiş yaparken geçişler ototmatik yapılır.

"""
int() -> Tam sayıya
float() -> ondalık sayıya
str() -> metinsel ifadeye
chr() veya ord() -> ASCII kararkterlerinin arasında dönüşüm yapar.
"""

number = "100"
print(int(number)*2)
print(float(number)*2)

character = 'A'
# character -> ASCII
print(ord(character))

# ASCII -> char
print(chr(65))

# ASCII -> char
# chr ( 65+3 )
print(chr(ord(character)+3))

strValue = "12345abc"
#print(int(strValue)) Convert yapılamaz , çevirelemeyecek ifade bulunuyor.

# eğer karakter verisi var ise veya 1 ise True
print(bool("A"))
print(bool(1))

#Eğer karakter verisi yok ise veya o ise False
print(bool(""))
print(bool(0))

x, y, z, = 1, 2, 3
print(bool(x),bool(y),bool(z))

a, b, c = False, False, True
print(not a and not b and not c)