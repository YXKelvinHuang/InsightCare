"""The home page of the app."""

from test import styles
from test.templates import template
from test.state import State

import reflex as rx
color = "rgb(107,99,246)"
# def title() -> rx.Component:
#     return rx.button("",
#                 rx.text("Welcome to InsightCare"),
#                   bg = "lightblue",
#                   )
    # rx.text("Hello World!", color="blue", font_size="1.5em")

def logo() ->rx.Component:
    return rx.image(src="/logo2.png", width="13em",
                    style={
                        'position': 'fixed',
                        'left': '10',
                        'bottom': '750',
                    })

def aboutus() ->rx.Component:
    return rx.image(src="/aboutus.png", width="7em",
                    style={
                        'position': 'fixed',
                        'right': '200',
                        'bottom': '700',
                    })

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=styles.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=styles.answer_style),
            text_align="left",
        ),
    )


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is InsightCare?",
            "A pre-consultation web app about postpartum depression!",
        ),
        (
            "What can I make with it?",
            "Nothing",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ],
        style={
            'position': 'fixed',
            'right': '10',
            'bottom': '200',
            'z_index': '1000',  # Optional, to make sure it's above other elements
        }
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.button("", 
                  rx.link("Begin your journey!", 
                          style={
                              'button_style': {
                                  'padding': '15px 30px',
                                  'margin': '10px',
                                  'border-radius': '8px',
                                  'transition': 'all 0.3s ease'
                              },
                              'background_image': "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 80%)",
                              'background_clip': "text",
                              'font_weight': "bold",
                              'font_size': "1.5em",
                              'hover': {
                                  'transform': 'scale(1.05)',
                                  'box-shadow': '0px 4px 20px rgba(0, 0, 0, 0.1)'
                              }
                          },
                          href="/about")
                  ),
        style={
            'position': 'fixed',
            'right': '125px',
            'bottom': '50px',
            'z_index': '1000',  # Optional, to make sure it's above other elements
        }
    )


# return rx.button(
#         "", 
#         rx.link(rx.image(src="/longlogo2.png",width="41em",length="1000em"), href="/about"),variant="unstyled",
#         style={
#             'position': 'fixed',
#             'left': '0',
#             'bottom': '700',
#             'z_index': '1000',  # Optional, to make sure it's above other elements
#         }
#     )

# def upload()->rx.Component:
#     """The main view."""
#     return rx.vstack(
#         rx.upload(
#             rx.vstack(
#                 rx.button(
#                     "Select File",
#                     color=color,
#                     bg="white",
#                     border=f"1px solid {color}",
#                 ),
#                 rx.text(
#                     "Drag and drop files here or click to select files"
#                 ),
#             ),
#             border=f"1px dotted {color}",
#             padding="5em",
#         ),
#         rx.hstack(rx.foreach(rx.selected_files, rx.text)),
#         rx.button(
#             "Upload",
#             on_click=lambda: State.handle_upload(
#                 rx.upload_files()
#             ),
#         ),
#         rx.button(
#             "Clear",
#             on_click=rx.clear_selected_files,
#         ),
#         # rx.foreach(
#         #     State.img, lambda img: rx.image(src=img)
#         # ),
#         padding="5em",
#         style={
#             'position': 'fixed',
#             'left': '0',
#             'bottom': '50',
#             'z_index': '1000',  # Optional, to make sure it's above other elements
#         }
#     )

#Function
def another_page()-> rx.Component:
    #return rx.link("About page", href="/about")
    return rx.button(
        "", 
        rx.link(rx.image(src="/longlogo2.png",width="41em",length="1000em"), href="/about"),variant="unstyled",
        style={
            'position': 'fixed',
            'left': '0',
            'bottom': '700',
            'z_index': '1000',  # Optional, to make sure it's above other elements
        }
    )

# def upload()-> rx.Component:
#     return rx.fragment(
#         rx.upload(rx.text("Upload files"), rx.icon(tag="upload")),
#         rx.button(on_submit=State.<your_upload_handler>)
#     )

def index() -> rx.Component:
    return rx.container(
        #title(),
        logo(),
        aboutus(),
        chat(),
        another_page(),
        action_bar(),
        # upload(),
    )

# @template(route="/", title="Home", image="/github.svg")
# def index() -> rx.Component:
#     """The home page.

#     Returns:
#         The UI for the home page.
#     """
#     with open("README.md", encoding="utf-8") as readme:
#         content = readme.read()
#     return rx.markdown(content, component_map=styles.markdown_style)


# def index():
#     return rx.heading(
#         "Welcome to Reflex!",
#         # Event handlers can be bound to event triggers.
#         on_click=ExampleState.next_color,
#         # State vars can be bound to component props.
#         color=ExampleState.color,
#         _hover={"cursor": "pointer"},
#     )