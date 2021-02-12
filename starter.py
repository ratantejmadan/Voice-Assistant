import ssl
import wolframalpha
import PySimpleGUI as sg
import wikipedia

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

app_id = 'AV5G74-8J4QU9WL9Q'
client = wolframalpha.Client(app_id)

sg.theme('DarkTeal4')
layout = [[sg.Text("What answers do you seek little one?")],
          [sg.Input(key='question')], [sg.Button('Seek'), sg.Button('Quit'),
                                       sg.Button('Clear')],
          [sg.Text(size=(40, 3), key='output')]]

window = sg.Window('Ultron', layout)

while True:
    event, values = window.read()

    if event in (None, 'Quit'):
        break

    if event == 'Clear':
        window['question']('')

    res = client.query(values['question'])

    window['output'].update(next(res.results).text)

window.close()
