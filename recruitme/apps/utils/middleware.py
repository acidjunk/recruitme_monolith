"""Add user created_by and modified_by foreign key refs to any model automatically.
   Almost entirely taken from https://github.com/Atomidata/django-audit-log/blob/master/audit_log/middleware.py"""
from django.db.models import signals
from django.utils.functional import curry


"""
FROM: stack overflow - http://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model
"""
from django.utils import timezone

class UserAuditMiddleware(object):
    def process_request(self, request):
        if request.method in ['POST']:
            if hasattr(request, 'user') and request.user.is_authenticated():
                user = request.user
            else:
                user = None

            audit = curry(self.user_audit, user)
            signals.pre_save.connect(audit, dispatch_uid=(self.__class__, request,), weak=False)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=(self.__class__, request,))
        return response

    def user_audit(self, user, sender, instance, **kwargs):
        for x in instance._meta.fields:
            if x.name == 'created_by' and not instance.id:
                instance.created_by = user
                instance.created_on = timezone.now()
            if x.name == 'modified_by':
                instance.modified_by = user
                instance.modified_on = timezone.now()