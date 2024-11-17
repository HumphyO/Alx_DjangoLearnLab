from django.shortcuts import render
from .models import Library

def libraryDetailView(request):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

