from django.shortcuts import render
from monitoring.models import Asin
from monitoring.forms import AsinForm
from django.shortcuts import redirect


def asin_view(request):
    asins = Asin.objects.all().order_by("created_at")
    if request.method == "POST":
        form = AsinForm(request.POST)
        if form.is_valid():
            new_asin = form.data.get("asin")
            Asin.objects.get_or_create(asin=new_asin)
            return redirect(asin_view)

    else:
        form = AsinForm()

    return render(
        request, "monitoring/home.html", context={"asins": asins, "form": form}
    )


def switch_system(request, pk):
    asin = Asin.objects.get(id=pk)
    asin.is_running = not asin.is_running
    asin.save()
    return redirect(asin_view)


def delete_asin(request, pk):
    Asin.objects.get(id=pk).delete()
    return redirect(asin_view)
