import os
from docx import Document
import re


def delcommonds(content):
    out = re.sub(r'/\*.*?\*/', '', content, flags=re.S)
    out = re.sub(r'(//.*)', '', out)
    return out

def read_file(file_path):
    with open(file_path, encoding='utf-8') as file_obj:
        content = file_obj.read()
    return content


def read_mir(dir_path,doc):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(root, file)
            #print(read_file(path))
            doc.add_paragraph(delcommonds(read_file(path)))

doc = Document()
read_mir("D:\\源码\\toptest\\scaProject\\src\\main\\java\\com\\sdstc",doc)
doc.save("D:\\D.docx")