import time
current_time = time.strftime("%H:%M:%S")
work_star_time = '09:00:00'
work_end_time='17:00:00'

total_water= 3500
glass_capacity = 200
no_of_glass= round(total_water/glass_capacity)
total_time  = 8*60*60
waiting_time =  total_time/no_of_glass


from pygame import mixer
mixer.init()  # Initialzing pyamge mixer


def getdate():
    import datetime
    return datetime.datetime.now()

def eye_exercise():
    print("This your eye exercise time")
    mixer.music.load('C:\\Users\\DEVENDRA\\Downloads\\doraemon.mpeg')  # Loading Music File
    mixer.music.play()  # Playing Music with Pygame
    mytext = input("Enter ""EYdone"" to stop the music").lower()
    if mytext == 'eydone':
        f = open("Eyes_exercise" + ".txt", "a")
        f.write("[" + str(getdate()) + "]:" + mytext + "\n")
        f.close()
        mixer.music.stop()
        print("Thank you!")
        time.sleep(1800)

def water_exercise():
    print("This your water dinking time")
    mixer.music.load('C:\\Users\\DEVENDRA\\Downloads\\doraemon.mpeg')  # Loading Music File
    mixer.music.play()  # Playing Music with Pygame
    mytext = input("Enter ""drank"" to stop the music").lower()
    if mytext == 'drank':
        f = open("water_drinking" + ".txt", "a")
        f.write("[" + str(getdate()) + "]:" + mytext + "\n")
        f.close()
        mixer.music.stop()
        print("Thank you!")
        time.sleep(waiting_time)


def physical_exercise():
    print("This your pyhsical exercise time")
    mixer.music.load('C:\\Users\\DEVENDRA\\Downloads\\doraemon.mpeg')  # Loading Music File
    mixer.music.play()  # Playing Music with Pygame
    mytext = input("Enter ""Exdone"" to stop the music").lower()
    if mytext == 'exdone':
        f = open("physical_exercise" + ".txt", "a")
        f.write("[" + str(getdate()) + "]:" + mytext + "\n")
        f.close()
        mixer.music.stop()
        print("Thank you!")
        time.sleep(2700)


if __name__ == '__main__':

    print("Welcome to the healthy programmer scheduled")
    print("music will be play for water, Eyes and physical health")

    glass=0
    print("For water song will play in every 1 hour from 9 to 5 ans starts from 9")
    while (work_star_time != work_end_time):
         if (work_star_time>=current_time) and (current_time<=work_end_time):
             if glass == 18:
                 pass
             else:
                 glass+=1

             water_exercise()
             eye_exercise()
             physical_exercise()


