from barcode import EAN13

from barcode.writer import ImageWriter

number = "4003673647257"
mycode = EAN13(number, writer=ImageWriter())

mycode.save("New_code")
