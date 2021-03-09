# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:28:14 2020

@author: Injo Kim
"""
from github import Github
from material import crawling_material
import pandas as pd
from tqdm import tqdm


def url_organizer(url) :
    return url[0:8] + url[12:23] + url[29:]


def search_by_keyword(keywords, topic) :
    
    # watchers have error -> print stargazer data 
    matrix = []
    
    for keyword in tqdm(keywords) :
        for period in crawling_material.periods :
            query = '+'.join([keyword]) +' created:' + period[0] + '..' + period[1]
            result = git.search_repositories(query, sort='stars', order='desc')
                
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
                       contributors, len(contributors), repo.stargazers_count, repo.forks_count, topic, url_organizer(url)]
                    
                matrix.append(row)

    return pd.DataFrame(matrix, columns=crawling_material.column)


if __name__ == '__main__' :
   
    # set constant 
    ACCESS_TOKEN = open('material/access_token.txt', 'r').read()
    git = Github(ACCESS_TOKEN)

    for topic in crawling_material.topics :
        data = search_by_keyword(crawling_material.keywords[topic], topic)
        data.to_csv('crawled_data/' + topic + '.csv', index=False)

    del topic, git
        
