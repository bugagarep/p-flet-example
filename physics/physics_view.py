import flet as ft

def Get_physics_view(page):
    return ft.View(
        route="/physics",
        controls=[
            ft.AppBar(title=ft.Text("Physics"), bgcolor=ft.colors.TRANSPARENT),
            ft.Text("Physics", size=30),
            ft.ElevatedButton(text="Go back", on_click=lambda _: page.go("/"))
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=26,
        bgcolor=ft.colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            image=ft.DecorationImage(
                src="physics/physics.jpg",
                fit=ft.ImageFit.COVER,
                opacity=0.4,
            )
        )
    )