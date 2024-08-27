import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Week 1 - Data and visualization")
st.markdown("Here we can see the dataframe created during this week's project.")

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)
PRICE = 666

# We have a limited budget, therefore we would like to exclude
# listings with a price above 100 Hong Kong dollars per night
dataframe = dataframe[dataframe["Price"] <= PRICE]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "HK$ " + dataframe["Price"].round(2).astype(str)
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)

# Add a new column 'color' and assign colors based on 'Location'
dark_blue = "#00008B"
pale_blue = "#9fc5e8"
dataframe['color'] = [dark_blue if location == 'To visit' else pale_blue for location in dataframe["Location"]]

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a pale blue dot and the location we've chosen with a darker blue dot.")

# Plot the map
st.map(data=dataframe, latitude="Latitude", longitude="Longitude", color='color', size=None, zoom=None, use_container_width=True)
