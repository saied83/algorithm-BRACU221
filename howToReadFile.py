# file input 

file_object = open('input1a.txt', 'r')
input_text: str = file_object.readline() #read one line at a time
input_text: str = file_object.readlines() #read all line at a time

# file output

file_output_object = open('output1a.txt', 'w')
str_a = "this is output\n"
file_output_object.write(str_a)
file_output_object.write("new line")