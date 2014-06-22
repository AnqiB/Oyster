import nltk
import nltk.data
import re #regular expression
fileread=open('C:/Users/Baiaq/Desktop/Harry_Potter_and_the_Goblet_of_Fire.txt','r')
filewrite=open('C:/Users/Baiaq/Desktop/outputHarry.txt','w')
'''读入一段话，进行处理。之所以这样做是因为文本文件可能比较大，分块处理比较好。'''
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
        if(line=="\n" and flag==1): #这种情况说明是段末
            flag=0
            string=' '.join(myset) #将一段话合成一个string
            '''正则表达式对一段话转成的句子进行处理，去掉不需要的部分，注意这里可以添加其它的正则表达式进行替换'''
            pattern=re.compile(r'\[.*\]') 
            string=pattern.sub(r'',string) #用设定的正则表达式对string进行处理，这里使用的是去掉'[]'及其中的内容
            
            sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
            sents = sent_detector.tokenize(string.strip())
           
            for sen in sents:
                filewrite.write(sen)
                filewrite.write('\n')
                #print sen
            del myset[:]

fileread.close()
filewrite.close()
            




