import pygds
import numpy as np
import asyncio
import time

from multiprocessing import Process,Queue,Pipe

class inputheadset:
    def __init__(self) -> None:
        pass
    
    def initializegds():
            d = pygds.GDS()
            return d
   
    def readInputData(d):
    
      t_end = time.time() + 60                                                              
      d.TriggerEnabled == d.Trigger
      d.Trigger = True
      d.SetConfiguration()

      for c in d.Configs:
       c.Trigger = True
      d.SetConfiguration()
      d.SamplingRate = 500
      w = True
      while time.time() < t_end:
        a = d.GetData(d.SamplingRate)
        res=[]
        res.append(a)
        return a

  
      print(a,len(a))

        

    

    d = pygds.GDS()
   # d =initializegds()
    readInputData(d)

    