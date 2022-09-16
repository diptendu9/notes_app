
from pyexpat import model
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
# Create your views here.

class NotesDeleteView(DeleteView):
    model= Notes
    success_url= '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model=Notes
    success_url= '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model=Notes
    # fields= ['title', 'text']
    success_url= '/smart/notes'
    form_class = NotesForm


class NoteListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name= 'notes/notes_list.html'

# def list(request):
#     all_notes= Notes.objects.all()
#     return render(request, 'note_list.html', {'notes':all_notes})


class NoteDetailView(DetailView):
    model= Notes
    context_object_name= "note"
    template_name= 'notes/note_detail.html'

# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes doesn't exist")
#     return render(request, 'notes/note_detail.html', {'notes': note})