## In this second dahs example we introduce now plots along with the map

#importing the necessary libraries, and new important dependencies such as Input and Output
import geopandas as gpd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
#Input will be the source data and Output the result of our call back function

app = Dash(__name__)

#Reading the data using the relative path
gdf: gpd.GeoDataFrame = gpd.read_file('saude_rmpa.geojson')

#to test if the data is being read correctly
#print(gdf)

#assigning a CRS to the project
gdf = gdf.to_crs(4326)

#The first thing will be to create a dropdown menu so we can choose which variable we want to analyze
#We will start by creating new columns
cols = [{'label': col, 'value':col} for col in ['ubs', 'hospitais', 'caps']]

#To generate the dropdown menu we need to alter the layout
app.layout = html.Div(
    [
        html.H1('Mapa coroplético saúde de RMPA', style={'textAlign': 'center'}),
        dcc.Dropdown(
            id='column-dropdown',
            options=cols,
            value='ubs',
            clearable=False,
            style={'width': '50%', 'margin': 'auto'}
        ),
    html.Div([
        dcc.Graph(id='choropleth-map', style={'display':'inline-block', 'width':'50%'}),
        dcc.Graph(id='histogram', style={'display': 'inline-block','width':'50%'})
    ])
])

#Now let's create the call back
@app.callback(
    [Output('choropleth-map', 'figure'), Output('histogram', 'figure')],
    [Input('column-dropdown', 'value')]
)
def update_graphs(selected_column):
    fig_map = px.choropleth(gdf, #Adding the geodataframe
        geojson=gdf.geometry, #creating a cathegory for the shapefile of all the zones
        locations = gdf.index, #creating an index based on locations or zones
        color = selected_column, #the color will varry according to the number of hospitals in each zone
        hover_name= 'codigo', #assigning the name of the hover as the cathegory color from our geojson
        title= 'Chloropleth map of hospitals in Porto Alegre, Brazil')
    fig_map.update_geos(fitbounds='locations', visible=False)
    
    fig_hist = px.histogram(gdf,
        x=selected_column,
        nbins=20,
        title=f'Histograma:{selected_column}'
    )
    return fig_map, fig_hist

if __name__ == '__main__':
    app.run_server(debug=True)