#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sched
import time
import logging
import subprocess
from threading import Timer

class ScreensaverDummy():
    def initialiseTimer(self):
        pass

    def resetTimer(self):
        pass

    def close(self):
        pass

    def show(self):
        pass

    def disable(self):
        pass

class Screensaver(ScreensaverDummy):
    def __init__(self, idletime, directory):

        self.directory = directory
        self.idletime = idletime
        self.process = ""
        #self.scheduler = sched.scheduler(time.time, time.sleep)
        self.scheduler = ""

    def initialiseTimer(self):

        logging.debug("Initialising screensaver")
        #self.scheduler.enter(int(self.idletime), 1, self.show, ())
        #self.scheduler.run()
        self.scheduler = Timer(int(self.idletime), self.show,())
        self.scheduler.start()

    def resetTimer(self):

        logging.debug("Resetting screensaver timer")
        try:
           # self.scheduler.cancel(self.scheduler)
            self.disable()

        except:
            logging.warning("Screensaver timer could not be reset")

        finally:
            self.initialiseTimer()

    def close(self):

        logging.debug("Closing screensaver")
        try:
            self.process.kill()
        except:
            logging.warning("Screensaver could not be closed")

    def show(self):

        logging.debug("Showing screensaver")
        command = "feh -Y -x -q -D 5 -B black -F -Z -z " + str(self.directory)
        self.process = subprocess.Popen([command])

    def disable(self):
        logging.debug("Closing all screensaver scheduled events")
        #list(map(self.scheduler.cancel, self.scheduler.queue))
        self.scheduler.cancel()
