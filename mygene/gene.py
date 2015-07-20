""" Represents a gene and it's data.
For more information about fields and what they mean
see: http://mygene.info/

author: Brian Schrader
since: 2015-06-26
"""


from api import endpoints, get, post


class Gene(object):
    """ A model of the gene object returned by Mygene APIs. """

    def __init__(self, entries):
        self.__dict__.update(entries)

    @staticmethod
    def find_by(**kwargs):
        """ Given a set of key-value pairs, or kwargs, search for the
        desired gene(s).
        :returns genes: list of matches for the query provided.
        """
        results = get(endpoints['get-query'], params=kwargs)
        genes = []
        for r in results.get('hits'):
            genes.append(Gene(r))
        return genes

    @staticmethod
    def find_multiple_by(**kwargs):
        """ Given a list of queries and key-value params.
        Find all of the genes that match any of the given criteria.
        :returns genes: list of matches for hte queries provieded.
        """
        results = post(endpoints['post-query'], params=kwargs)
        genes = []
        for r in results:
            genes.append(Gene(r))
        return genes

    @staticmethod
    def get(gene_id, **kwargs):
        """ Given a gene ID (as per the Mygene documentation)
        retrieve the given gene.
        :returns gene: a single gene object.
        """
        endpoint = endpoints['get-gene'].format(gene_id=gene_id)
        return Gene(get(endpoint, params=kwargs))

    @staticmethod
    def get_multiple(**kwargs):
        """ Given multiple gene IDs, retrieve all genes.
        :returns genes: list of genes with the IDs specified.
        """
        results = post(endpoints['post-gene'], params=kwargs)
        genes = []
        for r in results:
            genes.append(Gene(r))
        return genes
