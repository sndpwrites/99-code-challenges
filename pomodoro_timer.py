import time
import datetime


def pomodoro_timer(numberOfReps):
    print("\t##POMODORO TIMER##")
    print("25 minutes of work followed by")
    print("5 minutes of break")
    work_remaining = 25 * 60
    rest_remaining = 5 * 60

    print("Number of Pomodoros remaining: " + str(numberOfReps))
    while numberOfReps > 0:
        print("Time remaining until next REST")
        while work_remaining > 0:
            timer = datetime.timedelta(seconds=work_remaining)
            print(timer, end="\r")
            time.sleep(1)
            work_remaining -= 1
        print("Work time finished. Please rest now!")
        print("Time remaining until next WORK")
        while rest_remaining > 0:
            timer = datetime.timedelta(seconds=rest_remaining)
            print(timer, end="\r")
            time.sleep(1)
            rest_remaining -= 1
        print("Rest time finished. Back to work!")
        numberOfReps -= 1
        pomodoro_timer(numberOfReps)

    print("All pomodoros completed. Please take a longer rest and come back\n")
    time.sleep(5)


pomodoro_timer(4)
