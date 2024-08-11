import panel as pn
import random
import string

pn.extension()
pn.extension(sizing_mode="stretch_width")
rollover = pn.widgets.IntInput(name='Length ', value=15)
button = pn.widgets.Button(name='Submit')
dropdown = pn.widgets.Select(name='Select Difficulty', options=['Easy', 'Medium', 'Hard'])


def rollover_callback(complexity, length, sub):
    if sub:
        characters = ''

        if complexity == 'Easy':
            characters = string.ascii_lowercase
        elif complexity == 'Medium':
            characters = string.ascii_letters + string.digits
        elif complexity == 'Hard':
            characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return f'password : {password}'


pn.Column(dropdown, rollover, button, pn.bind(rollover_callback, dropdown, rollover, button)).servable(target='simple_app')
