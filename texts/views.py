from django.db import connection, transaction
from django.shortcuts import render

from .models import OneTimeText


def _supports_skip_locked():
    vendor = connection.vendor
    return vendor in {'postgresql', 'mysql', 'oracle'}


@transaction.atomic
def sentence_page(request):
    queryset = OneTimeText.objects.order_by('id')

    if _supports_skip_locked():
        text_row = queryset.select_for_update(skip_locked=True).first()
    else:
        text_row = queryset.first()

    if text_row is None:
        return render(request, 'texts/sentence_page.html', {
            'sentence': None,
            'remaining': 0,
            'is_empty': True,
            'show_admin_stats': request.user.is_authenticated and request.user.is_staff,
        })

    sentence = text_row.content
    text_row.delete()
    remaining = OneTimeText.objects.count()

    return render(request, 'texts/sentence_page.html', {
        'sentence': sentence,
        'remaining': remaining,
        'is_empty': False,
        'show_admin_stats': request.user.is_authenticated and request.user.is_staff,
    })
