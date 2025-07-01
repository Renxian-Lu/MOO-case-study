from pymoo.indicators.hv import HV
from pymoo.indicators.igd import IGD
from pymoo.problems import get_problem
import numpy as np

def hv(F):
    """Calculate hypervolume indicator"""
    ref = np.array([1.2] * F.shape[1])
    hv_indicator = HV(ref_point=ref)
    return hv_indicator(F)

def igd(F, prob_name):
    """Calculate IGD indicator"""
    problem = get_problem(prob_name, n_var=10, n_obj=3)
    true_pf = problem.pareto_front()
    igd_indicator = IGD(true_pf)
    return igd_indicator(F)