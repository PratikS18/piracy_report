from django.shortcuts import render
from django.db.models import Count
from .models import *
# Create your views here.
def index(request):
    items = TopList.objects.raw('SELECT * from piracyreport_toplist')
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)

def display_books(request):
    items = Books.objects.raw('SELECT x.* FROM piracyreport_books x JOIN (SELECT isbn, COUNT(*) total FROM piracyreport_books GROUP BY isbn) y ON y.isbn = x.isbn ORDER BY total DESC')
    context = {
        'items': items,
    }
    return render(request, 'display_books.html', context)

def display_1788478126(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788478126"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788478126"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788478126.html', context)

def display_1789955750(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789955750"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789955750"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789955750.html', context)


def display_1787125939(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1787125939"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1787125939"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787125939.html', context)

def display_1789131510(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789131510"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789131510"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131510.html', context)

def display_1789532051(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789532051"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789532051"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532051.html', context)

def display_1788834240(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788834240"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788834240"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788834240.html', context)

def display_1788295862(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788295862"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788295862"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788295862.html', context)

def display_1788996666(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788996666"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788996666"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788996666.html', context)

def display_1789139864(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789139864"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789139864"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139864.html', context)

def display_1789348013(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789348013"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789348013"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348013.html', context)

def display_1788297237(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788297237"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788297237"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788297237.html', context)

def display_1788839528(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788839528"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788839528"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839528.html', context)

def display_1789536669(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789536669"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789536669"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536669.html', context)

def display_1838559337(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838559337"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838559337"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838559337.html', context)

def display_178934056X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178934056X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178934056X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934056X.html', context)

def display_1787280543(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1787280543"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1787280543"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787280543.html', context)

def display_1788830644(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788830644"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788830644"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788830644.html', context)

def display_1788475291(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788475291"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788475291"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788475291.html', context)

def display_1788839048(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788839048"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788839048"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839048.html', context)

def display_178934641X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178934641X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178934641X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934641X.html', context)

def display_1789138906(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789138906"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789138906"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138906.html', context)

def display_1789138221(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789138221"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789138221"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138221.html', context)

def display_1838551026(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838551026"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838551026"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838551026.html', context)

def display_1789531365(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789531365"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789531365"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531365.html', context)

def display_1789615852(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789615852"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789615852"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615852.html', context)

def display_1789135990(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789135990"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789135990"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789135990.html', context)

def display_1789807352(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789807352"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789807352"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807352.html', context)

def display_1788624068(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788624068"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788624068"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788624068.html', context)

def display_1789804531(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789804531"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789804531"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804531.html', context)

def display_1788834097(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788834097"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788834097"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788834097.html', context)

def display_1788470591(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788470591"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788470591"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788470591.html', context)

def display_1789349869(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789349869"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789349869"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349869.html', context)

def display_1789347033(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789347033"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789347033"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347033.html', context)

def display_1789349796(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789349796"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789349796"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349796.html', context)

def display_1789956714(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789956714"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789956714"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956714.html', context)

def display_1789954398(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789954398"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789954398"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954398.html', context)

def display_1789613477(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789613477"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789613477"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789613477.html', context)

def display_1789615321(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789615321"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789615321"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615321.html', context)

def display_1789346371(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789346371"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789346371"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346371.html', context)

def display_1788392507(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788392507"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788392507"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788392507.html', context)

def display_1789534623(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789534623"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789534623"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534623.html', context)

def display_1789346460(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789346460"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789346460"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346460.html', context)

def display_178961290X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178961290X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178961290X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178961290X.html', context)

def display_1788290143(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788290143"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788290143"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788290143.html', context)

def display_178913496X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178913496X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178913496X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913496X.html', context)

def display_1785885588(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1785885588"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1785885588"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1785885588.html', context)

def display_1789615402(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789615402"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789615402"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615402.html', context)

def display_1789537819(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789537819"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789537819"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537819.html', context)

def display_1788837363(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788837363"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788837363"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837363.html', context)

def display_1838559353(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838559353"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838559353"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838559353.html', context)

def display_1788997565(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788997565"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788997565"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997565.html', context)

def display_1789344913(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789344913"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789344913"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344913.html', context)

def display_1789340748(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789340748"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789340748"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340748.html', context)

def display_1784396036(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1784396036"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1784396036"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1784396036.html', context)

def display_1838829024(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838829024"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838829024"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838829024.html', context)

def display_1788629876(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788629876"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788629876"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629876.html', context)

def display_1789805821(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789805821"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789805821"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805821.html', context)

def display_1788839250(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788839250"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788839250"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839250.html', context)

def display_1788626567(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788626567"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788626567"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626567.html', context)

def display_1789347068(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789347068"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789347068"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347068.html', context)

def display_1838645357(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838645357"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838645357"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838645357.html', context)

def display_1789951542(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789951542"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789951542"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951542.html', context)

def display_1838827366(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838827366"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838827366"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838827366.html', context)

def display_1789614503(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789614503"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789614503"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789614503.html', context)

def display_1789615690(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789615690"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789615690"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615690.html', context)

def display_1789349338(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789349338"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789349338"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349338.html', context)

def display_1789805465(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789805465"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789805465"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805465.html', context)

def display_1788990641(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788990641"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788990641"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788990641.html', context)

def display_178995004X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178995004X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178995004X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995004X.html', context)

def display_1789532019(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789532019"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789532019"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532019.html', context)

def display_1789136725(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789136725"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789136725"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136725.html', context)

def display_1789346347(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789346347"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789346347"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346347.html', context)

def display_1789537223(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789537223"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789537223"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537223.html', context)

def display_1789533880(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789533880"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789533880"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533880.html', context)

def display_1789808154(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789808154"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789808154"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808154.html', context)

def display_1789808898(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789808898"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789808898"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808898.html', context)

def display_1789950686(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789950686"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789950686"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789950686.html', context)

def display_1788990552(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788990552"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788990552"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788990552.html', context)

def display_1788626850(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788626850"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788626850"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626850.html', context)

def display_1789530091(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789530091"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789530091"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789530091.html', context)

def display_1788837045(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788837045"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788837045"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837045.html', context)

def display_1789800986(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789800986"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789800986"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800986.html', context)

def display_1789808537(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789808537"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789808537"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808537.html', context)

def display_1788832566(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788832566"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788832566"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788832566.html', context)

def display_1789951291(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789951291"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789951291"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951291.html', context)

def display_1786464535(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1786464535"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1786464535"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1786464535.html', context)

def display_1784393878(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1784393878"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1784393878"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1784393878.html', context)

def display_178995732X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178995732X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178995732X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995732X.html', context)

def display_1789132878(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789132878"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789132878"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132878.html', context)

def display_1787120953(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1787120953"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1787120953"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787120953.html', context)

def display_1789803829(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789803829"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789803829"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803829.html', context)

def display_1789345154(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789345154"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789345154"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345154.html', context)

def display_178847242X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178847242X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178847242X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178847242X.html', context)

def display_1789341655(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789341655"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789341655"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341655.html', context)

def display_1788991214(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788991214"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788991214"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991214.html', context)

def display_1784398934(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1784398934"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1784398934"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1784398934.html', context)

def display_1789343224(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789343224"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789343224"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343224.html', context)

def display_1788837681(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788837681"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788837681"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837681.html', context)

def display_1788831926(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788831926"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788831926"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788831926.html', context)

def display_1788995570(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788995570"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788995570"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995570.html', context)

def display_1788629418(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788629418"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788629418"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629418.html', context)

def display_1789137799(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789137799"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789137799"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137799.html', context)

def display_1788628462(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788628462"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788628462"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788628462.html', context)

def display_1788622057(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788622057"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788622057"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788622057.html', context)

def display_1789617871(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789617871"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789617871"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617871.html', context)

def display_1789800935(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789800935"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789800935"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800935.html', context)

def display_1838550917(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838550917"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838550917"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550917.html', context)

def display_1789538505(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789538505"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789538505"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538505.html', context)

def display_1788839110(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788839110"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788839110"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839110.html', context)

def display_178934834X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178934834X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178934834X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934834X.html', context)

def display_1789136369(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789136369"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789136369"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136369.html', context)

def display_1786463784(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1786463784"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1786463784"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1786463784.html', context)

def display_1789344697(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789344697"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789344697"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344697.html', context)

def display_1789617316(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789617316"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789617316"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617316.html', context)

def display_1789532027(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789532027"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789532027"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532027.html', context)

def display_1789952301(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789952301"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789952301"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789952301.html', context)

def display_1789340624(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789340624"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789340624"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340624.html', context)

def display_1788399803(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788399803"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788399803"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788399803.html', context)

def display_1788836529(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788836529"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788836529"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788836529.html', context)

def display_1788992512(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788992512"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788992512"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992512.html', context)

def display_1838641440(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838641440"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838641440"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838641440.html', context)

def display_1788832507(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788832507"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788832507"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788832507.html', context)

def display_1789617375(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789617375"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789617375"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617375.html', context)

def display_1838980849(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838980849"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838980849"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838980849.html', context)

def display_1789340764(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789340764"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789340764"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340764.html', context)

def display_1789615224(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789615224"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789615224"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615224.html', context)

def display_178899552X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178899552X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178899552X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178899552X.html', context)

def display_1788997026(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788997026"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788997026"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997026.html', context)

def display_1789343623(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789343623"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789343623"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343623.html', context)

def display_1788470710(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788470710"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788470710"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788470710.html', context)

def display_1788835883(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788835883"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788835883"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788835883.html', context)

def display_1788395158(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788395158"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788395158"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788395158.html', context)

def display_1788998758(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788998758"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788998758"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788998758.html', context)

def display_1789616190(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789616190"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789616190"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616190.html', context)

def display_178913871X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178913871X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178913871X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913871X.html', context)

def display_1789347327(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789347327"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789347327"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347327.html', context)

def display_1789537509(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789537509"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789537509"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537509.html', context)

def display_1838551212(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838551212"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838551212"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838551212.html', context)

def display_1789957753(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789957753"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789957753"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789957753.html', context)

def display_178847290X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178847290X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178847290X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178847290X.html', context)

def display_1838552189(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838552189"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838552189"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838552189.html', context)

def display_1789957052(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789957052"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789957052"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789957052.html', context)

def display_1789136431(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789136431"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789136431"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136431.html', context)

def display_1788399218(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788399218"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788399218"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788399218.html', context)

def display_178961337X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178961337X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178961337X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178961337X.html', context)

def display_1838644482(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838644482"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838644482"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838644482.html', context)

def display_1789531284(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789531284"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789531284"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531284.html', context)

def display_1789956463(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789956463"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789956463"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956463.html', context)

def display_178829274X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178829274X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178829274X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178829274X.html', context)

def display_1789342678(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789342678"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789342678"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342678.html', context)

def display_1789132304(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789132304"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789132304"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132304.html', context)

def display_1789533392(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789533392"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789533392"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533392.html', context)

def display_1785280007(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1785280007"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1785280007"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1785280007.html', context)

def display_178953173X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178953173X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178953173X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953173X.html', context)

def display_1787281396(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1787281396"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1787281396"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787281396.html', context)

def display_1789809509(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789809509"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789809509"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789809509.html', context)

def display_1788993918(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788993918"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788993918"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788993918.html', context)

def display_1788995236(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788995236"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788995236"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995236.html', context)

def display_1788995392(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788995392"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788995392"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995392.html', context)

def display_178847094X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178847094X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178847094X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178847094X.html', context)

def display_1838550364(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838550364"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838550364"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550364.html', context)

def display_1789537584(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789537584"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789537584"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537584.html', context)

def display_1789342759(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789342759"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789342759"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342759.html', context)

def display_1788835832(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788835832"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788835832"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788835832.html', context)

def display_1789803055(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789803055"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789803055"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803055.html', context)

def display_1838642730(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838642730"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838642730"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838642730.html', context)

def display_1789610788(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789610788"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789610788"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610788.html', context)

def display_1788837487(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788837487"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788837487"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837487.html', context)

def display_178980020X(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="178980020X"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="178980020X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980020X.html', context)

def display_1789532477(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789532477"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789532477"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532477.html', context)

def display_1788472489(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788472489"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788472489"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788472489.html', context)

def display_1788396715(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788396715"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788396715"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788396715.html', context)

def display_1789347394(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789347394"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789347394"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347394.html', context)

def display_1789801516(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789801516"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789801516"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801516.html', context)

def display_1838644652(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838644652"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838644652"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838644652.html', context)

def display_1789533910(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789533910"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789533910"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533910.html', context)

def display_1838823816(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838823816"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838823816"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838823816.html', context)

def display_1787287947(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1787287947"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1787287947"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787287947.html', context)

def display_1838827544(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838827544"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838827544"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838827544.html', context)

def display_1788290267(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788290267"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788290267"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788290267.html', context)

def display_1788629159(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788629159"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788629159"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629159.html', context)

def display_1789802075(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789802075"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789802075"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802075.html', context)

def display_1788478312(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788478312"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788478312"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788478312.html', context)

def display_1789610257(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789610257"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789610257"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610257.html', context)

def display_1789806984(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789806984"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789806984"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806984.html', context)

def display_1789133645(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789133645"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789133645"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133645.html', context)

def display_1785888633(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1785888633"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1785888633"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1785888633.html', context)

def display_1838823859(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838823859"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838823859"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838823859.html', context)

def display_1838822364(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838822364"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838822364"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838822364.html', context)

def display_1838821139(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838821139"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838821139"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838821139.html', context)

def display_1789348811(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789348811"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789348811"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348811.html', context)

def display_1787121321(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1787121321"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1787121321"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787121321.html', context)

def display_1838645578(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838645578"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838645578"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838645578.html', context)

def display_1839211962(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1839211962"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1839211962"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839211962.html', context)

def display_1784397695(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1784397695"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1784397695"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1784397695.html', context)

def display_1838648577(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838648577"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838648577"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838648577.html', context)

def display_1788833287(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1788833287"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1788833287"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788833287.html', context)

def display_1782167102(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1782167102"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1782167102"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1782167102.html', context)

def display_1789619785(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1789619785"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1789619785"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619785.html', context)

def display_1838550291(request):
    items = RawData.objects.raw('SELECT * from piracyreport_rawdata Where isbn=="1838550291"')
    collections = TopList.objects.raw('SELECT * from piracyreport_toplist  Where isbn=="1838550291"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550291.html', context)
