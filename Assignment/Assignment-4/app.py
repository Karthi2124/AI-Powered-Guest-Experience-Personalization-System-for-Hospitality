import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hotel_dashboard"]

# Fetch data from MongoDB
booking_data = pd.DataFrame(list(db.booking_data.find()))
dining_info = pd.DataFrame(list(db.dining_info.find()))
reviews_data = pd.DataFrame(list(db.reviews_data.find()))

# Drop MongoDB's default "_id" column
for df in [booking_data, dining_info, reviews_data]:
    df.drop(columns=["_id"], inplace=True, errors="ignore")

# Debugging - Print column names
print("Booking Data Columns:", booking_data.columns)
print("Dining Info Columns:", dining_info.columns)
print("Reviews Data Columns:", reviews_data.columns)

# Booking Data Visualization
if "number_of_stayers" in booking_data.columns and not booking_data.empty:
    booking_figure = px.histogram(
        booking_data, 
        x="number_of_stayers",
        title="Number of Stayers Distribution"
    )
else:
    booking_figure = px.histogram(pd.DataFrame({"x": []}), x="x", title="No valid data available in Booking Data")

# Dining Info Visualization
if "food_category" in dining_info.columns and "order_count" in dining_info.columns and not dining_info.empty:
    dining_figure = px.bar(
        dining_info, 
        x="food_category", 
        y="order_count",
        title="Dining Orders by Category"
    )
else:
    dining_figure = px.bar(pd.DataFrame({"x": [], "y": []}), x="x", y="y", title="No valid data available in Dining Info")

# Reviews Data Visualization
if "rating" in reviews_data.columns and not reviews_data.empty:
    reviews_figure = px.histogram(
        reviews_data, 
        x="rating",
        title="Guest Reviews Distribution"
    )
else:
    reviews_figure = px.histogram(pd.DataFrame({"x": []}), x="x", title="No valid data available in Reviews Data")

# Dash App
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Hotel Dashboard"),

    # Booking Data Section
    html.H2("Booking Data"),
    dcc.Graph(id="booking_histogram", figure=booking_figure),

    # Dining Info Section
    html.H2("Dining Information"),
    dcc.Graph(id="dining_bar_chart", figure=dining_figure),

    # Reviews Data Section
    html.H2("Guest Reviews"),
    dcc.Graph(id="reviews_histogram", figure=reviews_figure)
])

if __name__ == "__main__":
    app.run_server(debug=True)
