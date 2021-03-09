# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:28:14 2020

@author: Injo Kim
"""
from github import Github
import pandas as pd
from tqdm import tqdm


def url_organizer(url) :
    return url[0:8] + url[12:23] + url[29:]


def search_by_keyword(keywords) :
    
    # watchers have error -> print stargazer data 
    matrix = []
    
    for keyword in tqdm(keywords) :
        for period in periods :
            query = '+'.join([keyword]) +' created:' + period[0] + '..' + period[1]
            result = g.search_repositories(query, sort='stars', order='desc')
                
            print(f'\n\n Found {result.totalCount} repo(s)')
            print(query)
            
            for repo in tqdm(result) :
                contributors = [contributor.id for contributor in repo.get_contributors()]
                url = repo.url
                
                if repo.organization == None :
                    owner_type = 'user'
                else :
                    owner_type = 'organization'
                
                row = [repo.id, repo.name, repo.owner.id, repo.owner.name, owner_type, repo.created_at, repo.updated_at, repo.get_topics(), repo.language, 
                       contributors, len(contributors), repo.stargazers_count, repo.forks_count, url_organizer(url)]
                    
                matrix.append(row)

    return pd.DataFrame(matrix, columns=column)



if __name__ == '__main__' :
   
    # set constant 
    ACCESS_TOKEN = open('material/access_token.txt', 'r').read()
    topics = ['nlp', 'image-processing']
    keywords = {'nlp' : ['nlp', 'natural language processing'], 'image-processing' : ['vision', 'image processing']}
    g = Github(ACCESS_TOKEN)

    global column, periods
    
    column = ['repo_id', 'repo_name', 'owner_id', 'owner_name', 'owner_type', 'create_date', 'update_date', 'topics', 'language', 'contributors', 'contributor_counts',  
             'stargazer_counts', 'forker_counts', 'url']

    periods = [['2015-01-01', '2015-06-30'], ['2015-07-01', '2015-12-31'], ['2016-01-01', '2016-06-30'], ['2016-07-01', '2016-12-31'], ['2017-01-01', '2017-06-30'], 
              ['2017-07-01', '2017-12-31'], ['2018-01-01', '2018-06-30'], ['2018-07-01', '2018-12-31'], ['2019-01-01', '2019-06-30'], ['2019-07-01', '2019-12-31'], 
              ['2020-01-01', '2020-06-30'], ['2020-07-01', '2020-12-31'], ['2021-01-01', '2021-03-10']]
    
    for topic in topics :
        data = search_by_keyword(keywords[topic])
        data.to_csv('crawled_data/' + topic + '.csv', index=False)


        
