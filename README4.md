Working with external data
===========================
input, output, csv, json files

n.b. system only writes to file when ou close the file in the code
n.b. write overrites data in file so use append instead if you want to add to existing data

Json from the web
-----------------
Import json library
define function to get data using the url open function
the loads function takes a string of json and parses it to a native python object e.g. dictionary
To access you can use a for in statement

see https://docs.python.org/3.6/library/json.html

```
def main():
urlData = "http://myurl.com"
weburl = urllib.request.urlopen(urlData)
print("result code:" + str(weburl.getcode()))

if(weburl.getcode() == 200):
data - weburl.read()
print results(data)

else:
print("received an error", weburl.getcode())

```

XML
---
There are two ways that xml can be parsed

SAX - simple api for xml. Reads xml file one character at a time. generates various events e.g. start, tag, text
DOM - document object model

Working with files
------------------
Import the os module to interact with the operating system

print current working directory:

```
def display_cwd():
cwd = os.getcwd()
print("current working directory:", cwd)

```

Navigate folders:

```
def up_one_directory_level():
os.chdir("../")

```

list folders and files in a directory:
using os odule

```
def display_entries_in_director(directory):
with os.scandir(directry) as entries:
for entry as entries:
print(entry.name)

```
N.b. you can also use listdir() but this does not have all the information that can be accessed with entry.stat()

using glob - python's glob module lets you filter path names e.g. to display all png files

```
import glob

def display_pngs():
png_files = glob.glob('*.png')
print(png_files)
```

To filter by filename:

```
def find_monster_one():
filtered_items = glob.glob('*monster01*')
print(filtered_items)
```

N.b. you can add recursive = true to a for loop to loop through sub directories.

You can also use os walk function to navigate

```
def top_down_walk():
for dirpath, dirnames, files in os.walk('artwork/'):
print("Directory:", dirath)
print("includes these directories")
for dirname in dirnames:
print(dirnae)
rint("includes these files")
for filename in files:
print(filename)
print()

```

Using pathlib module:
you can use pathlib that represents files as objects and strings from pathlib import path

```
def print_directory_contents():
entries = path.cwd()

for entry in entries.iterdir():
print(entry.name)
print(entry.parent)
print(entryparent.parent)
print(entry.stem)
print(entry.suffix)
print(entry.stat)
print()

```
Create a directory:
using os module:

```
def make_logs_dir():
try:
os.mkdir("logs/")
except fileExistsError as ex:
print(logs directory already exists')
```

using pathlib directory:

```
def make_output_dir():
dir_path = path("output/")
dir_path.mkdir(exist_ok = true)
```

if file exists no entry is created and there is no error

Open files:
files can be opened using the oen function in different modes:
r mode = read only
a mode - append only
w mode - write only. If file does not exist python creates the file

files are written to using text mode but yu can specify binary ode e.g. r + b mode

```
def print_content():
f = open('descriptions/description-01.txt', r')
contents = f.read()
print(contents)
f.close()

```
write to a file:

```
def write_new_content():
f = open('descriptions/description-01.txt', 'w')
f.write("here is some text")
f.close()
```
N.b. if you use the with pattern it automatically closes the file

Read the first 10 bytes of a file:

```
print(f.read(10))
```
Parse json files:

```
def display_json():
with open('monster.json) as f:
content_json = json.load(f)
print(content_json)
```

Read csv files:
use the csv module

```
def display_csv_reader():
with open('monsters.csv') as f:
reader = csv.reader(f, delimiter = ',')
for row in reader
print(row[1])
```
N.b. row shows column values. You can also specify column name

```
def display_csv_reader_dict():
with open('monsters.csv') as f:
dictReader = csv.DictReader(f, deliiter - ',')
for row in dictReader:
print(row["monsterName"] + "is priced at" + row ["price"])
```
N.b. you can use pandas library to analyse data and perform statistical operations

pandas:
you need to install pandas from pip library - install pandas then import pandas

```
import pandas as pd

def display_csv_pandas():
df = pd.read_csv('monsters.csv')
print(df)
```

pdf:
use external library PyPDF2 to extract, encrypt decrypt file and merge pages.
download with pip - install PyPDF2
import the module - import PyPDF2

```
def read_pdf():
with open('recipe-book.pdf', 'r+b') as f:
reader = PyPDF2.pdfFileReader(f)
print(reader.numPages)
print(reader.getDocumentInfo())
pageObj - reader.getPage(2)
print("\n" + pageObj.extractText()
```

