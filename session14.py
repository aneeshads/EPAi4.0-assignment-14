import csv
from itertools import islice
from collections import namedtuple

file_named_tuple = {'personal_info.csv': 'PersonalInfo', 'employment.csv': 'Employment', 'vehicles.csv': 'Vehicles', 'update_status.csv': 'UpdateStatus'}

personal_info_data_type = ['INT', 'STRING', 'STRING', 'STRING','STRING']
vehicle_info_data_type = ['INT', 'STRING', 'STRING', 'INT']
employment_info_data_type = ['STRING', 'STRING', 'INT', 'INT']
update_info_data_type = ['INT', 'DATE', 'DATE']

def get_file(filename):
    """By default, Python reads the data of csv files as string. In order to assign \
    the appropriate data type to each of the fields present within a csv file, four \
    list have been prepared - 'personal_info_data_type', 'vehicle_info_data_type', \
    'employment_info_data_type' and 'update_info_data_type' - each one corresponding \
    to one of the four input csv files. The function 'get_file' has been written to \
    return the appropriate list when a specific file name is called.
    """
    
    if filename == 'personal_info.csv':
        return personal_info_data_type
    elif filename == 'employment.csv':
        return employment_info_data_type
    elif filename == 'vehicles.csv':
        return vehicle_info_data_type
    elif filename == 'update_status.csv':
        return update_info_data_type


def cast(data_type, value):
  """The function 'cast' has been written to convert the given data to the \
  respective types mentioned within the corresponding list (eg.,personal_info_data_type, \
  vehicle_info_data_type,employment_info_data_type, update_info_data_type). \
  The Issue Date has been converted to a list,which will be further converted \
  to a namedtuple; Summons Number and Violation code values have been converted \
  to type integer.Plate ID, Registration State, Plate Type,Vehicle Body type,\
  Vehicle Make and Violation Description have been converted to string type of data.
  """

  if data_type == 'DATE':
      Date = namedtuple('Date', 'Year Month Day')
      date  = [int(i) for i in value[:10].split('-')]
      date = Date(*date)
      return date
  elif data_type == 'INT':
    return int(value.replace("-", ""))
  else:
    return str(value)


def cast_row(data_types, data_row):
  """This function 'cast_row' has been written to convert the input data, which are \
  all of string type, to the type corresponding to what has been assigned to them \
  within the previous function.
  """
  return [cast(data_type, value)
          for data_type, value in zip(data_types, data_row)]


def read_file(file_name):
    """The function read_file has been written to read a csv file, where the fields \
    have been delimited by ',' (quote character refers to the character that is used to\
    quote a special character in case it appears within the field. In this case, the quote \
    character is "). The headers of the files are then collected and used to assign fields \
    to a new namedtuple that will contain the assembled data from the files. Each of the row \
    in the resulting tuple represent the data from a particular person, which will be printed \
    only when prompted, since the function is a generator.
    """
    with open(file_name) as f:
        file_iter = csv.reader(f, delimiter=',', quotechar='"')
        header = next(file_iter)
        NamedTuple_name = namedtuple(file_named_tuple[file_name], header)
        for row in file_iter:
            data = cast_row(get_file(file_name), row)
            namedtuple_row = NamedTuple_name(*data)
            yield namedtuple_row

rows = read_file('personal_info.csv')
for row in islice(rows, 5):
    print(row)

rows = read_file('vehicles.csv')
for row in islice(rows, 5):
    print(row)
    
rows = read_file('employment.csv')
for row in islice(rows, 5):
    print(row)
    
rows = read_file('update_status.csv')
for row in islice(rows, 5):
    print(row)
    
combined_data_type = ['INT', 'STRING', 'STRING', 'STRING','STRING', 'STRING', 'STRING', 'INT', 'STRING', 'STRING', 'INT', 'DATE', 'DATE']

