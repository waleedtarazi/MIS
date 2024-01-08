import pyterrier as pt
import pandas as pd
import os

if not pt.started():
    pt.init()

pd.set_option('display.max_colwidth', 150)

cord19 = pt.datasets.get_dataset('irds:cord19/trec-covid')

type(cord19)

d = []
for i in cord19.get_corpus_iter(verbose=False, count=10):
    d.append(i)
d = pd.DataFrame(d)

d.head(10)

docs_df = d

indexer = pt.DFIndexer("/content/terrier_cord19", overwrite=True)
index_ref = indexer.index(docs_df["abstract"], docs_df["docno"])
index_ref.toString()

index = pt.IndexFactory.of(index_ref)
type(index)

print(index.getCollectionStatistics().toString())

for kv in index.getLexicon():
    print("%s (%s) -> %s (%s)" % (kv.getKey(), type(kv.getKey()), kv.getValue().toString(), type(kv.getValue())))

index.getLexicon()["oxid"].toString()

pointer = index.getLexicon()["oxid"]
for posting in index.getInvertedIndex().getPostings(pointer):
    print(posting.toString() + " doclen=%d" % posting.getDocumentLength())

br = pt.BatchRetrieve(index, wmodel="Tf")
br.search("oxid")

queries = pd.DataFrame([["q1", "disease"], ["q2", "lung disease"]], columns=["qid", "query"])
br.transform(queries)

cord19.get_topics(variant='title').head(5)
cord19.get_qrels().head(10)
