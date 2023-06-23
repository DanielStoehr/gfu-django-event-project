import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.static import serve


@login_required
def serve_docs(request, path):
    """Serve static mkdocs documentation"""
    doc_path = settings.DOCS_DIR / path
    if os.path.isdir(doc_path):
        doc_path = os.path.join(doc_path / "index.html")
    return serve(request, doc_path, "/")
