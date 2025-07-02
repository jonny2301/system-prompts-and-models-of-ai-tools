from dataclasses import dataclass
from typing import Iterable, List

@dataclass
class Issue:
    id: int
    title: str

@dataclass
class LinearTask:
    id: int
    title: str
    issue_id: int


def sync_issues(issues: Iterable[Issue]) -> List[LinearTask]:
    tasks: List[LinearTask] = []
    for issue in issues:
        tasks.append(LinearTask(id=issue.id, title=issue.title, issue_id=issue.id))
    return tasks
