import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_id = "j.badiola@deusto.es"
token = "eyJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJ1X2NiNDFmMmI3LTMwYjgtNDdkMi1iNDJiLTk0YTViNDAzNTI0ZCIsInpvbmVpbmZvIjoiR01UIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9hYWMucGxhdGZvcm0uc21hcnRjb21tdW5pdHlsYWIuaXQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJqLmJhZGlvbGFAZGV1c3RvLmVzIiwibG9jYWxlIjoiZXMiLCJnaXZlbl9uYW1lIjoiSnVsZW4iLCJwaWN0dXJlIjoiaHR0cHM6XC9cL2xoMy5nb29nbGV1c2VyY29udGVudC5jb21cL2FcL0FBVFhBSndhM2pPWXRETWNfNGtmM29vTFBCeUJwT3FEaTNISkRRMGxnQWhVPXM5Ni1jIiwiYXVkIjpbImNfMGUwODIyZGYtOWRmOC00OGQ2LWI0ZDktYzU0MmE0NjIzZjFiIiwiYWFjLm9wZW5pZCIsImFhYy5wcm9maWxlIl0sIm5iZiI6MTY0MTE5ODc4MywiYXpwIjoiY18wZTA4MjJkZi05ZGY4LTQ4ZDYtYjRkOS1jNTQyYTQ2MjNmMWIiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIG9mZmxpbmVfYWNjZXNzIGVtYWlsIiwicmVhbG0iOiJpbnRlcmxpbmsiLCJleHAiOjE2NDEyNDE5ODMsImZhbWlseV9uYW1lIjoiQmFkaW9sYSBNYXJ0w61uZXoiLCJpYXQiOjE2NDExOTg3ODMsImVtYWlsIjoiai5iYWRpb2xhQGRldXN0by5lcyIsImp0aSI6ImlGQWVzM082cjUxeGR1WE94SjBuNG1pcmdOMCJ9.CPhQyQTmJa8-bvdASb7Vfre9U62igYhjJ6fKPp0CiYglTGai3Y-s2Bh5IGz9pLek0Qnjz-t9zRdSOo9Z7QjJcg4paAnn4c2YKD1U3MZHpTuDZMPAy2V62s2BJetzw2bg0__3Cas5jYd1zebxQg7wGZPOEO0fJ3-glxquoiE__jWwBdSpxWQ8omt0Fy3WqzKbzM0_Cqm58stwSNG3P8EV35sUcyCqn_PiAGEoQ7iyaY_jtULF8JsL-_fFD43oZtMMyLN7Vymggfm9MSTmtcZ9qjkZi3FJE_JLA1i7PQJp8C5vzzpfxxocs9mgRR6YI5rKBhpBTZBUMlJTrOAADBsdxg"
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
