#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
      csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
      employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
      employee_list = []
      for data in employee_file:
            data=data.keys
            employee_list.append(data)
      return (employee_list)


def process_data(employee_list):
      department_list = []
      for employee_data in employee_list:
            department_list.append(employee_data)
      department_data = {}
      for department_name in set(department_list):
            department_data[department_name] = department_list.count(department_name)
      return department_data

Employee_list=read_employees("C:\\Users\\USER\\Documents\\1000 Records.csv")

dictionary = process_data(Employee_list)
print(dictionary)
