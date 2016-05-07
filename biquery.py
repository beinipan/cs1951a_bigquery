from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials
import csv 
import time

start_time = time.time()

# Grab the application's default credentials from the environment.
credentials = GoogleCredentials.get_application_default()
# Construct the service object for interacting with the BigQuery API.
bigquery_service = build('bigquery', 'v2', credentials=credentials)

query = '''SELECT body, score 
FROM 
(SELECT subreddit, body, score, RAND() AS r1
FROM [fh-bigquery:reddit_comments.2016_01]
WHERE subreddit == "politics"
AND body != "[deleted]"
ORDER BY r1
LIMIT 20000)'''#training data

# query = '''SELECT subreddit, body FROM
# (SELECT subreddit, body, RAND() AS r1
# FROM [fh-bigquery:reddit_comments.2016_01]
# WHERE REGEXP_MATCH(body, r'(?i:obama)')
# AND subreddit IN (SELECT subreddit FROM (SELECT subreddit, count(*) AS c1 FROM [fh-bigquery:reddit_comments.2016_01] WHERE REGEXP_MATCH(body, r'(?i:obama)') GROUP BY subreddit ORDER BY c1 DESC LIMIT 10))
# ORDER BY r1
# LIMIT 100000)
# '''

try:
    # [START run_query]
    query_request = bigquery_service.jobs()
    query_data = {
        'query': (query)
    }

    query_response = query_request.query(
        projectId="reddit-1280",
        body=query_data).execute()
    # [END run_query]

    # [START print_results]
    print('Query Results:')
    print query_response['rows'][1]

    with open('bigquery.csv', 'wb') as csvfile:
	    writer = csv.writer(csvfile)

	    for row in query_response['rows']:
	    	writer.writerow([field['v'].encode('utf-8') for field in row['f']])
    # for row in query_response['rows']:

    #     print('\t'.join(field['v'] for field in row['f']))
    # [END print_results]

except HttpError as err:
    print('Error: {}'.format(err.content))
    raise err

elapsed_time = time.time() - start_time
print "elapsed time in seconds: " + str(elapsed_time)

