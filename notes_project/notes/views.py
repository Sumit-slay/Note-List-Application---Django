from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()  # Save the form data to create a new Note object
            return redirect('note_list')  # Redirect to the note list page
    else:
        form = NoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()  # Save the form data to update the existing Note object
            return redirect('note_list')  # Redirect to the note list page
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


