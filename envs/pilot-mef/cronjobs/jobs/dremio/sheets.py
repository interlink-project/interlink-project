
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_dict({
  "type": "service_account",
  "project_id": "interlink-deusto",
  "private_key_id": "d92f5cdc7a80cf76bd7b0f7733d3343ab16cba32",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDW/hXd9Qum1UTz\n/KGfjPdsdSUV2b4XE0t6DTseGt3eK8CzlqlqouseP7/AWe3IMuSmxTh7Tako3C4f\nS51GHgAI+Lv1oB9mK5kD70H9xryt8vRo+ET5mgZ7YrIvNmUqBBwfURofb7ik17zc\nacAD55qQYNeLPRYWFuoyCrXMkiF3rWRyZGyJDGzIJil6fDMsrpIQVbl7RdKZUWWB\nfBnNC1m7VfuPF/izuf68i6iOBovNIKcZiKVkVypm75WSwAmw+WdiyoF8SuJXy/EJ\npoYsonjoqcIjyshwGaHwpaKZWLLUK8iIawaT90FWN7HFuhXbOBQa0sWiYK4ismdc\nIOUNWTbNAgMBAAECggEADdj4lTIVYAq++Dm+oN8DIl861kXbsozLNCW20XrIugJD\nbs3QRIGqqmlP80m99EK8hRyRRY/il2Xz91wQpm8d1w+xiGHNFyQAi3pVQjOsyRKr\n0p8H6LPJ1LF7HJz6T+x+Pmrw4P/gx4bsL544Ge6u/yGqgHNpmsUH39VExG2dIW7r\nBAKwMx0CB4BmvswPd6b66hTVKmKPu5jB1e3FNwbeRWo+D/8K+6/7DBJcj0Fnor+a\n+6SmsIlXjF/LrLWmNMUWOhQ/VRKh5J5d7XkDAwlBvIruU3JhEjkq2fuAd3d7WEfG\nMEangfsgNV65yFiZV7xMAsP+ICQ54/90MBGsmjkLGQKBgQDvvEyT30heG3XIfi28\ntccRZkSTy9bKH0KfrzANvvZSbCqdaXu3+EBDmcUVRmSQQYzhQ833pvsJUpDSkLWw\nIyTE+iRs331v33DJ5I59Yq3QhMAZUUlntcGoRqe7z6ev6dAn0hEdvvIaGuo1BED2\nWUmjsS4se5SzNLHdaHhE4CFnMwKBgQDllA1amo4ojT+DaJJlEHUvuNsSeLLmuT7j\nNJeXa5f4UxenLL+Di2Kd2kdTTyF60f9HTLDbqWrfjOCv9WsiXWF3pKKyHZ4JNZrr\nbiC2uC6jI2rbKPfsCD9cRyQneZ4EKsTnz5oJsChEoIyvAL2NCeXd8rpBbLZ2APan\nhw/ODkLp/wKBgEGB/prZhHjSoBitAepy8XZ7r3mDVandaOMhh8v5xm03SV3CGSBo\nIYdXWVc66PfSMaDMWle1tRsTCKfBCySaNc3tXE6zsx8Cu1svrQ/uCvjTjXpdj+Va\n8RP+Wo8javrStSJscGjkaFthx2W9R9MJCupD3A4jprphR8jsZxDK/dWpAoGAVwPu\nq9C44RXoZN5V3oiGYjgmkLG+3USJWYStkG7vgue7p1mGnU1Pa5U4Q5NSlULTBytC\nPX/RSjoTT54tpTDPqJF2ORyQsdzngySSsa7NvnfGIJs+nO/jVA6C3ZNzGRE84MAH\nGnTyTlCsAgi9z59YyO8fOX0DC2cCFi1TCD7PjfECgYEAsdpQ2BIGOuz3NKLzzLwA\nS76ANqJZfLQMeZ/8qiDWDlaGTiwIahV9WtEYPY7tr1vIXKA6znC0iHrYzP5Fkvi/\n3o2UkAF/6Crf9tOzEahsHQSm8242YwGtB8g1KJF5ZnjA/fg1u0wEnJuiLTS6UEav\nCKGdcHJR2t5I//qz3IYmXmg=\n-----END PRIVATE KEY-----\n",
  "client_email": "kpis-106@interlink-deusto.iam.gserviceaccount.com",
  "client_id": "116674489579363548648",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/kpis-106%40interlink-deusto.iam.gserviceaccount.com"
}
, SCOPES)


service = build('sheets', 'v4', credentials=credentials)
driveservice = build('drive', 'v3', credentials=credentials)

sheet_id = "1WDA5hatG7NLCzBTpIoVFM_yiRU_Nn6kTsbeYyPXs03A"
if not sheet_id:
    spreadsheet = {
        'properties': {
            'title': "KPI results"
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
    user_permission = {
            'type': 'anyone',
            'role': 'writer',
        }
    perm = driveservice.permissions().create(
            fileId=spreadsheet.get('spreadsheetId'),
            body=user_permission,
            fields='id',
        ).execute()

    sheet_id = spreadsheet.get('spreadsheetId')