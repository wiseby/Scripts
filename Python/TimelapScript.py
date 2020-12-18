from picamera import PiCamera
from time import sleep
import time
import os
import sys
import logging as log
import argparse

parser = argparse.ArgumentParser(
    description='Timelaps script to use PiCamera Module.'
    )

parser.add_argument(
        '-t', '--time',
        metavar='\b',
        type=float,
        default=3600.0,
        help='Timelaps duration in seconds'
        )

parser.add_argument(
        '-i', '--interval',
        metavar='\b',
        type=int, default=2,
        help='Photo interval in seconds'
        )

parser.add_argument(
        '-f',
        '--folder',
        metavar='\b',
        default='',
        help='Location to store timelaps photos'
        )

parser.add_argument(
        '--version',
        action='version',
        version='TimelapsScript 0.1'
        )

args = parser.parse_args()

log.basicConfig(filename='progress.log', level=log.INFO)

timelapsStartTime = time.time()
timelapsDuration = args.time
picInterval = args.interval
prevTime = 0.0
currentTime = 0.0
elapsedTime = 0.0
currentFilename = ''
folder = ''

if (args.folder == ''):
    folder = '{}/timelaps'.format(os.getcwd())

print(timelapsDuration)
print(picInterval)
print(folder)

if (os.path.exists('./timelaps') is False):
    os.mkdir(folder)


def Main():
    log.info('Timelap Started')
    running = True
    fileNumber = 1
    prevTime = time.time()
    while running:
        currentTime = time.time()
        elapsedTime = currentTime - prevTime
        currentFileName = 'img{}.jpeg'.format(fileNumber)
        if (elapsedTime >= picInterval):
            with PiCamera(resolution=(1920, 1080)) as camera:
                sleep(2)
                camera.capture('{}/{}'.format(folder, currentFileName))
            log.info('{} created'.format(currentFileName))
            fileNumber += 1
            prevTime = currentTime

        running = EndTimelaps()


def EndTimelaps():
    currentTime = time.time()
    totalElapsedTime = currentTime - timelapsStartTime
    if (totalElapsedTime >= timelapsDuration):
        log.info('Timelap Ended')
        log.warning(totalElapsedTime)
        return False
    else:
        return True

if(__name__ == '__main__'):

    Main()

'''
sudo mencoder -nosound -ovc lavc
-lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080
-o timelapse.avi -mf type=jpeg:fps=24 mf://@stills.txt
'''
