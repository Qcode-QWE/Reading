#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from Reading.Utils import thread_utils

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Reading.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # 程序启动时执行定时任务
    # thread_utils.uploading_start()
    # thread_utils.reading_start()
    main()
