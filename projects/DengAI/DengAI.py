from pages.utils import (
    load_css,
    title_header,
    project_folder,
    project_buttons,
    im,
)

import streamlit as st

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | DengAI!",
    page_icon=im,
)

import pandas as pd
import plotly.graph_objects as go

load_css()
title_header("Forecasting Dengue Fever", title_class="title3", line=False)
this_project = project_folder / "DengAI"


# --------------------------------------------------------------
# Project Introduction
# --------------------------------------------------------------

with open(f"{this_project}/introduction.md", "r") as f:
    project_readme = f.read()


with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)


# --------------------------------------------------------------
# Project Map
# --------------------------------------------------------------

# create csutom css for map height on this project
# also removet the fullscreen button so the iphone display doesnt drift
map_height = 260
map_css = f"""
    <style>
        button[title="View fullscreen"].css-1xulgw9 {{
            display: none !important;
        }}
        .mapboxgl-map {{
            height: {map_height}px !important;
        }}
        #deckgl-overlay {{
            height: {map_height}px !important;
        }}
        .stDeckGlJsonChart {{
            height: {map_height}px !important;
        }}
    </style>
    """
st.markdown(map_css, unsafe_allow_html=True)

df_city_longlat = pd.read_csv(f"{this_project}/data/city_coordinates.csv")
st.map(df_city_longlat, size=100000, zoom=2.5)

# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------
# st.write("##")

with open(f"{this_project}/description.md", "r") as f:
    project_readme = f.read()


with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)


# --------------------------------------------------------------
# Comparison between cities and their properties
# --------------------------------------------------------------
train_data = pd.read_parquet(
    f"{this_project}/data/dengai_cleaned.parquet"
).reset_index()
city_options = {"San Juan, Puerto Rico": "sj", "Iquitos, Peru": "iq"}
# st.markdown('<div class="PortMarker">', unsafe_allow_html=True)

