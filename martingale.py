# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:25:16 2020

@author: pavel_000
"""

# monte carlo - roulette martingale strategy simulation

import numpy as np

min_bet = 1
win_multiple = 2
bet_multiple = 2


def odd_even(draw):
    odd_even = str("")
    if draw % 2 == 1: odd_even = "odd"
    return odd_even

def pl(draw, bet_amount, win_multiple = 2, type_bet = 'odd_even', bet = 'odd'):
    if type_bet == 'odd_even':
        if odd_even(draw) == 'odd':
            pnl = bet_amount * win_multiple
        else: pnl = -bet_amount
    return pnl

import pandas as pd

goal_profit = 1000
bankruptcy = -1000

rounds =  10



np.random.seed(0)

scorecard = pd.DataFrame(index = range(1, rounds + 1), columns = ['draw', 'bet', 'PL'])
scorecard.iloc[0]['bet'] = min_bet

for i in range(0, 10):
    draw = np.random.randint(0, 37)
    if not scorecard.iloc[i-1]['PL'] < 0:
         scorecard.iloc[i]['bet'] = min_bet
    else:
         scorecard.iloc[i]['bet'] = scorecard.iloc[i-1]['bet'] * bet_multiple 
    
    scorecard.iloc[i]['draw'] =  draw
    scorecard.iloc[i]['PL'] = pl(draw, scorecard.iloc[i]['bet']) + (0 if np.isnan(scorecard.iloc[i-1]['PL']) else scorecard.iloc[i-1]['PL']) 
    
scorecard 


