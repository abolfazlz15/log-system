import logging
import datetime
import inspect
from .models import LogEntry
logger = logging.getLogger('django')


class CustomLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request before the view is called
        response = self.get_response(request)

        # Process the response after the view is called
        self.process_response(request, response)

        return response

    def process_response(self, request, response):
        status_code = response.status_code
        user = request.user.username if request.user.is_authenticated else "Anonymous"

        # Use datetime.datetime.now() to capture the current date and time
        date_time = datetime.datetime.now()

        method = request.method

        # Determine the module (Django app) dynamically
        module = self.get_module_name(request)

        table = ""  # Add logic to determine the relevant table

        log_entry = LogEntry.objects.create(
            status=status_code,
            user=user,
            date_time=date_time,
            method=method,
            module=module,
            table=table,
        )

        # Optionally, log the entry using Python's logging module
        if status_code < 400:
            logger.info(f"INFO: {log_entry}")
        elif status_code > 399 and status_code < 500:
            logger.warning(f"WARNING: {log_entry}")
        else: 
            logger.error(f"ERROR: {log_entry}")

    def get_module_name(self, request):
        # Get the module (Django app) dynamically based on the file name
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        module_name = module.__name__.split('.')[0] if module else "UnknownModule"
        return module_name
