MyGene-Api
=============

A simple Python wrapper for the MyGene API.

For extensive API documentation, see the [MyGene](http://mygene.info) site.

Install me from PyPi! `pip install mygene-api`

*Basic Example*

Find a given gene with the id: CDK2.

```python
""" Use the query API to find a gene with 
the given symbol.
"""
from mygene.gene import Gene

results = Gene.find_by(q='CDK2')
for r in result:
    print r._id, r.name

>>> 1017 cyclin-dependent kinase 2
12566 cyclin-dependent kinase 2
362817 cyclin dependent kinase 2
52004 CDK2-associated protein 2
...
```

*Detailed Example*

Given an known gene, get it's begin and end coordinates. 

```python
""" Use the annotation API to find the full 
details of a given gene.
"""
from mygene.gene import gene

gene = Gene.get('1017')
print gene._id, gene.genomic_pos_hg19['start'], gene.genomic_pos_hg19['end']

>>> 1017 56360553 56366568
```

This library also supports the metadata API.

```python
from mygene.metadata import Metadata

metadata = Metadata.get_metadata()
print metadata.stats['total_genes']

>>> 12611464
```



