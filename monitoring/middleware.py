import logging
import datetime
import inspect
from .models import LogEntry, LogController
logger = logging.getLogger('django')


class CustomLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Process the response after the view is called
        self.process_response(request, response)

        return response

    def process_response(self, request, response):
        status_code = response.status_code
        log_controller_instance = LogController.objects.first()
        status_code_list = log_controller_instance.status_codes.values_list('status_code', flat=True)

        if status_code < 400 and 200 in status_code_list or 300 in status_code_list:
            log_entry = self.save_log(request, status_code)
            logger.info(f'INFO: {log_entry}')
        elif status_code > 399 and status_code < 500 and 400 in status_code_list:
            log_entry = self.save_log(request, status_code)
            logger.warning(f'WARNING: {log_entry}')
        elif 500 in status_code_list: 
            log_entry = self.save_log(request, status_code)
            logger.error(f'ERROR: {log_entry}')

    def get_module_name(self, request):
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        module_name = module.__name__.split('.')[0] if module else 'UnknownModule'
        return module_name

    def save_log(self, request, status_code):
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        date_time = datetime.datetime.now()
        method = request.method
        module = self.get_module_name(request)
        table = ''  # Add logic to determine the relevant table
        log_entry = LogEntry.objects.create(
            status=status_code,
            user=user,
            date_time=date_time,
            method=method,
            module=module,
            table=table,
        )
        return log_entry