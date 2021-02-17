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

df.Season_bat = pd.to_numeric(df.Season_bat)

df = df[df['Season_bat'] >= 2000]

min_year = df.Season_bat.min()
max_year = df.Season_bat.max()

df['Points'] = 0

dttable = ['Points','Season_bat','Name_bat','Age_bat','Team_bat','AB_bat','H_bat','1B_bat','2B_bat','3B_bat','HR_bat','R_bat','RBI_bat','BB_bat','IBB_bat','SB_bat','CS_bat','SO_bat','GS_pit','CG_pit','ShO_pit','W_pit','L_pit','SV_pit','BS_pit','IP_pit','SO_pit','H_pit','ER_pit','BB_pit','IBB_pit','HBP_pit','BK_pit','WP_pit']



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
                # X-Axis
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
                        value='AB_bat',
                        placeholder="X-Axis",
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
                    
                ], style={'margin-left': '1%', 'margin-right': '2%'}),

            ]),

            ], width= 8, style={'margin-left': '0.5%', 'margin-right': '2%'}), # Center Graph



        ]), # End Points Row


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
    dff = dff[(dff.Season_bat >= Smin) & (dff.Season_bat <= Smax)]


    if Team_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.Team_bat.apply(lambda x: any(item for item in Team_Checkbox if item in x))]


    playerList = dff.Name_bat.unique()
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
    dff = dff[(dff.Season_bat >= Smin) & (dff.Season_bat <= Smax)]




    TeamList = dff.Team_bat.unique()
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
    Input(component_id='WP_p',component_property='value')])

def Points(dropdown_X,Season,Player_Checkbox,Team_Checkbox,AB_p,H_p,Single_p,Double_p,Triple_p,HR_p,R_p,RBI_p,BB_p,IBB_p,
SB_p,CS_p,SO_p,GS_p,CG_p,ShO_p,W_p,L_p,SV_p,BS_p,IP_p,K_p,H_Allow_p,
ER_Allow_p,BB_Allow_p,IBB_Allow_p,HBP_Allow_p,BK_p,WP_p):

    dff = df

    # print(Season[0])
    Smin = Season[0] # - From Range Slider
    Smax = Season[1] # - From Range Slider
    dff = dff[(dff.Season_bat >= Smin) & (dff.Season_bat <= Smax)]

    if Player_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.Name_bat.apply(lambda x: any(item for item in Player_Checkbox if item in x))]



    if Team_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.Team_bat.apply(lambda x: any(item for item in Team_Checkbox if item in x))]



    Total = ( (AB_p * dff['AB_bat']) +
        (H_p * dff['H_bat']) +
        (Single_p * dff['1B_bat']) +
        (Double_p * dff['2B_bat']) +
        (Triple_p * dff['3B_bat']) +
        (HR_p * dff['HR_bat']) +
        (R_p * dff['R_bat']) +
        (RBI_p * dff['RBI_bat']) +
        (BB_p * dff['BB_bat']) +
        (IBB_p * dff['IBB_bat']) +
        (SB_p * dff['SB_bat']) +
        (CS_p * dff['CS_bat']) +
        (SO_p * dff['SO_bat']) +
        (GS_p * dff['GS_pit']) +
        (CG_p * dff['CG_pit']) +
        (ShO_p * dff['ShO_pit']) +
        (W_p * dff['W_pit']) +
        (L_p * dff['L_pit']) +
        (SV_p * dff['SV_pit']) +
        (BS_p * dff['BS_pit']) +
        (IP_p * dff['IP_pit']) +
        (K_p * dff['SO_pit']) +
        (H_Allow_p * dff['H_pit']) +
        (ER_Allow_p * dff['ER_pit']) +
        (BB_Allow_p * dff['BB_pit']) +
        (IBB_Allow_p * dff['IBB_pit']) +
        (HBP_Allow_p * dff['HBP_pit']) +
        (BK_p * dff['BK_pit']) +
        (WP_p * dff['WP_pit']) )


    dff.Points = Total


    scatter = px.scatter(
    dff, x=dropdown_X, y=dff.Points, 
    color=dff.Team_bat, size=dff.AB_bat, marginal_y='histogram',
    hover_data=[dff.Season_bat, dff.Name_bat, dff.Team_bat, dff.Age_bat])





    table = dff[['Points','Season_bat','Name_bat','Age_bat','Team_bat','AB_bat','H_bat','1B_bat','2B_bat','3B_bat','HR_bat','R_bat','RBI_bat','BB_bat','IBB_bat','SB_bat','CS_bat','SO_bat','GS_pit','CG_pit','ShO_pit','W_pit','L_pit','SV_pit','BS_pit','IP_pit','SO_pit','H_pit','ER_pit','BB_pit','IBB_pit','HBP_pit','BK_pit','WP_pit']]

    data = table.to_dict('records')
    

    

    return scatter, data



if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

