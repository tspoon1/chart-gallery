# three_charts.py

import plotly
import plotly.graph_objs as go

#
# CHART 1 (PIE)
#

#pie_data = [
#    {"company": "Company X", "market_share": 0.55},
#    {"company": "Company Y", "market_share": 0.30},
#    {"company": "Company Z", "market_share": 0.15}
#]
#
#company_list = [x["company"] for x in pie_data]
#market_share_list = [x["market_share"] for x in pie_data]
#
#labels = company_list
#values = market_share_list
#
#trace = go.Pie(labels=labels, values=values)
#
#plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)

#print("----------------")
#print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data

#
# CHART 2 (LINE)
#

#line_data = [
#    {"date": "2019-01-01", "stock_price_usd": 100.00},
#    {"date": "2019-01-02", "stock_price_usd": 101.01},
#    {"date": "2019-01-03", "stock_price_usd": 120.20},
#    {"date": "2019-01-04", "stock_price_usd": 107.07},
#    {"date": "2019-01-05", "stock_price_usd": 142.42},
#    {"date": "2019-01-06", "stock_price_usd": 135.35},
#    {"date": "2019-01-07", "stock_price_usd": 160.60},
#    {"date": "2019-01-08", "stock_price_usd": 162.62},
#]
#
#
#date_list = [x["date"] for x in line_data]
#stock_price_list = [x["stock_price_usd"] for x in line_data]
#    
#plotly.offline.plot({
#    "data": [go.Scatter(x=date_list, y=stock_price_list)],
#    "layout": go.Layout(title="Stock Prices Over Time")
#}, auto_open=True)


#print("----------------")
#print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data




#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

genre_list = [x["genre"] for x in bar_data]
viewer_count_list = [x["viewers"] for x in bar_data]

fig = go.Figure(go.Bar(
            x=viewer_count_list,
            y=genre_list,
            orientation='h'))

fig.show()

#print("----------------")
#print("GENERATING BAR CHART...")
#print(bar_data) # TODO: create a horizontal bar chart based on the bar_data