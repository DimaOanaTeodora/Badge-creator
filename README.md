# Badge Creator :mage_man:
Python script created for writing people names on different badges design. Also was made to be used by [Asociația Studenților la Matematică și Informatică](https://www.asmi.ro/) for Teambuilding badges.

### Demo

### Specifications:
:diamond_shape_with_a_dot_inside: Badge dimension: ```1200 x 1800 px```.

:diamond_shape_with_a_dot_inside: Badge format ```.jpg```.

:diamond_shape_with_a_dot_inside: Excel table contains the names of the departments on columns.

:diamond_shape_with_a_dot_inside: The names of the badges corespond with name of the columns from Excel file.

:diamond_shape_with_a_dot_inside: Photoshop versions supported ```2020```, ```cc2019```, ```cc2018```, ```cc2017```.

### What you can do with this app ?
:heavy_check_mark: Give a local directory on your PC where you have the unfinished badges.

:heavy_check_mark: Give the local Excel table with your departments and the names of the people.

:heavy_check_mark: Give the font you want to use (.ttf file).

:heavy_check_mark: Give the color of the text (RGB value).

:heavy_check_mark: Give the font size (measured in units - same as font size set in Photoshop).

### You need to modify the code if you want to:
:hammer_and_wrench: Change position for the names on the badge. 

:hammer_and_wrench: Change names for departments which involves renaming ```.jpg``` files.

:hammer_and_wrench: Disable the Bold and Strong style of the font.  

:hammer_and_wrench: Change the dimension of the badge.

### Technologies used :woman_technologist:

 ```Python v3.8.5```
 
- ```photoshop_python_api``` for the interaction with the Photoshop application. [Find documentation here](https://photoshop-python-api.readthedocs.io/en/master/)
- ```Tkinter``` library for GUI. [Find documentation here](https://docs.python.org/3/library/tk.html)
