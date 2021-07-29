# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:55:20 2021

@author: emann
"""

def is_pangram(user):
    '''
    

    Parameters
    ----------
    user : String
        Receives the string to compare

    Returns
    -------
    Boolean: True
        if string is pangram
        else false
        

    '''
    
    check=""
    flag=True
    check=("abcdefghijklmnopqrstuvwxyz")
    user=user.lower()
    for char in check:
        if char not in user:
            flag=False
    return flag