# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:28:14 2020

@author: Injo Kim
"""
from github import Github
from material import crawling_material
import numpy as np
import pandas as pd
import time

#%%
def crawling_data(repo, crawled_data, idx, keyword) :
    try :
    	contributors = [contributor.id for contributor in repo.get_contributors()]
    	url = repo.url
    	owner_type = crawling_material.find_owner_type(repo.organization)
    
    	try :
            row = [idx, repo.id, repo.name, repo.owner.id, owner_type, repo.full_name, repo.created_at, repo.updated_at, repo.get_topics(), repo.language, 
               contributors, len(contributors), repo.stargazers_count, repo.forks_count, keyword, crawling_material.url_organizer(url), repo.get_readme().size, repo.fork, 
               repo.open_issues, repo.parent]
        
    	except :
        	row = [idx, repo.id, repo.name, repo.owner.id, owner_type, repo.full_name, repo.created_at, repo.updated_at, repo.get_topics(), repo.language, 
               contributors, len(contributors), repo.stargazers_count, repo.forks_count, keyword, crawling_material.url_organizer(url), None, repo.fork, 
               repo.open_issues, repo.parent]
    
    	crawled_data.append(row)
        
    except :
        print('error occur')
    
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
        
    
def save_data(crawled_data, year, mode) :
    
    if mode == 'repo' :
        data = crawling_material.data_processing(pd.DataFrame(crawled_data, columns=crawling_material.repository_column), ['topics', 'contributors'])
        data.to_csv('crawled_data/data' + '_' + str(year)  + '.csv', mode='a', index=False, header=False)
        print('csv saved \n')
        
    elif mode == 'user' :
        data = crawling_material.data_processing(pd.DataFrame(crawled_data, columns=crawling_material.user_column), ['repo_id', 'followers', 'following', 'organization_list'])
        data.to_csv('crawled_data/user_' + str(year) + '.csv', index=False)


def search_by_keyword(start_date, end_date, save_point) :
    
    # watchers have error -> print stargazer data 
    # variable declare
    crawled_data = []; tiredness = 0 ; doc_idx = 0; idx = 0
    
    for period in crawling_material.make_periods_list(start_date, end_date) :  
        for keyword in crawling_material.keywords :
            if idx < save_point : 
                idx += crawling_material.number_of_repos[keyword][period]
                break
            
            else :
                try :
                    count_per_iteration = 0
                    query = '+'.join([keyword]) +' created:' + str(period)
                    result = git.search_repositories(query, sort='stars', order='desc')
                    
                    for repo in result :
                        crawled_data = crawling_data(repo, crawled_data, idx, keyword)
                            
                        print('{0} \t keyword : {1}, period : {2} \t {3}th data crawling out of {4} total data \t tiredness : {5}'.format(idx, keyword, period, 
                                                                                                                                              result.totalCount, count_per_iteration, tiredness))
                        count_per_iteration += 1
                        
                        time.sleep(np.random.random())
                        tiredness += 1
                        idx += 1
                        if tiredness == 300 or tiredness == 600 :
                            save_data(crawled_data, start_date[:4], mode='repo')
                            tiredness = crawling_material.rest(tiredness)
                            doc_idx+=1
                            crawled_data.clear()
                except :
                    print('repository does not exist')
                    
    save_data(crawled_data, start_date[:4], mode='repo')




#%%
if __name__ == '__main__' :
   
    # set constant 
    ACCESS_TOKEN = open('material/access_token.txt', 'r').readlines()
    INJO_TOKEN = ACCESS_TOKEN[0][:-1] ; JUNGMIN_TOKEN = ACCESS_TOKEN[1][:-1]; JAEHAN_TOKEN = ACCESS_TOKEN[3]
    SAVE_POINT = 0
    
    git = Github(JAEHAN_TOKEN)


    # topics 
    # machine-leaning
    # processed : image-processing, deep-learning
    # complete : aritificial-intelligence, autonomous-vehicle, automl, nlp, speech-recognition
    search_by_keyword('2016-01-01', '2016-12-31', SAVE_POINT)

    del git
        
