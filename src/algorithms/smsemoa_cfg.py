from pymoo.algorithms.moo.sms import SMSEMOA
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.termination import get_termination

def smsemoa(pop=100):
    return SMSEMOA(
        pop_size=pop,
        sampling=FloatRandomSampling(),
        crossover=SBX(eta=15, prob=0.9),
        mutation=PM(eta=20),
        eliminate_duplicates=True,
        hv_ref_point=[1.2, 1.2, 1.2],
        termination=get_termination("n_gen", 300)
    )
