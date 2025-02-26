from zk import ZK
import xlsxwriter

conn = None
zk = ZK('192.168.1.203', port=4370, timeout=50)
try:
    print ('Connecting to device ...')
    conn = zk.connect()
    
    print(conn.get_firmware_version())

    attendances = conn.get_attendance()

    workbook = xlsxwriter.Workbook('attendance_data_table.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd HH:mm:ss'})
    day_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
    time_format = workbook.add_format({'num_format': 'HH:mm:ss'})

    print('Writing to Excel File...')

    for attendance in attendances:
        worksheet.write(row, col, attendance.user_id)
        worksheet.write(row, col + 1, 'Ahmed Huseein')
        worksheet.write(row, col + 2, 'IT')
        worksheet.write(row, col + 3, 'Web Developer')
        worksheet.write_datetime(row, col + 4, attendance.timestamp, date_format)
        worksheet.write_datetime(row, col + 5, attendance.timestamp, day_format)
        worksheet.write_datetime(row, col + 6, attendance.timestamp, time_format)
        row += 1
    
    workbook.close()
except Exception as e:
    print (f"Error message: {e}")
    print ("Process terminate")
finally:
    if conn:
        conn.disconnect()