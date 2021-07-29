# -*- coding: utf-8 -*-
def future_investment_value(investment_amount,monthly_interest_rate,number_of_years):
    
    '''
    Parameters 
    ----------
    investment amount : int,float,double
        represents the amount of investment
    
    monthly interest rate : int,float,doubel
        represents the monthly interest
        
    number of years : int,float,double
        represents the number of years
    
    returns
    -------
    Returns the future investment value
    
    '''
    var=(1+monthly_interest_rate)**number_of_years
    var2=var*12
    futureVal=var2*investment_amount

    return futureVal


    
    


    
