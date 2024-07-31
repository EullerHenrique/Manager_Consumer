
import io
import xlsxwriter

def gerarExcel(data):
    json = data.json()

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    #Colunas
    keys = [key for key, value in json[0].items() if not isinstance(value, dict)]
    for i in range(len(keys)):
        worksheet.write(0, i, keys[i])

    #Linha
    for i in range(len(json)):
        for key, value in json[i].items():
            if not isinstance(value, dict):
                worksheet.write(i+1, keys.index(key), value)

    worksheet.autofit()
    workbook.close()
    output.seek(0)
   
    return output
