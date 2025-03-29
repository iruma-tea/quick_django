from datetime import date
from django import forms

from .validates import compare_today


class BookForm(forms.Form):
    isbn = forms.CharField(label='ISBNコード', required=True, max_length=20, error_messages={
        'required': 'ISBNコードは必須です。',
        'max_length': 'ISBNコードは20文字以内で入力してください。',
    })
    title = forms.CharField(label='書名', required=True, max_length=100, error_messages={
        'required': '書名は必須です。',
        'max_length': '書名は100文字以内で入力してください。'
    })
    price = forms.IntegerField(label='価格', required=True, min_value=0, error_messages={
        'required': '価格は必須です。',
        'min_value': '価格は正数で入力してください。'
    })
    publisher = forms.ChoiceField(label='出版社', choices=[
        ('翔泳社', '翔泳社'),
        ('技術評論社', '技術評論社'),
        ('秀和システム', '秀和システム'),
        ('SBクリエティブ', 'SBクリエティブ'),
        ('日経BP', '日経BP'),
    ])
    published = forms.DateField(label='刊行日', required=True, validators=[compare_today], error_messages={
        'required': '刊行日は必須です。',
        'invalid': '刊行日はYYYY-MM-DDの形式で入力してください。',
    })

    # def clean_published(self):
    #     published = self.clean_data['published']

    #     if date.today() < published:
    #         raise forms.ValidationError('刊行日は今日以前の日付で入力してください。')

    #     return published

    def clean(self):
        cleaned_data = super().clean()
        isbn = cleaned_data.get('isbn')
        published = cleaned_data.get('published')

        if isbn and published:
            if published.year < 2007:
                if len(isbn) != 13:
                    raise forms.ValidationError('ISBNコードは13桁で入力してください。')
            else:
                if len(isbn) != 17:
                    raise forms.ValidationError('ISBNコードは17桁で入力してください。')
