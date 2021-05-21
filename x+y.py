'''
This question is from movie x + y.
Q.)Twenty random cards are placed in a row all face down. A turn consists of taking two adjacent cards 
where the left one is face down and the right one can be face up or face down and flipping them both.
Show that this process must terminate.
'''

def transform(b):
    for i in range(len(b)-1):
        if b[i]=='1':
            b[i]='0'
            if b[i+1]=='0':
                b[i+1]='1'
            else:
                b[i+1] = '0'
            

    return b

if __name__ == "__main__":
    a = list("11101110111110111111")
    print(a)
    while a != transform(a.copy()):
        a = transform(a.copy())
    print(a)

