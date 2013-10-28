from django.http import HttpResponse
from django.utils import simplejson


class JsonResponse(HttpResponse):
    """Return Json with no hassles"""
    
    def __init__(self, content, status):
        super(JsonResponse), self).__init__(
            content=simplejson.dumps(content),
            status=status,
            mimetype='application/json',
            content_type='application/json',
        )