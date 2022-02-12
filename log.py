import datetime, os, sys

def log (message):
    # print to terminal
    rawtime = datetime.datetime.now()
    time = str(rawtime.strftime("%m/%d/%Y %I:%M:%S %p"))

    print(f"[{time}] {message}\n")


# super duper simple logging thing, didnt want to use logging cuz pycord already uses it
