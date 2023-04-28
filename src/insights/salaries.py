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
    try:
        min_salary, max_salary = verify_values(job)
    except ValueError:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError("O 'min_salary' deve ser menor que o 'max_salary'")

    return min_salary <= verify_salary(salary) <= max_salary


def verify_values(job: Dict) -> Dict:
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError("'min_salary' e 'max_salary' estão ausentes em job")
    verify_salary_type(job)
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
    except ValueError:
        raise ValueError("'min_salary' ou 'max_salary' não tem valor numerico")

    return [min_salary, max_salary]


def verify_salary(salary: Union[int, str]):
    if not isinstance(salary, (int, str)):
        raise ValueError('tipo invalido')
    try:
        return int(salary)
    except ValueError:
        raise ValueError("O 'salary' deve ser numero")


def verify_salary_type(job: Dict):
    if not isinstance(job['min_salary'], (str, int)):
        raise ValueError('tipo invalido')
    if not isinstance(job['max_salary'], (str, int)):
        raise ValueError('tipo invalido')


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
