import requests
import os
import json
import pandas as pd

JIRA_SERVER = os.environ.get("JIRA_SERVER")
HEADERS = {"Authorization": "Bearer " + os.environ.get("TOKEN")}


def search_issues(project:str):
    response = requests.get(f"{JIRA_SERVER}/rest/api/2/search?jql=project={project}&maxResults=10000",
                            headers=HEADERS)
    response.raise_for_status()
    j = response.json()
#    with open(file="out.json", mode='w') as file:
#        json.dump(j, file, indent=2)
    print("found {j['total']} issues")
    out = []
    for issue in j["issues"]:
        out.append({'id': issue['id'],
                    'key': issue['key'],
                    'FY': issue['fields']['fixVersions'][0]['name'],  # 'FY24'
                    'aggregatetimespent': issue['fields']['aggregatetimespent'],
                    'timespent': issue['fields']['timespent'],
                    'assignee': issue['fields']['assignee']['name'] if issue['fields']['assignee'] is not None else '',
                    }
                   )
    return out


def get_issue(issueID: str):
    # endpoint =""/rest/api/2/issue/{issueIdOrKey}
    # https://docs.atlassian.com/software/jira/docs/api/REST/9.14.0/#api/2/issue-getIssue
    response = requests.get(f"{JIRA_SERVER}/rest/api/2/issue/{issueID}", headers=HEADERS)
    response.raise_for_status()
    j = response.json()
    formatted_json = json.dumps(j, indent=4)
    print(formatted_json)


def get_worklog(issueID: str):
    """
    :param issueID:  issue to lookup work log
    :return: dictionary of users:hoursSpent
    """
    uri = f"{JIRA_SERVER}/rest/api/2/issue/{issueID}/worklog"
    print(uri)
    response = requests.get(uri, headers=HEADERS)
    response.raise_for_status()
    j = response.json()
    # print(json.dumps(j, indent=4))

    out = []
    for log in j['worklogs']:
        seconds = log['timeSpentSeconds']
        username = log['author']['name']
        started = log['started']
        out.append({'issue_id': issueID, 'seconds': seconds, 'username': username, 'started': started})
    return out


def create_worklog_summary(project:str):
    issues = search_issues(project)
    all_logs = []
    for issue in issues:
        logs = get_worklog(issue["key"])
        all_logs.extend(logs)

    df_work_logs = pd.DataFrame(all_logs)
    df_work_logs.to_csv(f'{project}.csv',index=False)


create_worklog_summary("CWMSPM")
create_worklog_summary("WMESPM")