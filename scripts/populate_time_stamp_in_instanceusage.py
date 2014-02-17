import os
import sys

sys.path.append(os.environ.get('STACKTACH_INSTALL_DIR', '/stacktach'))

from stacktach import models


def main():
    active_launches_query = \
        """select * from stacktach_instanceusage u where not
           exists (select 1 from stacktach_instancedeletes where
           instance = u.instance );"""
    usages = models.InstanceUsage.objects.raw(active_launches_query)
    for usage in usages:
        latest_raw = models.RawData.objects.filter(
            instance=usage.instance).order_by('-id')[0]
        usage.last_notification_timestamp = latest_raw.when
        usage.save()


if __name__ == '__main__':
    main()
