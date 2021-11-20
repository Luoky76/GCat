import base64
import codecs
import pandas as pd
import numpy as np
import jieba.posseg
import jieba.analyse
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from click.globals import push_context
from github import Github


stopkey = [w.strip() for w in codecs.open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]

def dataprepos(text, stopkey):
    l = []
    pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
    seg = jieba.posseg.cut(text)  # 分词
    for i in seg:
        if i.word not in stopkey and i.flag in pos:  # 去停用词 + 词性筛选
            l.append(i.word)
    return l



# 推送推荐仓库的full_name列表
class RepositoryRcmd():
    def __init__(self, g:Github)->None:
        self.__user = g.get_user()

    """
           TF-IDF权重：
               1、CountVectorizer 构建词频矩阵
               2、TfidfTransformer 构建tfidf权值计算
               3、文本的关键字
               4、对应的tfidf矩阵
    """

    def __getKeywords_tfidf(self, corpus, topK):
        # 1、构建词频矩阵，将文本中的词语转换成词频矩阵
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)  # 词频矩阵,a[i][j]:表示j词在第i个文本中的词频
        # 2、统计每个词的tf-idf权值
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(X)
        # 3、获取词袋模型中的关键词
        word = vectorizer.get_feature_names()
        # 4、获取tf-idf矩阵，a[i][j]表示j词在i篇文本中的tf-idf权重
        weight = tfidf.toarray()
        # 5、打印词语权重
        keys = []
        for i in range(len(weight)):
            #print(u"-------这里输出第", i + 1, u"篇文本的词语tf-idf------")
            df_word, df_weight = [], []  # 当前文章的所有词汇列表、词汇对应权重列表
            for j in range(len(word)):
                #print(word[j], weight[i][j])
                df_word.append(word[j])
                df_weight.append(weight[i][j])
            df_word = pd.DataFrame(df_word, columns=['word'])
            df_weight = pd.DataFrame(df_weight, columns=['weight'])
            word_weight = pd.concat([df_word, df_weight], axis=1)  # 拼接词汇列表和权重列表
            word_weight = word_weight.sort_values(by="weight", ascending=False)  # 按照权重值降序排列
            keyword = np.array(word_weight['word'])  # 选择词汇列并转成数组格式
            word_split = [keyword[x] for x in range(0, topK)]  # 抽取前topK个词汇作为关键词
            keys.append(word_split)
        #print(keys)
        return keys

    def __get_keyword(self):
        """获取用户的收藏仓库&高频keyword``[(事件类型，发生时间),...]``
            :param userID:用户名
            :return:返回一个keyword[[]]列表
        """
        readme_list = list()
        for repo in self.__user.get_starred():
            content = repo.get_readme()
            decode_content = base64.b64decode(content.content)
            readme_str = str(decode_content, 'utf-8')
            dataprepos(readme_str, stopkey)  # 文本预处理
            readme_list.append(readme_str)
        result = self.__getKeywords_tfidf(readme_list, 2)
        return result

    def getRcmd(self,g:Github)->list:
        md_list = self.__get_keyword()
        result_list = list()
        for each_md in md_list:
            for each_word in each_md:
                cnt = 0
                for repo in g.search_repositories(each_word, "stars", "desc"):
                    if cnt == 9:
                        break
                    cnt += 1
                    #print(repo.url)
                    result_list.append(repo.url)
        return result_list
