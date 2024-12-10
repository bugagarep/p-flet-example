import flet as ft

def Get_Pressure_Archimedes_view(page):
    return ft.View(
        route="/physics/pressureArchimedesLaw",
        controls=[
            ft.AppBar(title=ft.Text("Pressure.Archimedes law.Interaction of force bodies"), bgcolor=ft.colors.TRANSPARENT),
            ft.Text("Pressure.Archimedes law.Interaction of force bodies", size=45),
            ft.ElevatedButton(text="Go back", on_click=lambda _: page.go("/physics")),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="I=U/R"),
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
