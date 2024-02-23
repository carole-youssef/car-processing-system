#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:17:59 2022

@author: macbook
"""
#function 1
def load_car_list (filename):
    list1 = []
    file = open(filename, "r")
    
    for line in file:
      stripped_line = line.strip()
      line_tuple = tuple(stripped_line.split(","))
      list1.append(line_tuple)
    file.close()
    
    return list1





#function 2
def load_car_dict(filename):
    dictionary = {}
    file = open(filename, "r")
    
    for line in file:
      stripped_line = line.strip()
      line_tuple = tuple(stripped_line.split(","))
      
      dictionary[line_tuple[4]] = line_tuple[0:]  
    file.close()
      
    return dictionary





#function 3
def cars_with_make(car_list, make):    
    list1 = []
    
    for car in car_list:
        if car[0] == make:
            list1.append(car)
    return(list1)



    

#function 4
def cars_with_color(car_list, color):    
    list1 = []
    
    for car in car_list:
        if car[2] == color:
            list1.append(car)
    
    return (list1)





#function 5
def sort_by_year(car_list):
    
  list1=[]
    
  for car in car_list:
      list1.append(car)
      
  length = len(list1) -1

  listSorted= False

  while listSorted is False:
      listSorted = True

      for i in range(0,length):
          if list1[i][3] > list1[i+1][3]:
              temp = list1[i]
              list1[i] = list1[i+1]
              list1[i+1] = temp
              listSorted = False
  return (list1)
  


  
#function 6
def remove_car(car_dict, id):
    
    if id in car_dict:
            del car_dict[id]
            #print(car_dict)
        
    else:
           raise KeyError (id, "not in dictionary")
        

    
   

#function 7
def print_make_count(car_list):
    
    list1=[]
    
    for car in car_list:
      list1.append(car[0])
    
    freq = [None] * len(list1)
    check = -1 
   
    for i in range(0, len(list1)):  
        count = 1
        
        for j in range(i+1, len(list1)):  
            if(list1[i] == list1[j]):  
                count += 1 
                freq[j] = check
          
        if(freq[i] != check):  
            freq[i] = count  
     
            print(str(list1[i]) + "  " + str(freq[i]))



#function 8 
def write_to_file(car_dict, file_name):
    file = open(file_name, "w")
    list1 = []

    for car in car_dict.values():
        list1.append(car)
    
    for car in list1:
        str1 = ','.join(car)
        file.write(str1)
        file.write('\n')
    
    file.close


   



    
    



