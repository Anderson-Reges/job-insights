from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    list_industries = list()
    for job in jobs_list:
        if not job["industry"] in list_industries and job["industry"]:
            list_industries.append(job["industry"])
    return list_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_jobs_per_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            list_jobs_per_industry.append(job)
    return list_jobs_per_industry
