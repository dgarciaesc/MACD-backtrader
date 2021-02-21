from datetime import date
import dash
import dash_html_components as html
import dash_core_components as dcc
import re
from download_data_btc import download_trade_files

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(2020, 1, 1),
        max_date_allowed=date(2021, 2, 1),
        initial_visible_month=date(2020, 8, 1),
        end_date=date(2021, 2, 1)
    ),
    html.Div(id='output-container-date-picker-range'),
    html.Button(
                'Send Dates!',
                id='button'
            )
])
start_date=None
end_date=None

@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date'),
     dash.dependencies.Input('button', 'n_clicks')]
)
def update_output(start_date, end_date,n_clicks):
    if n_clicks!=0:
        string_prefix = 'You have selected: '
        if start_date is not None:
            if end_date is not None:
                download_trade_files(start_date,end_date)
        if len(string_prefix) == len('You have selected: '):
            return 'Select a date to see it displayed here'
        else:
            return string_prefix


if __name__ == '__main__':
    app.run_server(debug=True)