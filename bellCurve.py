import csv
import pandas as pd
import plotly.figure_factory as ff

data_frame = pd.read_csv("C:/Users/sravy/White Hat Jr/Project 108- Bell Curve/data.csv")

chart = ff.create_distplot([data_frame["Average Rating"].tolist()], ["Average Rating"], colors = ['#F66095'])

chart.update_layout(
                font_family = "Courier New",
                font_size = 20,
                title_text = 'Average Ratings of Mobile Phones of different Brands on Amazon',
                title_x = 0.5,
                title_font_size = 30,
                title_font_family = "Times New Roman",
                title_font_color = "#752E47",
                legend_font_size = 20,
                legend_font_color = "#F7AAC5")

chart.update_xaxes(color = "#75515E")
chart.update_yaxes(color = "#C24C75")

chart.show()