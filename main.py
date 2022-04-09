import pandas as pd
import json
import urllib3


def get_divisions_dataframe(data):

    """
    Given a dictionary of division data, output a
    pandas dataframe of key variables
    """

    # a dictionary to hold the results
    results = {
        "vote_name": [],
        "vote_date": [],
        "is_bill": [],
        "vote_outcome": [],
        "member_code": [],
        "yes": [],
        "no": [],
        "abstain": []
    }

    # member vote -> vote field
    vote_code = {
        "Níl": results["no"],
        "Tá": results["yes"],
        "Staon": results["abstain"]
    }

    # traverse the JSON tree and append data to results
    for division in data["results"]:
        vote = division["division"]
        vote_name = vote["debate"]["showAs"]
        vote_date = vote["date"]
        vote_outcome = vote["outcome"]
        is_bill = vote["isBill"]
        for tally in vote["tallies"].values():
            if not tally:
                continue
            member_vote = tally["showAs"]
            for member in tally["members"]:
                results["vote_name"].append(vote_name)
                results["vote_date"].append(vote_date)
                results["is_bill"].append(is_bill)
                results["vote_outcome"].append(vote_outcome)
                results["member_code"].append(member['member']['memberCode'])
                for mv in vote_code:
                    vote_code[mv].append(int(mv == member_vote))

    return pd.DataFrame(results)


def get_members_dataframe(data):

    """
    Given a dictionary of member data, output a
    pandas dataframe of key variables
    """

    # a dictionary to hold the results
    results = {
        "member_code": [],
        "first_name": [],
        "last_name": [],
        "party_code": [],
        "represent_code": [],
        "represent_type": [],
    }

    # traverse the JSON tree and append data to results
    for member in data["results"]:
        # basic info
        m = member["member"]
        member_code = m["memberCode"]
        first_name = m["firstName"]
        last_name = m["lastName"]
        # find current active membership
        for membership in m["memberships"]:
            mem = membership["membership"]
            if mem["dateRange"]["end"] is not None:
                continue    # expired membership - skip
            # find current party
            for party in mem["parties"]:
                p = party["party"]
                if p["dateRange"]["end"] is not None:
                    continue    # member not currently with this party - skip
                party_code = p["partyCode"]
            if len(mem["represents"]) == 1:
                represent_code = mem["represents"][0]["represent"]["representCode"]
                represent_type = mem["represents"][0]["represent"]["representType"]
            else:
                raise(Exception("What?"))
            # write results
            results["member_code"].append(member_code)
            results["first_name"].append(first_name)
            results["last_name"].append(last_name)
            results["party_code"].append(party_code)
            results["represent_code"].append(represent_code)
            results["represent_type"].append(represent_type)

    return pd.DataFrame(results)


def query_api(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    # print(response.status)
    return json.loads(response.data.decode('utf-8'))


if __name__ == "__main__":

    # // query params //
    date_start = "2020-01-01"
    date_end = "2099-01-01"
    chamber_id = ""
    chamber_type = "house"
    chamber = "dail"
    record_limit = 9999
    outcome = "Carried"

    # // get data from API //
    # divisions data
    url = (f"https://api.oireachtas.ie/v1/divisions?"
           f"chamber_type={chamber_type}&"
           f"chamber_id={chamber_id}&"
           f"chamber={chamber}&"
           f"date_start={date_start}&"
           f"date_end={date_end}&"
           f"limit={record_limit}&"
           f"outcome={outcome}")
    divs_data = query_api(url)
    # member data
    url = (f"https://api.oireachtas.ie/v1/members?"
           f"date_start={date_start}&"
           f"chamber_id={chamber_id}&"
           f"chamber={chamber}&"
           f"date_end={date_end}&"
           f"limit={record_limit}")
    members_data = query_api(url)

    # // get data as dataframe //
    votes_dataframe = get_divisions_dataframe(divs_data)
    member_dataframe = get_members_dataframe(members_data)

    # // output DF to csv //
    votes_dataframe.to_csv("DailVotes.csv", index=False)
    member_dataframe.to_csv("DailMembers.csv", index=False)

