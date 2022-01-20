# Session 14 assignment of EPAi4.0
### Submitted by Aneesha Das
### E-mail id: dasaneesha@gmail.com

### Link to Deepnote notebook containing the logs of the program written in the current assignment is as follows: https://deepnote.com/project/TSAI-EPAi-4-Duplicate-cghVpdKuQCOyzm5CZlAoPw/%2FSession-14%2FProject%20-%20Description.ipynb/#00005-c2e653f8-745d-4c95-b8be-ad4eb673e9f8

## Brief description of the assignment

For this project, four files had been provided – personal_info.csv [containing personal information such as name, gender, etc. (one row per person)], vehickes.csv [what vehicle people own (one row per person)], employment.csv [where a person is employed (one row per person)] and update_status.csv [when the person's data was created and last updated]. Each file contains a key, SSN, which uniquely identifies a person. This key is present in all four files and it only appears once per file. In addition, the files are all sorted by SSN, i.e. the SSN values appear in the same order in each file.

Goal 1: The first task is to create iterators for each of the four files that contained cleaned up data, of the correct type (e.g. string, int, date, etc), and represented by a named tuple. For now these four iterators are just separate, independent iterators.

Goal 2: To create a single iterable that combines all the columns from all the iterators. The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match! All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.

Make sure the SSN is not repeated 4 times - one time per row is enough!

Goal 3: To identify any stale records, where stale simply means the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on the last_updated field from the status_update file.

Goal 4: To find the largest group of car makes for each gender. Possibly more than one such group per gender exists (equal sizes).

## Description of functions implemented for solving Goal 1

### get_file

By default, Python reads the data of csv files as string. In order to assign the appropriate data type to each of the fields present within a csv file, four list have been prepared - 'personal_info_data_type', 'vehicle_info_data_type', 'employment_info_data_type' and 'update_info_data_type' - each one corresponding to one of the four input csv files. The function 'get_file' has been written to return the appropriate list when a specific file name is called.

#### Usage

get_datatype(filename)

### cast

The function 'cast' has been written to convert the given data to the respective types mentioned within the corresponding list (eg., ‘personal_info_data_type’,  ‘vehicle_info_data_type’, ‘employment_info_data_type’, ‘update_info_data_type’). The Issue Date has been converted to a list, which will be further converted  to a namedtuple; Summons Number and Violation code values have been converted to type integer. Plate ID, Registration State, Plate Type, Vehicle Body type, Vehicle Make and Violation Description have been converted to string type of data.

#### Usage

cast(data_type, value)

### cast_row

This function 'cast_row' has been written to convert the input data, which are all of string type, to the type corresponding to what has been assigned to them within the previous function.

#### Usage

cast_row(data_types, data_row)

### read_file

The function ‘read_file’ has been written to read a csv file, where the fields have been delimited by ',' (quote character refers to the character that is used to quote a special character in case it appears within the field. In this case, the quote character is "). The headers of the files are then collected and used to assign fields to a new namedtuple that will contain the assembled data from the files. Each of the row in the resulting tuple represent the data from a particular person, which will be printed only when prompted, since the function is a generator.

#### Usage

read_file(file_name)

## Description of functions implemented for solving Goal 2

### combined_file_row_generator

The function 'combined_file_row_generator' has been written to open each of the files 'personal_info.csv', 'vehicles.csv', 'employment.csv' and 'update_status.csv', and then to collect the fields of data which are present in the header of the file. The headers are being collected to assemble the data into a namedtuple that will contain the data from all the four files. The file contains unique data about each person and the information of a single person is displayed each time only when required since the function is a generator.

#### Usage

combined_file_row_generator()
for row in islice(rows, 5):
     print(row)

## Description of functions implemented for solving Goal 3

### combined_file_row_generator_filter_stale

The function 'combined_file_row_generator_filter_stale' has been written to collect the headers from all the four files being used in the current project, and then to create a namedtuple containing the assembled information from all the four files. From this namedtuple, a filter has been created that returns only those records that have been updated on or after 1st March, 2017 when prompted (since the function is a generator) and does not return those records that have been  updated before the aforementioned date.

#### Usage

combined_file_row_generator_filter_stale()
for row in islice(rows, 5):
     print(row)


## Description of functions implemented for solving Goal 4

### car_make_according_to_gender

The function 'car_make_according_to_gender' has been written to calculate the highest selling car corresponding to each gender. This function calls another function 'combined_file_row_generator' within it and uses the output of this class - which is a namedtuple containing the combined information for each person that has been collected from the 4 original files. Two dictionaries have been created - one for each gender of male and female - where the Vehicle Make are the keys and the counts corresponding to each Vehicle Make act as the values. From such a dictionary, the Python in-built function of  'sorted'
has been used to arrange the values in the descending order, thus giving the user the information about which Vehicle Make ranks highest corresponding to each gender.

#### Usage

car_make_according_to_gender()
