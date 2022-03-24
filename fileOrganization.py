import shutil, os
import csv

# Read train.csv
imageData = []
files = []
with open('./train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        imageData.append(row)
        files.append(row[0])

# Extract the different species
species = []
for i in range(1, len(imageData)):
    if imageData[i][1] not in species:
        species.append(imageData[i][1])

# Create a label dict for species
speciesDict = {}
for i in range(len(species)):
    speciesDict[species[i]] = i

for i in species:
    os.mkdir('./organized_train_images/'+str(speciesDict[i]))

# files = ['file1.txt', 'file2.txt', 'file3.txt']
# os.mkdir('my_new_folder')
for f in range(1, len(imageData)):
    print()
    print('./train_images/'+imageData[f][0]+ 'Moved To' + './organized_train_images/'+str(speciesDict[imageData[f][1]])+'/')
    shutil.copy('./train_images/'+imageData[f][0], './organized_train_images/'+str(speciesDict[imageData[f][1]])+'/')