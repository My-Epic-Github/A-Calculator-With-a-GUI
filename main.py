import operator
import numexpr
import math
import PySimpleGUI as sg
import winshell, win32com.client, os
import output


theme = sg.theme('DarkGray11')
desk = winshell.desktop()
def sqrt(args : float):
    out = math.sqrt(args)
    return out
def add(args):
    return add(args)
def sin(args):
    return math.sin(args)

path = os.path.join(desk, 'Calculator.lnk')
target = f'{desk}\A-Fucking-Calculator-With-a-GUI\dist\Calculator.exe'
icon = f'{desk}\A-Fucking-Calculator-With-a-GUI\dist\Calculator.exe'

shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()


layout = [[sg.Input(key='in', size=31)],
          [sg.ReadFormButton('C'), sg.ReadFormButton('√'), sg.ReadFormButton('x²'), sg.ReadFormButton('**')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('+')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('/')]
          ]

window = sg.Window('Calculator', default_button_element_size = (5, 2), auto_size_buttons = False, grab_anywhere = False, resizable=False, use_custom_titlebar=True, titlebar_background_color='black', titlebar_text_color='white', titlebar_icon=output.icon)
window.layout(layout)

current_num = []
full_operation = []


while True:
    try:
        button, values = window.read()

        if button == sg.WINDOW_CLOSED:
            break

        if button in ['0', '1', '2', '3', '4', '5', '6', '7' , '8', '9', '.']:
            current_num.append(button)
            num_string = ''.join(current_num)
            window['in'].update(num_string)


        if button in ['+', '-', '*', '/']:
            full_operation.append(''.join(current_num))
            current_num = []
            e = full_operation.append(button)
            window['in'].update(e)


        if button == '=':
            full_operation.append(''.join(current_num))
            result = eval(''.join(full_operation))
            window['in'].update(result)
            full_operation = []


        elif button == 'C':
            full_operation = []
            current_num = []
            window['in'].update('')


        elif button == '√':
            sqr = values['in']
            sqr = float(sqr)
            window['in'].update(float(sqrt(sqr)))
            full_operation = []

        elif button == 'x²':
            srq = values['in']
            srq = float(srq)
            window['in'].update(srq**2)

        elif button == '**':
            full_operation.append(''.join(current_num))
            current_num = []
            e = full_operation.append(button)
            window['in'].update(e)
    except Exception as e:
        sg.popup_error(e)






