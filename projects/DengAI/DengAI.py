from pages.utils import (
    text_loader,
    v_space,
    load_css,
    title_header,
    project_folder,
    project_buttons,
    im,
)

from datetime import timedelta

import streamlit as st

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | DengAI!",
    page_icon=im,
)

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

load_css()

custom_css2 = """
<style>

.modebar-container{
    display: none !important;
}

div[data-testid="stVerticalBlock"].e1f1d6gn0 > div > div[data-testid="stVerticalBlock"].e1f1d6gn0:not(:has(div>div>div>.PortMarker)) {
    background-color: #313636 !important;
    box-shadow: 10px 10px 15px 1px rgba(0, 0, 0, 0.3) !important;
    border: 1px solid #7a7c7c !important;
    border-radius: 15px !important;
    padding: 3% 5% 5% 5% !important;
}
.stSlider {
    width: 90% !important;
    margin-left: auto;
    margin-right: auto;
    # margin-top: -0.75rem;
}
.css-geph28 {
    margin-bottom: -0.25rem;
}

.main-svg {
    width: 98% !important;
    margin-left: auto;
    margin-right: auto;
}

div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] {
    padding: 0% 10% 0% 10% !important;
}

.modebar-container{
    display: none !important;
}

.row-widget.stButton {
    padding: 0% 5% 0% 5% !important;
}

div.row-widget.stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
    background-color: rgba(83, 180, 200, 1);
}
div[data-testid="stTickBar"] {
    display: none !important;
}
.stRadio {
            padding: 0% 5% 0% 5% !important;
        }

.stCheckbox {
            padding: 0% 5% 0% 5% !important;
        }



</style>
"""
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
st.markdown(custom_css2, unsafe_allow_html=True)


title_header("Forecasting Dengue Fever", title_class="title3", line=False)
this_project = project_folder / "DengAI"

# --------------------------------------------------------------
# Project Introduction
# --------------------------------------------------------------
v_space(1)

project_readme = text_loader(this_project, "introduction")
with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)

# --------------------------------------------------------------
# Project Map
# --------------------------------------------------------------
# create csutom css for map height on this project
# also removet the fullscreen button so the iphone display doesnt drift
v_space(1)

df_city_longlat = pd.read_csv(f"{this_project}/data/city_coordinates.csv")
st.map(df_city_longlat, size=100000, zoom=2.5)

# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------
v_space(1)

project_description = text_loader(this_project, "description")
with st.container():
    st.markdown(project_description, unsafe_allow_html=True)

# --------------------------------------------------------------
# Comparison between cities and their properties
# --------------------------------------------------------------
v_space(1)

train_data = pd.read_parquet(
    f"{this_project}/data/dengai_cleaned.parquet"
).reset_index()

city_options = {"San Juan, Puerto Rico": "sj", "Iquitos, Peru": "iq"}
feature_options = {
    "Temperature": "station_avg_temp_c",
    "Precipitation": "station_precip_mm",
    "Humidity": "reanalysis_relative_humidity_percent",
}
project_analysis = text_loader(this_project, "analysis")


with st.container():
    v_space(1)

    st.markdown(project_analysis, unsafe_allow_html=True)
    # Create columns to control the layout
    # left_space, city_col, feature_col, right_space = st.columns([1, 8, 8, 2])
    # city_col, feature_col = st.columns([1, 1])

    selected_city_name = st.radio(
        "Select City",
        options=list(city_options.keys()),
        horizontal=False,
        label_visibility="hidden",
    )
    selected_feature = st.radio(
        "Select Feauture",
        options=list(feature_options.keys()),
        horizontal=False,
        label_visibility="hidden",
    )

    left_space, log_col, right_space = st.columns([1, 3, 1])

    log_features = st.checkbox(
        "Apply log to 'Total Cases'?",
        key="log_features",
    )

    cases_column = "total_cases"
    y2_type = "log" if log_features else "linear"

    city_data = train_data[train_data["city"] == city_options[selected_city_name]]
    feature = feature_options[selected_feature]

    # Create a figure
    fig = go.Figure()

    # Add the feature line on the primary y-axis (right), with red color
    fig.add_trace(
        go.Scatter(
            x=city_data["week_start_date"],
            y=city_data[feature],
            name=f"Average {selected_feature}",
            line=dict(color="rgba(83, 180, 200, 1.0)"),
        )
    )

    # Add the total_cases line on the secondary y-axis (left), with blue color
    cases_label = "Total Cases (logged)" if log_features else "Total Cases"
    fig.add_trace(
        go.Scatter(
            x=city_data["week_start_date"],
            y=city_data[cases_column],
            name="Total Cases",
            yaxis="y2",
            line=dict(color="rgba(176, 107, 199, 1.0)"),
        )
    )

    # Window fixtures
    last_date = city_data["week_start_date"].max()
    first_date_in_last_six_months = last_date - timedelta(
        days=(36 * 30)
    )  # Approximation
    one_month = timedelta(days=30)

    fig.update_layout(
        autosize=True,
        margin=dict(l=40, r=40),
        width=800,
        paper_bgcolor="rgba(49, 54, 54, 1)",
        plot_bgcolor="rgba(49, 54, 54, 1)",
        yaxis2=dict(
            type=y2_type,
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
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5,
        ),
        title=f"{selected_feature} Trends",
        title_x=0.5,
        title_xanchor="center",
        xaxis=dict(
            gridcolor="white",
            rangeslider=dict(visible=True, autorange=True),
            type="date",
            range=[first_date_in_last_six_months, last_date],
        ),
    )

    st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------------------
# forecasting with variable proprties to show how cases are effected
# --------------------------------------------------------------
v_space(1)


