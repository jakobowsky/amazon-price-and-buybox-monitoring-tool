from django.shortcuts import render
from monitoring.models import Asin
from monitoring.forms import AsinForm
from django.shortcuts import redirect


def asin_view(request):
    asins = Asin.objects.all().order_by("created_at")
    asins_list = []
    for asin in asins:
        try:
            buybox_winner = asin.data_rows.filter(is_buy_box_winner=True).order_by("-created_at").first().listing_price
        except:
            buybox_winner = 0

        asins_list.append(
            {'asin_obj': asin, 'num_of_offers': asin.data_rows.count(),
             'buybox_winner': buybox_winner}
        )
    if request.method == "POST":
        form = AsinForm(request.POST)
        if form.is_valid():
            new_asin = form.data.get("asin")
            Asin.objects.get_or_create(asin=new_asin)
            return redirect(asin_view)

    else:
        form = AsinForm()
    print(asins_list)
    return render(
        request, "monitoring/home.html", context={"asins": asins_list, "form": form}
    )


def switch_system(request, pk):
    asin = Asin.objects.get(id=pk)
    asin.is_running = not asin.is_running
    asin.save()
    return redirect(asin_view)


def delete_asin(request, pk):
    Asin.objects.get(id=pk).delete()
    return redirect(asin_view)
