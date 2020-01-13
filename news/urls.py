from django.urls import path
from news.views import NewsView

app_name = "news"

urlpatterns = [
    path(r'', NewsView.as_view()),
]