from re import template
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash
# dash component to create the app layout
from dash import html
# dash component to add data too layout
from dash import dcc


#----------------------------------------------------------------------------------------------------------------------------------------------------


# read data
steam = pd.read_csv('Valve_Player_Data.csv')
steam['Date'] = pd.to_datetime(steam['Date'], format='%Y-%m')
steam = steam.sort_values(ascending=True, by='Date')

twitch = pd.read_csv('Twitch_game_data.csv')

# data per game
gta = steam[steam['Game_Name'] == 'Grand Theft Auto V']
csgo = steam[steam['Game_Name'] == 'Counter Strike: Global Offensive']
fgu = steam[steam['Game_Name'] == 'Fall Guys: Ultimate Knockout']
pubg = steam[steam['Game_Name'] == 'PUBG: Battlegrounds']
rdr = steam[steam['Game_Name'] == 'Red Dead Redemption II']
mhw = steam[steam['Game_Name'] == 'Monster Hunter: World']
de = steam[steam['Game_Name'] == 'DOOM Eternal']
dot = steam[steam['Game_Name'] == 'DOTA 2']
rss = steam[steam['Game_Name'] == "Tom Clancy's Rainbow Six Siege"]
cpk = steam[steam['Game_Name'] == 'Cyberpunk 2077']
amu = steam[steam['Game_Name'] == 'Among Us']
des = steam[steam['Game_Name'] == 'Destiny 2']
mbb = steam[steam['Game_Name'] == 'Mount & Blade II: Bannerlord']
pha = steam[steam['Game_Name'] == 'Phasmophobia']
bor = steam[steam['Game_Name'] == 'Borderlands 3']
crk = steam[steam['Game_Name'] == 'Crusader Kings III']
ark = steam[steam['Game_Name'] == 'ARK: Survial Evolved']
sot = steam[steam['Game_Name'] == 'Sea of Thieves']
bga = steam[steam['Game_Name'] == "Baldur's Gate 3"]
wrf = steam[steam['Game_Name'] == 'Warframe']
esc = steam[steam['Game_Name'] == 'The Elder Scrolls Online']
smc = steam[steam['Game_Name'] == "Sid Meier's Civilization VI"]
hal = steam[steam['Game_Name'] == 'Halo: The Master Chief Collection']
dbd = steam[steam['Game_Name'] == 'Dead by Daylight']

# viewers per game
gta_t = twitch[twitch['Game'] == 'Grand Theft Auto V']
csgo_t = twitch[twitch['Game'] == 'Counter-Strike: Global Offensive']
lol_t = twitch[twitch['Game'] == 'League of Legends']
de_t = twitch[twitch['Game'] == 'DOOM Eternal']
rss_t = twitch[twitch['Game'] == "Tom Clancy's Rainbow Six Siege"]
cpk_t = twitch[twitch['Game'] == 'Cyberpunk 2077']


#----------------------------------------------------------------------------------------------------------------------------------------------------
# figures
#----------------------------------------------------------------------------------------------------------------------------------------------------
# fig1 

games = sorted(set(steam['Game_Name'].unique()))

fig=go.Figure()

game_plot_names = []
buttons=[]

default_game = "Counter Strike: Global Offensive"

for game_name in games:
    game = steam[steam['Game_Name'] == game_name]
   
    fig.add_trace(go.Scatter(x=game["Date"], y=game["Avg_players"], line={}, visible=(game_name==default_game)))
  
    game_plot_names.extend([game_name])
    
for game_name in games:
    buttons.append(dict(method='update',
                        label=game_name,
                        args = [{'visible': [game_name==r for r in game_plot_names]}]))

fig.add_annotation(x='2020-03-01',y=0, text='Lockdown for COVID-19', showarrow=True, arrowhead=5, ax=0, ay=-90)
# Add dropdown menus to the figure
fig.update_layout(showlegend=False, template='plotly_dark', updatemenus=[{"buttons": buttons, "direction": "down", "active": games.index(default_game), "showactive": True, "x": 0.5, "y": 1.30}])
# fig.update_yaxes(title_text='Average players')

#----------------------------------------------------------------------------------------------------------------------------------------------------
# fig2 

fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=gta['Date'],y=gta['Gain'], mode='lines+markers', name='GTA'))
fig2.add_trace(go.Scatter(x=csgo['Date'],y=csgo['Gain'], mode='lines+markers', name='CS:GO'))
fig2.add_trace(go.Scatter(x=fgu['Date'],y=fgu['Gain'], mode='lines+markers', name='Fall Guys'))
fig2.add_trace(go.Scatter(x=pubg['Date'],y=pubg['Gain'], mode='lines+markers', name='PUBG'))
fig2.add_trace(go.Scatter(x=rdr['Date'],y=rdr['Gain'], mode='lines+markers', name='Red Dead Redemption'))
fig2.add_trace(go.Scatter(x=mhw['Date'],y=mhw['Gain'], mode='lines+markers', name='Monster Hunter'))
fig2.add_trace(go.Scatter(x=de['Date'],y=de['Gain'], mode='lines+markers', name='DOOM Eternal'))
fig2.add_trace(go.Scatter(x=dot['Date'],y=dot['Gain'], mode='lines+markers', name='DOTA 2'))
fig2.add_trace(go.Scatter(x=rss['Date'],y=rss['Gain'], mode='lines+markers', name='Rainbow Seige'))
fig2.add_trace(go.Scatter(x=cpk['Date'],y=cpk['Gain'], mode='lines+markers', name='Cyberpunk 2077'))
fig2.add_trace(go.Scatter(x=amu['Date'],y=amu['Gain'], mode='lines+markers', name='Among Us'))
fig2.add_trace(go.Scatter(x=des['Date'],y=des['Gain'], mode='lines+markers', name='Destiny 2'))

fig2.update_layout(template='plotly_dark')
fig2.add_annotation(x='2020-03-01',y=0, text='Lockdown for COVID-19', showarrow=True, arrowhead=5, ax=0, ay=90)

#----------------------------------------------------------------------------------------------------------------------------------------------------
# fig 3

fig3 = go.Figure()

fig3.add_trace(go.Scatter(x=gta['Date'],y=gta['Peak_Players'], mode='lines+markers', name='GTA'))
fig3.add_trace(go.Scatter(x=csgo['Date'],y=csgo['Peak_Players'], mode='lines+markers', name='CS:GO'))
fig3.add_trace(go.Scatter(x=fgu['Date'],y=fgu['Peak_Players'], mode='lines+markers', name='Fall Guys'))
fig3.add_trace(go.Scatter(x=pubg['Date'],y=pubg['Peak_Players'], mode='lines+markers', name='PUBG'))
fig3.add_trace(go.Scatter(x=rdr['Date'],y=rdr['Peak_Players'], mode='lines+markers', name='Red Dead Redemption'))
fig3.add_trace(go.Scatter(x=mhw['Date'],y=mhw['Peak_Players'], mode='lines+markers', name='Monster Hunter'))
fig3.add_trace(go.Scatter(x=de['Date'],y=de['Peak_Players'], mode='lines+markers', name='DOOM Eternal'))
fig3.add_trace(go.Scatter(x=dot['Date'],y=dot['Peak_Players'], mode='lines+markers', name='DOTA 2'))
fig3.add_trace(go.Scatter(x=rss['Date'],y=rss['Peak_Players'], mode='lines+markers', name='Rainbow Seige'))
fig3.add_trace(go.Scatter(x=cpk['Date'],y=cpk['Peak_Players'], mode='lines+markers', name='Cyberpunk 2077'))
fig3.add_trace(go.Scatter(x=amu['Date'],y=amu['Peak_Players'], mode='lines+markers', name='Among Us'))
fig3.add_trace(go.Scatter(x=des['Date'],y=des['Peak_Players'], mode='lines+markers', name='Destiny 2'))

fig3.update_layout(template='plotly_dark')
fig3.add_annotation(x='2020-03-01',y=0, text='Lockdown for COVID-19', showarrow=True, arrowhead=5, ax=0, ay=-120)

#----------------------------------------------------------------------------------------------------------------------------------------------------
# fig 4

fig4 = make_subplots(rows=6,cols=1, subplot_titles=('GTA V','CS:GO', 'League of Legends', 'DOOM Eternal','Rainbow Six Siege','Cyberpunk 2077'))

fig4.add_trace(go.Bar(x=gta_t['Year'],y=gta_t['Avg_viewers'], marker_color='indianred',showlegend=False),row=1,col=1)
fig4.add_trace(go.Bar(x=csgo_t['Year'],y=csgo_t['Avg_viewers'], marker_color='lightsalmon',showlegend=False),row=2,col=1)
fig4.add_trace(go.Bar(x=lol_t['Year'],y=lol_t['Avg_viewers'], marker_color='goldenrod',showlegend=False),row=3,col=1)
fig4.add_trace(go.Bar(x=de_t['Year'],y=de_t['Avg_viewers'], marker_color='magenta',showlegend=False),row=4,col=1)
fig4.add_trace(go.Bar(x=rss_t['Year'],y=rss_t['Avg_viewers'], marker_color='green',showlegend=False),row=5,col=1)
fig4.add_trace(go.Bar(x=cpk_t['Year'],y=cpk_t['Avg_viewers'], marker_color='yellow',showlegend=False),row=6,col=1)
fig4.update_layout(barmode='group', height=700, template='plotly_dark')

#----------------------------------------------------------------------------------------------------------------------------------------------------
# fig 5

fig5 = make_subplots(rows=6,cols=1, subplot_titles=('GTA V','CS:GO', 'League of Legends', 'DOOM Eternal','Rainbow Six Siege','Cyberpunk 2077'))

