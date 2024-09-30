from decimal import Decimal as dec
input_data = open('input.txt', 'r')
data = input_data.read()
output_data = open('output.txt', 'w')
output_data.write(str(round(dec ('2.7182818284590452353602875'), int(data))))
input_data.close()
output_data.close()