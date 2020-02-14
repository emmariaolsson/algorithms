"""
Write a function that does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)

An example:
www.saadbenn.com?a=1&b=2&a=2') // returns 'www.saadbenn.com?a=1&b=2'
"""
from collections import defaultdict
import urllib
import urllib.parse

# Here is a very non-pythonic grotesque solution
def strip_url_params1(url, params_to_strip=None):
    checked = 0
    visited_Branches = [0] * 32
    print("\n")

    if not params_to_strip:
        visited_Branches[0] = 1
        params_to_strip = []
    else:
        visited_Branches[1] = 1
    if url:
        visited_Branches[2] = 1
        result = '' # final result to be returned
        tokens = url.split('?')
        domain = tokens[0]
        query_string = tokens[-1]
        result += domain
        # add the '?' to our result if it is in the url
        if len(tokens) > 1:
            visited_Branches[3] = 1
            result += '?'
        else:
            visited_Branches[4] = 1
        if not query_string:
            visited_Branches[5] = 1
            for i in range(len(visited_Branches)):
                checked += (1 if visited_Branches[i] == 1 else 0)
            print(visited_Branches)
            print(str(checked/len(visited_Branches)+"%"))
            return url
        else:
            visited_Branches[6] = 1
            # logic for removing duplicate query strings
            # build up the list by splitting the query_string using digits
            key_value_string = []
            string = ''
            for char in query_string:
                visited_Branches[7] = 1
                if char.isdigit():
                    visited_Branches[8] = 1
                    key_value_string.append(string + char)
                    string = ''
                else:
                    visited_Branches[9] = 1
                    string += char
            dict = defaultdict(int)
            # logic for checking whether we should add the string to our result
            for i in key_value_string:
                visited_Branches[10] = 1
                _token = i.split('=')
                if _token[0]:
                    visited_Branches[11] = 1
                    length = len(_token[0])
                    if length == 1:
                        visited_Branches[12] = 1
                        if _token and (not(_token[0] in dict)):
                            visited_Branches[13] = 1
                            if params_to_strip:
                                visited_Branches[14] = 1
                                if _token[0] != params_to_strip[0]:
                                    visited_Branches[15] = 1
                                    dict[_token[0]] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else:
                                    visited_Branches[16] = 1
                            else:
                                visited_Branches[17] = 1
                                if not _token[0] in dict:
                                    visited_Branches[18] = 1
                                    dict[_token[0]] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else:
                                    visited_Branches[19] = 1
                        else: 
                            visited_Branches[20] = 1
                    else:
                        visited_Branches[21] = 1
                        check = _token[0]
                        letter = check[1]
                        if _token and (not(letter in dict)):
                            visited_Branches[22] = 1
                            if params_to_strip:
                                visited_Branches[23] = 1
                                if letter != params_to_strip[0]:
                                    visited_Branches[24] = 1
                                    dict[letter] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else:
                                    visited_Branches[25] = 1
                            else:
                                visited_Branches[26] = 1
                                if not letter in dict:
                                    visited_Branches[27] = 1
                                    dict[letter] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else:
                                    visited_Branches[28] = 1
                        else: 
                            visited_Branches[29] = 1
                else:
                    visited_Branches[30] = 1
    else:
        visited_Branches[31] = 1
    
    for i in range(len(visited_Branches)):
        checked += (1 if visited_Branches[i] == 1 else 0)
    
    print(visited_Branches)
    print(str(checked/len(visited_Branches))+"%")
    
    return result

# A very friendly pythonic solution (easy to follow)
def strip_url_params2(url, param_to_strip=[]):
    if '?' not in url:
        return url

    queries = (url.split('?')[1]).split('&')
    queries_obj = [query[0] for query in queries]
    for i in range(len(queries_obj) - 1, 0, -1):
        if queries_obj[i] in param_to_strip or queries_obj[i] in queries_obj[0:i]:
            queries.pop(i)

    return url.split('?')[0] + '?' + '&'.join(queries)


# Here is my friend's solution using python's builtin libraries
def strip_url_params3(url, strip=None):
    if not strip: strip = []
    
    parse = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parse.query)
    
    query = {k: v[0] for k, v in query.items() if k not in strip}
    query = urllib.parse.urlencode(query)
    new = parse._replace(query=query)
    
    return new.geturl()