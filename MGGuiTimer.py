# Copyright @ 2018 Michael George
#
# MGGuiTimer.py - a simple timer class
#   2018-12-19 add the callback arg; just for example and maybe we can use a caller uniqueness id
#          add the basic main routine so this will run as a stand-alone demo 
#
import time
from threading import Event, Thread

# create a timer to call a user function at interval
class mgGuiTimer():

  """Repeat `function` every `interval` seconds."""
  #the timer thread instance initialization
  #  (interval is the timer interval in SECONDS)
  #  (function is the caller's entry point called each interval event)
  #  (args is a simple list of arguments)
  #  (kwargs is a key-value list of arguments)
  def __init__(self, interval, function, *args, **kwargs):
      self.interval = interval
      self.function = function
      self.args = args
      self.kwargs = kwargs
      # here is an example of reference to kwargs items using .get() 
      self.guitag = kwargs.get('callbackid') # remove this for production
      self.start = time.time()
      self.event = Event()
      self.thread = Thread(target=self._target)
      self.thread.start()

  # the timer thread worker function executes the caller-supplied callback function
  def _target(self):
      while not self.event.wait(self._time):
          self.function(*self.args, **self.kwargs)

  # do some math to perpetually compute 10 second interval from real time
  @property
  def _time(self):
      return self.interval - ((time.time() - self.start) % self.interval)

  #timer thread stop() method
  def stop(self):
      self.event.set()
      self.thread.join()

if __name__ == '__main__':
    from tkinter import Tk

    #callback registered in the timer instance
    #
    def timercallback(args, kwargs):
      # just print the args to the standard output for this example
      print( kwargs.get('callbackid'), kwargs.get('c1'))
      for i in yyy:
        print (i)

    # main program example to   
    myroot = Tk()
    myroot.title( "MGTimer-3.10-001-122118")

    # the keyword args for this example
    xxxx = {'callbackid':999,'c1':888}
    # the list args for this example
    yyy = [ 1, 2, 3, 4 ]
    # create the timer instance 10 seconds interval
    mytimer = mgGuiTimer(10, timercallback, yyy, xxxx)
    # standard tkinter main loop
    myroot.mainloop()
    #cleanup some of the key runtime elements when the main win exits 
    mytimer.stop()
    mytimer = None


