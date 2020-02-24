import os
import datetime
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from data_parse import main as main_data_parse
from leads_from_inst import main as main_leads_from_inst
from dotenv import load_dotenv
load_dotenv()


def ceonnect_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('json_keyfile'), scope)
    client = gspread.authorize(creds)
    sheet = client.open(os.getenv('name_sheet')).sheet1
    return sheet


def getyesterday():
    today = datetime.now()
    yesterday = today + timedelta(days=-1)
    if yesterday.day < 10:
        day = '0' + str(yesterday.day)
    else:
        day = str(yesterday.day)
    if yesterday.month < 10:
        month = '0' + str(yesterday.month)
    else:
        month = str(yesterday.month)
    yesterday_correct = day + '.' + month + '.' + str(yesterday.year)
    # print('yesterday_correct', yesterday_correct)
    return yesterday_correct


def main():
    sheet = ceonnect_google_sheets()
    search = sheet.find(getyesterday())
    final_val, final_cost, final_doc, fb_result, final_leads = main_data_parse()
    date = getyesterday()
    row_col1 = sheet.update_cell(int(search.row), int(search.col) + 1, str(final_val))
    row_col2 = sheet.update_cell(int(search.row), int(search.col) + 2, str(final_cost))
    row_col3 = sheet.update_cell(int(search.row), int(search.col) + 3, str(fb_result))
    row_col4 = sheet.update_cell(int(search.row), int(search.col) + 4, str(final_doc))
    row_col5 = sheet.update_cell(int(search.row), int(search.col) + 5, str(final_leads))
    print('Данные по Beautymarket успешно записаны в таблицу. Дата: ', date)
    print('Выручка', str(final_val), '\nСебестоимость', str(final_cost),
          '\nЗатраты по рекламе', str(fb_result), '\nКоличество покупок', str(final_doc),
          '\nКоличество диалогов', str(final_leads))

if __name__ == '__main__':
    main()