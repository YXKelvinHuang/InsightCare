"""Welcome to Reflex!."""

from test import styles
from test.state import State
# Import all the pages.
from test.pages import *

import reflex as rx

from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# accent_color = "#f81ce5"
# style = {
#     "::selection": {
#         "background_color": accent_color,
#     },
#     ".some-css-class": {
#         "text_decoration": "underline",
#     },
#     "#special-input": {"width": "20vw"},
#     # rx.Text: {
#     #     "font_family": styles.SANS,
#     # },
#     rx.Divider: {
#         "margin_bottom": "1em",
#         "margin_top": "0.5em",
#     },
#     rx.Heading: {
#         "font_weight": "500",
#     },
#     rx.Code: {
#         "color": accent_color,
#     },
# }

app = rx.App()
# Add state and page to the app.
# app = rx.App()
app.add_page(index)
# app.add_page(question,route="/question")
app.add_page(about,route="/about")
app.compile()


# # Create the app and compile it.
# app = rx.App(style=styles.base_style)
# app.compile()
