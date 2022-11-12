"""
Module history analysis
"""
from datetime import datetime
from ast import literal_eval as make_tuple

def sites_on_date(visits: list, date: str) -> set():
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    """
    result_list = []
    for element in visits:
        if element[2] == date:
            result_list.append(element[0])
    return set(result_list)

def most_frequent_sites(visits: list, number: int) -> set():
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    """
    local_dictionary = {}
    result_list = []
    for element in visits:
        if element[0] not in local_dictionary:
            local_dictionary[element[0]] = 1
        else:
            value = local_dictionary[element[0]]
            value += 1
            local_dictionary[element[0]] = value
    sorted_dict = dict(sorted(local_dictionary.items(), key= lambda item: item[1], reverse= True))
    index = 0
    for element in sorted_dict:
        if index<number:
            result_list.append(element)
            index += 1
        else:
            break
    return set(result_list)

def get_url_info(visits: list, url: str) -> tuple():
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([('https://post.ua.nova.poshta/', 'NovaPoshta', '2020-09-15',\
    '11:31:55.290758', 188377297),\
    ('https://www.blank.com/', 'Blank', '2020-08-16', '23:20:32.633446', 119414007),\
    ('https://blanker.org/', 'Blanker', '2020-09-16', '14:15:34.901814', 369809373),\
    ('https://post.ua.nova.poshta/', 'NovaPoshta', '2020-09-15', '17:08:29.949781', 65220926)], \
    'https://www.blank.com/')
    ('Blank', '2020-08-16', '23:20:32.633446', 1, 119414007.0)
    """
    count = 0
    local_list = []
    for element in visits:
        if element[0] == url:
            if element[1] in local_list:
                count += 1
                date_visit_previous = datetime.strptime(local_list[1], '%Y-%m-%d').date()
                date_visit_current = datetime.strptime(element[2], '%Y-%m-%d').date()
                if date_visit_current > date_visit_previous:
                    local_list[1] = element[2]
                    local_list[2] = element[3]
                elif date_visit_current == date_visit_previous:
                    local_list[1] = element[2]
                    local_list[2] = max(element[3], local_list[2])
                local_list[3] = count
                local_list[4] += element[4]
            else:
                count = 1
                local_list.append(element[1])
                local_list.append(element[2])
                local_list.append(element[3])
                local_list.append(count)
                local_list.append(element[4])
    if count > 0:
        local_list[4] /= count
        return tuple(local_list)
    return ("","","",0,0)

def read_file(fine_name : str) -> list:
    """
    Returns list of history.
    """
    with open(fine_name, 'r', encoding="utf8") as file:
        str_read = file.read()
        history_list = list(make_tuple(str_read))
        return history_list

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
