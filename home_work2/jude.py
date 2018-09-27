head = 'Hey Jude,'
tail = ' to make it better'

JudeMatrix = [
    ['don\'t make it bad','Take a sad song and make it better','Remember to let her into your heart','Then you can start']
    ,['don\'t be afraid','You were made to go out and get her','The minute you let her under your skin','Then you begin']
    ,['don\'t let me down','You have found her, now go and get her','Remember to let her into your heart','Then you can start']
    ,['don\'t make it bad','Take a sad song and make it better','Remember to let her under your skin','Then you\'ll begin']
]

for verse in JudeMatrix:
    print('{}{}{}{}'.format(head ,   '\n'.join([str(line) for line in verse]),tail,'\n\n'))
