import xlrd


def xls_read(file_name):
    cep_list = []
    excel_file = xlrd.open_workbook(file_name)
    sheet_name = excel_file.sheet_by_index(0)
    for row in range(1, sheet_name.nrows):
        cep = sheet_name.cell_value(rowx=row, colx=1)
        cep_list.append(str(int(cep)))
    return cep_list
