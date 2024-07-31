
import io
import xlsxwriter

def gerarExcel(data, keys):

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    #Colunas
    for i in range(len(keys)):
        worksheet.write(0, i, keys[i])

    #Linhas
    for i in range(len(data)):
        for key, value in data[i].items():
            if key in keys:
                worksheet.write(i+1, keys.index(key), value)

    worksheet.autofit()
    workbook.close()
    output.seek(0)
   
    return output
