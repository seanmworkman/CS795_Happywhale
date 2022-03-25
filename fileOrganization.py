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
    os.mkdir('./organized_train2_images/'+str(speciesDict[i]))
    os.mkdir('./organized_validation_images/'+str(speciesDict[i]))
    os.mkdir('./organized_test_images/'+str(speciesDict[i]))


trainBreak = int(len(imageData) * 0.7)
valBreak = int(len(imageData) * 0.15)
testBreak = int(len(imageData) * 0.15)
# print(trainBreak)
# print(valBreak)
# print(testBreak)


for f in range(1, len(imageData)):
    if f < trainBreak:
        print()
        print('./train_images/'+imageData[f][0]+ ' Moved To ' + './organized_train2_images/'+str(speciesDict[imageData[f][1]])+'/')
        shutil.copy('./train_images/'+imageData[f][0], './organized_train2_images/'+str(speciesDict[imageData[f][1]])+'/')
    elif f < (trainBreak + valBreak):
        print()
        print('./train_images/'+imageData[f][0]+ ' Moved To ' + './organized_validation_images/'+str(speciesDict[imageData[f][1]])+'/')
        shutil.copy('./train_images/'+imageData[f][0], './organized_validation_images/'+str(speciesDict[imageData[f][1]])+'/')
    elif f < (trainBreak + valBreak + testBreak):
        print()
        print('./train_images/'+imageData[f][0]+ ' Moved To ' + './organized_test_images/'+str(speciesDict[imageData[f][1]])+'/')
        shutil.copy('./train_images/'+imageData[f][0], './organized_test_images/'+str(speciesDict[imageData[f][1]])+'/')

    