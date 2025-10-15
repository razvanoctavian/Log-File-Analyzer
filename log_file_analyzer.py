#LIBRARIES
import re
from collections import Counter
import matplotlib.pyplot as plt

#ANALYZE LOG
def analyzer(filename):
    
    #pattern
    pattern = (
    r'^(\d{1,3}(?:\.\d{1,3}){3}) - - ' # IP
    r'\[(\d{2}/[A-Za-z]{3}/\d{4}):' # Date day/month/year 
    r'[0-9]{2}:[0-9]{2}:[0-9]{2} [+\-][0-9]{4}\] ' # Hour + timezsone
    r'"(GET|POST) (.*?) HTTP/1\.\d*" ' #method + url
    r'(\d{3}) \d+$' # Status code
)
    #lists for ip, statuses, days
    ips, statuses, days = [], [], []

    #read the file
    with open(filename, "r") as f:
        #searching in every line
        for line in f:
            match=re.search(pattern,line.strip())
            if match: 
                ips.append(match.group(1))
                days.append(match.group(2))
                statuses.append(match.group(5))
    
    #results
    ip_counts = Counter(ips).most_common(5) 
    status_counts = Counter(statuses) 
    day_counts = Counter(days)

    #GRAPH
    
    #1.TOP 5 IP
    x,y=zip(*ip_counts)
    plt.bar(x,y)
    plt.title("Top 5 IPs")
    plt.xlabel("IP Address")
    plt.ylabel("Requests")
    plt.show()

    #2.STATUS CODES
    x, y = zip(*status_counts.items())
    plt.bar(x, y)
    plt.title("HTTP Status Codes")
    plt.xlabel("Status Code")
    plt.ylabel("Frequency")
    plt.show()




analyzer("info.txt")