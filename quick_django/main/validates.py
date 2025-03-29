from datetime import date

from django.forms import ValidationError


def compare_today(value):
    if date.today() < value:
        raise ValidationError('刊行日は今日以前の日付で入力してください。')
