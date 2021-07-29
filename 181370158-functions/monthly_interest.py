# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:05:05 2021

@author: emann
"""

def interest_monthly(balance,annual_interest_rate):
    '''
    

    Parameters
    ----------
    balance : float,int
        represents the balance of account
    annual_interest_rate : float,int
        represents the annual interest rate

    Returns
    -------
    interest monthly : float,int

    '''
    interest= balance*(annual_interest_rate/1200)
    return interest