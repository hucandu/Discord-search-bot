from collections import OrderedDict
from rest_framework.renderers import JSONRenderer
from . import error_codes

class MyOperatorRenderer(JSONRenderer):

    default_empty_message = ""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """

        code = data.get('code', '200')
        status = self._get_status(code)
        message = data['message'] if 'message' in data else self._get_message(code)
        res_dict = OrderedDict(
            status=status,
            code=code,
            data={},
            errors={},
            message=message
        )
        if status == 'success':
            del res_dict['errors']
            res_dict['data'] = data.get('data')
        elif status == 'error':
            del res_dict['data']
            res_dict['errors'] = data.get('errors')

        ret = super().render(res_dict, accepted_media_type, renderer_context)

        return ret

    def _get_status(self, code):
        error = False
        if code != '200':
            error = True
        return 'error' if error else 'success'


    def _get_message(self, code):
        errors = dict(error_codes.ERRORS)
        return errors.get(code, self.default_empty_message)
