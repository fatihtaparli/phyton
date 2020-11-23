# import a library to detect encodings
import chardet
import glob

# for every text file, print the file name & a gues of its file encoding
print("File".ljust(33), "Encoding")
for filename in glob.glob('./Texte/*.txt'):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read())
    print(filename.ljust(33), result['encoding'])


# for nur eine text
import chardet
import glob
with open("./Texte\Sprachen.txt", ""rb") as rawdata:
    result=chardet.detect(rawdata.read())
    print(result)