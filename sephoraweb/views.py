from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .models import BeautyReview, Beauty,Good
from .forms import BeautyForm, GoodForm


class BeautyList(ListView):

    queryset = Beauty.objects.all().order_by('-date')
    context_object_name = 'latest_beauty_list'
    template_name = 'sephoraweb/beauty_list.html'


class BeautyDetail(DetailView):
    model = Beauty
    template_name = 'sephoraweb/beauty_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BeautyDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = BeautyReview.RATING_CHOICES
        return context


class BeautyCreate(CreateView):
    model = Beauty
    template_name = 'sephoraweb/form.html'
    form_class = BeautyForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BeautyCreate, self).form_valid(form)


class BeautyEdit(UpdateView):
    model = Beauty
    template_name = 'sephoraweb/form.html'
    form_class = BeautyForm


class GoodDetail(DetailView):
    model = Good
    template_name = 'sephoraweb/good_detail.html'


class GoodCreate(CreateView):
    model = Good
    template_name = 'sephoraweb/form.html'
    form_class = GoodForm

    # Associate form.instance.user with self.request.user and get pk value.
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.beauty = Beauty.objects.get(id=self.kwargs['pk'])
        return super(GoodCreate, self).form_valid(form)


class GoodEdit(UpdateView):
    model = Good
    template_name = 'sephoraweb/form.html'
    form_class = GoodForm


def review_create(request, pk):
    beauty = get_object_or_404(Beauty, pk=pk)
    review = BeautyReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        beauty=beauty)
    review.save()
    return HttpResponseRedirect(reverse('sephoraweb:beauty_detail', args=[pk]))

