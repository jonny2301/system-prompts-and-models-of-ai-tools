from ghostframe_tasks import sync_linear_issues


def test_sync_issues_creates_tasks():
    issues = [sync_linear_issues.Issue(id=1, title="Bug")]
    tasks = sync_linear_issues.sync_issues(issues)
    assert len(tasks) == 1
    assert tasks[0].issue_id == 1
    assert tasks[0].title == "Bug"
