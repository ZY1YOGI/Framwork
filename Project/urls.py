from Frameworks.router import Path
from account import views

ROUTES = [
    Path('/', views.print_received),
    Path('/json', views.json_point),
    Path('/test', views.test),
]