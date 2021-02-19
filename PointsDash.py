# Creating a Baseball Dashboard for 
# MLB Fantasy Points based leagues

# Goal is to create a tool managers can use to help
# rank players based on specific league settings

import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.express as px #(need to pip install plotly==4.4.1)


# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
# Allows Heroku to connect to servers:
server = app.server


df = pd.read_csv("All_Stats.csv")

df.Season = pd.to_numeric(df.Season)

df = df[df['Season'] >= 2000]

min_year = df.Season.min()
max_year = df.Season.max()

df.insert(1, "Points", 0)
#df['Points'] = 0

dttable = ['Points','Season','Name','Age','Team','AB','H_bat','1B','2B','3B','HR_bat','R_bat','RBI','BB_bat','IBB_bat','SB','CS','SO_bat','GS','CG','ShO','W','L','SV','BS','IP','SO_pit','H_pit','ER','BB_pit','IBB_pit','HBP_pit','BK','WP']

print(df.head())

#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([

        dbc.Row([
            dbc.Col([

                # Page Title

                html.H3("Fantasy Baseball: League Specific Points Based Rankings", 
                style={'fontSize': 24, 'margin-right': '5%', 'margin-left': '5%', 'margin-top': '2%', 'margin-bottom': '0.5%'})
                

            ]), # End Top Col
        ]), # End Top Row

        dbc.Row([
            dbc.Col( [
                html.Div([
                    # Select Year Ranges
                    
                    dcc.RangeSlider(
                        id='Season',
                        marks={
                            1850: {'label': '1850', 'style': {'color': '#77b0b1'}},
                            1860: {'label': '1860'},
                            1870: {'label': '1870'},
                            1880: {'label': '1880', 'style': {'color': '#f50'}},
                            1890: {'label': '1890', 'style': {'color': '#77b0b1'}},
                            1900: {'label': '1900'},
                            1910: {'label': '1910'},
                            1920: {'label': '1920', 'style': {'color': '#f50'}},
                            1930: {'label': '1930', 'style': {'color': '#77b0b1'}},
                            1940: {'label': '1940'},
                            1950: {'label': '1950'},
                            1960: {'label': '1960', 'style': {'color': '#f50'}},
                            1970: {'label': '1970', 'style': {'color': '#77b0b1'}},
                            1980: {'label': '1980'},
                            1990: {'label': '1990'},
                            2000: {'label': '2000'},
                            2010: {'label': '2010', 'style': {'color': '#f50'}},
                            2020: {'label': '2020'},
                            2030: {'label': '2030'},
                            2040: {'label': '2040', 'style': {'color': '#f50'}}
                        },
                        step=1,
                        min = min_year,
                        max = max_year,
                        value = [2020, 2020],
                        dots = True,
                        allowCross = False,
                        disabled = False,
                        pushable = 0,
                        updatemode = 'drag',
                        included = True,
                        vertical = False,
                        # verticalHeight = 900,
                        className = 'None',
                        # tooltip = {"always visible":False, "placement":'bottom'}

                    ),
                ]), 
                
            ], width=10) # End Range Slider Col

        ]), # End Range Slider Row




        dbc.Row([
            dbc.Col( [

                html.H5("League Points", style={'font-weight': 'bold'}),

                html.H6("Batting: "),

                html.H6("AB: "),

                html.Div([
                dcc.Input(
                    id='AB_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=0,
                    debounce=False,
                    placeholder='Points Per AB'),
                ]),

                html.H6("H: "),

                html.Div([
                dcc.Input(
                    id='H_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=0,
                    debounce=False,
                    placeholder='Points Per H'),
                ]),


                html.H6("Single: "),

                html.Div([
                dcc.Input(
                    id='Single_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per 1b'),
                ]),


                html.H6("Double: "),

                html.Div([
                dcc.Input(
                    id='Double_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=2,
                    debounce=False,
                    placeholder='Points Per 2B'),
                ]),


                html.H6("Triple: "),

                html.Div([
                dcc.Input(
                    id='Triple_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=3,
                    debounce=False,
                    placeholder='Points Per 3B'),
                ]),


                html.H6("HR: "),

                html.Div([
                dcc.Input(
                    id='HR_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=6,
                    debounce=False,
                    placeholder='Points Per HR'),
                ]),


                html.H6("Runs: "),

                html.Div([
                dcc.Input(
                    id='R_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per R'),
                ]),


                html.H6("RBI: "),

                html.Div([
                dcc.Input(
                    id='RBI_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per RBI'),
                ]),


                html.H6("Walk: "),

                html.Div([
                dcc.Input(
                    id='BB_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per BB'),
                ]),

                html.H6("Intentional Walk: "),

                html.Div([
                dcc.Input(
                    id='IBB_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per IBB'),
                ]),

                html.H6("Stolen Base: "),

                html.Div([
                dcc.Input(
                    id='SB_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per SB'),
                ]),


                html.H6("Caught Stealing: "),

                html.Div([
                dcc.Input(
                    id='CS_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per CS'),
                ]),

                html.H6("Strike Out: "),

                html.Div([
                dcc.Input(
                    id='SO_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per SO'),
                ]),


                # Missing Stats:
                # Cycle, GS Hr, and Errors

            ], width=1, style={'margin-left': '2%', 'margin-right': '0.5%'}), # End Batting Point Col


            dbc.Col( [

                html.H6(" "),
                html.H6(" "),

                html.H6("Pitching: "),

                html.H6("Games Started: "),

                html.Div([
                dcc.Input(
                    id='GS_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=0,
                    debounce=False,
                    placeholder='Points Per GS'),
                ]),

                html.H6("Complete Game: "),

                html.Div([
                dcc.Input(
                    id='CG_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=10,
                    debounce=False,
                    placeholder='Points Per CG'),
                ]),

                html.H6("Shut Outs: "),

                html.Div([
                dcc.Input(
                    id='ShO_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=5,
                    debounce=False,
                    placeholder='Points Per ShO'),
                ]),

                html.H6("Wins: "),

                html.Div([
                dcc.Input(
                    id='W_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=5,
                    debounce=False,
                    placeholder='Points Per W'),
                ]),

                html.H6("Loss: "),

                html.Div([
                dcc.Input(
                    id='L_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-5,
                    debounce=False,
                    placeholder='Points Per L'),
                ]),

                html.H6("Save: "),

                html.Div([
                dcc.Input(
                    id='SV_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=5,
                    debounce=False,
                    placeholder='Points Per SV'),
                ]),

                html.H6("Blown Save: "),

                html.Div([
                dcc.Input(
                    id='BS_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-5,
                    debounce=False,
                    placeholder='Points Per BS'),
                ]),



                html.H6("Innings Pitched: "),

                html.Div([
                dcc.Input(
                    id='IP_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=3,
                    debounce=False,
                    placeholder='Points Per IP'),
                ]),

                html.H6("Strike Outs: "),

                html.Div([
                dcc.Input(
                    id='K_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=1,
                    debounce=False,
                    placeholder='Points Per K'),
                ]),


                html.H6("Hits Allowed: "),

                html.Div([
                dcc.Input(
                    id='H_Allow_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per Hits Allowed'),
                ]),

                html.H6("Earned Runs Allowed: "),

                html.Div([
                dcc.Input(
                    id='ER_Allow_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-2,
                    debounce=False,
                    placeholder='Points Per ER Allowed'),
                ]),

                html.H6("Walks Issued: "),

                html.Div([
                dcc.Input(
                    id='BB_Allow_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per BB Issued'),
                ]),

                html.H6("Intential Walks Issued: "),

                html.Div([
                dcc.Input(
                    id='IBB_Allow_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per IDD Issued'),
                ]),

                html.H6("Hit Batsman: "),

                html.Div([
                dcc.Input(
                    id='HBP_Allow_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per HBP'),
                ]),

                html.H6("Balks: "),

                html.Div([
                dcc.Input(
                    id='BK_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per BK'),
                ]),

                html.H6("Wild Pitch: "),

                html.Div([
                dcc.Input(
                    id='WP_p',
                    type='number',
                    step=1,
                    min=-200,
                    max=200,
                    minLength=0,
                    maxLength=3,
                    value=-1,
                    debounce=False,
                    placeholder='Points Per WP'),
                ]),



                # Missing Stats:
                # No Hitters, Perfect Games, Quality Starts, Holds

            ], width=1, style={'margin-left': '0.5%', 'margin-right': '1%'}), # End Pitching Point Col

            dbc.Col( [

                html.Div([
                # Center Large Scatter Plot
                dbc.Spinner(children=[

                dcc.Graph(id="scatter-plot", figure={},style={'width': '100%', 'height': '80vh'})
                
                ], size="lg", color="primary", type="grow", fullscreen=False,),
                
                ]),

            dbc.Row([
                # X-Axis / 
                dbc.Col( [


                    html.H6("Select X-Axis:", style={'fontSize': 11}),
                    # Select 'X' Axis
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_X',
                        options=[
                                {'label': column, 'value': column}
                                for column in df.columns.unique()
                                ],   
                        value='AB',
                        placeholder="X-Axis",
                        multi=False,
                        clearable=False,
                    ),

                    ]),


                    html.H6("Select Y-Axis:", style={'fontSize': 11}),
                    # Select 'Y' Axis
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_Y',
                        options=[
                                {'label': column, 'value': column}
                                for column in df.columns.unique()
                                ],   
                        value='Points',
                        placeholder="Y-Axis",
                        multi=False,
                        clearable=False,
                    ),

                    ]),

                    html.H6("Color Grouping:", style={'fontSize': 11}),
                    # Select Color Grouping
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_Color',
                        options=[
                                {'label': column, 'value': column}
                                for column in df.columns.unique()
                                ],   
                        value='Team',
                        placeholder="Color",
                        multi=False,
                        clearable=False,
                    ),

                    ]),

                ], width=3, style={'margin-left': '2%', 'margin-right': '1%'}),

                # Sekect Teams
                dbc.Col( [

                    html.H6("Select Teams:"),

                    # Select Teams
                    html.Div([ 
                    dcc.Dropdown(
                        id='Team_Checkbox',
                        multi=True,
                        value = [],
                        placeholder="Select Teams"
                        ),
                    ]),

                    html.H6("Select trendline:", style={'fontSize': 11}),
                    # Select Facet
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_trendline',
                        options=[
                                {'label': 'None', 'value': 'None'},
                                {'label': 'ols', 'value': 'ols'},
                                {'label': 'lowess', 'value': 'lowess'}
                                ],   
                        value=None,
                        placeholder="trendline",
                        multi=False,
                        clearable=False,
                    ),
                    
                    ]),

                                        html.H6("Select Facet:", style={'fontSize': 11}),
                    # Select Facet
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_facet',
                        options=[
                                {'label': 'None', 'value': 'None'},
                                {'label': 'Season', 'value': 'Season'},
                                {'label': 'Team', 'value': 'Team'},
                                {'label': 'Age', 'value': 'Age'},
                                {'label': 'Name', 'value': 'Name'},
                                {'label': 'League', 'value': 'lgID'},
                                {'label': 'Bats', 'value': 'bats'},
                                {'label': 'Throws', 'value': 'throws'},
                                {'label': 'Division', 'value': 'divID'},
                                {'label': 'Division Win', 'value': 'DivWin_team'},
                                {'label': 'Wild Card Win', 'value': 'WCWin_team'},
                                {'label': 'League Win', 'value': 'LgWin_team'},
                                {'label': 'World Series Win', 'value': 'WSWin_team'}
                                ],   
                        value=None,
                        placeholder="facet",
                        multi=False,
                        clearable=False,
                    ),
                    
                    ]),


                ], style={'margin-left': '1%', 'margin-right': '1%'}),

                # Select Players
                dbc.Col( [

                    html.H6("Select Players: "),

                    # Select Players
                    html.Div([ 
                    dcc.Dropdown(
                        id='Player_Checkbox',
                        multi=True,
                        value = [],
                        placeholder="Select Players"
                        ),

                    ]),


                    html.H6("Position Eligibility: "),

                    # Select Position Eligibility
                    html.Div([
                    dcc.Input(
                        id='input_pos_appear',
                        type='number',
                        step=1,
                        min=0,
                        max=200,
                        minLength=0,
                        maxLength=3,
                        value=20,
                        debounce=False,
                        placeholder='Position Eligibility',


                    ),
                    ]),


                    html.H6("Select Positions: "),

                    # Select Positions
                    html.Div([ 
                    dcc.Dropdown(
                        id='Positions_Checkbox',
                        multi=True,
                        options=[
                                {'label': 'Pitcher', 'value': 'G_p'},
                                {'label': 'Catcher', 'value': 'G_c'},
                                {'label': '1st Baseman', 'value': 'G_as_1B'},
                                {'label': '2nd Baseman', 'value': 'G_as_2B'},
                                {'label': '3rd Baseman', 'value': 'G_as_3B'},
                                {'label': 'ShortStop', 'value': 'G_as_SS'},
                                {'label': 'Left Fielder', 'value': 'G_as_LF'},
                                {'label': 'Center Fielder', 'value': 'G_as_CF'},
                                {'label': 'Right Fielder', 'value': 'G_as_RF'},
                                {'label': 'Outfielder', 'value': 'G_as_OF'},
                                {'label': 'Pitch Hitter', 'value': 'G_as_PH'},
                                {'label': 'Pitch Runner', 'value': 'G_as_pr'},
                                {'label': 'Designated Hitter', 'value': 'G_as_DH'}
                                ], 
                        value = [],
                        placeholder="Select Positions"
                        ),
                    ]),
                    



                ], style={'margin-left': '1%', 'margin-right': '2%'}),

            ]),




            ], width= 8, style={'margin-left': '0.5%', 'margin-right': '2%'}), # Center Graph



        ]), # End Points Row


        #Position Violin Graphs
        dbc.Row([



        ]),

        #DataTable
        dbc.Row([

            # DataTable
            dbc.Col( [

            dbc.Spinner(children=[

            # Data Table
            dash_table.DataTable(
                id='datatable',
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                columns= [{"name": i, "id": i} for i in dttable],
                style_table={
                    'maxHeight': '500px',
                    'maxWidth': '90%',
                    'overflowY': 'scroll',
                    'overflowX': 'scroll',
                    'border': 'thin lightgrey solid'
                }
            )
                
            ], size="lg", color="primary", type="grow", fullscreen=False,),
              

            ], width=12, style={'margin-left': '2%', 'margin-right': '2%','margin-top': '2%','margin-bottom': '2%',}), # end Table


        ]),




    ]) # End html.div

]) # End App Layout




