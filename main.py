import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.express as px

# ---------------------------------------------
# STYLE INIT

# the style arguments for the parameterbar.
PARAMETERBAR_STYLE = {
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '96%',
    'margin-left': '2%',
    'margin-right': '2%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-top': '2%',
    'margin-left': '2%',
    'margin-right': '2%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

# ---------------------------------------------
# PARAMETER LABEL INIT

controls = dbc.FormGroup(
    [
        # Slide bar to select years you want to study
        html.P('Choose your study period', style={'textAlign': 'center'}),
        dcc.RangeSlider(
            id='years_wanted',
            min=1961,
            max=2021,
            step=None,
            marks={
                # 1951: '1951',
                # 1952: '1952',
                # 1953: '1953',
                # 1954: '1954',
                # 1955: '1955',
                # 1956: '1956',
                # 1957: '1957',
                # 1958: '1958',
                # 1959: '1959',
                # 1960: '1960',
                1961: '1961',
                1962: '1962',
                1963: '1963',
                1964: '1964',
                1965: '1965',
                1966: '1966',
                1967: '1967',
                1968: '1968',
                1969: '1969',
                1970: '1970',
                1971: '1971',
                1972: '1972',
                1973: '1973',
                1974: '1974',
                1975: '1975',
                1976: '1976',
                1977: '1977',
                1978: '1978',
                1979: '1979',
                1980: '1980',
                1981: '1981',
                1982: '1982',
                1983: '1983',
                1984: '1984',
                1985: '1985',
                1986: '1986',
                1987: '1987',
                1988: '1988',
                1989: '1989',
                1990: '1990',
                1991: '1991',
                1992: '1992',
                1993: '1993',
                1994: '1994',
                1995: '1995',
                1996: '1996',
                1997: '1997',
                1998: '1998',
                1999: '1999',
                2000: '2000',
                2001: '2001',
                2002: '2002',
                2003: '2003',
                2004: '2004',
                2005: '2005',
                2006: '2006',
                2007: '2007',
                2008: '2008',
                2009: '2009',
                2010: '2010',
                2011: '2011',
                2012: '2012',
                2013: '2013',
                2014: '2014',
                2015: '2015',
                2016: '2016',
                2017: '2017',
                2018: '2018',
                2019: '2019',
                2020: '2020',
                2021: '2021'
            },
            value=[2010, 2021]
        ),
        html.Br(),
        html.Br(),

        # Check Box to select meteorological events you want to study
        html.P('Choose meteorological events you want to study', style={'textAlign': 'center'}),
        dbc.Card([
            dbc.Checklist(
                id='Check_all_events',
                options=[{'label': 'SELECT ALL', 'value': False}],
                value=[],
                inline=True
            ),

            dbc.Checklist(
            id='events_wanted',
            options=[
                {
                    'label': 'AVALANCHE',
                    'value': 'Avalanche'
                },
                {
                    'label': 'BLIZZARD',
                    'value': 'Blizzard'
                },
                {
                    'label': 'COASTAL FLOOD',
                    'value': 'Coastal Flood'
                },
                {
                    'label': 'COLD/WINTER CHILL',
                    'value': 'Cold/Winter Chill'
                },
                {
                    'label': 'DEBRIS FLOW',
                    'value': 'Debris Flow'
                },
                {
                    'label': 'DENSE FOG',
                    'value': 'Dense Fog'
                },
                {
                    'label': 'DROUGHT',
                    'value': 'Drought'
                },
                {
                    'label': 'DUST DEVIL',
                    'value': 'Dust Devil'
                },
                {
                    'label': 'DUST STORM',
                    'value': 'Dust Storm'
                },
                {
                    'label': 'EXCESSIVE HEAT',
                    'value': 'Excessive Heat'
                },
                {
                    'label': 'EXTREME COLD/WIND CHILL',
                    'value': 'Extreme Cold/Wind Chill'
                },
                {
                    'label': 'FLASH FLOOD',
                    'value': 'Flash Flood'
                },
                {
                    'label': 'FLOOD',
                    'value': 'Flood'
                },
                {
                    'label': 'FREEZING FOG',
                    'value': 'Freezing Fog'
                },
                {
                    'label': 'FROST/FREEZE',
                    'value': 'Frost/Freeze'
                },
                {
                    'label': 'FUNNEL CLOUD',
                    'value': 'Funnel Cloud'
                },
                {
                    'label': 'HAIL',
                    'value': 'Hail'
                },
                {
                    'label': 'HEAT',
                    'value': 'Heat'
                },
                {
                    'label': 'HEAVY RAIN',
                    'value': 'Heavy Rain'
                },
                {
                    'label': 'HEAVY SNOW',
                    'value': 'Heavy Snow'
                },
                {
                    'label': 'HEAVY WIND',
                    'value': 'Heavy Wind'
                },
                {
                    'label': 'HIGH SURF',
                    'value': 'High Surf'
                },
                {
                    'label': 'HIGH WIND',
                    'value': 'High Wind'
                },
                {
                    'label': 'HURRICANE (TYPHOON)',
                    'value': 'Hurricane (Typhoon)'
                },
                {
                    'label': 'ICE STORM',
                    'value': 'Ice Storm'
                },
                {
                    'label': 'LAKE EFFECT SNOW',
                    'value': 'Lake Effect Snow'
                },
                {
                    'label': 'LIGHTNING',
                    'value': 'Lightning'
                },
                {
                    'label': 'NORTHERN LIGHTS',
                    'value': 'Northern Lights'
                },
                {
                    'label': 'OTHER',
                    'value': 'Other'
                },
                {
                    'label': 'RIP CURRENT',
                    'value': 'Rip Current'
                },
                {
                    'label': 'SEICHE',
                    'value': 'Seiche'
                },
                {
                    'label': 'SLEET',
                    'value': 'Sleet'
                },
                {
                    'label': 'STORM SURGE/TIDE',
                    'value': 'Storm Surge/Tide'
                },
                {
                    'label': 'STRONG WIND',
                    'value': 'Strong Wind'
                },
                {
                    'label': 'THUNDERSTORM WIND',
                    'value': 'Thunderstorm Wind'
                },
                {
                    'label': 'TORNADO',
                    'value': 'Tornado'
                },
                {
                    'label': 'TROPICAL STORM',
                    'value': 'Tropical Storm'
                },
                {
                    'label': 'VOLCANIC ASH',
                    'value': 'Volcanic Ash'
                },
                {
                    'label': 'WATERSPOUT',
                    'value': 'Waterspout'
                },
                {
                    'label': 'WILDFIRE',
                    'value': 'Wildfire'
                },
                {
                    'label': 'WINTERSTORM',
                    'value': 'Winterstorm'
                },
                {
                    'label': 'WINTER WEATHER',
                    'value': 'Winter Weather'
                },
            ],
            value=['Lightning'],
            inline=True
        )]),
        html.Br(),

        # Check Box to select states you want to study
        html.P('Choose states of America you want to study', style={'textAlign': 'center'}),
        dbc.Card([
            dbc.Checklist(
                id='Check_all_states',
                options=[{'label': 'SELECT ALL', 'value': False}],
                value=[],
                inline=True
            ),

            dbc.Checklist(
            id='states_wanted',
            options=[
                {
                    'label': 'ALABAMA',
                    'value': 'ALABAMA'
                },
                {
                    'label': 'ALASKA',
                    'value': 'ALASKA'
                },
                {
                    'label': 'ARIZONA',
                    'value': 'ARIZONA'
                },
                {
                    'label': 'ARKANSAS',
                    'value': 'ARKANSAS'
                },
                {
                    'label': 'CALIFORNIA',
                    'value': 'CALIFORNIA'
                },
                {
                    'label': 'COLORADO',
                    'value': 'COLORADO'
                },
                {
                    'label': 'CONNECTICUT',
                    'value': 'CONNECTICUT'
                },
                {
                    'label': 'DELAWARE',
                    'value': 'DELAWARE'
                },
                {
                    'label': 'FLORIDA',
                    'value': 'FLORIDA'
                },
                {
                    'label': 'GEORGIA',
                    'value': 'GEORGIA'
                },
                {
                    'label': 'HAWAII',
                    'value': 'HAWAII'
                },
                {
                    'label': 'IDAHO',
                    'value': 'IDAHO'
                },
                {
                    'label': 'ILLINOIS',
                    'value': 'ILLINOIS'
                },
                {
                    'label': 'INDIANA',
                    'value': 'INDIANA'
                },
                {
                    'label': 'IOWA',
                    'value': 'IOWA'
                },
                {
                    'label': 'KANSAS',
                    'value': 'KANSAS'
                },
                {
                    'label': 'KENTUCKY',
                    'value': 'KENTUCKY'
                },
                {
                    'label': 'LOUISIANA',
                    'value': 'LOUISIANA'
                },
                {
                    'label': 'MAINE',
                    'value': 'MAINE'
                },
                {
                    'label': 'MARYLAND',
                    'value': 'MARYLAND'
                },
                {
                    'label': 'MASSACHUSETTS',
                    'value': 'MASSACHUSETTS'
                },
                {
                    'label': 'MICHIGAN',
                    'value': 'MICHIGAN'
                },
                {
                    'label': 'MINNESOTA',
                    'value': 'MINNESOTA'
                },
                {
                    'label': 'MISSISSIPPI',
                    'value': 'MISSISSIPPI'
                },
                {
                    'label': 'MISSOURI',
                    'value': 'MISSOURI'
                },
                {
                    'label': 'MONTANA',
                    'value': 'MONTANA'
                },
                {
                    'label': 'NEBRASKA',
                    'value': 'NEBRASKA'
                },
                {
                    'label': 'NEVADA',
                    'value': 'NEVADA'
                },
                {
                    'label': 'NEW HAMPSHIRE',
                    'value': 'NEW HAMPSHIRE'
                },
                {
                    'label': 'NEW JERSEY',
                    'value': 'NEW JERSEY'
                },
                {
                    'label': 'NEW MEXICO',
                    'value': 'NEW MEXICO'
                },
                {
                    'label': 'NEW YORK',
                    'value': 'NEW YORK'
                },
                {
                    'label': 'NORTH CAROLINA',
                    'value': 'NORTH CAROLINA'
                },
                {
                    'label': 'NORTH DAKOTA',
                    'value': 'NORTH DAKOTA'
                },
                {
                    'label': 'OHIO',
                    'value': 'OHIO'
                },
                {
                    'label': 'OKLAHOMA',
                    'value': 'OKLAHOMA'
                },
                {
                    'label': 'OREGON',
                    'value': 'OREGON'
                },
                {
                    'label': 'PENNSYLVANIA',
                    'value': 'PENNSYLVANIA'
                },
                {
                    'label': 'RHODE ISLAND',
                    'value': 'RHODE ISLAND'
                },
                {
                    'label': 'SOUTH CAROLINA',
                    'value': 'SOUTH CAROLINA'
                },
                {
                    'label': 'SOUTH DAKOTA',
                    'value': 'SOUTH DAKOTA'
                },
                {
                    'label': 'TENNESSEE',
                    'value': 'TENNESSEE'
                },
                {
                    'label': 'TEXAS',
                    'value': 'TEXAS'
                },
                {
                    'label': 'UTAH',
                    'value': 'UTAH'
                },
                {
                    'label': 'VERMONT',
                    'value': 'VERMONT'
                },
                {
                    'label': 'VIRGINIA',
                    'value': 'VIRGINIA',
                },
                {
                    'label': 'WASHINGTON',
                    'value': 'WASHINGTON'
                },
                {
                    'label': 'WEST VIRGINIA',
                    'value': 'WEST VIRGINIA'
                },
                {
                    'label': 'WISCONSIN',
                    'value': 'WISCONSIN'
                },
                {
                    'label': 'WYOMING',
                    'value': 'WYOMING'
                },
            ],
            value=['ALABAMA', 'ALASKA','ARIZONA','ARKANSAS','CALIFORNIA','COLORADO','CONNECTICUT','DELAWARE','FLORIDA','GEORGIA','IDAHO','ILLINOIS','INDIANA','IOWA','KANSAS','KENTUCKY','LOUISIANA','MAINE','MARYLAND','MASSACHUSETTS','MICHIGAN','MINNESOTA','MISSISSIPPI','MISSOURI','MONTANA','NEBRASKA','NEVADA','NEW HAMPSHIRE','NEW JERSEY','NEW MEXICO','NEW YORK','NORTH CAROLINA','NORTH DAKOTA','OHIO','OKLAHOMA','OREGON','PENNSYLVANIA','RHODE ISLAND','SOUTH CAROLINA','SOUTH DAKOTA','TENNESSEE','TEXAS','UTAH','VERMONT','VIRGINIA','WASHINGTON','WEST VIRGINIA','WISCONSIN','WYOMING'],
            inline=True
        )]),
        html.Br(),

        # Submit button
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True
        ),
    ]
)

