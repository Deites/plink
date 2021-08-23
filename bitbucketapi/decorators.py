from .models import RequestsList


def save_request(function):
    def wrap(request, *args, **kwargs):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            current_ip = x_forwarded_for.split(",")[-1].strip()
        else:
            current_ip = request.META.get("REMOTE_ADDR")

        data = None
        if request.method == "GET":
            data = request.GET
        elif request.method == "POST":
            data = request.POST

        r = RequestsList(
            ip_user=current_ip,
            request_itself=f"{request.method} {request.path}",
            json=data,
        )
        r.save()

        return function(request, *args, **kwargs)

    return wrap