#---------------------------------------------------------------

@app.callback(
    Output("Player_Checkbox", "options"),
    [Input(component_id='Season',component_property='value'),
    Input(component_id='Player_Checkbox',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')],
    [State("Player_Checkbox", "options")])

def player_options(Season, Player_Checkbox, Team_Checkbox, options):

    dff = df

    # print(Season[0])
    Smin = Season[0] # - From Range Slider
    Smax = Season[1] # - From Range Slider
    dff = dff[(dff.Season >= Smin) & (dff.Season <= Smax)]


    if Team_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.Team.apply(lambda x: any(item for item in Team_Checkbox if item in x))]


    playerList = dff.Name.unique()
    # print(teamList)

    options = options=[
                    {'label': i, 'value': i}
                    for i in playerList]
    # print(options)


    return options




@app.callback(
    Output("Team_Checkbox", "options"),
    [Input(component_id='Season',component_property='value'),
    Input(component_id='Player_Checkbox',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')],
    [State("Team_Checkbox", "options")])

def team_options(Season, Player_Checkbox, Team_Checkbox, options):

    dff = df

    # print(Season[0])
    Smin = Season[0] # - From Range Slider
    Smax = Season[1] # - From Range Slider
    dff = dff[(dff.Season >= Smin) & (dff.Season <= Smax)]




    TeamList = dff.Team.unique()
    # print(teamList)

    options = options=[
                    {'label': i, 'value': i}
                    for i in TeamList]
    # print(options)

    return options



@app.callback(
    Output("scatter-plot", "figure"),  
    Output("datatable", "data"), 
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='dropdown_Y', component_property='value'),
    Input(component_id='dropdown_Color', component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Player_Checkbox',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value'),
    Input(component_id='AB_p',component_property='value'),
    Input(component_id='H_p',component_property='value'),
    Input(component_id='Single_p',component_property='value'),
    Input(component_id='Double_p',component_property='value'),
    Input(component_id='Triple_p',component_property='value'),
    Input(component_id='HR_p',component_property='value'),
    Input(component_id='R_p',component_property='value'),
    Input(component_id='RBI_p',component_property='value'),
    Input(component_id='BB_p',component_property='value'),
    Input(component_id='IBB_p',component_property='value'),
    Input(component_id='SB_p',component_property='value'),
    Input(component_id='CS_p',component_property='value'),
    Input(component_id='SO_p',component_property='value'),
    Input(component_id='GS_p',component_property='value'),
    Input(component_id='CG_p',component_property='value'),
    Input(component_id='ShO_p',component_property='value'),
    Input(component_id='W_p',component_property='value'),
    Input(component_id='L_p',component_property='value'),
    Input(component_id='SV_p',component_property='value'),
    Input(component_id='BS_p',component_property='value'),
    Input(component_id='IP_p',component_property='value'),
    Input(component_id='K_p',component_property='value'),
    Input(component_id='H_Allow_p',component_property='value'),
    Input(component_id='ER_Allow_p',component_property='value'),
    Input(component_id='BB_Allow_p',component_property='value'),
    Input(component_id='IBB_Allow_p',component_property='value'),
    Input(component_id='HBP_Allow_p',component_property='value'),
    Input(component_id='BK_p',component_property='value'),
    Input(component_id='WP_p',component_property='value'),
    Input(component_id='dropdown_facet', component_property='value'),
    Input(component_id='dropdown_trendline', component_property='value'),
    Input(component_id='Positions_Checkbox',component_property='value'),
    Input(component_id='input_pos_appear',component_property='value')])

def Points(dropdown_X,dropdown_Y,dropdown_Color,Season,Player_Checkbox,Team_Checkbox,AB_p,H_p,Single_p,Double_p,Triple_p,HR_p,R_p,RBI_p,BB_p,IBB_p,
SB_p,CS_p,SO_p,GS_p,CG_p,ShO_p,W_p,L_p,SV_p,BS_p,IP_p,K_p,H_Allow_p,
ER_Allow_p,BB_Allow_p,IBB_Allow_p,HBP_Allow_p,BK_p,WP_p,dropdown_facet,dropdown_trendline,Positions_Checkbox,input_pos_appear):

    dff = df

    # print(Season[0])
    Smin = Season[0] # - From Range Slider
    Smax = Season[1] # - From Range Slider
    dff = dff[(dff.Season >= Smin) & (dff.Season <= Smax)]

    if Player_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.Name.apply(lambda x: any(item for item in Player_Checkbox if item in x))]



    if Team_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.Team.apply(lambda x: any(item for item in Team_Checkbox if item in x))]



    # Player Positions
    if Positions_Checkbox == []:
        dff = dff
    else:
        PositionList = pd.DataFrame() # Clear List

        for i in Positions_Checkbox:

            PositionTemp = dff[ dff[i] >= input_pos_appear ]
            PositionList = PositionList.append(PositionTemp, ignore_index=True)

        dff = PositionList


    Total = ( (AB_p * dff['AB']) +
        (H_p * dff['H_bat']) +
        (Single_p * dff['1B']) +
        (Double_p * dff['2B']) +
        (Triple_p * dff['3B']) +
        (HR_p * dff['HR_bat']) +
        (R_p * dff['R_bat']) +
        (RBI_p * dff['RBI']) +
        (BB_p * dff['BB_bat']) +
        (IBB_p * dff['IBB_bat']) +
        (SB_p * dff['SB']) +
        (CS_p * dff['CS']) +
        (SO_p * dff['SO_bat']) +
        (GS_p * dff['GS']) +
        (CG_p * dff['CG']) +
        (ShO_p * dff['ShO']) +
        (W_p * dff['W']) +
        (L_p * dff['L']) +
        (SV_p * dff['SV']) +
        (BS_p * dff['BS']) +
        (IP_p * dff['IP']) +
        (K_p * dff['SO_pit']) +
        (H_Allow_p * dff['H_pit']) +
        (ER_Allow_p * dff['ER']) +
        (BB_Allow_p * dff['BB_pit']) +
        (IBB_Allow_p * dff['IBB_pit']) +
        (HBP_Allow_p * dff['HBP_pit']) +
        (BK_p * dff['BK']) +
        (WP_p * dff['WP']) )


    dff.Points = Total.round(1)



    scatter = px.scatter(
    dff, x=dropdown_X, y=dropdown_Y, trendline=dropdown_trendline, facet_col=dropdown_facet, facet_col_wrap=6,
    color=dropdown_Color, marginal_y='histogram', 
    hover_data=[dff.Season, dff.Name, dff.Team, dff.Age])





    table = dff[['Points','Season','Name','Age','Team','AB','H_bat','1B','2B','3B','HR_bat','R_bat','RBI','BB_bat','IBB_bat','SB','CS','SO_bat','GS','CG','ShO','W','L','SV','BS','IP','SO_pit','H_pit','ER','BB_pit','IBB_pit','HBP_pit','BK','WP']]

    data = table.to_dict('records')
    

    

    return scatter, data



if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

