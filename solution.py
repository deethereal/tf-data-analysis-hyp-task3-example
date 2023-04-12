import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 264956206  # Ваш chat ID, не меняйте название переменной
alpha = 0.06


def solution(x, y) -> bool:
    # Проверяем равенство дисперсий выборок
    var_x = np.var(x)
    var_y = np.var(y)

    # Выполняем t-тест
    t_stat, p_val = ttest_ind(x, y, equal_var=var_x == var_y)

    # Сравниваем p-значение с уровнем значимости
    return p_val < alpha  # Не отклоняем нулевую гипотезу