parameterbar = html.Div(
    [
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=PARAMETERBAR_STYLE,
)

# ---------------------------------------------
# VISUAL CONTENTS

# First view : Localisation of meteorological events on the map
content_first_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_1'), md=12
        )
    ]
)

# Second view : Bar graph of stacked histograms of meteorological events according to years in United States of America
content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_2'), md=12
        )
    ]
)

# Label of content in order to manage views
content = html.Div(
    [
        html.H2('METEOROLOGICAL EVENTS STUDY IN UNITED STATES OF AMERICA SINCE 1961 TO NOWADAYS', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row
    ],
    style=CONTENT_STYLE
)

# ---------------------------------------------
# APP LAYOUT

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.H1("DSIA PROJECT DASHBOARD", style={'text-align': 'center'}),
    html.Br(),

    parameterbar,
    content
])

# ---------------------------------------------
# INTERACTIONS, CALLBACKS

# Callback signal to check all events and uncheck them all
@app.callback(
    Output('events_wanted', 'value'),
    Output('Check_all_events', 'value'),
    [Input('submit_button', 'n_clicks')],
    [State('events_wanted', 'options'), State('Check_all_events', 'value'),
     State('events_wanted', 'value')
     ])
def select_all_none(n_clicks, events_wanted_options, check_all_events_value, events_wanted_value):
    if check_all_events_value :
        all_or_none = [option["value"] for option in events_wanted_options]
    elif not check_all_events_value and events_wanted_value == [option["value"] for option in events_wanted_options]:
        all_or_none = []
    else :
        all_or_none = events_wanted_value
    return all_or_none, check_all_events_value

