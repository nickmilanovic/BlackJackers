'''
    Card counting app used for BlackJack in online casinos to keep track of the
    running count during a black jack game. When a new deck of cards is brought in,
    reset the count to 0, and when all the cards on the table have been played, click
    the corresponding card value in the interface. A 2-6 will increase the count by
    1, a 7-9 will not increase/decrease the count, all other cards will decrease the
    the count by one. The higher the count, the higher the chances of the dealer
    busting.
'''

import PySimpleGUI as sg
import wmi


def main():
    ## Setting the font and layoug
    font = ("Arial, 20")
    count = 0
    layout = [
            [sg.pin(sg.Text("CLICK THE CARD THAT WAS JUST PLAYED"))],
            [sg.pin(sg.Text(" "))],
            [sg.pin(sg.Button("          2-6          "))],
            [sg.pin(sg.Text(" "))],
            [sg.pin(sg.Button("          7-9          "))],
            [sg.pin(sg.Text(" "))],
            [sg.pin(sg.Button("     10 J Q K A     "))],
            [sg.pin(sg.Text(" "))],
            [sg.pin(sg.Button("RESET COUNT"))],
            [sg.pin(sg.Text("The Count is {0}".format(count), font=font))],
            [sg.pin(sg.Button("QUIT"))]

    ]
    ## Create a Window object using PySimpleGui
    window = sg.Window("Black Jackers", layout)

    while True:
        ## Re rendering everytime a user clicks a button to notify user that a click wasn't missed
        event, values = window.Read()
        if event == "          2-6          ":
            count += 1
            layout = [
                [sg.pin(sg.Text("CLICK THE CARD THAT WAS JUST PLAYED"))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          2-6          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          7-9          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("     10 J Q K A     "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("RESET COUNT"))],
                [sg.pin(sg.Text("The Count is {0}".format(count), font=font))],
                [sg.pin(sg.Button("QUIT"))]
            ]
            window1 = sg.Window("Black Jackers", layout)
            window.Close()
            window = window1
        if event == "          7-9          ":
            count = count
            layout = [
                [sg.pin(sg.Text("CLICK THE CARD THAT WAS JUST PLAYED"))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          2-6          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          7-9          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("     10 J Q K A     "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("RESET COUNT"))],
                [sg.pin(sg.Text("The Count is {0}".format(count), font=font))],
                [sg.pin(sg.Button("QUIT"))]
            ]
            window2 = sg.Window("Black Jackers", layout)
            window.Close()
            window = window2
        if event == "     10 J Q K A     ":
            count -= 1
            layout = [
                [sg.pin(sg.Text("CLICK THE CARD THAT WAS JUST PLAYED"))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          2-6          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          7-9          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("     10 J Q K A     "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("RESET COUNT"))],
                [sg.pin(sg.Text("The Count is {0}".format(count), font=font))],
                [sg.pin(sg.Button("QUIT"))]
            ]
            window9 = sg.Window("Black Jackers", layout)
            window.Close()
            window = window9
        ## Reset count when fresh deck of cards is played
        if event == "RESET COUNT":
            count = 0
            layout = [
                [sg.pin(sg.Text("CLICK THE CARD THAT WAS JUST PLAYED"))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          2-6          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("          7-9          "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("     10 J Q K A     "))],
                [sg.pin(sg.Text(" "))],
                [sg.pin(sg.Button("RESET COUNT"))],
                [sg.pin(sg.Text("The Count is {0}".format(count), font=font))],
                [sg.pin(sg.Button("QUIT"))]
            ]
            window10 = sg.Window("Black Jackers", layout)
            window.Close()
            window = window10
        if event == "QUIT" or event == sg.WIN_CLOSED:
            break

    window.Close()


'''
    Added security measure to ensure functionality when a unique USB drive
    is connected. Update the SN variable with the USB drive you wish to upload to
    and uncomment lines 123-134 and comment out line 136 to use this
'''
# if __name__ == '__main__':
    # check for compatible drtive
    # SN = '4C530000160412213323'
    # c = wmi.WMI()
    # for drive in c.Win32_DiskDrive():

        # print(getattr(drive, 'PNPDeviceID'))
        # print(getattr(drive, 'SerialNumber'))

        # if 'PROD_CRUZER_BLADE&REV_1.00' in getattr(drive, 'PNPDeviceID'):
            # if SN == getattr(drive, 'SerialNumber'):
                # main()

main()
