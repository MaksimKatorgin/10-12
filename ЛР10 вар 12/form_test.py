import pickle
TESTS=[ 'Test 1. Which of these operators is a complimentary operator??' \
            '<br>1. *<br> 2. +<br>3. ~;1' ,
        'Test 2. Which of these operators is higher in priority?' \
            '<br>1. &<br>2. **<br>3. >>;2' ,
        'Test 3. Which of these operators is not an assignation operator??' \
            '<br>1. ==<br>2. //=<br>3. %=;1' ,
        'Test 4. Which of these operators does not belong to Boolean operators ?' \
            '<br>1. and<br>2. not<br>3. is;3' ,
        'Test 5. Which of these operators is an integer division operator?' \
            '<br>1. /<br>2. %<br>3. //;3' ]
f= open('tests.dat' , 'wb')
pickle.dump(TESTS,f)
f.close()
print ( "It's done" )
