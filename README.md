# zoho-people-attendance

Regularize attendance on Zoho People.

# Configure cookies

1. `cp mycookies-sample.py mycookies.py`
2. Make a request on the zoho people website to get the curl request, its headers and cookies (from JS console) 
3. The URL you are looking for is a post to `/AttendanceAction.zp` endpoint
4. You can use https://curlconverter.com/python/ to copied cURL content from your JS console of your browser
5. Copy HEADERS, ERECNO, CONREQCSR, and ENDPOINT url into mycookies.py
6. Update YEAR and MONTH in mycookies.py
7. Run "python main.py"
