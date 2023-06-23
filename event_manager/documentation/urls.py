from django.urls import include, path, re_path

from .views import serve_docs

urlpatterns = [
    # 127.0.0.1/documentation/how-to-guide
    re_path(r"^(?P<path>.*)$", serve_docs)
]