def load_data(selected_city_name_wv):
    return pd.read_csv(
        f"{this_project}/data/complete_scenario_{city_options[selected_city_name_wv]}.csv"
    )


weather_variables = text_loader(this_project, "weather_variables")

with st.container():
    st.markdown(weather_variables, unsafe_allow_html=True)

    selected_city_name_wv = st.radio(
        "Select City",
        key="weather_variables",
        options=list(city_options.keys()),
        horizontal=False,
        label_visibility="hidden",
    )
    v_space(1)

    data = load_data(selected_city_name_wv)
    data["week_start_date"] = pd.to_datetime(data["week_start_date"])

    scenario_most_cases = data.drop(columns="week_start_date").sum().idxmax()
    scenario_least_cases = data.drop(columns="week_start_date").sum().idxmin()
    most_cases = eval(scenario_most_cases)
    least_cases = eval(scenario_least_cases)

    col1, col2, col3 = st.columns(3)

    # Initializing session state variables if they don't exist
    if "humidity" not in st.session_state:
        st.session_state.humidity = 0
        st.rerun()

    if "precipitation" not in st.session_state:
        st.session_state.precipitation = 0
        st.rerun()

    if "temperature" not in st.session_state:
        st.session_state.temperature = 0
        st.rerun()

    # Handle button presses
    if col1.button("Lowest Cases", use_container_width=True):
        (
            st.session_state.humidity,
            st.session_state.precipitation,
            st.session_state.temperature,
        ) = least_cases

    if col2.button("Reset", use_container_width=True):
        st.session_state.humidity = (
            st.session_state.precipitation
        ) = st.session_state.temperature = 0

    if col3.button("Highest Cases", use_container_width=True):
        (
            st.session_state.humidity,
            st.session_state.precipitation,
            st.session_state.temperature,
        ) = most_cases

    # Sliders for selecting scenarios
    new_humidity = st.slider(
        "Humidity",
        -2,
        2,
        st.session_state.humidity,
        step=1,
        key="humidity_slider",
    )

    new_precipitation = st.slider(
        "Precipitation",
        -2,
        2,
        st.session_state.precipitation,
        step=1,
        key="precipitation_slider",
    )

    new_temperature = st.slider(
        "Temperature",
        -2,
        2,
        st.session_state.temperature,
        step=1,
        key="temperature_slider",
    )

    if (
        new_humidity != st.session_state.humidity
        or new_precipitation != st.session_state.precipitation
        or new_temperature != st.session_state.temperature
    ):
        st.session_state.humidity = new_humidity
        st.session_state.precipitation = new_precipitation
        st.session_state.temperature = new_temperature

        st.rerun()

    selected_column = str(
        (
            st.session_state.humidity,
            st.session_state.precipitation,
            st.session_state.temperature,
        )
    )

    fig = go.Figure()

    # Add the total_cases line on the secondary y-axis (left), with blue color
    fig.add_trace(
        go.Scatter(
            x=data["week_start_date"],
            y=data[str(most_cases)],
            line=dict(color="rgba(176, 107, 199, 0.3)"),
        )
    )
    # Add the total_cases line on the secondary y-axis (left), with blue color
    fig.add_trace(
        go.Scatter(
            x=data["week_start_date"],
            y=data[str(least_cases)],
            line=dict(color="rgba(176, 107, 199, 0.3)"),
            fill="tonexty",
            fillcolor="rgba(176, 107, 199, 0.1)",
        )
    )
    # Add the feature line on the primary y-axis (right), with red color
    fig.add_trace(
        go.Scatter(
            x=data["week_start_date"],
            y=data[selected_column],
            line=dict(color="rgba(176, 107, 199, 1)"),
        )
    )

    # Window fixtures
    last_date = data["week_start_date"].max()
    first_date_in_last_six_months = last_date - timedelta(
        days=(36 * 30)
    )  # Approximation
    one_month = timedelta(days=30)

    fig.update_layout(
        autosize=True,
        height=200,
        margin=dict(l=40, r=40, b=0, t=25),
        paper_bgcolor="rgba(49, 54, 54, 1)",
        plot_bgcolor="rgba(49, 54, 54, 1)",
        yaxis=dict(
            side="right",
            gridcolor="white",
            # tickfont=dict(color="rgba(83, 180, 200, 1.0)"),
        ),
        showlegend=False,
        title_text=f"Total Predicted Cases",
        # title_automargin=True,
        title_x=0.5,
        title_xanchor="center",
        # title_pad=dict(l=0, r=0, t=1000, b=0),
        xaxis=dict(
            gridcolor="white",
            # rangeslider=dict(visible=True, autorange=True),
            type="date",
        ),
    )
    v_space(1)
    st.plotly_chart(fig, use_container_width=True)

    # Calculate total cases and average for the selected scenario
    total_cases = round(data[selected_column].sum())
    average_cases = round(total_cases / len(data), 2)

    cases_printout = f"""
    <div style="padding-left: 3%; padding-right: 5%; text-align: center;">
        Total Cases: {total_cases} <br>
        Average Cases (per week): {average_cases:.2f}
    </div>
    """
    st.markdown(cases_printout, unsafe_allow_html=True)
    v_space(20)


# --------------------------------------------------------------
# Credits
# --------------------------------------------------------------
v_space(1)
credit_readme = text_loader(this_project, "credit")

with st.container():
    st.markdown(credit_readme, unsafe_allow_html=True)

# --------------------------------------------------------------
# Buttons
# --------------------------------------------------------------
github_link = "https://www.github.com/jeroencvlier/DengAI"
project_buttons(github_link)
