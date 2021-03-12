# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:19:14 2021

@author: user
"""
import time
    
# variable declare

 
periods = [['2015-01-01', '2015-06-30'], ['2015-07-01', '2015-12-31'], ['2016-01-01', '2016-06-30'], ['2016-07-01', '2016-12-31'], ['2017-01-01', '2017-06-30'], 
           ['2017-07-01', '2017-12-31'], ['2018-01-01', '2018-06-30'], ['2018-07-01', '2018-12-31'], ['2019-01-01', '2019-06-30'], ['2019-07-01', '2019-12-31'], 
           ['2020-01-01', '2020-06-30'], ['2020-07-01', '2020-12-31'], ['2021-01-01', '2021-03-10']]

repository_column = ['total_index', 'repo_id', 'repo_name', 'owner_id', 'owner_type', 'create_date', 'update_date', 'topics', 'language', 'contributors', 'contributor_counts',  
         'stargazer_counts', 'forker_counts', 'keyword', 'readme_url']

user_column = ['total_index', 'user_id', 'user_name', 'repo_list', 'repo_count', 'company', 'email', 'location', 'followers', 'follower_count', 'following', 'following_count', 
               'organization_list', 'contributed_repo_count', 'forked_repo', 'forked_repo_count', 'url']

topics = ['image-processing', 'nlp', 'artificial-intelligence', 'autonomous-vehicle']

keywords = {'image-processing' : ['vision', 'image processing'], 'nlp' : ['nlp', 'natural language processing'], 
            'artificial-intelligence' : ['artificial intelligence', 'machine learning', 'deep learning'], 'autonomous-vehicle' : ['autonomous vehicle', 'human machine interface']}

number_of_repos = {'vision' : {'2015-01-01' : 1292, '2015-07-01' : 1398, '2016-01-01' : 2141, '2016-07-01' : 2459, '2017-01-01' : 1, '2017-07-01' : 1, '2018-01-01' : 1, '2018-07-01' : 1,
                               '2019-01-01' : 1, '2019-07-01' : 1, '2020-01-01' :1 , '2020-07-01' : 8949}, 
                   'image-processing' : {'2015-01-01' : 1013, '2015-07-01' : 1211, '2016-01-01' : 1427, '2016-07-01' : 1778, '2017-01-01' : 1, '2017-07-01' : 1, '2018-01-01' :1, '2018-07-01' : 1,
                               '2019-01-01' : 1, '2019-07-01' : 1, '2020-01-01' : 1, '2020-07-01' : 4983}}


# define method

def data_processing(data, column_list) :
    
    # change list data to string
    for col in column_list :
        data[col] = ['#'.join(map(str, corpus)) for corpus in data[col]] 
    
    return data


def url_organizer(url) :
    return url[0:8] + url[12:23] + url[29:]


def find_owner_type(string) :
    if string == None :
        owner_type = 'user'
    else :
        owner_type = 'organization'
    
    return owner_type

def make_user_id_set(data) :
    owner = list(set(data['owner_id']))
    contributors = list(set(data['contributors']))
    
    users = sorted(list(set(owner+contributors)))
    return users    


def rest(tiredness) :
    print('crawling process get in rest')
    
    tiredness = 0
    time.sleep(400)
    
    return tiredness