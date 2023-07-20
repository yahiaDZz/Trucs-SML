# read text from image and type it
# char by char
import pyautogui
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
def read_text_from_image(image_path):
    with Image.open(image_path) as img:
        img = img.convert('L')
        text = pytesseract.image_to_string(img,lang='eng',config='--psm 6 --oem 1')
    return text
image_path = "C:\\Users\\DELL\\Desktop\\Capture.PNG"
# text = read_text_from_image(image_path)
# print(text)
text="then will good can life between all she got call almost us is don't few find oil only for move read tree high write your of write side here earth let story head after far number its often does them show world start she close most earth around important hand answer he ask never way call large make did now group where long light state tree on together here add about on your most always children down start most play way try take on change into they can place almost land one it good girl what plant which stop went our point many mile number even between oil with river both an had being of more away is been quite sea keep up home along made had hand people left hard after them think mountain write night story say second learn water school close my him turn something this well even new seem feet under soon us next answer said line might two hear been about new eye talk out sentence only family much end another life question think thought before where at large so home also their along really along run never how was when eat then live this he move point quickly well thought father live came see seem boy picture just how song show boy page know first see girl form feet near spell many far use way got every part until right walk what animal group all feet did small that night side below my be one just year let more without sea world four state old above start we be an need why my hand children while any while idea house no too who make begin world will me not example every eat her righ"

def type_word_from_file(speed=0.1):
        pyautogui.typewrite(text, interval=speed)
typing_speed = 0.08
type_word_from_file(typing_speed)