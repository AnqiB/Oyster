import nltk
import nltk.data
import re #regular expression
fileread=open('C:/Users/Baiaq/Desktop/Harry_Potter_and_the_Goblet_of_Fire.txt','r')
filewrite=open('C:/Users/Baiaq/Desktop/outputHarry.txt','w')
'''����һ�λ������д���֮��������������Ϊ�ı��ļ����ܱȽϴ󣬷ֿ鴦��ȽϺá�'''
flag=0
myset=list()
for line in fileread.readlines():
    if(line): #not the end of file
        
        if(line!="\n" and flag==0):
            flag=1
        if(line!="\n" and flag==1):
            myset.append(line.strip())
            #print "--------"
            #print line
        if(line=="\n" and flag==1): #�������˵���Ƕ�ĩ
            flag=0
            string=' '.join(myset) #��һ�λ��ϳ�һ��string
            '''������ʽ��һ�λ�ת�ɵľ��ӽ��д���ȥ������Ҫ�Ĳ��֣�ע������������������������ʽ�����滻'''
            pattern=re.compile(r'\[.*\]') 
            string=pattern.sub(r'',string) #���趨��������ʽ��string���д�������ʹ�õ���ȥ��'[]'�����е�����
            
            sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
            sents = sent_detector.tokenize(string.strip())
           
            for sen in sents:
                filewrite.write(sen)
                filewrite.write('\n')
                #print sen
            del myset[:]

fileread.close()
filewrite.close()
            




