
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info({
    "type": "service_account",
    "project_id": os.environ.get("KPIS_GOOGLE_PROJECT_ID"),
    "private_key_id": os.environ.get("KPIS_GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.environ.get("KPIS_GOOGLE_PRIVATE_KEY_ID"),
    "client_email": os.environ.get("KPIS_GOOGLE_CLIENT_EMAIL"),
    "client_id": os.environ.get("KPIS_GOOGLE_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get("KPIS_GOOGLE_CLIENT_X509"),
    "universe_domain": "googleapis.com"
})
credentials = credentials.with_scopes(SCOPES)

service = build('sheets', 'v4', credentials=credentials)
driveservice = build('drive', 'v3', credentials=credentials)

sheet_id = os.environ.get("KPIS_SHEET_ID")
if not sheet_id:
    spreadsheet = {
        'properties': {
            'title': "KPI results"
        }
    }
    spreadsheet = service.spreadsheets().create(
        body=spreadsheet, fields='spreadsheetId').execute()
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
