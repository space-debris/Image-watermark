from tkinter import *
from tkinter import filedialog, ttk
import tkinter
from PIL import Image, ImageDraw, ImageFont, ImageStat

# im = Image.new('RGBA', (400, 400), (0, 255, 0, 255))
# draw = ImageDraw.Draw(im)

# # Draw a line from (100, 200) to (150, 300)
# draw.line((100, 200, 150, 300), fill=128)

# # To draw a thick line, specify the width
# # draw.line((100, 200, 150, 300), fill=128, width=3)

# # Display the image
# im.show()
def add_watermark(image_path,watermar_text):
  image=Image.open(image_path)
  draw=ImageDraw.Draw(image)

  #font
  width,height = image.size
  font_size=int(min(width,height)*0.05)
  #make a popup asking for font type
  font = ImageFont.truetype("arial.ttf",font_size)

  #positioning the text to bottom right
  #study this textlenght thingggg
  text_widht=draw.textlength(watermar_text,font)
  x=width-text_widht-10
  y=width-text_widht-10

  #calculating the avg brightness
  def brightness_checker(image):
    #study this convert and imagestat
    im=image.convert('L')
    stat=ImageStat.Stat(im)
    return stat.mean[0]/255
  
  #setting the fill wrt to the brightness
  if brightness_checker(image=image)>0.5:
    fill=(0,0,0,128)
  else:
    fill=(255,255,255,128)
  
  #draw the watermark
  draw.text((x,y),watermar_text,fill=fill,font=font)

  #saving the image
  #study this pathhhh
  output_path=f"./{image_path.split('/')[-1]}"
  image.save(output_path)
  image.show()





  #aybe enhance image before watermark? or ask to enhance?

def open_file():
  file_path=filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
  image_entry.delete(0, END)
  image_entry.insert(0,file_path)

def watermark():
  image_path=image_entry.get()
  watermark_text=watermark_entry.get()

  if not image_path or not watermark_text:
    message_label.config(text="Please fill in all fields.")
  else:
    add_watermark(image_path, watermark_text)
    message_label.config(text="Watermark added successfully")
  
#creatig the main window
window=tkinter.Tk()
window.title("Watermark your image")
window.config(padx=10, pady=20)
window_width = 420
window_height = 300
screen_widht = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_widht/2-window_width/2)
center_y = int(screen_height/2-window_height/2)
# ### insert the favicon on the top of the window
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# window.resizable(False,False)

# show a label
label = ttk.Label(window, text='Watermark Your Image', font=("Helvetica", 14))
label.grid(row=0, column=1, columnspan=3, sticky="nsew", padx=0, pady=10)

####insert an image on top of the text ok using image label
### add download button using text and favicon ook
#label.pack(ipadx=10, ipady=10)
#label.config(pady=12)



#get to the image
image_label = ttk.Label(window, text="Select image :")
image_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

image_entry = Entry(window)
image_entry.config(width=30)
image_entry.grid(row=1, column=1, padx=5, pady=5)

browse_button = ttk.Button(window, text="Browse", command=open_file)
browse_button.grid(row=1, column=2, padx=(5,20), pady=5)

#watermarking
watermark_label = ttk.Label(window, text="Enter watermark text :")
watermark_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

watermark_entry = Entry(window)
watermark_entry.config(width=30)
watermark_entry.grid(row=2, column=1, padx=5, pady=5)

watermark_button = ttk.Button(window,text="Watermark", command=watermark)
#watermark_button.config(pady=4, padx=2)
watermark_button.grid(row=3, column=1)

#popup
message_label = Label(window, text="")
message_label.grid(row=4, column=1)




window.mainloop()