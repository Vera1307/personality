# import the opencv library
import cv2
from PIL import Image

import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# define a video capture object
vid = cv2.VideoCapture(0)
def extract_name(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(Image.fromarray(img), config = "tessedit_char_blacklist=0123456789/[]^")
    names = re.findall("[A-Z]+", text)
    black_list = ['REPUBLICA',
                 'MOLDOVA',
                 'MDA',
                 'CA',
                 'BULETIN',
                 'DE',
                 'IDENTITATE']
    names = [name for name in names if name not in black_list and len(name)>2]
    return ' '.join(names)
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    text = extract_name(frame)
    print(text)
    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()