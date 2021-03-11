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

column = ['total_index', 'repo_id', 'repo_name', 'owner_id', 'owner_type', 'create_date', 'update_date', 'topics', 'language', 'contributors', 'contributor_counts',  
         'stargazer_counts', 'forker_counts', 'keyword', 'readme_url']

topics = ['image-processing']

keywords = {'image-processing' : ['vision', 'image processing'], 'nlp' : ['nlp', 'natural language processing']}

number_of_repos = {'vision' : {'2015-01-01' : 1292, '2015-07-01' : 1398, '2016-01-01' : 2141, '2016-07-01' : 2459}, 
                   'image-processing' : {'2015-01-01' : 1013, '2015-07-01' : 1211, '2016-01-01' : 1427, '2016-07-01' : 1778}}


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


def rest(crawling_result, tiredness) :
    print('crawling process get in rest')
    
    tiredness = 0
    time.sleep(500)
    
    return tiredness