custom_css = """
<style>

div[data-testid="stVerticalBlock"].css-1n76uvr.e1f1d6gn0 > div > div[data-testid="stVerticalBlock"].css-1n76uvr.e1f1d6gn0 {
    background-color: #313636 !important;
    box-shadow: 10px 10px 15px 1px rgba(0, 0, 0, 0.3) !important;
    border: 1px solid #7a7c7c !important;
    border-radius: 15px !important;
    padding: 3% 5% 5% 5% !important;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


with st.container():
    # Create columns to control the layout
    left_space, center_col, right_space = st.columns([1, 2, 1])

    selected_city_name = center_col.radio(
        "", options=list(city_options.keys()), horizontal=True
    )
    city_data = train_data[train_data["city"] == city_options[selected_city_name]]

    # Create a figure
    fig = go.Figure()

    # Add the station_avg_temp_c line on the primary y-axis (right), with red color
    fig.add_trace(
        go.Scatter(
            x=city_data["week_start_date"],
            y=city_data["station_avg_temp_c"],
            name="Average Temperature",
            line=dict(color="rgba(83, 180, 200, 1.0)"),
        )
    )

    # Add the total_cases line on the secondary y-axis (left), with blue color
    fig.add_trace(
        go.Scatter(
            x=city_data["week_start_date"],
            y=city_data["total_cases"],
            name="Total Cases",
            yaxis="y2",
            line=dict(color="rgba(176, 107, 199, 1.0)"),
        )
    )

    # Update the layout to create a secondary y-axis on the left and add a date slider
    fig.update_layout(
        autosize=True,
        # width=600,
        # margin_pad=60,
        # title_pad=dict(l=20, r=20, t=20, b=20),  # Adjust the values as needed
        # margin=dict(t=500),
        # newshape_label_padding=600,
        paper_bgcolor="rgba(49, 54, 54, 1)",  # Adjust the color as needed
        plot_bgcolor="rgba(49, 54, 54, 1)",  # Adjust the color as needed
        yaxis2=dict(
            title="Total Cases",
            titlefont=dict(color="white"),
            tickfont=dict(color="white"),
            overlaying="y",
            side="left",
            gridcolor="white",
            showgrid=False,  # Hide gridlines for the secondary y-axis
        ),
        yaxis=dict(
            title="Average Temperature",
            titlefont=dict(color="white"),
            tickfont=dict(color="white"),
            side="right",
            gridcolor="white",
        ),
        legend=dict(
            orientation="h",  # Horizontal orientation
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5,
        ),
        title="Temperature Trends",
        title_x=0.5,  # Center the title at the middle of the x-axis
        title_xanchor="center",  # Anchor the title at its center
        xaxis=dict(
            gridcolor="white",
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1M", step="month", stepmode="backward"),
                        dict(count=6, label="6M", step="month", stepmode="backward"),
                        dict(count=1, label="1Y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        ),
    )
    # Create columns with specific proportions
    # left_space, center_col, right_space = st.columns(
    #     [1, 10, 1]
    # )  # Adjust these values to your preference

    # # Plot the Plotly chart in the center column
    # with center_col:
    #     st.plotly_chart(fig)
    st.plotly_chart(fig)
    # Displaying the chart in Streamlit
    # st.plotly_chart(fig)  # Displaying the chart in Streamlit


# --------------------------------------------------------------
# forecasting with variable proprties to show how cases are effected
# --------------------------------------------------------------
# Start of the custom container with "PortMarker" class

# train_data = pd.read_parquet(
#     f"{this_project}/data/dengai_cleaned.parquet"
# ).reset_index()
# city_options = {"San Juan, Puerto Rico": "sj", "Iquitos, Peru": "iq"}

# # Create columns inside the custom container
# left_space, center_col, right_space = st.columns([1, 2, 1])

# # Add radio buttons to the center column
# selected_city_name = center_col.radio(
#     "Select the City",
#     options=list(city_options.keys()),
#     horizontal=True,
#     label_visibility="hidden",
# )
# city_data = train_data[train_data["city"] == city_options[selected_city_name]]

# fig = go.Figure()
# # Add the station_avg_temp_c line on the primary y-axis (right), with red color
# fig.add_trace(
#     go.Scatter(
#         x=city_data["week_start_date"],
#         y=city_data["station_avg_temp_c"],
#         name="Average Temperature",
#         line=dict(color="red"),
#     )
# )

# # Add the total_cases line on the secondary y-axis (left), with blue color
# fig.add_trace(
#     go.Scatter(
#         x=city_data["week_start_date"],
#         y=city_data["total_cases"],
#         name="Total Cases",
#         yaxis="y2",
#         line=dict(color="blue"),
#     )
# )

# # Update the layout to create a secondary y-axis on the left and add a date slider
# fig.update_layout(
#     yaxis2=dict(
#         title="Total Cases",
#         titlefont=dict(color="blue"),
#         tickfont=dict(color="blue"),
#         overlaying="y",
#         side="left",
#     ),
#     yaxis=dict(
#         title="Average Temperature",
#         titlefont=dict(color="red"),
#         tickfont=dict(color="red"),
#         side="right",
#     ),
#     legend=dict(
#         orientation="h",  # Horizontal orientation
#         yanchor="bottom",
#         y=1,
#         xanchor="center",
#         x=0.5,
#     ),
#     title="Temperature Trends",
#     xaxis=dict(
#         rangeselector=dict(
#             buttons=list(
#                 [
#                     dict(count=1, label="1M", step="month", stepmode="backward"),
#                     dict(count=6, label="6M", step="month", stepmode="backward"),
#                     dict(count=1, label="1Y", step="year", stepmode="backward"),
#                     dict(step="all"),
#                 ]
#             )
#         ),
#         rangeslider=dict(visible=True),
#         type="date",
#     ),
# )

# # Displaying the chart in Streamlit
# st.plotly_chart(fig)  # Displaying the chart in Streamlit


# --------------------------------------------------------------
# Buttons
# --------------------------------------------------------------
github_link = "https://www.github.com/jeroencvlier/MultiAgent-Tennis-MADDPG"
project_buttons(github_link)
