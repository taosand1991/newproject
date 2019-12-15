from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseForbidden, Http404
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import reverse


class RestrictStaffToAdminMiddleware(MiddlewareMixin):
    """
    A middleware that restricts staff members access to administration panels.
    """
    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated:
                if not request.user.is_staff:
                    raise Http404
            else:
                raise Http404
