
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


creds = None
spreadsheet_id='1Sz00iYvI81OjCAj2hKDvmJfzZqLhhkmb-XSJyIVwJp0'
name='Data!A:A'
age='Data!B:B'
place='Data!C:C'

flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('sheets', 'v4', credentials=creds)


result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=name).execute()
name_val = result.get('values', [])

result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=age).execute()
age_val = result.get('values', [])

result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=place).execute()
place_val = result.get('values', [])

data = [
    {
        'range': 'Name!A:A',
        'values': name_val
    },
]
body = {
    'valueInputOption': 'RAW',
    'data': data
}
result = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

data = [
    {
        'range': 'Age!A:A',
        'values': age_val
    },
]
body = {
    'valueInputOption': 'RAW',
    'data': data
}
result = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()


data = [
    {
        'range': 'Place!A:A',
        'values': place_val
    },
]
body = {
    'valueInputOption': 'RAW',
    'data': data
}
result = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
