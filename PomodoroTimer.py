import time, sys
import SevSeg

minutesInput = input("Please enter how many minutes you want to study:\n")
minutesBreak = input("Please enter how many minutes you want to rest:\n")
sessionsToStudy = input("Please enter how many sessions you want to study:\n")

minutesInputted = int(minutesInput) * 60
minutesBreakInput = int(minutesBreak) * 60

studySecondsLeft = minutesInputted
studySecondsLeftRest = minutesBreakInput

studyIntervals = int(sessionsToStudy)

def pomodoroCountTimer(timeLeft):
    while timeLeft > 0:
        hours = str(timeLeft // 3600)
        minutes = str((timeLeft % 3600) // 60)
        seconds = str(timeLeft % 60)

        hoursRest = str((int(hours) // 5))
        minutesRest = str(int(minutes) // 5)
        secondsRest = str(int(seconds) // 5)

        HDigits = SevSeg.getSevSegStr(hours, 2)
        HTopRow, HMiddleRow, HBottmRow = HDigits.splitlines()

        MDigits = SevSeg.getSevSegStr(minutes, 2)
        MTopRow, MMiddleRow, MBotttomRow = MDigits.splitlines()

        SDigits = SevSeg.getSevSegStr(seconds, 2)
        STopRow, SMiddleRow, SBottomRow = SDigits.splitlines()

        print(HTopRow + "       " + MTopRow + "       " + STopRow)
        print(HMiddleRow + "   *   " + MMiddleRow + "   *   " + SMiddleRow)
        print(HBottmRow + "   *   " + MBotttomRow + "   *   " + SBottomRow)
        print()
        print("Press Ctrl-C to quit.")

        time.sleep(1)
        timeLeft -= 1


try:
    while studyIntervals > 0:
        print("\n\t\tStudy Session")
        print("\n\tSessions Left: " + str(studyIntervals))
        pomodoroCountTimer(studySecondsLeft)
        print("\n  Time to take a break!\n")
        pomodoroCountTimer(studySecondsLeftRest)
        studyIntervals -= 1
except KeyboardInterrupt:
    print("\nQuitting")
    sys.exit()

