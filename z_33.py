input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()
output_data = open('output.txt', 'w')
output_data.write(str(int(data[1]) - 1) + " " + str(int(data[0]) - 1))
input_data.close()
output_data.close()