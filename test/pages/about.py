from test import styles
from test.templates import template
from test.state import State

import reflex as rx

color = "rgb(107,99,246)"



def main_button()-> rx.Component:
    #return rx.link("About page", href="/about")
    return rx.button(
        rx.link(rx.image(src="/logo22.png", width="13em"), href="http://localhost:3000"),variant="unstyled",
        style={
                'position': 'fixed',
                'left': '0',
                'bottom': '700',
            }
    )


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=styles.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=styles.answer_style,
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        style={
            'float' : 'right',
            'bottom': '90',
        }
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Send a message",
            on_change=State.set_question,
            style=styles.input_style,
        ),
        rx.button(
            "Send",
            on_click=State.answer,
            style=styles.button_style,
        ),
        style={
            'position': 'fixed',
            'left': '5',
            'bottom': '20',
        }
    )


def about() -> rx.Component:
    return rx.container(
        main_button(),
        # upload(),
        chat(),
        action_bar(),
    )



# def button()-> rx.Component:
#     #return rx.link("About page", href="/about")
#     return rx.button(
#         "", 
#         rx.link("Main", href="http://localhost:3000"),
#         bg="lightblue", color="black", size="sm",color_scheme='teal',
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
