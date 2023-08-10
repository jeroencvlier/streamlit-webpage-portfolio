import streamlit.components.v1 as components


def og_tags():
    _component_func = components.declare_component(
        "og_tags", url="https://wwwjeroencvlier.com"
    )

    return _component_func()
