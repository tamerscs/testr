from flet import *

def main(page: Page):
    page.title = 'Test'
    page.bgcolor = 'Black'
    page.window.width = 370
    page.window.height = 740
    
    
    def close_app(e):
        page.window_close()
    
    
    container = Container(
        content=Column(
            controls=[
                Text(
                    value="تامر",
                    size=24,
                    weight=FontWeight.BOLD,
                    color='black',
                    text_align=TextAlign.CENTER  
                ),
                ElevatedButton(
                    text="خروج",
                    on_click=close_app,  
                )
            ],
            alignment=MainAxisAlignment.CENTER,  
            horizontal_alignment=CrossAxisAlignment.CENTER  
        ),
        height=720,
        bgcolor='white',
        border_radius=25,
        alignment=alignment.center  
    )
    
    page.add(container)
    page.update()

app(target=main)
