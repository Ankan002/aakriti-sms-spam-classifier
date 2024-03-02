from streamlit_extras.let_it_rain import rain

def animation():
    rain(
        emoji="❌",
        font_size=64,
        falling_speed=1.5,
        animation_length="10",
    )