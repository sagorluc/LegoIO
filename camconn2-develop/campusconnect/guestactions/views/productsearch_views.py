from django.shortcuts import render
from ..myfunctions.es_ops.check_connection import get_es_connection
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from django.http import JsonResponse
from django.views.generic import (ListView,)
from django.views.generic.base import TemplateView


class ProductSearchResultsView(TemplateView):
    template_name = 'guestactions/product-search/layout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get user input query from GET request
        user_input_query = self.request.GET.get('query', None)

        # Connect to Elasticsearch client
        es_client = get_es_connection()

        # Build search query
        search_query = {
            "query": { 
                "match": {
                    "title": { "query": user_input_query }
                }
            }
        }

        # Search Elasticsearch index and get results
        results = es_client.search(index="mango2082", body=search_query)
        results = [i['_source'] for i in results['hits']['hits']]

        # Add search results to context
        context['results'] = results
        context['search_query_input_from_user'] = search_query['query']['match']['title']['query']

        context['product_line']     = 'Product Search'
        context['pg_layout_type']   = 'all_serv_list'
        context['pg_header']        = 'Search Results'

        return context
