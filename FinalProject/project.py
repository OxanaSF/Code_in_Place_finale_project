'''
README
To be able to run the program:
    - pip install numpy
    - pip install plotly

Data source: https://population.un.org/wpp/Download/Standard/Population/
'''

import random
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# CONSTANT variables
FILE = "sex_ratio_of_total_population.csv"
WORLD_PARTS = [
                'SUB-SAHARAN AFRICA',
                'NORTHERN AFRICA AND WESTERN ASIA',
                'CENTRAL AND SOUTHERN ASIA',
                'EASTERN AND SOUTH-EASTERN ASIA',
                'LATIN AMERICA AND THE CARIBBEAN',
                'AUSTRALIA/NEW ZEALAND',
                'OCEANIA (EXCLUDING AUSTRALIA AND NEW ZEALAND)',
                'EUROPE AND NORTHERN AMERICA'
            ]



def main():
    """
    This function asks a user to choose from which World's region he would like to see
    a visualized change in sex ratio over the past 70 years in the World. A user has choice to pick info
    from eight World parts or to get it from a randomly generated country.
    :return: a Line Chart that automatically opens as an HTML file in a browser window
    """


    entry_greeting()

    while True:
        user_iinput = options_for_user_input()

        if user_iinput == 1:

            user_choice = region_choose_user()

            region = WORLD_PARTS[user_choice - 1]
            y = get_data_from_csv(region)
            plot_chart(y, region)



        elif user_iinput == 2:
            random_num = random.randint(25, 256)
            random_region = get_random_country(random_num)
            y = get_data_from_csv(random_region)
            plot_chart(y, random_region)



        elif user_iinput == 3:

            set_region = "WORLD"

            y = get_data_from_csv(set_region)
            plot_chart(y, set_region)



        elif user_iinput == -1:
            return

        else:
            print("Incorrect input.")


def entry_greeting():
    print("\n""Let's find out some statistics about male/female ratio in different World's parts over the past 70 years!\n""")




def options_for_user_input():
    """
    This function returns a prompt for user to read instructions and
    chose one of the options offered.
    """
    user_iinput = int(input('- to chose from the set of parts of the World, press 1,\n'
                            '- to receive data from a random country, press 2,\n'
                            "- to get total World's number, press 3\n"
                            '- to exit, press -1\n'
                            'Press here: '))
    return user_iinput




def region_choose_user():
    """
    This function returns a prompt for user to choose one
    of several World's parts.
    """
    print()
    for i in range(len(WORLD_PARTS)):
        print(f'{i + 1} {WORLD_PARTS[i]}')

    user_choose_region = int(input('Select number accordingly: '))

    return user_choose_region




def get_data_from_csv(world_region):
    """
    This function returns a list contained the digits that represent males per 100 females
    for chosen region per specific years years from a csv file
    Input: no input
    Returns: list of ratios from 1950, 1970, 1990, 2010 and 2020
    Doctests:
    >>> get_data_from_csv("WORLD")
    [99.7, 99.9, 100.1, 100.3, 100.6, 100.6, 100.8, 101.0, 101.1, 101.4, 101.4, 101.6, 101.7, 101.7]
    >>> get_data_from_csv("OCEANIA (EXCLUDING AUSTRALIA AND NEW ZEALAND)")
    [112.1, 108.8, 107.5, 106.2, 105.5, 104.9, 104.6, 104.3, 104.2, 103.9, 103.5, 103.6, 103.6, 103.6, 103.7]
    """
    data_for_region = []


    with open(FILE) as f:
        for line in f:
            line = line.split(",")
            if line[2] == world_region:
                for i in range(7, 22):
                    data_for_region.append(float(line[i]))


        return data_for_region




def plot_chart(y_values, region):
    """
    This function creates and returns a graphic
    Input: int -> x_coord, int -> y_coord, string -> region
    Returns: plot created with plotly and numpy.
    """

    x_coord = np.linspace(1950, 2020, 15)
    y_coord = np.array(y_values)
    trace2 = go.Scatter(x=x_coord, y=y_coord,
                        mode='lines+markers', name='lines')
    data = [trace2]
    layout = go.Layout(title=f'Sex ratio in 1950 - 2020 in {region}',
                       xaxis_title="Years",
                       yaxis_title="Males per 100 females",
                       font=dict(
                           family="Courier New, monospace",
                           size=16,
                           color="RebeccaPurple"
                       )
                       )
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig)

    return pyo.plot(fig)




def get_random_country(num):
    """
    This function retrieves and returns a country
    by index by applying a random number.
    Input: int -> x
    Output: string
    Returns: string with a country name.
    Doctests:
    >>> get_random_country(217)
    'Russian Federation'
    >>> get_random_country(255)
    'United States of America'
    """
    with open(FILE) as f:
        for line in f:
            line = line.split(",")
            if line[0] == str(num):
                return line[2]








if __name__ == '__main__':
    main()
