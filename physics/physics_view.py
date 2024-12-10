import flet as ft
from flet_core.colors import BLACK12, GREEN
from flet_core import RouteChangeEvent, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, AppBar, Text, \
    ViewPopEvent

from physics.thermal_phenomena.thermal_phenomena import Get_thermalPhenomena_view
def main(page: ft.Page) -> None:
    page.title = "Calculator"
    """background_container = ft.Container(
        expand=True,
        image_src="Science-Subjects.png",
        image_fit=ft.ImageFit.COVER,
        opacity=0.5
    )
    page.add(background_container)"""

    def Route_Change(e: RouteChangeEvent) -> None:
        page.views.clear()



def Get_physics_view(page):
    return ft.View(
        route="/physics",
        controls=[

            ft.AppBar(title=ft.Text("Physics"), bgcolor=ft.colors.TRANSPARENT),
            ft.Text("Physics", size=45),
            ft.ElevatedButton(text="Go back", on_click=lambda _: page.go("/")),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Thermal phenomena", on_click=lambda _: page.go("/physics/thermalPhenomena")),
                    ft.ElevatedButton(text="Electric phenomena", on_click=lambda _: page.go("/physics/electricPhenomena")),
                    ft.ElevatedButton(text="Mechanical work and energy", on_click=lambda _: page.go("/physics/mechanicalWork")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=25,
                ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Pressure.Archimedes law.Interaction of force bodies", on_click=lambda _: page.go("/physics/pressureArchimedesLaw")),
                    ft.ElevatedButton(text="Mechanical movement", on_click=lambda _: page.go("/physics/mechanicalMovement")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Library of constant values"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=26,
        bgcolor=ft.colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            image=ft.DecorationImage(
                src="physics/physics.jpg",
                fit=ft.ImageFit.COVER,
                opacity=4,
            )
        )
    )
