# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:38:45 2021

@author: emann
"""
from scipy.spatial import distance
def euclidian_distance(point1,point2):
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
        euclidean distance between two points.

    '''
    print(distance.euclidean(point1, point2))
    return distance.euclidean(point1, point2)