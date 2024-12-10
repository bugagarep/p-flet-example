import flet as ft
from flet_core import RouteChangeEvent, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, AppBar, Text, \
    ViewPopEvent

from chemistry.chemistry_view import Get_chemistry_view
from mathematics.mathematics_view import Get_mathematics_view
from physics.Mechanical_work_and_energy.Mechanical_work_and_energy import Get_mechanical_work_view
from physics.electric_phenomena.electric_phenomena import Get_electriclPhenomena_view
from physics.mechanical_movement.mechanical_movement import Get_mehanical_movement_view
from physics.physics_view import Get_physics_view
from physics.thermal_phenomena.thermal_phenomena import Get_thermalPhenomena_view
from physics.Pressure_AchimedesLaw_Interaction_of_force_bodies.Pressure_AchimedesLaw_Interaction_of_force_bodies import Get_Pressure_Archimedes_view


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
        elif page.route == "/physics/thermalPhenomena":
            page.views.append(Get_thermalPhenomena_view(page))
        elif page.route == "/physics/electricPhenomena":
            page.views.append(Get_electriclPhenomena_view(page))
        elif page.route == "/physics/mechanicalMovement":
            page.views.append(Get_mehanical_movement_view(page))
        elif page.route == "/physics/mechanicalWork":
            page.views.append(Get_mechanical_work_view(page))
        elif page.route == "/physics/pressureArchimedesLaw":
            page.views.append(Get_Pressure_Archimedes_view(page))

        page.update()


    def View_pop(e: ViewPopEvent) -> None:
        tmp_page = page.views.pop(1)
        paths = tmp_page.route.split("/")
        if len(paths) > 1:
            page.go(f"/{paths[1]}")
        else:
            page.go("/")
        #top_view: ft.View = page.views[-1]
        #page.go(top_view.route)


    page.on_route_change = Route_change
    page.on_view_pop = View_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)