from stanfordcorenlp import StanfordCoreNLP

# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port, timeout=30000)

# The sentence you want to parse
sentence = open('sample.txt', 'r').read()
#
# POS
print('POS：', nlp.pos_tag(sentence))

# NER
print('NER：', nlp.ner(sentence))

# co-reference resolution
res = nlp.annotate(sentence,
                   properties={
                       'annotators': 'coref',
                        'outputFormat': 'json',
                       'timeout': 30000,
                   })
print(res)
# Sentimental Analysis
res = nlp.annotate(sentence,
                   properties={
                       'annotators': 'sentiment',
                        'outputFormat': 'json',
                       'timeout': 30000,
                   })
print(res)


# Close Stanford Parser
nlp.close()