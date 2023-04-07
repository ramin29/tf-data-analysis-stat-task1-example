import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
  
    qrr = np.ndarray(1000)  # range like только в numpy
    lst = list(range(1000))
    
    t = 10
    a = qrr/t

    a_m = np.mean(a)
    o = 1/a_m
    return x.mean() # Ваш ответ
