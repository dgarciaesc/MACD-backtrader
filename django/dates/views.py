from django.views.generic.edit import CreateView
from .forms import Promise
from .forms import PromiseForm

class PromiseCreateView(CreateView):
    model = Promise
    form_class = PromiseForm