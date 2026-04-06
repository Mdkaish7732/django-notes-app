from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm, SearchForm
from django.http import JsonResponse

# View to display all notes and search functionality
def index(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            notes = Note.objects.filter(title__icontains=query)
        else:
            notes = Note.objects.all()
    else:
        notes = Note.objects.all()
    
    return render(request, 'notes/index.html', {'notes': notes, 'form': form})


# View to add a new note
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    
    return render(request, 'notes/add_note.html', {'form': form})


# ✅ Edit Note
def edit_note(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/add_note.html', {'form': form})


# ✅ Delete Note
def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('index')


# API view to return all notes in JSON format
def notes_api(request):
    notes = Note.objects.all().values('id', 'title', 'content', 'created_at')
    return JsonResponse(list(notes), safe=False)