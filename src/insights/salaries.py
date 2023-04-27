from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    salaries = list()
    for job in jobs_list:
        if job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))
    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    salaries = list()
    for job in jobs_list:
        if job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("'min_salary' e/ou 'max_salary' ausentes")
    if not (
        str(job["min_salary"]).isdigit() and str(job["max_salary"]).isdigit()
    ):
        raise ValueError("'min_salary' e/ou 'max_salary' não são dígitos")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("'min_salary' é maior que 'max_salary'")
    if not str(salary).isdigit():
        raise ValueError("'salary' não é um dígito")
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