N.b. this library may not extract all text in the file

Rename a file:
os module:

```
def rename_os():
os.rename('images/monster01.png', 'images/monster_01.png')
```
pathlib:

```
def rename pathlib():
file = path('images/monster02.png')
file.rename('images/monster_02.png')
```
move files:
use the shutil module to move files from one folder to another

move multiple files
```
def move_files():
shutil.move('images/', 'png/')
```
make a directory then move a single file:
```
def move file():
os.mkdir('vg')
shutil.move(ng/monster03.svg', 'svg/)
```

copy files:
use the shutil module. specify file and filder to copy to. To copy file with its metadata use the copy2 function. You can also copy a directory
by specifying directory and destination directory.

```
def copy_file():
shutil.copy('monster01.png', 'images/png')

def copy_file_with_metadata():
shutil.copy2('monster02.ng', 'images/png')

def copy_directory():
shutil.copytree('images/', 'backup-images/')
```

Delete files and directories
N.b. directory must be empty before you can delete it (otherwise use shutil instead)

```
def_delete_file_os():
os.remove('screenshots/screenshot1.png')

def delete_file_pathlib():
file = path("screenshots/screenshot2.png")
file.unlink()

def delete_directory_os():
os.rmdir("screenshots/")

def delete_directory_pathlib():
directory = path("other-screenshots/")
directory.rmdir()

def delete_directory_including_subdir():
shutil_rmtree('old-images/')

save tabular data to csv:
use csv olbject if your data is saved as a list

```
import csv

def write_to_csv_list():
with ope('products.csv' 'w') as file:
writer = csv.writer(file)
writer.writerow(["id", "category", "name"]}
writer.writerow([41, "furnishings", "office chair"])
writer.writerow([20, "office supplies", "pens"])
```
N.b. enter cat products.csv on the commandline to see what a file contains 

if data is saved as a dictionary use the following:

```
def write_to_csv_dictionary():
with open('maintenance-products.csv', 'w') as file:
headers = ['id', 'name', 'quantity', 'price']
writer = csv.dictwriter(file, fieldnames = headers)
writer.writeheader()
item - {'id' = 65, 'name' = 'ladder', 'quantity' = 33, 'price' = 50 }
writer.writerow(item)
```

write to json file:
from dictionary object

```
import json

def generate_dictionary(monster_name, title, price, scariness):
return { 'monster_name' = monster_name, 'title' = title, 'price' = price, 'scarinexx' = scariness }

def write_to_json(dictionary_data):
with open ('monsters.json', 'w') as file:
json.dump(dictionary_data, file)

if __name__ = "__main__":
monster one = generate_dictionary('file', 'baker by day' 29, 3)
monster two = generate_dictionary('timber', 'database expert', 19, 2)
write_to_json([monster_one, monster_two])

```
zip files:
use zip file module

create zip

```
def create_zip(files)
with zipfile.zipFile('archive.zip', 'w') as archive:
for file in files:
archive.write(file)

if __name__ -- __main__":
files = ["png/monster01.png", "png/monster02.png"]
create_zip(files)
```
Read zip fil and extract files:

```
import zipfile

def read_zip():
with zipfile.zipFile('archive.zip', 'r') as archive:
print(archive.namelist())

def retrieve_file_info_zip():
with zipfile.zipFile('archive.zip', 'r') as archive:
file_info = archive.getinfo('description01.txt')
print(file_info)

def read_file_in_zip():
with zipfile.zipFile('archive.zip', 'r') as archive:
with archive.open('description01.txt') as file:
print (file.read())

def extract_file(archive, file_to_extract):
with zipfile.zipFile(archive, 'r') as my_archive:
my_archive.extract(file_to_extract)

if __name__ = "__main__":
extract_file('archive.zip', 'description01.txt')
```

Temporary files:
using the tempfile module. Files are automatically deleted when the file is closed
Open in write and read file w+

N.b. python puts a dursor in the file after writing. To go back to the beginning of the file (so that you can read it) use seek()

```
def work_with_temporary_file():
with tempfile.Temporaryfile('w+') as tf:
tf.write('this is a sntence')
tf.seek(0)
print(tf.read())
```



documentation 
===================
https://docs.python.org/3.6/library/json.html

