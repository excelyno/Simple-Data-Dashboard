import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from utils.data_processing import load_data, get_summary_statistics

app = dash.Dash(__name__)

# Load data
df = load_data('data/data.csv')

# App layout
app.layout = html.Div([
    html.H1("Dashboard Data Analyst"),
    
    # Dropdown untuk memilih kolom
    dcc.Dropdown(id="select_column",
                 options=[{"label": col, "value": col} for col in ['Annual Salary', 'Bonus %', 'Age']],
                 multi=False,
                 value='Annual Salary',
                 style={'width': "40%"}),

    # Grafik garis
    dcc.Graph(id="line_chart", figure={}),
    
    # Summary statistics
    html.Div(id="summary_stats", style={'margin-top': '20px'})
])

# Callback untuk memperbarui grafik dan statistik
@app.callback(
    [Output('line_chart', 'figure'),
     Output('summary_stats', 'children')],
    [Input('select_column', 'value')]
)
def update_dashboard(column_name):
    fig = px.histogram(df, x=column_name, title=f'Distribusi {column_name}')
    stats = get_summary_statistics(df, column_name)
    stats_text = [
        html.P(f"Mean: {stats['mean']:.2f}"),
        html.P(f"Median: {stats['median']:.2f}"),
        html.P(f"Max: {stats['max']:.2f}"),
        html.P(f"Min: {stats['min']:.2f}")
    ]
    return fig, stats_text

if __name__ == '__main__':
    app.run_server(debug=True)
