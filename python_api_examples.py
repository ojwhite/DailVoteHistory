import oireachtas_api
from OireachtasAPI.oireachtas_api.rest import ApiException
from pprint import pprint
import pandas as pd
import json


def consituencies_example():
    # create an instance of the API class
    # api_instance = oapi.ConstituenciesApi(oapi.ApiClient(configuration))
    api_instance = oireachtas_api.ConstituenciesApi(oireachtas_api.ApiClient)
    chamber_id = ['[]']  # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
    chamber = ''  # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
    house_no = 56  # int | filter by house number (optional)
    skip = 0  # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
    limit = 50  # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)

    try:
        # Constituencies List
        api_response = api_instance.constituencies(chamber_id=chamber_id, chamber=chamber, house_no=house_no, skip=skip, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConstituenciesApi->constituencies: %s\n" % e)


def debates_example():
    # create an instance of the API class
    api_instance = oireachtas_api.DebatesApi()
    chamber_type = 'house'  # str | (house, committee)
    chamber_id = ['[]']  # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
    chamber = 'dail'  # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
    date_start = '2020-01-01'  # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
    date_end = '2022-01-01'  # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
    skip = 0  # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
    limit = 50  # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
    member_id = ''  # str | Filter by Member uri. (optional)
    debate_id = ''  # str | Filter by debate uri (optional)

    try:
        # Debates List
        api_response = api_instance.debates(chamber_type=chamber_type,
                                            chamber_id=chamber_id,
                                            chamber=chamber,
                                            date_start=date_start,
                                            date_end=date_end,
                                            skip=skip,
                                            limit=limit,
                                            member_id=member_id,
                                            debate_id=debate_id)

        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebatesApi->debates: %s\n" % e)


def legislation_example():
    # create an instance of the API class
    api_instance = oireachtas_api.LegislationApi()
    bill_status = [
        ['Current']
    ]  # list[str] | An array which is used to filter legislation by status detailed in default settings below.  Separated by comma. (optional) (default to [Current, Withdrawn, Enacted, Rejected, Defeated, Lapsed])
    bill_source = ['']  # list[str] | An array used to filter legislation by origin source. (optional) (default to [Government, Private Member])
    date_start = '2022-01-01'  # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
    date_end = '2022-03-01'  # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
    skip = 0  # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
    limit = 50  # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
    member_id = ''  # str | Filter by Member uri. (optional)
    bill_id = ''  # str | Filter results by Bill URI Example   /ie/oireachtas/bill/2016/2  (optional)
    bill_no = ''  # str | Filter Bill by number. (optional)
    bill_year = ''  # str | Filter Bill by year. (optional)
    chamber_id = ['[]']  # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
    act_year = ''  # str | Filter Bill by Act year. (optional)
    act_no = ''  # str | Filter Bill by Act number. (optional)
    lang = 'en'  # str | language of document to extract. Defaults to English (en) (optional) (default to en)

    try:
        # Legislation API
        api_response = api_instance.legislation(bill_status=bill_status, bill_source=bill_source, date_start=date_start, date_end=date_end, skip=skip, limit=limit, member_id=member_id, bill_id=bill_id, bill_no=bill_no, bill_year=bill_year,
                                                chamber_id=chamber_id, act_year=act_year, act_no=act_no, lang=lang)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegislationApi->legislation: %s\n" % e)