# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:14:50 2021

@author: emann
"""
from scipy.spatial import distance
def manhattan_distance(point1,point2):
    '''
    

    Parameters
    ----------
    point1 : float,int
        represents the vectors of ponint 1 
    point2 : float,int
        represents the vectors of point 2

    Returns
    -------
    float,int
        manhattan distance between two points.

    '''
    
    return distance.cityblock(point1, point2)
    

