import gspread

gc = gspread.service_account(filename='Python Google Sheets/credentials.json') 
sh = gc.open_by_key('1dT1mkVTvXv-1fpt-2TpgsaMht-i5zVoDQTB8UGbbKr4')
worksheet = sh.sheet1

res = worksheet.get_all_records()
print(res)