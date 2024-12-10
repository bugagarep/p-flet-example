import flet as ft

def Get_electriclPhenomena_view(page):
    return ft.View(
        route="/electricPhenomena",
        controls=[
            ft.AppBar(title=ft.Text("ElectricPhenomena"), bgcolor=ft.colors.TRANSPARENT),
            ft.Text("ElectricPhenomena", size=45),
            ft.ElevatedButton(text="Go back", on_click=lambda _: page.go("/")),
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
