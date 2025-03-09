from django.db import models


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(
        verbose_name='ISBNコード',
        max_length=20
    )
    title = models.CharField(
        verbose_name='書名',
        max_length=100
    )
    price = models.IntegerField(
        verbose_name='価格',
        default=0
    )
    publisher = models.CharField(
        verbose_name='出版社',
        max_length=50,
        choices=[
            ('翔泳社', '翔泳社'),
            ('技術評論社', '技術評論社'),
            ('秀和システム', '秀和システム'),
            ('SBクリエイティブ', 'SBクリエティブ'),
            ('日経BP', '日経BP'),
        ],
    )
    published = models.DateField(
        verbose_name='刊行日'
    )

    def __str__(self):
        return f'{self.title}({self.publisher}/{self.price}円)'
