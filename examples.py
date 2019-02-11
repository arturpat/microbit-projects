##########################################################################
# This is an example of distance measuring function. Due to micropython  #
# limitations it's not scaled perfectly to any units (the function       #
# returns cm-ish result). Feel free to modify it as needed or write the  #
# new one from scratch.                                                  #
#                                                                        #
# To configure PyCharm you will need MicroPython plugin from official    #
# PyCharm repo. All you need to do is enable it in settings later, it    #
# will do all the micro:bit magic for you.                               #
# Hint 1: To see the distance measurements you can use neo pixels and    #
#         light them up accordingly the shorter the distance.            #
# Hint 2: The slower you move, the more accurate the distance reading.   #
# Hint 3: The lowest distance I managed to measure was '4'.              #
#                                                                        #
# The code has been created with a lot of help from the BitBot producer, #
# 4tronix. Thanks Gareth!                                                #
##########################################################################


from microbit import *

sonar = pin15


def get_distance():
    start = running_time()
    for i in range(100):
        sonar.write_digital(1)  # Send 10us pulse to trigger
        sleep(0.01)  # sleep will not sleep less then 6ms, that's why we need to average out of multiple measurements
        sonar.write_digital(0)
        while sonar.read_digital() == 1:
            pass
    stop = running_time()
    elapsed = (stop - start - 16) / 3.77
    distance = int(elapsed)
    return distance
