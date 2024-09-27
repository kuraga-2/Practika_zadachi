input_data = open('input.txt', 'r')
data = input_data.read()
a1 = int(data)
A2 = 9
a3 = A2 - a1
c=str(a1) + str(A2) + str(a3)
output_data = open('output.txt', 'w')
output_data.write(c)
input_data.close()
output_data.close()