from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count
from django.db.models.functions import Substr
from .models import Book
import random
from datetime import datetime
from datetime import date

# Create your views here.


def index(request):
    return HttpResponse('こんにちは、世界！')


def temp(request):
    context = {
        'msg': 'こんにちは、世界！'
    }
    return render(request, 'main/temp.html', context)


def list(request):
    # すべての書籍情報を取得する
    books = Book.objects.all()
    return render(request, 'main/list.html', {'books': books})


def iftag(request):
    return render(request, 'main/iftag.html', {
        'random': random.randint(0, 100)
    })


def yesno(request):
    return render(request, 'main/yesno.html', {
        'flag': True
    })


def firstof(request):
    return render(request, 'main/firstof.html', {
        # 'a': 'おはようございます！',
        # 'b': 'こんにちは！',
        # 'c': 'こんばんは！'
    })


def forloop(request):
    return render(request, 'main/forloop.html', {
        'weeks': ['月', '火', '水', '木', '金', '土', '日']
    })


def forempty(request):
    return render(request, 'main/forempty.html', {
        'members': ['鈴木三郎', '佐藤洋子', '山田次郎']
    })


def fortag(request):
    return render(request, 'main/fortag.html')


def ifchanged(request):
    return render(request, 'main/ifchanged.html', {
        'schedule': [
            (10, 'A企画反省会'),
            (10, 'B書籍脱稿'),
            (15, 'WINGS定例会議'),
            (30, 'C企画打合せ'),
        ]
    })


def regroup(request):
    return render(request, 'main/regroup.html', {
        'members': [
            {'name': '鈴木三郎', 'sex': '男', 'birth': '1980-12-23'},
            {'name': '山田次郎', 'sex': '男', 'birth': '1978-10-13'},
            {'name': '佐藤健司', 'sex': '男', 'birth': '1976-04-06'},
            {'name': '山本花子', 'sex': '女', 'birth': '1981-07-28'},
            {'name': '田中久美', 'sex': '女', 'birth': '1980-09-07'},
        ]
    })


def cycle(request):
    return render(request, 'main/cycle.html', {
        'members': [
            {'name': '鈴木三郎', 'sex': '男', 'birth': '1980-12-23'},
            {'name': '山田次郎', 'sex': '男', 'birth': '1978-10-13'},
            {'name': '佐藤健司', 'sex': '男', 'birth': '1976-04-06'},
            {'name': '山本花子', 'sex': '女', 'birth': '1981-07-28'},
            {'name': '田中久美', 'sex': '女', 'birth': '1980-09-07'},
        ]
    })


def escape(request):
    return render(request, 'main/escape.html', {
        'msg': '''<img src="https://wings.msn.to/image/wings.jpg" title="ロゴ" />
            <p>WINGSへようこそ</p>'''
    })


def temptag(request):
    return render(request, 'main/temptag.html')


def verbatim(request):
    return render(request, 'main/verbatim.html')


def master(request):
    return render(request, 'main/master.html', {
        'msg': 'こんにちは、世界！'
    })


def include(request):
    return render(request, 'main/include.html', {
        'name': '鈴木',
        'current': datetime.datetime.now(),
    })


def static(request):
    return render(request, 'main/static.html')


def strformat(request):
    return render(request, 'main/strformat.html', {
        'data1': None,
        'data2': 'WINGS\nWww INtegrated Guide on Server-architecture',
        'data3': 'https://wings.msn.to/',
        'data4': ['い', 'ろ', 'は', 'に', 'ほ', 'へ'],
        'data5': 987.654,
        'data6': 'hello django'
    })


def slice(request):
    return render(request, 'main/slice.html', {
        'data': ['い', 'ろ', 'は', 'に', 'ほ', 'へ']
    })


def date_time(request):
    return render(request, 'main/date_time.html', {
        'today': datetime.datetime.now()
    })


def filter(request):
    books = Book.objects.filter(publisher='翔泳社')
    # AND 条件
    # books = Book.objects.filter(publisher='翔泳社', price=2800)
    # 大小比較
    # books = Book.objects.filter(price__lt=3000)
    # 部分一致
    # books = Book.objects.filter(title__contains='独習')
    # 正規表現
    # books = Book.objects.filter(title__regex=r'[0-9]+')
    # NULL比較
    # books = Book.objects.filter(title__isnull=True)
    # 範囲比較
    # books = Book.objects.filter(published__range=(date(2018, 1, 1), date(2018, 12, 31)))
    # 候補比較
    # books = Book.objects.filter(publisher__in=['翔泳社', '技術評論社', '日経BP'])
    # 日付比較(年/月/日)
    # books = Book.objects.filter(published__year=2019)
    # books = Book.objects.filter(published__year__lte=2019)
    # books = Book.objects.filter(published__week_day__range=(2, 6))
    return render(request, 'main/book_list.html', {
        'books': books,
    })


def filter_or(request):
    # books = Book.objects.filter(publisher='翔泳社').filter(price__gte=2800)
    # Qオブジェクトの基本
    # books = Book.objects.filter(Q(publisher='翔泳社') | Q(price__gte=2800))

    # より複雑な条件式
    books = Book.objects.filter(
        ~Q(publisher='翔泳社') & (Q(published_year=2018) | (Q(published_year=2020)))
    )
    return render(request, 'main/book_list.html', {
        'books': books,
    })


def filter_other(request):
    # 出版社(昇順)／刊行日の降順でソート
    books = Book.objects.order_by('publisher', '-published')

    # ランダムにソート
    # books = Book.objects.order_by('?')

    # 取得範囲の指定
    # books = Book.objects.order_by('-price')[2:5]

    # 取得列の制約
    # books = Book.objects.values('title', 'price')

    # 書名から最初の5文字だけを取り出す
    # books = Book.objects.values('price', short_title=Substr('title', 1, 5))
    # return HttpResponse(books[0]['short_title'])

    # リストとして取得
    # books = Book.objects.values_list('title', flat=True)
    # return HttpResponse(books[0])

    return render(request, 'main/book_list.html', {
        'books': books,
    })


def exclude(request):
    books = Book.objects.exclude(publisher='翔泳社')
    return render(request, 'main/book_list.html', {
        'books': books,
    })


def get(request):
    book = Book.objects.get(pk=1)
    return render(request, 'main/book_detail.html', {
        'book': book,
    })


def groupby(request):
    return render(request, 'main/groupby.html', {
        'groups': Book.objects.values('publisher')
        .annotate(pub_count=Count('publisher')).order_by('-pub_count')
    })

    # cnt = Book.objects.filter(publisher='翔泳社').count()
    # return HttpResponse(cnt)

    # flag = Book.objects.filter(publisher='翔泳社').exists()
    # return HttpResponse(flag)


def union(request):
    b1 = Book.objects.filter(publisher='翔泳社')
    b2 = Book.objects.filter(publisher='技術評論社')
    return render(request, 'main/book_list.html', {
        'books': b1.union(b2),
    })


def raw(request):
    books = Book.objects.raw('SELECT * FROM main_book WHERE publisher = %s', ['翔泳社'])
    return render(request, 'main/book_list.html', {
        'books': books,
    })
