# Badge creator :mage_man:
Python script created for writing people names on different badges design. It was made to be used by [Asociația Studenților la Matematică și Informatică](https://www.asmi.ro/) for Teambuilding badges.

 :pushpin: *You can find the organization's repository (romanian translation of the README.md) [here](https://github.com/as-mi/creatorul-de-badgeuri).*

<hr>
<div align="center">
<img src="https://cdn.icon-icons.com/icons2/112/PNG/512/python_18894.png" width="45" height="45"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Photoshop_CC_icon.png/615px-Photoshop_CC_icon.png" width="35" height="35"/>
</div>
<hr>

### Demo

<img src="https://user-images.githubusercontent.com/61749814/132041715-9009c6ad-cc3f-4005-805f-f220c0b1530d.gif" width="550" height="300"/>

### How do you use it?
```git clone https://github.com/DimaOanaTeodora/Badge-Creator.git``` command from GitBash.

### Specifications:
:diamond_shape_with_a_dot_inside: Badge dimension: ```750 x 1181 px```.

:diamond_shape_with_a_dot_inside: Badge format ```.jpg```.

:diamond_shape_with_a_dot_inside: Excel table contains the names of the departments on columns.

:diamond_shape_with_a_dot_inside: The names of the badges corespond with name of the columns from Excel file.

:diamond_shape_with_a_dot_inside: Photoshop versions supported ```2020```, ```cc2019```, ```cc2018```, ```cc2017```.

:diamond_shape_with_a_dot_inside: If the last name is longer than 11 chars, it will automatically reduce the font size.
```python
# Font size depends on family name length
      if len(family_name) > 10:
            FONT_SIZE = FONT_SIZE - len(family_name) 
            font_size_px = ImageFont.truetype(FONT_PATH , FONT_SIZE)
      else:
            font_size_px = ImageFont.truetype(FONT_PATH , FONT_SIZE)
 ```

### What you can do with this app ?
:heavy_check_mark: Give a local directory on your PC where you have the unfinished badges.

:heavy_check_mark: Give the local Excel table with your departments and the names of the people.

:heavy_check_mark: Give the font you want to use (```.ttf``` file).

:heavy_check_mark: Give the color of the text (RGB value).

:heavy_check_mark: Give the font size (measured in units - same as font size set in Photoshop).

### You need to modify the code if you want to:
:hammer_and_wrench: Change position for the names on the badge or change the dimension of the badge.
```python
# Script_PS.py
[...]

POSITION_Y = 750
DOC_WIDTH = 827 #pixels

[...]

# X units * 0.75 (px/unit)
new_text_layer.textItem.position = [DOC_WIDTH / 2 - maximum_length[0] / (FONT_SIZE * 0.75), POSITION_Y] # [OX, OY]
``` 
*The formula ```DOC_WIDTH / 2 - maximum_length[0] / (FONT_SIZE * 0.75)``` helps to center positioning relative to the vertical line.*

:hammer_and_wrench: Change names for departments which involves renaming ```.jpg``` files.

*This doesn't need changes in code. The changes will be made just in Excel table and the names of the badges.*

:hammer_and_wrench: Disable the Bold and Strong style of the font.  
```python
#Script_PS.py
[...]

new_text_layer.textItem.antiAliasMethod = AntiAlias(4) # 4 coresponds to Strong property
[...]

new_text_layer.textItem.fauxBold = True
```

### Technologies used :woman_technologist:

 ```Python v3.8.5```

- ```photoshop_python_api``` for the interaction with the Photoshop application. [Find documentation here](https://photoshop-python-api.readthedocs.io/en/master/).
- ```Tkinter``` library for GUI. [Find documentation here](https://docs.python.org/3/library/tk.html).

