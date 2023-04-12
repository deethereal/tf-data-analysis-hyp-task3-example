import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 264956206  # Ваш chat ID, не меняйте название переменной
alpha = 0.06


def solution(x, y) -> bool:
    # Проверяем равенство дисперсий выборок
    p_value = ttest_ind(x, y).pvalue
    return p_value < alpha