# Callback signal to check all states and uncheck them all
@app.callback(
    Output('states_wanted', 'value'),
    Output('Check_all_states', 'value'),
    [Input('submit_button', 'n_clicks')],
    [State('states_wanted', 'options'), State('Check_all_states', 'value'),
     State('states_wanted', 'value')
     ])
def select_all_none(n_clicks, states_wanted_options, check_all_states_value, states_wanted_value):
    if check_all_states_value :
        all_or_none = [option["value"] for option in states_wanted_options]
    elif not check_all_states_value and states_wanted_value == [option["value"] for option in states_wanted_options]:
        all_or_none = []
    else :
        all_or_none = states_wanted_value
    return all_or_none, check_all_states_value

# Callback signal displaying on map events wanted according to period wanted in states wanted
@app.callback(
    Output('graph_1', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('years_wanted', 'value'), State('events_wanted', 'value'),
     State('states_wanted', 'value')
     ])
def update_graph_1(n_clicks, years_wanted_value, events_wanted_value, states_wanted_value):
    dataframe = pd.DataFrame()
    years = range(years_wanted_value[0], years_wanted_value[-1] + 1)
    for year in years:
        post_concatenate_dataframe = pd.read_csv("Datas\StormEvents_details_" + str(year) + ".csv", usecols=['YEAR', 'STATE', 'EVENT_TYPE', 'BEGIN_LAT', 'BEGIN_LON'])
        dataframe = dataframe.append(post_concatenate_dataframe)

    dataframe = dataframe.loc[(dataframe['STATE'].isin(states_wanted_value))]
    df = dataframe.loc[(dataframe['EVENT_TYPE'].isin(events_wanted_value))]

    # make a pertinent title
    if len(years) != 1:
        title_year = 'from ' + str(years[0]) + ' to ' + str(years[-1])
    else:
        title_year = 'in ' + years[0]
    if len(events_wanted_value) != 1:
        title_event = 'meteorologic'
    else:
        title_event = events_wanted_value[0]
    if len(states_wanted_value) != 1:
        title_state = 'by states'
    else:
        title_state = 'in ' + states_wanted_value[0].title()
    graph_tilte = 'Map of ' + title_event + ' events ' + title_state + ' in USA ' + title_year

    fig = px.scatter_geo(df, lat=df['BEGIN_LAT'], lon=df['BEGIN_LON'], color=df['EVENT_TYPE'], hover_name=df['STATE'], size=df['YEAR'], projection='albers usa', size_max=3, title=graph_tilte)
    fig.update_layout({
        'height': 600
    })
    return fig

