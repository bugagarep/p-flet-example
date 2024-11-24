import flet as ft
from flet_core import RouteChangeEvent, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, AppBar, Text, \
    ViewPopEvent

from chemistry.chemistry_view import Get_chemistry_view
from mathematics.mathematics_view import Get_mathematics_view
from physics.physics_view import Get_physics_view


def main(page: ft.Page) -> None:
    page.title = "Calculator"
    """background_container = ft.Container(
        expand=True,
        image_src="Science-Subjects.png",
        image_fit=ft.ImageFit.COVER,
        opacity=0.5
    )
    page.add(background_container)"""

    def Route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # Main view
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    AppBar(title=Text("Home"), bgcolor=ft.colors.TRANSPARENT),
                    Text("Home", size=30),
                    ElevatedButton(text="Chemistry", on_click=lambda _: page.go("/chemistry")),
                    ElevatedButton(text="Mathematics", on_click=lambda _: page.go("/mathematics")),
                    ElevatedButton(text="Physics", on_click=lambda _: page.go("/physics")),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26,
                bgcolor=ft.colors.TRANSPARENT,
                decoration=ft.BoxDecoration(
                    image=ft.DecorationImage(
                        src="Science-Subjects.png",
                        fit=ft.ImageFit.COVER,
                        opacity=0.4,
                    )
                )
            )
        )

        if page.route == "/chemistry":
            page.views.append(Get_chemistry_view(page))
        elif page.route == "/mathematics":
            page.views.append(Get_mathematics_view(page))
        elif page.route == "/physics":
            page.views.append(Get_physics_view(page))

        page.update()


    def View_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = Route_change
    page.on_view_pop = View_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)