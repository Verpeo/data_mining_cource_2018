import re

def is_Good_Pass(pwd):
    regex = '(?=.*\W+.*)(?=.{6}.*)(?=.*[a-z]+.*)(?=.*[A-Z]+.*)(?=.*[0-9]+.*)'
    #regex = '(?i)(?=.*\d[^a-z]+.*)(?=.{6}.*)(?=.*[a-z]+.*)(?=.*[A-Z]+.*)(?=.*[0-9]+.*)'
    return not re.match(regex,pwd) is None

pass_counter = 0
pass_true_counter = 0

with  open('10-million-password-list-top-500.txt','r', encoding='utf-8') as tmp_file:
    for password in tmp_file:
        pass_counter +=1
        if is_Good_Pass(password):
            pass_true_counter +=1

if pass_counter > 0:
    print('total pass count: {}, Good passes: {}, proportion of good passes: {}'.format(pass_counter,pass_true_counter, pass_true_counter/float(pass_counter) ))

#-------------------------------


poem = """5 little piges.
This little pig went to market,
This little pig stayed at home,
This little pig had roast beef,
And this little pig had none,
This little pig said, "Wee, wee, wee!
I can't find my way home."""

#with re:
#print(len(set(re.sub('[^\w ]', '', poem).lower().split())))

#with replace:
print(len(set(poem.replace('.','').replace(',','').replace('!','').replace('"','').lower().split())))


#-------------------------------
ss = 'AAAAAhBBBBBhCCCCChDDDDDD'
#ss = 'habrahabr'
#ss = 'hh'
letter = 'h'


# l = len(ss)
# end_pos = -1
# beg_pos = -1
# for a in range(l):
#     if  ss[-a-1] == letter:
#         end_pos = l-a
#         break

beg_pos = int(ss.find(letter))
end_pos = int(ss.rfind(letter))+1

if    beg_pos <=  end_pos:
    print(ss[:beg_pos]  + ss[end_pos:])
