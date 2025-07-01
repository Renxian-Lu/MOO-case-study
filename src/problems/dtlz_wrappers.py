from pymoo.factory import get_problem

def get_dtlz(name: str, n_var: int = 10, n_obj: int = 3):
    """Return a DTLZ problem instance with the study-case spec."""
    return get_problem(name.lower(), n_var=n_var, n_obj=n_obj)