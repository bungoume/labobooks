from django.shortcuts import redirect


def home(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    if not request.user.org_memberships.exists():
        return redirect('organization_new')
    main_org = request.user.org_memberships.last()
    return redirect('dashboard', organization_slug=main_org.id_slug)
