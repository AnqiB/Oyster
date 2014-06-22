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
            pattern1=re.compile(r'Mr\.') 
            string=pattern1.sub(r'Mr&',string) #后面还需要换回来

            pattern1_=re.compile(r'Mrs\.') 
            string=pattern1_.sub(r'Mrs&',string)
            
            pattern2=re.compile(r'(\.|\!|\?)\"')
            string=pattern2.sub(r'',string)     #直接去掉就不会被分开

            pattern3=re.compile(r' - ')
            string=pattern3.sub(r' ',string)                   

            pattern4=re.compile(r'\[.*\]') 
            string=pattern4.sub(r'',string)
            
            sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
            sents = sent_detector.tokenize(string.strip())
           
            for sen in sents:
			   
                pattern5=re.compile(r'(D|d)on\'t')
                sen=pattern5.sub(r'do not',sen)

                pattern6=re.compile(r'(C|c)an\'t')
                sen=pattern6.sub(r'can not',sen)

                pattern7=re.compile(r'(W|w)on\'t')
                sen=pattern7.sub(r'will not',sen)

                pattern8=re.compile(r'(D|d)oesn\'t')
                sen=pattern8.sub(r'does not',sen)

                pattern9=re.compile(r'(W|w)e\'re')
                sen=pattern9.sub(r'we are',sen)
                    
                pattern10=re.compile(r'(W|w)e\'ll')
                sen=pattern10.sub(r'we will',sen)

                pattern11=re.compile(r'(I|i)\'ve')
                sen=pattern11.sub(r'I have',sen)
                    
                pattern12=re.compile(r'(L|l)et\'s')
                sen=pattern12.sub(r'let us',sen)

                pattern13=re.compile(r'Mr\&') 
                sen=pattern13.sub(r'Mr ',sen)

                pattern13_=re.compile(r'Mrs\&') 
                sen=pattern13_.sub(r'Mrs ',sen)

                pattern14=re.compile(r'\'s') 
                sen=pattern14.sub(r' s',sen)

                #除了字母，其它所有的符号都删除
                sen=filter(lambda ch:ch in 'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM',sen)		
				
                filewrite.write(sen)
                filewrite.write('\n')
                #print sen
            del myset[:]

fileread.close()
filewrite.close()
            




