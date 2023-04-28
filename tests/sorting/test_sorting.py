from src.pre_built.sorting import sort_by


list_jobs = [
    {"min_salary": 1120, "max_salary": 2150, "date_posted": "2023-04-27"},
    {"min_salary": 2100, "max_salary": 3820, "date_posted": "2027-04-27"},
    {"min_salary": 5350, "max_salary": 8000, "date_posted": "2013-04-27"},
]
sort_by_max_salary = [
    {"min_salary": 5350, "max_salary": 8000, "date_posted": "2013-04-27"},
    {"min_salary": 2100, "max_salary": 3820, "date_posted": "2027-04-27"},
    {"min_salary": 1120, "max_salary": 2150, "date_posted": "2023-04-27"},
]
sort_by_min_salary = [
    {"min_salary": 1120, "max_salary": 2150, "date_posted": "2023-04-27"},
    {"min_salary": 2100, "max_salary": 3820, "date_posted": "2027-04-27"},
    {"min_salary": 5350, "max_salary": 8000, "date_posted": "2013-04-27"},
]
sort_by_date_posted = [
    {"min_salary": 2100, "max_salary": 3820, "date_posted": "2027-04-27"},
    {"min_salary": 1120, "max_salary": 2150, "date_posted": "2023-04-27"},
    {"min_salary": 5350, "max_salary": 8000, "date_posted": "2013-04-27"},
]


def test_sort_by_criteria():
    sort_by(list_jobs, 'max_salary')
    assert list_jobs == sort_by_max_salary
    sort_by(list_jobs, 'min_salary')
    assert list_jobs == sort_by_min_salary
    sort_by(list_jobs, 'date_posted')
    assert list_jobs == sort_by_date_posted
