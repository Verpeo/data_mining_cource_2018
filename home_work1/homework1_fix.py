time = 1.57
print('{0:0>2.0f}:{1:0>2.0f}'.format(*divmod(time*3*60,60)))

N = 15605
print('{0:0>2.0f}:{1:0>2.0f}:{2:0>2.0f}'.format(*divmod((N//60),60),N%60))