def combined_file_row_generator():
    """The function 'combined_file_row_generator' has been written to open each of the \
    files 'personal_info.csv', 'vehicles.csv', 'employment.csv' and 'update_status.csv',\
    and then to collect the fields of data which are present in the header of the file. \
    The headers are being collected to assemble the data into a namedtuple that will \
    contain the data from all the four files. The file contains unique data about each \
    person and the information of a single person is displayed each time only when required \
    since the function is a generator.
    """
    with open('personal_info.csv') as fpersonal:
        personal_info_rows = csv.reader(fpersonal, delimiter=',', quotechar='"')
        personal_info_header = next(personal_info_rows)
        with open('vehicles.csv') as fvehicle:
            vehicle_info_rows = csv.reader(fvehicle, delimiter=',', quotechar='"')
            vehicle_info_header  = next(vehicle_info_rows)
            with open('employment.csv') as femployment:
                employment_info_rows = csv.reader(femployment, delimiter=',', quotechar='"')
                employment_info_header = next(employment_info_rows)
                with open('update_status.csv') as fupdate:
                    update_info_rows = csv.reader(fupdate, delimiter=',', quotechar='"')
                    update_info_header = next(update_info_rows) 
                    CombinedInfo = namedtuple("CombinedInfo", personal_info_header+vehicle_info_header[1:]+employment_info_header[:-1]+update_info_header[1:])
                    for personal, vehicle, employment, update in zip(personal_info_rows, vehicle_info_rows, employment_info_rows, update_info_rows):
                        final_row = personal+vehicle[1:]+employment[:-1]+update[1:]
                        final_row = cast_row(combined_data_type, final_row)
                        info_row = CombinedInfo(*final_row)
                        yield  info_row

rows = combined_file_row_generator()
for row in islice(rows, 5):
    print(row)
    
def combined_file_row_generator_filter_stale():
    """The function 'combined_file_row_generator_filter_stale' has been written \
    to collect the headers from all the four files being used in the current \
    project, and then to create a namedtuple containing the assembled information \
    of all the four files.From this namedtuple, a filter has been created that returns \
    only those records that have been updated on or after 1st March, 2017 when prompted \
    (since the function is a generator) and does not return those records that have been \
    updated before the aforementioned date
    """
    with open('personal_info.csv') as fpersonal:
        personal_info_rows = csv.reader(fpersonal, delimiter=',', quotechar='"')
        personal_info_header = next(personal_info_rows)
        with open('vehicles.csv') as fvehicle:
            vehicle_info_rows = csv.reader(fvehicle, delimiter=',', quotechar='"')
            vehicle_info_header  = next(vehicle_info_rows)
            with open('employment.csv') as femployment:
                employment_info_rows = csv.reader(femployment, delimiter=',', quotechar='"')
                employment_info_header = next(employment_info_rows)
                with open('update_status.csv') as fupdate:
                    update_info_rows = csv.reader(fupdate, delimiter=',', quotechar='"')
                    update_info_header = next(update_info_rows) 
                    CombinedInfo = namedtuple("CombinedInfo", personal_info_header+vehicle_info_header[1:]+employment_info_header[:-1]+update_info_header[1:])
                    for personal, vehicle, employment, update in zip(personal_info_rows, vehicle_info_rows, employment_info_rows, update_info_rows):
                        final_row = personal+vehicle[1:]+employment[:-1]+update[1:]
                        final_row = cast_row(combined_data_type, final_row)
                        info_row = CombinedInfo(*final_row)
                        if ((info_row.last_updated.Year >= 2017) and (info_row.last_updated.Month >= 3) and (info_row.last_updated.Day >= 1)):
                            yield  info_row
                        else:
                            pass
                          
rows = combined_file_row_generator_filter_stale()
for row in islice(rows, 5):
    print(row)
    

male_vehicle_dict = {}
female_vehicle_dict = {}

def car_make_according_to_gender():
    """The function 'car_make_according_to_gender' has been written to calculate the highest \
    selling car corresponding to each gender. This function calls another function \
    'combined_file_row_generator' within it and uses the output of this class - which is a \
    namedtuple containing the combined information for each person that has been collected \
    from the 4 original files. Two dictionaries have been created - one for each gender of \
    male and female - where the Vehicle Make are the keys and the counts corresponding to \
    each Vehicle Make act as the values. From such a dictionary,the in-built functions of \
    'sorted' in Python has been used to arrange the values in the descending order, \
    thus giving the user the information about which Vehicle Make ranks highest corresponding \
    to each gender.
    """
    rows = combined_file_row_generator()
    for row in rows:
        if(row.gender == 'Male'):
            if row.vehicle_make not in male_vehicle_dict:
                male_vehicle_dict.__setitem__(row.vehicle_make, 1)
            else:
                male_vehicle_dict[row.vehicle_make] = male_vehicle_dict[row.vehicle_make] + 1
        elif(row.gender == 'Female'):
            if row.vehicle_make not in female_vehicle_dict:
                female_vehicle_dict.__setitem__(row.vehicle_make, 1)
            else:
                female_vehicle_dict[row.vehicle_make] = female_vehicle_dict[row.vehicle_make] + 1
    male_dict_list = sorted(male_vehicle_dict.items(), key=lambda x:x[1], reverse = True)
    print("Male : ", male_dict_list)
    female_dict_list = sorted(female_vehicle_dict.items(), key=lambda x:x[1], reverse = True)
    print("Female : ", female_dict_list)

car_make_according_to_gender()
    
