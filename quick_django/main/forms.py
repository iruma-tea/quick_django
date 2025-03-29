from django import forms


class BookForm(forms.Form):
    isbn = forms.CharField(label='ISBNコード', required=True, max_length=20)
    title = forms.CharField(label='書名', required=True, max_length=100)
    price = forms.IntegerField(label='価格', required=True, min_value=0)
    publisher = forms.ChoiceField(label='出版社', choices=[
        ('翔泳社', '翔泳社'),
        ('技術評論社', '技術評論社'),
        ('秀和システム', '秀和システム'),
        ('SBクリエティブ', 'SBクリエティブ'),
        ('日経BP', '日経BP'),
    ])
    published = forms.DateField(label='刊行日', required=True)
