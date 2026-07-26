from docx import Document
from pathlib import Path

file_path = Path(__file__).parent / "FinalProject.docx"


current_number = ""
numbers = []


def add_number(number):
    result = 0
    for i in number:
        result += i
    return result

def path():
    path = input("Please Enter your .docx File Path Without \" or Leave it for Default: ")
    if not path:
        return file_path
    else:
        return path



 
    
    

ques = "Y"
while ques != "N":
    doc = Document(path())
    for paragraph in doc.paragraphs:
        for i, char in enumerate(paragraph.text):
            if char.isdigit():
                current_number += char
            elif (char == "." or char == "٫" or char == "/") and (i + 1 < len(paragraph.text) and paragraph.text[i + 1].isdigit()):
                char = "."
                current_number += char
            else:
                if current_number:
                    numbers.append(float(current_number))
                    current_number = ""   
    print("Numbers found in the text:", numbers)
    print("Total sum of the numbers:", add_number(numbers))
    numbers = []
    ques = input("Wanna Do That Again: (Y or N) ").strip().upper()




