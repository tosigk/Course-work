## Name: Giuliana Tosi
## weightedAverage.py
##
## Purpose: Calculate numeric data (weighted averages) from a text file
##
## Input: weights and averages of text file
## Output: average grade of text file

#define the function
def weightedAverage(inFileName, outFileName):
#open file and read the lines
    with open(inFileName, 'r') as file:
        data = file.readlines()
    eachAverage = []
    outLine = []
#create a list of the lines and create vvariables needed in the upcoming for loop
    for line in data:
        line = line.split(' ')
        average = 0
        weightTotal = 0
#a loop to calculate the weighted averages for each student
        for i in range(2,int(len(line)),2):
            weight = line[i]
            weightTotal += float(weight)
            grade = line[i + 1]
            calculation = float(weight) * float(grade)
            average = (average + calculation)
        message = line[0] + ' ' + line[1] + "'s average: "
#conditionals to provide an error if the weighted total is not equal 100
        if weightTotal == 100:
            average /= 100
            eachAverage.append(average)
            outLine.append(message + str(average))
        elif weightTotal < 100:
            outLine.append(message + 'Error: The weights are less than 100.')
        elif weightTotal > 100:
            outLine.append(message + 'Error: The weights are more than 100.')
#creating an output file to write the weighged averages for each student and the class average
    with open(outFileName, 'w') as file:
        for line in outLine:
            file.write(line + '\n')
        file.write('\n')
        file.write('Class Average: ' + str(sum(eachAverage)/len(eachAverage)))
#calls the function of weightedAverage inside of main
def main():
    weightedAverage('grades.txt', 'GiulianaTosiAvg.txt')
main()