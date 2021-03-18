# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:19:14 2021

@author: user
"""
import datetime
import time
    
# variable declare   
        
repository_column = ['total_index', 'repo_id', 'repo_name', 'owner_id', 'owner_type', 'full_name', 'create_date', 'update_date', 'topics', 'language', 'contributors', 'contributor_counts',  
          'stargazer_counts', 'forker_counts', 'keyword', 'readme_url', 'read_length', 'is_it_forked_repo', 'open_issues', 'original_repo']

user_column = ['total_index', 'user_id', 'user_name', 'repo_list', 'repo_count', 'company', 'email', 'location', 'followers', 'follower_count', 'following', 'following_count', 
               'organization_list', 'contributed_repo_count', 'forked_repo', 'forked_repo_count', 'readme_size', 'url']

'''
keywords = {'image-processing' : ['computer vision'], 'nlp' : ['nlp'], 'speech-recognition' : ['speech recognition'],
            'artificial-intelligence' : ['artificial intelligence'], 'machine-learning' : ['machine learning'], 'deep-learning' : ['deep learning'], 'autonomous-vehicle' : ['autonomous vehicle'],
            'auto-ml' : ['automl']}
'''
keywords = ['computer vision', 'nlp', 'speech recognition', 'artificial intelligence', 'machine learning', 'deep learning', 'autonomous vehicle', 'automl']


number_of_repos = {'vision' : {'2015-01-01' : 1292, '2015-07-01' : 1398, '2016-01-01' : 2141, '2016-07-01' : 2459, '2017-01-01' : 3928, '2017-07-01' : 4456, '2018-01-01' : 5556, '2018-07-01' : 5658,
                               '2019-01-01' : 7025, '2019-07-01' : 7022, '2020-01-01' :9412 , '2020-07-01' : 8949}, 
                   'image processing' : {'2015-01-01' : 1013, '2015-07-01' : 1211, '2016-01-01' : 1427, '2016-07-01' : 1778, '2017-01-01' : 2372, '2017-07-01' : 2556, '2018-01-01' :3207, '2018-07-01' : 3443,
                               '2019-01-01' : 4112, '2019-07-01' : 4353, '2020-01-01' : 5238, '2020-07-01' : 4983},
                   'image recognition' : {'2015-01-01' : 144, '2015-07-01' : 186, '2016-01-01' : 272, '2016-07-01' : 407, '2017-01-01' : 723, '2017-07-01' : 901, '2018-01-01' :1307, '2018-07-01' : 1341,
                               '2019-01-01' : 1737, '2019-07-01' : 1536, '2020-01-01' : 1987, '2020-07-01' : 2100},
                   'nlp' : {'2015-01-01' : 986, '2015-07-01' : 1179, '2016-01-01' : 1656, '2016-07-01' : 2089, '2017-01-01' : 3504, '2017-07-01' : 4366, '2018-01-01' :6442, '2018-07-01' : 7239,
                               '2019-01-01' : 9251, '2019-07-01' : 10298, '2020-01-01' : 15021, '2020-07-01' : 15244},
                   'artificial intelligence' : {'2015-01-01' : 626, '2015-07-01' : 711, '2016-01-01' : 930, '2016-07-01' : 1072, '2017-01-01' : 1772, '2017-07-01' : 2087, '2018-01-01' :2462, '2018-07-01' : 2375,
                               '2019-01-01' : 2885, '2019-07-01' : 2848, '2020-01-01' : 4016, '2020-07-01' : 3499},
                   'machine learning' : {'2015-01-01' : 5315, '2015-07-01' : 6623, '2016-01-01' : 8854, '2016-07-01' : 10718, '2017-01-01' : 15952, '2017-07-01' : 20583, '2018-01-01' :26705, '2018-07-01' : 28480,
                               '2019-01-01' : 32010, '2019-07-01' : 32920, '2020-01-01' : 45405, '2020-07-01' : 44778},
                   'deep learning' : {'2015-01-01' : 504, '2015-07-01' : 670, '2016-01-01' : 1592, '2016-07-01' : 2574, '2017-01-01' : 7139, '2017-07-01' : 8941, '2018-01-01' :10734, '2018-07-01' : 12118,
                               '2019-01-01' : 14891, '2019-07-01' : 14488, '2020-01-01' : 20681, '2020-07-01' : 18640},
                   'autonomous vehicle' : {'2015-01-01' : 30, '2015-07-01' : 33, '2016-01-01' : 55, '2016-07-01' : 74, '2017-01-01' : 162, '2017-07-01' : 191, '2018-01-01' :247, '2018-07-01' : 235,
                               '2019-01-01' : 305, '2019-07-01' : 293, '2020-01-01' : 383, '2020-07-01' : 396},
                    'speech recognition' : {'2015-01-01' : 228, '2015-07-01' : 271, '2016-01-01' : 350, '2016-07-01' : 474, '2017-01-01' : 623, '2017-07-01' : 772, '2018-01-01' :1002, '2018-07-01' : 908,
                               '2019-01-01' : 1061, '2019-07-01' : 1220, '2020-01-01' : 1601, '2020-07-01' : 1539}  ,
                    'automl' : {'2015-01-01' : 10, '2015-07-01' : 15, '2016-01-01' : 12, '2016-07-01' : 13, '2017-01-01' : 19, '2017-07-01' : 40, '2018-01-01' :76, '2018-07-01' : 190,
                               '2019-01-01' : 256, '2019-07-01' : 307, '2020-01-01' : 388, '2020-07-01' : 510}                                   
                   }


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
    #time.sleep(500)
    
    return tiredness


def make_periods_list(start, end) :
    start = datetime.date(int(start.split('-')[0]), int(start.split('-')[1]), int(start.split('-')[2]))
    end = datetime.date(int(end.split('-')[0]), int(end.split('-')[1]), int(end.split('-')[2]))
    time_delta = end - start
        
    date_result = [(start + datetime.timedelta(days=day)).isoformat() for day in range(time_delta.days)]
        
    return date_result
            
    
            
    
    