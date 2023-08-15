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
map_height = 270
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
with open(f"{this_project}/analysis.md", "r") as f:
    project_analysis = f.read()

custom_css = """
<style>
div[data-testid="stVerticalBlock"].e1f1d6gn0 > div > div[data-testid="stVerticalBlock"].e1f1d6gn0 {
    background-color: #313636 !important;
    box-shadow: 10px 10px 15px 1px rgba(0, 0, 0, 0.3) !important;
    border: 1px solid #7a7c7c !important;
    border-radius: 15px !important;
    padding: 3% 5% 5% 5% !important;
}

.modebar-container{
    display: none !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

train_data = pd.read_parquet(
    f"{this_project}/data/dengai_cleaned.parquet"
).reset_index()

city_options = {"San Juan, Puerto Rico": "sj", "Iquitos, Peru": "iq"}
feature_options = {
    "Temperature": "station_avg_temp_c",
    "Precipitation": "station_precip_mm",
}


with st.container():
    st.write("##")
    st.markdown(project_analysis, unsafe_allow_html=True)
    # Create columns to control the layout
    left_space, city_col, feature_col, right_space = st.columns([2, 3, 3, 1])

    selected_city_name = city_col.radio(
        "Select City",
        options=list(city_options.keys()),
        horizontal=False,
        label_visibility="visible",
    )
    selected_feature = feature_col.radio(
        "Select Feauture",
        options=list(feature_options.keys()),
        horizontal=False,
        label_visibility="visible",
    )

    city_data = train_data[train_data["city"] == city_options[selected_city_name]]
    feature = feature_options[selected_feature]

    # Create a figure
    fig = go.Figure()

    # Add the station_avg_temp_c line on the primary y-axis (right), with red color
    fig.add_trace(
        go.Scatter(
            x=city_data["week_start_date"],
            y=city_data[feature],
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
        margin=dict(l=40, r=40),
        paper_bgcolor="rgba(49, 54, 54, 1)",
        plot_bgcolor="rgba(49, 54, 54, 1)",
        yaxis2=dict(
            overlaying="y",
            side="left",
            gridcolor="white",
            tickmode="sync",
            tickfont=dict(color="rgba(176, 107, 199, 1.0)"),
        ),
        yaxis=dict(
            side="right",
            gridcolor="white",
            tickfont=dict(color="rgba(83, 180, 200, 1.0)"),
        ),
        legend=dict(
            orientation="h",  # Horizontal orientation
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5,
        ),
        title=f"{selected_feature} Trends",
        title_x=0.5,  # Center the title at the middle of the x-axis
        title_xanchor="center",  # Anchor the title at its center
        xaxis=dict(
            gridcolor="white",
            rangeslider=dict(visible=True),
            type="date",
        ),
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write("\n")


# --------------------------------------------------------------
# forecasting with variable proprties to show how cases are effected
# --------------------------------------------------------------


# --------------------------------------------------------------
# Buttons
# --------------------------------------------------------------
github_link = "https://www.github.com/jeroencvlier/MultiAgent-Tennis-MADDPG"
project_buttons(github_link)
