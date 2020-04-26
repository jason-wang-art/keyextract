from collections import defaultdict
import math
import operator
def loadDataSet():
    dataset =[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
           ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
           ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
           ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
           ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
           ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表好，0代表不好
    return dataset, classVec
def feature_select(list_words):
    doc_frequency=defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i]+=1
    word_tf={}
    for i in doc_frequency:
        word_tf[i]=doc_frequency[i]/sum(doc_frequency.values())
        doc_num=len(list_words)
        word_idf={}
        word_doc=defaultdict(int)
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i]+=1
    for i in doc_frequency:
        word_idf[i]=math.log(doc_num/(word_doc[i]+1))
        word_tf_idf={}
    for i in doc_frequency:
        word_tf_idf[i]=word_tf[i]*word_idf[i]
        dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_feature_select
if __name__ == '__main__':
    data_list, label_list = loadDataSet()  # 加载数据
    features = feature_select(data_list)  # 所有词的TF-IDF值
    print(features)
    print(len(features))