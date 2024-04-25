"""
Простейший код для чтения данных из Google Sheets.
Для авторизации необходим:
1. Сервисный аккаунт Google Cloud
2. ID таблицы
3. Идентификатор пользователя из Google Cloud для разрешения доступа к таблице

Авторы: Happy Python
Сайт: https://happypython.ru
Telegram: https://t.me/happypython_team
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dotenv
import os

# Загрузка переменных окружения из .env файла
dotenv.load_dotenv()

# Получение значений переменных из .env файла
credentials_file = os.getenv('CREDENTIALS_FILE')
spreadsheet_id = os.getenv('SPREADSHEET_ID')
sheet_name = os.getenv('SHEET_NAME')
data_range = os.getenv('DATA_RANGE')

# Объект авторизации
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key(spreadsheet_id)
sheet = spreadsheet.worksheet(sheet_name)
data = sheet.get(data_range)
for row in data:
    print(row)