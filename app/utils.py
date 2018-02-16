INDEX_PATTERN = 'api'
PRODUCT_DOCTYPE = 'products'

def query_builder(params):
    query = {'query': {}}
    key, value = params.split(":")
    if key == 'sku': return filter_by_sku(value, query)
    elif key == 'category': return filter_by_category(value, query)
    elif key == 'created_at': return filter_by_date(value, query)
    return query

def filter_by_sku(sku, query):
    query['query']['match'] = {}
    query['query']['match']['sku'] = sku
    return query

def filter_by_category(category, query):
    query['query']['constant_score'] = {'filter': {'bool': {'must': [] }}}
    query_term = {"term" : {"category": category }}
    query['query']['constant_score']['filter']['bool']['must'].append(query_term)
    return query

def filter_by_date(date, query):
    query['query']['range'] = {'created_at': {}}
    query['query']['range']['created_at']['gte'] = date
    return query
