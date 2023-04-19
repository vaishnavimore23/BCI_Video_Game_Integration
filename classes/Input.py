import pygame
from pygame.locals import *
from classes.headsetInput import inputheadset
from classes.bci_processing_and_classification import Preprocessing_and_Classification
import sys
import io, os, sys, types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
import asyncio
from classes.headsetInput import inputheadset

def moveinf(movement):
    l = len(movement)
    count0 = 0
    count1 = 0
    count2 = 0
    for a in range(l):
        if movement[a] == 0:
            count0 = count0 + 1
        elif movement[a] == 1:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    if count0 > count1 and count0 > count2:
        return count0
    elif count1 > count0 and count1 > count2:
        return count1
    else:
        return count2




class Input:


    # def realTimeInput():
    #  while True:
    #    data= pc.bci_processing_and_classification.preProcessData(inputheadset.inputheadset())
    #    movement = pc.bci_processing_and_classification.predictMovement(data)
    #    return movement 
      
   
    def __init__(self, entity):
        self.mouseX = 0
        self.mouseY = 0
        
        self.entity = entity
    
    d= inputheadset.initializegds()
        
    def checkForInput(self,d):
        events = pygame.event.get()
        self.checkForKeyboardInput(d)
        self.checkForMouseInput(events)
        self.checkForQuitAndRestartInputEvents(events)

   
    
    def checkForKeyboardInput(self,d):
          pressedKeys = pygame.key.get_pressed()
          data= Preprocessing_and_Classification.preProcessData(inputheadset.readInputData(d))
          movement = Preprocessing_and_Classification.predictMovement(data)
        
          move = moveinf(movement)

     
          if move == 0 or pressedKeys[K_LEFT] or pressedKeys[K_h] and not pressedKeys[K_RIGHT]:
            self.entity.traits["goTrait"].direction = -1
          elif move == 1 or pressedKeys[K_RIGHT] or pressedKeys[K_l] and not pressedKeys[K_LEFT] :
            self.entity.traits["goTrait"].direction = 1
          elif move == 2 or  pressedKeys[K_SPACE] or pressedKeys[K_UP] or pressedKeys[K_k] :
             self.entity.traits['jumpTrait'].jump(True)
          else:
            self.entity.traits['goTrait'].direction = 0

        # isJumping = pressedKeys[K_SPACE] or pressedKeys[K_UP] or pressedKeys[K_k]
        # self.entity.traits['jumpTrait'].jump(isJumping)

          self.entity.traits['goTrait'].boost = pressedKeys[K_LSHIFT]

    def checkForMouseInput(self,events):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.isRightMouseButtonPressed(events):
            self.entity.levelObj.addKoopa(
                mouseY / 32, mouseX / 32 - self.entity.camera.pos.x
            )
            self.entity.levelObj.addGoomba(
                mouseY / 32, mouseX / 32 - self.entity.camera.pos.x
            )
        if self.isLeftMouseButtonPressed(events):
            self.entity.levelObj.addCoin(
                mouseX / 32 - self.entity.camera.pos.x, mouseY / 32
            )

    def checkForQuitAndRestartInputEvents(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and \
                (event.key == pygame.K_ESCAPE or event.key == pygame.K_F5):
                self.entity.pause = True
                self.entity.pauseObj.createBackgroundBlur()

    def isLeftMouseButtonPressed(self, events):
        return self.checkMouse(events,1)



    def isRightMouseButtonPressed(self, events):
        return self.checkMouse(events,3)


    def checkMouse(self, events, button):
        for e in events:
                if e.type == pygame.MOUSEBUTTONUP:
                    if e.button == button:
                       return True
        else:
                       return False