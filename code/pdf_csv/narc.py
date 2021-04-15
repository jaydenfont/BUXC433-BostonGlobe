# Import Module 
import tabula
import os                               
  
count = 0
# tabula.convert_into("test.pdf", "output/output.csv", output_format="csv", pages='all')
directory = '/Users/momol/BU/BUXC433-BostonGlobe/code/pdf_csv/pdfs'
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        tabula.convert_into(os.path.join(directory, filename), "output/"+filename[:-4]+".csv", output_format="csv", pages='all')
        count += 1
        print(count)
    else:
        continue