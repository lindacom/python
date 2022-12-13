# A simple script to calculate BMI
from pywebio import *
from pywebio.input import input, FLOAT, textarea
from pywebio.output import put_text, put_html, put_markdown, put_table
# from functools import partial # for buttons not working

# put_row() : Use row layout to output content. The content is arranged horizontally

#put_column() : Use column layout to output content. The content is arranged vertically

#put_grid() : Output content using grid layout

# styling .style('color: red')

def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)
    area = textarea("enter text here")
    # select = select find out how to format a select
    # checkbox = checkbox("checkbox") find out how to format
    # radio = radio("radio") find out how to format
    # slider = slider("slider") find out how to format
    # actions = actions("actions") find out how to format
    # file_upload = file_upload("file_upload") find out how to format
    # input_group = input_group("input_group") find out how to format
    # input_update = input_update("input_update") find out how to format

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            # HTML from the pywebio.output
            put_markdown('# **Results**')
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            put_html('<br><br>')
            put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
            put_html('<hr>')
            put_table([
                ['Your BMI', 'Category'],
                [BMI, status],
            ])
            # put_button("Click me", onclick=lambda: toast("Clicked"))  # single button example
            break
    #logical operators AND, OR, NOT
    if BMI and area: 
            put_text("Thank you for your comments: ", area)

    # while loop




            
#run the function on port 80
if __name__ == '__main__':
   # pywebio.start_server(bmi, port=80)
    bmi() # script mode
  # start_server(bmi, port=8080, debug=True)