##Name: Giuliana Tosi
## cdTime.py
##
## Purpose: To calculate total time given multiple
##
## Input: Inputs: Total number of tracks in the cd and number of minutes and seconds within the track(s)
## Output: Outputs: Total time of all tracks listed by user

def main():
    print('This program asks the user to enter: \n -Total number of cds \n -Total number of tracks \n -Number of minutes/seconds in each track')
    cd_total = int(input('Enter the total number of cds: '))
    total_minutes = 0
    total_seconds = 0
##Outer loop
    for cd in range(cd_total):
##Input: Asking the user to enter in their data for total number of tracks and minutes/seconds in each track
        total = int(input('Enter in the total number of tracks within cd' + str(cd+1) + ': '))
        print('Enter in the minutes and seconds for each track')
        minutes = 0
        seconds = 0
##Inner loop
        for t in range(total):
            print('Track ' + str(t + 1))
            minutes = minutes + int(input('Minutes: '))
            seconds = seconds + int(input('Seconds: '))

##Output: Adding the extra seconds to minutes and leaving the remainder seconds under 60
        minutes = minutes + int(seconds/60)
        seconds = seconds % 60
        total_minutes = total_minutes + minutes
        total_seconds = total_seconds + seconds
        print('Cd', str(cd+1), ': ', minutes, 'minutes', seconds, 'seconds')
    total_minutes = total_minutes + int(total_seconds/60)
    total_seconds = total_seconds % 60
    total_hours = int(total_minutes/60)
    total_minutes = total_minutes % 60
    print('Total time of all CDs: ', total_hours, 'hours', total_minutes, 'minutes', total_seconds, 'seconds')
main()


