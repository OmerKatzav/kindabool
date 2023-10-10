from kindabool import *  # usually a bad idea, but its kinda essential to the library


if True:
    print("This will always be printed")

if KindaTrue:
    print("This has a 75% chance of being printed")

if Neutral:
    print("This has a 50% chance of being printed")

if KindaFalse:
    print("This has a 25% chance of being printed")

if False:
    print("This will never be printed")

if kindabool.kinda_bool.KindaBool(1):  # constructor takes an int from 1-5
    print("This will never be printed")
