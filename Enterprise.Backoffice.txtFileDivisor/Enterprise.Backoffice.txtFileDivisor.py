import os


def read_file(path):
    with open(path, 'r') as file:
        return file.readlines()
    
def split_file(input_data, number_of_rows):
    splitted_data = [input_data[ i : i + number_of_rows] for i in range (0, len (input_data), number_of_rows)]

def write_output_flies(output_data,):
    #TODO implementar código
def main():
    path_input = input("Interage ae tio")
    number_of_rows_by_fle = int(input("Interage aqui tb"))
    
    input_data = read_file(path_input)
    splitted_data = split_file(input_data, number_of_rows_by_fle)
    write_file_output (splitted_data, )
    
if __name__ == "__main__":
    main()