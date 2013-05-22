import datetime


class NotificationPayload(object):
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, payload_json):
        self.deleted_at = ''
        self.options = payload_json['image_meta']['com.rackspace__1__options']
        self.bandwidth_in = payload_json['bandwidth']['public']['bw_in']
        self.bandwidth_out = payload_json['bandwidth']['public']['bw_out']

        self.launched_at = datetime.datetime.strptime(
            payload_json['launched_at'],
            NotificationPayload.DATETIME_FORMAT)

        self.audit_period_beginning = datetime.datetime.strptime(
            payload_json['audit_period_beginning'],
            NotificationPayload.DATETIME_FORMAT)

        self.audit_period_ending = datetime.datetime.strptime(
            payload_json['audit_period_ending'],
            NotificationPayload.DATETIME_FORMAT)

        if payload_json['deleted_at']:
            self.deleted_at = datetime.datetime.strptime(
                payload_json['deleted_at'],
                NotificationPayload.DATETIME_FORMAT)

        self.tenant_id = payload_json['tenant_id']
        self.instance_id = payload_json['instance_id']
        self.flavor = payload_json['instance_type_id']

    def start_time(self):
        start_time = max(self.launched_at, self.audit_period_beginning)
        return datetime.datetime.strftime(start_time,
                                          NotificationPayload.DATETIME_FORMAT)

    def end_time(self):
        if not self.deleted_at:
            return datetime.datetime.strftime(
                self.audit_period_ending,
                NotificationPayload.DATETIME_FORMAT)
        end_time = min(self.deleted_at, self.audit_period_ending)
        return datetime.datetime.strftime(end_time,
                                          NotificationPayload.DATETIME_FORMAT)