# Callback signal displaying bar graph of stacked histograms which count events wanted according to the period in states wanted
@app.callback(
    Output('graph_2', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('years_wanted', 'value'), State('events_wanted', 'value'),
     State('states_wanted', 'value')
     ])
def update_graph_2(n_clicks, years_wanted_value, events_wanted_value, states_wanted_value):
    dataframe = pd.DataFrame()
    years = range(years_wanted_value[0],years_wanted_value[-1]+1)
    for year in years:
        post_concatenate_dataframe = pd.read_csv("Datas\StormEvents_details_" + str(year) + ".csv", usecols=['YEAR', 'STATE', 'EVENT_TYPE'])
        dataframe = dataframe.append(post_concatenate_dataframe)

    dataframe = dataframe.loc[(dataframe['STATE'].isin(states_wanted_value))]
    df = dataframe.loc[(dataframe['EVENT_TYPE'].isin(events_wanted_value))]

    df['EVENT_TYPE'] = df['EVENT_TYPE'].astype('category')
    df_hist = df.groupby(['STATE', 'YEAR', 'EVENT_TYPE']).size()
    df.unstack()

    # make a pertinent title
    if len(years) != 1 :
        title_year = 'from ' + str(years[0]) + ' to ' + str(years[-1])
    else :
        title_year = 'in ' + years[0]
    if len(events_wanted_value) != 1 :
        title_event = 'meteorologic'
    else :
        title_event = events_wanted_value[0]
    if len(states_wanted_value) != 1 :
        title_state = 'by states'
    else :
        title_state = 'in ' + states_wanted_value[0].title()
    graph_tilte = 'Number of ' + title_event + ' events ' + title_state + ' in USA ' + title_year

    fig = px.histogram(df_hist, x=df['STATE'], color=df['EVENT_TYPE'], title=graph_tilte)
    return fig


if __name__ == '__main__':
    app.run_server(port='8085')

