import flet as ft

def Get_chemistry_view(page):
    return ft.View(
        route="/chemistry",
        controls=[
            ft.AppBar(title=ft.Text("Chemistry"), bgcolor=ft.colors.TRANSPARENT),
            ft.Text("Chemistry", size=30),
            ft.ElevatedButton(text="Go back", on_click=lambda _: page.go("/"))
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=26,
        bgcolor=ft.colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            image=ft.DecorationImage(
                src="chemistry/chemistry.jpg",
                fit=ft.ImageFit.COVER,
                opacity=0.4,
            )
        )
    )