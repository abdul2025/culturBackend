import json
import datetime
from tokenize import group
from admin_api.portals_admin.queries import filter_munjiz_nationality
from munjiz.utils import get_gender, get_status
from admin_api.hiring_admin.queries import get_munjiz_nationality
from munjiz import utils
from django.db.models import Q
from django.db import connection
from munjiz.utils import proposal_status, order_status, hire_request_status, get_roles


def session_fields(key, munjiz_nationality):
    switcher = {
        "city": "time_slot__opportunity__job_location__city__en_name",
        "corporate": "time_slot__opportunity__order__proposal__hire_request__corporate__name__contains",
        "nationality": get_munjiz_nationality(munjiz_nationality),
        "date_range": "time_slot__start_date__range",

    }
    return switcher.get(key, key)


class FilterService():

    @staticmethod
    def session_query(filters, session_defualt_key):
        # this function converts a list of filters to excuatable query
        # or defualtKey for filteration
        queries = {}
        now = utils.now()
        one_month_ago = datetime.datetime(now.year, now.month - 1, 1)
        month_end = datetime.datetime(now.year, now.month, 1) - datetime.timedelta(seconds=1)

        def _defaultFilter(session_defualt_key):
            return {
                'default': Q(time_slot__end_date__gt=one_month_ago) &
                           Q(time_slot__end_date__lt=month_end) &
                           Q(status=202) &
                           Q(munjiz_id__isnull=False)}.get(session_defualt_key)

        if session_defualt_key:
            queries = _defaultFilter(session_defualt_key)
        else:
            fil = json.loads(filters)

            for filter in fil:
                for key, value in filter.items():
                    if key == "city":
                        key = "time_slot__opportunity__job_location__city__en_name"
                    elif key == "corporate":
                        key = "time_slot__opportunity__order__proposal__hire_request__corporate__name__contains"
                    elif key == "nationality":
                        munjiz_nationality = value
                        key = "munjiz_id__in"
                        value = get_munjiz_nationality(munjiz_nationality)
                    elif key == "date_range":
                        key = 'time_slot__start_date__range'

                    queries[key] = value
        return queries

    @staticmethod
    def opportunity_time_slot_query(filters):

        queries = {}
        fil = json.loads(filters)
        for filter in fil:
            for key, value in filter.items():
                if key == "corporate":
                    key = "opportunity__order__proposal__hire_request__corporate__name__contains"
                elif key == "date_range":
                    key = 'start_date__range'
                queries[key] = value
        return queries

    @staticmethod
    def munjiz_interview_query(filters):
        '''
            Filtration for mujiz register application in new admin         
        '''
        queries = {}
        fil = json.loads(filters)
        for filter in fil:
            for key, value in filter.items():
                if key == "gender":
                    gender_given_value = value
                    key = "munjiz_application__gender"
                    value = get_gender(gender_given_value)
                elif key == "nationality":
                    key = "id__in"
                    nationality_value = value
                    value = filter_munjiz_nationality(nationality_value)
                elif key == "mobile_number":
                    key = "munjiz_application__mobile_number__contains"
                elif key == "status":
                    key="munjiz_application__status"
                    status_filter = value
                    value = get_status(status_filter)
                elif key == "reviewed":
                    key="reviewed_flag"
                elif key == "first_name":
                    key = "munjiz_application__first_name__contains"
                elif key == "last_name":
                    key = "munjiz_application__last_name__contains"
                queries[key] = value
        return queries

    @staticmethod
    def custom_user_query(filters):
        queries = {}
        fil = json.loads(filters)
        for filter in fil:
            for key, value in filter.items():
                if key == "mobile_number":
                    key = "username__contains"
                elif key == "first_name":
                    key = "first_name__contains"
                elif key == "last_name":
                    key = "last_name__contains"
                elif key == "groups":
                    value = get_roles(value)
                queries[key] = value
        return queries  

    @staticmethod
    def rowSqlQuery(queryString: str, params: list):
        with connection.cursor() as cursor:
            cursor.execute(queryString, params)
            row = cursor.fetchall()
            return row
