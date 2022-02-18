import time
import random
import os
import json
import webbrowser
import click
import sys
import ctypes
import timeit

########window title set##########
ctypes.windll.kernel32.SetConsoleTitleW("Christmas challenge")

########print_slow event##############
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.3)

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def print_even_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.9)

###cls event###
def cls():
    click.clear()
###############

######################################main loadup + challenge 1###############################################
print_slow("hello friend...\n")
key = input("enter keY number here:")
key = int(key)

if key == 7:
    cls()
    print_fast("okay... that was your first test there will be")
    time.sleep(0.76)
    print_fast(" 2 more.\n")
    print_fast("the prize is [******] pass test no.[!2!] to find out what the prize is...")
    time.sleep(3)
    cls()
##############################challenge 2#############################################
    print_slow("""welcome To challenge *number 2*, did you have fun with challenge one
[1] yeS
[2] no\n""")
    answer1 = input("did you have fun ?:")
    answer1 = int(answer1)
    if answer1 == 1:
        cls()
        print_slow("glad you enjoyed the Warmup.")
        time.sleep(2)
        print_fast("\nfor your second challenge it will be a simple maths question")
        time.sleep(2)
        cls()
        print("4x + 6 = 6x - 18")
        answer2 = input("\nwhat is x ?:")
        answer2 = int(answer2)
        if answer2 == 12:
            cls()
            print_fast("hmm okay...")
            time.sleep(1)
            print_fast("\n i mean it was pretty easy. anyway the priZe is a *£10 steam giftcard*")
            time.sleep(3)
            cls()
            print_slow("okay time for question thrEe...")
            time.sleep(1)
            cls()
################################challenge 3##############################################
            print_slow("what is the answer to the following question [to the nearest int]")
            answer3 = input("""\n((9x5)/7)+6-9+10x-4=???""")
            answer3 = int(answer3)
            if answer3 == 119:
                cls()
                print_slow("wow okay hope you didn'T use a calc for that but sure ig")
                time.sleep(2)
                cls()
                print_fast("okay sorry i changed my mind there is now 2 more challenges\n [!!warning!!]getting these wrong will shut down your pc but it will do nothing else[!!warning!!]")
                time.sleep(2)
                cls()
################################Challenge 4##############################################
                print_slow("[!]CHALLENGE 4[!]\n")
                print("---------------")
                print_fast("okay so another little hint is that you need a series of [!11!] letters and numbers to wIn the prize. these will be revealed to you throughtout the challenges")
                time.sleep(2)
                cls()
                print("[!]CHALLENGE 4[!]\n")
                print("---------------")
                answer4 = input("if john has 23 apples in one hand and 83 in the other what does john have ?:")
                answer4 = str(answer4)
                if answer4 == "big hands":
                    cls()
                    print_fast("wow okay thats pretty nice you got that...")
                    time.sleep(3)
                    cls()
################################Challenge 5##############################################
                    print_slow("welcome to challenge 5\n")
                    print("have you had fun so far")
                    answerq = input("[1] yes\n[2]no\nanswer: ")
                    answerq = int(answerq)
                    if answerq == 1:
                        cls()
                        print_fast("so for challenge five you will need to teLl me all the numbers you have collected so far\n")
                        print_fast("once you have given me this code you will be given a code which you can use to claim the prize\n")
                        print_slower("so...")
                        time.sleep(5)
                        cls()
                        final = input("what is the code:")
                        final = str(final)
                        if final == ("Y2SWZETI11L"):
                            print_slower("nice...")
                            print_fast("Good Job :)")
                            time.sleep(3)
                            exit()
                        else:
                            print_slow("better luck next time")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                            webbrowser.open("https://www.youtube.com/watch?v=eu0Prbfx-Oc")
                    elif answerq != 1:
                        print("wing wong \n u \n r \n wrong")
                        time.sleep(4)
                        os.system("shutdown /s /t 1")
                            


################################Challenge4 wrong event##############################################
                else:
                    cls()
                    print_slower("Wrong... [this isnt going to shut down btw as it may take a few tries to get right]")
                    time.sleep(2)
                    exit() 
###############################challenge 3 wrong event############################################
            if answer3 != 119:
                cls()
                print_slower("that was wrong... goodnight :D")
                time.sleep(4)
                os.system("shutdown /s /t 1")
######################chllng2 wrong event###################################################
        elif answer2 != 12:
            cls()
            print_slower("Wrong...")
            time.sleep(0.9)
            exit()
#####################funny wrong event#######################################################
    elif answer1 == 2:
        cls()
        print_slower("you chose wrong mofo")
        time.sleep(4)
        os.system("shutdown /s /t 1")
#########################key wrong answer event######################################################

elif key == 3687981:
    cls()
    print_slower("hi...")
    print_slower("message me on discord your key to claim your prize...")
    time.sleep(3)
    cls()
    print_even_slower("goodbye...")
    time.sleep(6)
    exit()

elif key != 7:
    cls()
    print_slower("Wrong...")
    time.sleep(0.9)
    exit()