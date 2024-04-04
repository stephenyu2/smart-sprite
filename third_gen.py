import pygame
import numpy as np
from sys import exit

class neural: 

    def __init__(self, mutate = .1):

        self.best_score = 0
        self.model = None
        self.mutate = mutate

    def rand_fit(self): 

        pass ## Randomly fits a NN

    def direction(self): 

        if self.model == None: 

            raise ValueError("Need to run rand_fit before calling direction")
        
        else: 
            
            return [.2, .2, .6] ## Outputs NN Results from inputs

    def next_gen(self): 

        pass ## Something about keeping best score