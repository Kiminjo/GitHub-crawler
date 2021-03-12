# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:28:14 2020

@author: Injo Kim
"""
from github import Github
from material import crawling_material, db_connect
import numpy as np
import pandas as pd
import time

#%%
def crawling_data(repo, crawled_data, idx) :
    contributors = [contributor.id for contributor in repo.get_contributors()]
    url = repo.url
    owner_type = crawling_material.find_owner_type(repo.organization)
    
    row = [idx, repo.id, repo.name, repo.owner.id, owner_type, repo.created_at, repo.updated_at, repo.get_topics(), repo.language, 
           contributors, len(contributors), repo.stargazers_count, repo.forks_count, topic, crawling_material.url_organizer(url)]
    crawled_data.append(row)
    
    return crawled_data


def crawling_user(user_list) :
    # modify 'repos'
    # can not crawling where user contribute and fork
    
    doc_idx = 0; idx = 0; tiredness = 0; crawled_data = []
    
    for user_id in user_list : 
        user = git.get_user_by_id(user_id)
        repos = [repo for repo in user.get_repos()]
        followers = [follower for follower in user.get_followers()]
        followings = [following for following in user.get_followings()]
        organizations = [organization for organization in user.get_orgs()]
        
        row = [idx, user_id, user.name, repos, len(repos), user.company, user.email, user.location, followers, len(followers), followings, len(followings), organizations, user.contributions,
               user.url]
        
        crawled_data.append(row)
        idx += 1; tiredness += 1
        
        if tiredness == 300 :
            save_data(crawled_data, doc_idx, mode='user')
            tiredness = crawling_material.rest(tiredness)
            doc_idx += 1
        
    
def save_data(crawled_data, idx, mode) :
    
    if mode == 'repo' :
        data = crawling_material.data_processing(pd.DataFrame(crawled_data, columns=crawling_material.repository_column), ['topics', 'contributors'])
        data.to_csv('crawled_data/' + topic + '_' + str(idx) + '.csv', index=False)
        
    elif mode == 'user' :
        data = crawling_material.data_processing(pd.DataFrame(crawled_data, columns=crawling_material.user_column), ['repo_id', 'followers', 'following', 'organization_list'])
        data.to_csv('crawled_data/user_' + str(idx) + '.csv', index=False)


def search_by_keyword(keywords, topic, save_point) :
    
    # watchers have error -> print stargazer data 
    # variable declare
    crawled_data = []; tiredness = 0 ; doc_idx = 11; idx = 0

    for period in crawling_material.periods :
        for keyword in keywords :
            if idx < save_point : 
                idx += crawling_material.number_of_repos[keyword][period[0]]
                break
            
            else :
                count_per_iteration = 0
                query = '+'.join([keyword]) +' created:' + period[0] + '..' + period[1]
                result = git.search_repositories(query, sort='stars', order='desc')
                
                for repo in result :
                    crawled_data = crawling_data(repo, crawled_data, idx)
                        
                    print('{0} \t keyword : {1}, period : {2}-{3} \t {4}th data crawling out of {5} total data \t tiredness : {6}'.format(idx, keyword, period[0], period[1], 
                                                                                                                                          result.totalCount, count_per_iteration, tiredness))
                    count_per_iteration += 1
                    
                    time.sleep(np.random.random())
                    tiredness += 1
                    idx += 1
                    if tiredness == 300 :
                        save_data(crawled_data, doc_idx, mode='repo')
                        tiredness = crawling_material.rest(tiredness)
                        doc_idx+=1
    
                        #connection = db_connect.db_connect()
                        #db_connect.send_data_to_db(connection, data)
                        
    save_data(crawled_data, doc_idx)



#%%
if __name__ == '__main__' :
   
    # set constant 
    ACCESS_TOKEN = open('material/access_token.txt', 'r').readlines()
    INJO_TOKEN = ACCESS_TOKEN[0][:-1] ; JUNGMIN_TOKEN = ACCESS_TOKEN[1][:-1]; SEONGSEOP_TOKEN = ACCESS_TOKEN[2][:-1]; SAEROME_TOKEN = ACCESS_TOKEN[3]
    SAVE_POINT = 3000
    
    git = Github(INJO_TOKEN)

    for topic in crawling_material.topics :
        search_by_keyword(crawling_material.keywords[topic], topic, SAVE_POINT)

    del topic, git
        
