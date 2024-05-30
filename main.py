import json
import requests
import calendar
from datetime import datetime
from mycookies import COOKIES, CONREQCSR, ERECNO, YEAR, MONTH, ENDPOINT


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://people.zoho.in",
    "Connection": "keep-alive",
    "Referer": "https://people.zoho.in/colligenceresearch/zp",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
}


def enumerate_date(year, month):
    _, num_days = calendar.monthrange(year, month)
    dates = [
        datetime(year, month, day).strftime("%d-%b-%Y")
        for day in range(1, num_days + 1)
        if datetime(year, month, day).weekday() < 5
    ]
    return dates


def main():
    dates = {}
    for date in enumerate_date(YEAR, MONTH):
        data = {
            "mode": "bulkAttendReg",
            "conreqcsr": CONREQCSR,
            "erecno": ERECNO,
            "fdate": date,
            "isFromEntryPage": "true",
            "dataObj": json.dumps(
                {
                    date: {
                        "fromDate": date,
                        "toDate": date,
                        "reasonanddesc": {"reason": "Forgot to check-in"},
                        "ftime": 594,
                        "ttime": 894,
                    }
                }
            ),
        }
        response = requests.post(
            ENDPOINT,
            cookies=COOKIES,
            headers=headers,
            data=data,
        )
        print(date, response)


if __name__ == "__main__":
    main()
