# An Data Entry App for a Hypothetical Company - ABQ Agrilab


ABQ Data Entry Program Spec
===========================


Description
-----------
The program is being created to minimize data entry errors for lab measurements.


Functionality
-------------
The program must:
* allow all relevant, valid data to be entered (per field chart)
* append entered data to a .csv file
  * The csv must have a filename: `abq_data_record_{CURRENT_DATE}.csv` with CURRENT_DATE in `YYYY-MM-DD` format
  * The csv must have all fields in field chart
* enforce correct data types per field

The program should, whenever possible:
* enforce reasonable limits on data entered
* auto-fill data
* suggest likely-correct values
* provide a smooth and efficient workflow


Functionality Not Required
--------------------------
The program need not:
* allow editing of data
* allow deletion of data


Limitations
-----------
The program must:
* be efficiently operable by keyboard-only users
* be accessible to colorblind users
* run on Debian Linux
* run acceptably on a low-end PC


Data Fields
-----------

Field       | Data Type | Units | Range         | Description
==========================================================================
Date        | Date      |       |               | Date of record
Time        | Time      |       | 8, 12, 16, 20 | Time period
Lab         | Str       |       | A - E         | Lab ID
Technician  | Str       |       |               | Tech name
Plot        | Int       |       | 1 - 20        | Plot ID
Seed Sample | Str       |       |               | Seed sample ID
Fault       | Bool      |       |               | Fault on sensor
Light       | Float     | klx   | 0 - 100       | Light at plot
Humidity    | Float     | g/m^3 | 0.5 - 52.0    | Abs humidity at plot
Temperature | Float     | C     | 4 - 40        | Temperature at plot
Blossoms    | Int       |       | 0 - 1000      | # blossoms in plot
Fruit       | Int       |       | 0 - 1000      | # fruits in plot
Plants      | Int       |       | 0 - 20        | # plants in plot
Max Height  | Float     | cm    | 0 - 1000      | Height of tallest plant
Min Height  | Float     | cm    | 0 - 1000      | Height of shortest plant
Median Hght | Float     | cm    | 0 - 1000      | Median height of plants
Notes       | Str       |       |               | Misc. notes
