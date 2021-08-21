# capitalize_word_in_crossword

###bozorg kardane horof
def capitalize_word_in_crossword(crossword,word):
    if not word or not crossword:
        return None
    listed=None
    copy_crossword=crossword
    #olaviyat ofoghi 
    listed=find_word_horizontal(crossword,word)
    if listed:
    
        h=listed[0]
        v=listed[1]
        for index in range(len(word)):
            copy_crossword[h][v+index]=copy_crossword[h][v+index].upper()
        
        
        
    if listed==None:
        listed=find_word_vertical(crossword,word)
       
        if listed!=None:
            print(listed)
            h=listed[0]
            v=listed[1]        
            for index in range(len(word)):
               
                copy_crossword[h+index][v]=copy_crossword[h+index][v].upper()
    
    return copy_crossword
    
#ofhoghi chisi peyda mikone   
def find_word_horizontal(crossword,word):    
    dic={}
    i=0
    listed_index=[]
    row_index="none"
    word_one=word[0]
    for i in range(len(crossword)):
        dic[i]=crossword[i]
        string="".join(dic[i])
        if word in string:
          
            row_index=i
            column_index=dic[i].index(word_one)
           
    if row_index!="none":
        listed_index.append(row_index)
        listed_index.append(column_index)
  
        return listed_index
    else:
        return None
#amodi chisi peyda mikone
def find_word_vertical(crossword,word):
    if not crossword or not word:
        return None    
    number_of_columns=len(crossword[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crossword)):
            temp_str=temp_str+crossword[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None
#test
crossword=[['s','d','o','g'],['c','a','t','m'],['c','f','d','t'],['t','e','t','k']]
word='safe'
print(capitalize_word_in_crossword(crossword,word))
