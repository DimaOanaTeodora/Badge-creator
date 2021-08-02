from numpy.core.numeric import NaN
import photoshop.api as ps
from photoshop.api.enumerations import AntiAlias, Justification
from PIL import ImageFont
from pathlib import Path
import os
import sys

# Globals && Constants
TEXT_COLOR = ps.SolidColor()
BADGE_PATH = NaN 
FONT_PATH = NaN
FONT_SIZE = NaN
POSITION_Y = 1150 
DOC_WIDTH = 1200
SAVE_DIRECTORY =NaN

app = ps.Application()

def set_const(red, green, blue, font_size, badge_path, font_path):
      global BADGE_PATH, TEXT_COLOR, FONT_SIZE, BADGE_PATH, FONT_PATH, SAVE_DIRECTORY

      BADGE_PATH = os.path.abspath(badge_path)
      FONT_PATH = os.path.abspath(font_path)
      TEXT_COLOR.rgb.red = int(red)
      TEXT_COLOR.rgb.green = int(green)
      TEXT_COLOR.rgb.blue = int(blue)
      FONT_SIZE = int(font_size)
      SAVE_DIRECTORY = BADGE_PATH[: BADGE_PATH.rindex('\\')] + '\Badgeuri'

def photoshop_open(badge_name):
      global BADGE_PATH, app
      # Open 
      doc = app.load(BADGE_PATH + '\\' + badge_name +'.jpg')
      # DOC_WIDTH = doc.width 
      new_doc = doc.artLayers.add()
      return new_doc, doc

def photoshop_write(new_doc, full_name):
      global FONT_SIZE, TEXT_COLOR, POSITION_Y, FONT_PATH, DOC_WIDTH
      # Adjust splitting of lines if name is longer than 10 chars
      if len(full_name) > 10:
            common_name, family_name = full_name.split(" ")[0], full_name.split(" ")[1]
      else:
            common_name, family_name = full_name, ""

      # Font size depends on family name length
      if len(family_name) > 10:
            FONT_SIZE = FONT_SIZE - len(family_name) 
            font_size_px = ImageFont.truetype(FONT_PATH , FONT_SIZE)
      else:
            font_size_px = ImageFont.truetype(FONT_PATH , FONT_SIZE)

      # OX position depends on the length of the longer name
      maximum_length = NaN
      if len(common_name) > len(family_name):
            maximum_length = font_size_px.getsize(common_name)
      else:
            maximum_length = font_size_px.getsize(family_name)

      # Text layer
      new_text_layer = new_doc
      new_text_layer.kind = ps.TextType.ParagraphText
      new_text_layer.textItem.antiAliasMethod = AntiAlias(4) # 4 coresponds to Strong property

      font_style= FONT_PATH.split('\\')
      font_style= font_style[len(font_style)-1].split('.ttf')[0]
      new_text_layer.textItem.font = font_style

      new_text_layer.textItem.justification = Justification.Center
      # Potoshop doesn't recognize '\n' character . Use '\r' for next line.
      new_text_layer.textItem.contents = common_name + '\r' + family_name
      # 48 units * 0.75 (px/unit) => 36 
      new_text_layer.textItem.position = [DOC_WIDTH / 2 - maximum_length[0] / 36, POSITION_Y] # [OX, OY]
      new_text_layer.textItem.size = FONT_SIZE
      new_text_layer.textItem.fauxBold = True
      new_text_layer.textItem.color = TEXT_COLOR

def photoshop_save(full_name, doc):
      # Save document
      options = ps.JPEGSaveOptions(quality=5)
      document_name = full_name + '.jpg'
      
      Path(SAVE_DIRECTORY).mkdir(parents=True, exist_ok=True)
      doc.saveAs(SAVE_DIRECTORY+ '/' + document_name, options, asCopy=True)
      doc.close()

def successfully_completed():
      global app
      path = str(SAVE_DIRECTORY).replace("\\", "/")
      app.doJavaScript(f'alert("Saved all successfully in Badgeuri directory: {path}")')
      sys.exit()
      
