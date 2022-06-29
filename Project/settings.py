from Frameworks.app import App

from .urls import ROUTES
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


app = App()
app.set_static('/static/', os.path.join(BASE_DIR,'static'))







app.set_routes(ROUTES)