fig5.add_trace(go.Bar(x=gta_t['Year'],y=gta_t['Streamers'], marker_color='indianred',showlegend=False),row=1,col=1)
fig5.add_trace(go.Bar(x=csgo_t['Year'],y=csgo_t['Streamers'], marker_color='lightsalmon',showlegend=False),row=2,col=1)
fig5.add_trace(go.Bar(x=lol_t['Year'],y=lol_t['Streamers'], marker_color='goldenrod',showlegend=False),row=3,col=1)
fig5.add_trace(go.Bar(x=de_t['Year'],y=de_t['Streamers'], marker_color='magenta',showlegend=False),row=4,col=1)
fig5.add_trace(go.Bar(x=rss_t['Year'],y=rss_t['Streamers'], marker_color='green',showlegend=False),row=5,col=1)
fig5.add_trace(go.Bar(x=cpk_t['Year'],y=cpk_t['Streamers'], marker_color='yellow',showlegend=False),row=6,col=1)
fig5.update_layout(barmode='group', height=700, template='plotly_dark')


#----------------------------------------------------------------------------------------------------------------------------------------------------
# fig 6

fig6 = make_subplots(rows=6,cols=1, subplot_titles=('GTA V','CS:GO', 'League of Legends', 'DOOM Eternal','Rainbow Six Siege','Cyberpunk 2077'))

fig6.add_trace(go.Bar(x=gta_t['Year'],y=gta_t['Avg_channels'], marker_color='indianred',showlegend=False),row=1,col=1)
fig6.add_trace(go.Bar(x=csgo_t['Year'],y=csgo_t['Avg_channels'], marker_color='lightsalmon',showlegend=False),row=2,col=1)
fig6.add_trace(go.Bar(x=lol_t['Year'],y=lol_t['Avg_channels'], marker_color='goldenrod',showlegend=False),row=3,col=1)
fig6.add_trace(go.Bar(x=de_t['Year'],y=de_t['Avg_channels'], marker_color='magenta',showlegend=False),row=4,col=1)
fig6.add_trace(go.Bar(x=rss_t['Year'],y=rss_t['Avg_channels'], marker_color='green',showlegend=False),row=5,col=1)
fig6.add_trace(go.Bar(x=cpk_t['Year'],y=cpk_t['Avg_channels'], marker_color='yellow',showlegend=False),row=6,col=1)
fig6.update_layout(barmode='group', height=700, template='plotly_dark')

#----------------------------------------------------------------------------------------------------------------------------------------------------


# add CSS file here
app = dash.Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# add components to layout
app.layout = html.Div( 
    children=
        [
            # html.H1('Steam Dashboard', style={'textAlign':'center', 'color':'grey'}),
            html.Div
            (
                [
                    html.Img(src='https://icons-for-free.com/iconfiles/png/128/games+steam+icon-1320191654350952195.png', className='one columns'),
                    html.H1('Steam Dashboard', style={'textAlign':'center', 'color':'grey'}, className='one columns') # , 'line-height':'2'})
                ]
            
            ,className='row'),

            html.Br(),

            html.P('Effect of Covid-19 on the Gaming Scene', style={'textAlign':'center', 'color':'white', 'backgroundColor':'grey'}),
            
            html.Div
            (
                [
                    html.Div
                        (
                            [
                                html.H3('Games Average Players', style={'textAlign':'center', 'color':'#c7d5e0'}),
                                dcc.Graph(id='figure1', figure=fig)
                            ]
                        ),

                html.Br(),

                html.Div
                    (
                        [
                            html.Div
                                (
                                    [
                                        html.H3('Gain of Players', style={'textAlign':'center', 'color':'#c7d5e0'}),
                                        dcc.Graph(id='figure2', figure=fig2)
                                    ]
                                , className='six columns'),

                            html.Div
                                (
                                    [
                                        html.H3('Number of Players at Peak Popularity', style={'textAlign':'center', 'color':'#c7d5e0'}),
                                        dcc.Graph(id='figure3', figure=fig3)
                                    ]
                                , className='six columns'),
                        ]

                    ,className='row')
                ]
            ),
            
            html.Br(),

            html.Div
            (
                [
                    html.Div
                        (   
                            [
                                html.H3('Average Viewers on Twitch', style={'textAlign':'center', 'color':'#c7d5e0'}),
                                dcc.Graph(id='figure4', figure=fig4)
                            ]
                        , className='four columns'),
                    
                    html.Div
                        (
                            [
                                html.H3('Streamers on Twitch', style={'textAlign':'center', 'color':'#c7d5e0'}),
                                dcc.Graph(id='figure5', figure=fig5)
                            ]
                        , className='four columns'),
                    
                    html.Div
                        (   
                            [
                                html.H3('Average Channels/Month on Twitch', style={'textAlign':'center', 'color':'#c7d5e0'}),
                                dcc.Graph(id='figure6', figure=fig6)
                            ]
                        , className='four columns')
                ]

            ,className='row')
        ]

    ,className='row' , style={'backgroundColor':'#171a21'}
)

app.run_server()

