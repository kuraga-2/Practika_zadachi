input_data = open('input.txt', 'r')
data = input_data.read()
output_data = open('output.txt', 'w')
output_data.write(str(int(int(data) / 6)) + " " + str(int(4 * int(data) / 6)) + " " + str(int(int(data) / 6)))
input_data.close()
output_data.close()