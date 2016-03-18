from django.shortcuts import render_to_response


def response(request):
    return render_to_response('mailing/confirm.html')
