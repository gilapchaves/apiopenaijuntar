from PyPDF2 import PdfMerger

merger = PdfMerger()

input1 = open("pdf/AULA17.pdf","rb")
input2 = open("pdf/AULA18.pdf","rb")

merger.append(fileobj=input1)
merger.append(fileobj=input2)

output = open("aulas_Gil.pdf","wb")

merger.write(output)