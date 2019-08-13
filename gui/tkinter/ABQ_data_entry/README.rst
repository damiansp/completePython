==========================
ABQ Data-Entry Application
==========================

Description
===========

This program provides a data entry form for ABQ Agrilabs laboratory data.

Features
--------

* Provides a validated entry form to ensure correct data
* Stores data to ABQ-format .csv files
* Auto-fills form fields whenever possible

Authors
=======
Alan D Moore, 2008 (original)
Damian Satterthwaite-Phillips, 2019 (reformatting and refactoring)

Requirements
============

* Python 3
* Tkinter

Usage
=====

To start the application run::
  python3 ABQ_Data_Entry/abq_data_entry.py

General Notes
=============

The CSV file will be saved to your current directory in the format "abq_data_record_{TODAY}.csv" where {TODAY} is yyyy-mm-dd
