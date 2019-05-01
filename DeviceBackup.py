"""
Safe backup of all types of usb-devices.
Plug it in and strat the program. All data will be stored on the server.

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
    A snapshot of the udev info page was taken before insertion and compared
    to one taken after insertion.

-   Menu Items change depending on the device in use. Has it been used before?
    The devices that is used with this program stores configurations in the
    backup directory.

-   Things to Verify:
    -   Backup destination? Remote or Locale.
    -   Adding device to be recognized as a default one?
    -   Formatting of files and type.
"""

global initUdev = []
global compUdev = []
global deviceInfo = []
