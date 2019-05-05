"""
Safe backup of all types of usb-devices.
Plug it in and start the program. All data will be stored on the server.

I have thought alot on what hardware to use and if any at all.
Maybe an RGB status led is enough with color codes for the
progress-identification. Maybe a 16x2 row LCD HAT module with buttons for
interaction?

For starters I will be monitoring the testing over ssh.

A logfile should be available so the status of the
progrma could be intercepted over an ssh session.

configuration is necessary for advanced funktions like remote backup to server
and other features.
A default backup scenario is allways configured on new devices for fast and
simple backup.

Big Steps:

-   Start program.
-   When prompted, insert device in USB-port
-   Select action from list.
-   Wait for finish.
-   When prompted unplugg device.
-   Done

Small Steps:

-   Start Program.
-   When prompted, insert device in USB-port
-   The device is compared to a list of known devices to determine default
    actions. This is accomplished using custom udev rules.
    A snapshot of /dev/ before insertion to determine name of device to use
    with udevadm info.
    A snapshot of the udev info page was taken before insertion and compared
    to one taken after insertion.
    Using dmesg for usb detection.

-   Menu Items change depending on the device in use. Has it been used before?
    The devices that is used with this program stores configurations in the
    backup directory.

-   Things to Verify:
    -   Backup destination? Remote or Locale.
    -   Adding device to be recognized as a default one?
    -   Formatting of files and type.
"""

import shutil
import subprocess
import sys
import os

global initUdev = []
global compUdev = []
global deviceInfo = []


def program():
    """ Main Program."""

    # Determine the device path.
    oldDevices = os.listdir('/dev')
    print('Insert device for backup and press any key')
    input('>>')
    newDevices = os.listdir('/dev')

    newDevices -= oldDevices
    # Search all udev attributes for the device.

    # Make an estimation on the backup size and


if(__name__="__main__"):
    program()
