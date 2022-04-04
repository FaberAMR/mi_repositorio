from multiprocessing import context
from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render

class ParienteView(TemplateView):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
         return super().get_context_data(**kwargs)