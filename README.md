# car-processing-system
The program reads the list of car records from a text file, performs some operations on the data, and writes outputs to texts files. 

The input file format:
- The input file is a text file containing a list of cars. Each line in the file describes a car using a set of comma separated strings. The format of each line is as follows:
  make,model,color,year,identifier
  
The program:
- Writing a module called cars.py. This module contains a set of functions for processing and manipulating car data. Each car will be represented by a tuple of strings in the form
  (make,model,color,year,identifier)

List of functions in cars.py.

def load_car_list(file_name)
- Input: the name of a file containing cars data
- Output: a list of cars. Remember, each car is a tuple.

def load_car_dict(file_name)
- Input: the name of a file containing cars data
- Output: a dictionary of cars. The keys in the dictionary are the identification numbers of the cars. The values are tuples of cars. 

def cars_with_make(car_list, make)
- Input: a list of cars.
- Output: a list of cars with the make given by make. 

def cars_with_color(car_list, color)
- Input: a list of cars.
- Output: a list of cars with the color given by color. For example, if color is ‘Green’, then the output list contains all the green cars in car_list.

def sort_by_year(car_list)
- Sort the given list of cars by year in an ascending order without using the sort function. 

def remove_car(car_dict, id)
- Remove the car with identification number equal to id from the dictionary car_dict. Check if a car with key equal to id exists in the dictionary; if it doesn’t then raise a KeyError exception
  with an appropriate message.

def print_make_count(car_list)
- Prints the number of cars for each make in the given list. 
    
def write_to_file(car_dict, file_name)
- Writes the given car dictionary to a file with name file_name.
- The format of the output should be the same as that of the original input file to the program. That means, each car is written in a separate line with the format
  make,model,color,year,identifier
