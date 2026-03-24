def next(s : str) -> str:
    chars = list(s)
        
    for i in range(len(chars) - 1, -1, -1): # Run on the rightmost

        if chars[i] == 'a':
            
            chars[i] = 'b'
                
            return "".join(chars)
        elif chars[i] == 'b':
            
            chars[i] = 'c'
                
            return "".join(chars) #Stop 
        elif chars[i] == 'c':
                chars[i] = 'a' #replace c with a
                
    return "a" * (len(s) + 1) 

    #aaa
def previous(s : str) -> str:
    chars = list(s)
        
    for i in range(len(chars)-1,-1,-1):
        if(chars[i] == 'a'):
            chars[i] = 'c' #replace a with c
        elif(chars[i] == 'b'):
            chars[i] = 'a'
            return ''.join(chars) 
        elif(chars[i] == 'c'):
            chars[i] ='b'
            return ''.join(chars)
            

    return 'c' * (len(s) + 1) 
def next_char(c : str) -> str:
    A = ['a','b','c']
    
    p_index = [i for i in range(0,len(A)) if c == A[i]]
    
    return A[-1] if A[p_index[0]] == 'a' else A[p_index[0] - 1]

if __name__ == '__main__':

    #test case for 1 2 
    print('aaa')
    print(f'next: {next('aaa')}, previous: {previous('aaa')}')
    print('cccc')
    print(f'next: {next('cccc')}, previous: {previous('cccc')}')
    #3
    print('a')
    print('b')
    print(f'stand behind character: {next_char('a')}')
    print(f'stand behind character: {next_char('b')}')
