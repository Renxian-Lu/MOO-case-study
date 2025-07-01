import numpy as np, pandas as pd, pathlib, tqdm
from pymoo.optimize import minimize
from src.problems.dtlz_wrappers import get_dtlz
from src.algorithms.nsga2_cfg import nsga2
from src.algorithms.smsemoa_cfg import smsemoa
from src.utils.hv_tools import hv, igd
from pymoo.indicators.hv import HV

PROBLEMS = ["dtlz1", "dtlz2", "dtlz4"]
ALGOS = {"NSGA2": nsga2, "SMS_EMOA": smsemoa}
RUNS = 30
SEEDS = np.arange(RUNS)

root = pathlib.Path(__file__).resolve().parents[2] / "results"

records = []
for prob in PROBLEMS:
    problem = get_dtlz(prob)
    for name, get_algo in ALGOS.items():
        for seed in tqdm.tqdm(SEEDS, desc=f"{prob}-{name}"):
            res = minimize(
                problem,
                get_algo(),
                seed=int(seed),
                save_history=True,
                verbose=False
            )

            F = res.F
            hv_val = hv(F)
            igd_val = igd(F, prob)

            # Save per-run Pareto front
            np.savez(root / "raw" / f"{prob}_{name}_{seed}.npz", F=F)

            # Save convergence HV history
            hv_ref = [1.2] * problem.n_obj
            hv_calc = HV(ref_point=hv_ref)
            hv_hist = [
                hv_calc(gen.opt.get("F"))
                for gen in res.history
            ]
            np.savez(root / "raw" / f"{prob}_{name}_{seed}_hv_hist.npz", hv_hist=hv_hist)

            # Record summary indicators
            records.append({
                "problem": prob,
                "algo": name,
                "seed": int(seed),
                "HV": hv_val,
                "IGD": igd_val
            })

# Save full summary table
summary_path = root / "indicators" / "summary.csv"
summary_path.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(records).to_csv(summary_path, index=False)
