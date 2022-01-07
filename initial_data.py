import logging
import requests
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_id = "j.badiola@deusto.es"
token = os.getenv("intertoken")
headers = {'Authorization': f'Bearer {token}'}

def main() -> None:
    print("TEAM CREATION")
    resp_team = requests.post("http://localhost/teammanagement/api/v1/teams/", headers=headers, json={
        "name": "Demo team",
        "description": "We are from eo",
        "logotype": "https://lh3.googleusercontent.com/a/AATXAJwa3jOYtDMc_4kf3ooLPByBpOqDi3HJDQ0lgAhU=s96-c",
    })
    print(resp_team._content)
    team = resp_team.json()

    print("MEMBERSHIP CREATION")
    resp_membership = requests.post("http://localhost/teammanagement/api/v1/memberships/", headers=headers, json={
        "user_id": user_id,
        "team_id": team["id"],
    })
    print(resp_membership._content)
    membership = resp_membership.json()

    print("COPROD CREATION")
    resp_coproductionprocess = requests.post("http://localhost/coproduction/api/v1/coproductionprocesses/", headers=headers, json={
        "name": "Example",
        "description": "This is a demo process 2",
        "logotype": "/static/demodata/interlinkers/slack.png",
        "team_id": team["id"],
    })

    print(resp_coproductionprocess._content)
    coproductionprocess = resp_coproductionprocess.json()

if __name__ == "__main__":
    logger.info("Creating initial data")
    main()
    logger.info("Initial data created")
