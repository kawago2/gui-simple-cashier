
import PySimpleGUI as sg
import pandas as pd
# add some color to the window
sg.theme('Topanga')


EXCEL_FILE = 'databases.xlsx'
df = pd.read_excel(EXCEL_FILE)


layout = [
    [sg.Text('Masukkan barang yang mau ditambahkan')],
    [sg.Text('Kode barang', size=(15, 1)), sg.InputText(key='Kode Barang')],
    [sg.Text('Nama barang', size=(15, 1)), sg.InputText(key='Nama Barang')],
    [sg.Text('Harga Satuan', size=(15, 1)), sg.InputText(key='Harga Satuan')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple Example', layout)


def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Barang Tersimpan')
        clear_input()

window.close()
