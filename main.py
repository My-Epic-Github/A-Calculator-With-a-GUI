import operator
import numexpr
import math
import PySimpleGUI as sg



def sqr(args : float):
    out = math.sqrt(args)
    return out
def add(args):
    return add(args)
def percent(args):
    return


layout = [[sg.Input(key='in', size=31)],
          [sg.ReadFormButton('C'), sg.ReadFormButton('√')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('+')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('/')]
          ]

window = sg.FlexForm('CALCULATOR', default_button_element_size = (5, 2), auto_size_buttons = False, grab_anywhere = False, resizable=False)
window.layout(layout)

current_num = []
full_operation = []


while True:
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
        window['in'].update('')
        full_operation = []

    elif button == '√':
        sqrt = values['in']
        res = float(sqrt)
        res = sqr(res)
        window['in'].update(res)




