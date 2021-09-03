import pandas as pd
import re
import Script_PS as PS
import os

def start(red, green, blue, font_size, badge_path, excel_path, font_path):
      
      df = pd.ExcelFile(os.path.abspath(excel_path)).parse('Sheet1') 
      
      #header = ['CD', 'Alumn', 'Design&PR', 'HR', 'FR', 'Edu', 'Proiecte']

      header = df.columns.values
      
      for i in range (df.shape[1]): # df.shape -> tuple (number of written rows - 1 (without header) , number of written columns)
            names=[]
            names.append(str(df[header[i]]))
            names = names[0].split('\n')
            for full_name in names:
                  full_name = re.sub("[0123456789]", "", full_name)
                  full_name = full_name.strip()
                  if full_name == 'NaN':
                        break
                  if "Name:" in full_name:
                        break
                  # Call methods for photoshop app
                  PS.set_const(red, green, blue, font_size, badge_path, font_path)
                  new_doc, doc = PS.photoshop_open(header[i])
                  PS.photoshop_write(new_doc, full_name)
                  PS.photoshop_save(full_name, doc)
            
      PS.successfully_completed()

     



