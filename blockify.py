import json
import urlparse


def lambda_handler(event, context):
    print event
     
    params = urlparse.parse_qs(event['body'])
    message = ''
    if 'text' not in params or not params['text']:
        message = 'Bad Request'
        return {
            'statusCode': str(200),
            'body': json.dumps({'text': message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    command = params['text'][0]
    print command
    opts = command.split(' ')
    print opts
    if len(opts) < 2:
        message = 'Must provide emoji and text'
        return {
            'statusCode': str(200),
            'body': json.dumps({'text': message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    e = opts[0]
    text = command[(len(e)+1):]
    
    b = ':blank:'
    #e = event['queryStringParameters']['emoji']
    if e[0] != ':':
        e = ':' + e
    if e[-1] != ':':
        e += ':'

    letters = []
    
    a = [
        b + e + b,
        e + b + e,
        e + e + e,
        e + b + e,
        e + b + e,  
        ]
    letters.append(a)
    
    B = [
        e + e + b,
        e + b + e,
        e + e + b,
        e + b + e,
        e + e + b,  
        ]
    letters.append(B)
    
    c = [
        e + e + e,
        e + b + b,
        e + b + b,
        e + b + b,
        e + e + e,  
        ]
    letters.append(c)
    
    d = [
        e + e + b,
        e + b + e,
        e + b + e,
        e + b + e,
        e + e + b,  
        ]
    letters.append(d)
    
    E = [
        e + e + e,
        e + b + b,
        e + e + e,
        e + b + b,
        e + e + e,  
        ]
    letters.append(E)
    
    f = [
        e + e + e,
        e + b + b,
        e + e + e,
        e + b + b,
        e + b + b,  
        ]
    letters.append(f)
    
    g = [
        b + e + e,
        e + b + b,
        e + b + e,
        e + b + e,
        b + e + e,  
        ]
    letters.append(g)
    
    h = [
        e + b + e,
        e + b + e,
        e + e + e,
        e + b + e,
        e + b + e,  
        ]
    letters.append(h)
    
    i = [
        e + e + e,
        b + e + b,
        b + e + b,
        b + e + b,
        e + e + e,  
        ]
    letters.append(i)
    
    j = [
        b + b + e,
        b + b + e,
        b + b + e,
        e + b + e,
        e + e + e,  
        ]
    letters.append(j)
    
    k = [
        e + b + e,
        e + b + e,
        e + e + b,
        e + b + e,
        e + b + e,  
        ]
    letters.append(k)
    
    l = [
        e + b + b,
        e + b + b,
        e + b + b,
        e + b + b,
        e + e + e,  
        ]
    letters.append(l)
    
    m = [
        e + b + b + b + e,
        e + e + b + e + e,
        e + b + e + b + e,
        e + b + b + b + e,
        e + b + b + b + e,  
        ]
    letters.append(m)
    
    n = [
        e + e + e,
        e + b + e,
        e + b + e,
        e + b + e,
        e + b + e,  
        ]
    letters.append(n)
    
    o = [
        e + e + e,
        e + b + e,
        e + b + e,
        e + b + e,
        e + e + e,  
        ]
    letters.append(o)
    
    p = [
        e + e + e,
        e + b + e,
        e + e + e,
        e + b + b,
        e + b + b,  
        ]
    letters.append(p)
    
    q = [
        e + e + e + b,
        e + b + e + b,
        e + b + e + b,
        e + b + e + b,
        e + e + e + e,  
        ]
    letters.append(q)
    
    r = [
        e + e + b,
        e + b + e,
        e + e + b,
        e + b + e,
        e + b + e,  
        ]
    letters.append(r)
    
    s = [
        b + e + e,
        e + b + b,
        b + e + b,
        b + b + e,
        e + e + b,  
        ]
    letters.append(s)
    
    t = [
        e + e + e,
        b + e + b,
        b + e + b,
        b + e + b,
        b + e + b,  
        ]
    letters.append(t)
    
    u = [
        e + b + e,
        e + b + e,
        e + b + e,
        e + b + e,
        e + e + e,  
        ]
    letters.append(u)
    
    v = [
        e + b + e,
        e + b + e,
        e + b + e,
        e + b + e,
        b + e + b,  
        ]
    letters.append(v)
    
    w = [
        e + b + b + b + e,
        e + b + b + b + e,
        e + b + e + b + e,
        e + e + b + e + e,
        e + b + b + b + e,    
        ]
    letters.append(w)
    
    x = [
        e + b + e,
        e + b + e,
        b + e + b,
        e + b + e,
        e + b + e,  
        ]
    letters.append(x)
    
    y = [
        e + b + e,
        e + b + e,
        e + e + e,
        b + e + b,
        b + e + b,  
        ]
    letters.append(y)
    
    z = [
        e + e + e,
        b + b + e,
        b + e + b,
        e + b + b,
        e + e + e,  
        ]
    letters.append(z)
    
    numbers = []
    zero = [
        b + e + b,
        e + b + e,
        e + b + e,
        e + b + e,
        b + e + b,  
        ]
    numbers.append(zero)
    
    one = [
        b + e + b,
        e + e + b,
        b + e + b,
        b + e + b,
        e + e + e,  
        ]
    numbers.append(one)
    
    two = [
        e + e + b,
        b + b + e,
        b + e + b,
        e + b + b,
        e + e + e,  
        ]
    numbers.append(two)
    
    three = [
        e + e + e,
        b + b + e,
        b + e + e,
        b + b + e,
        e + e + e,  
        ]
    numbers.append(three)
    
    four = [
        e + b + e,
        e + b + e,
        e + e + e,
        b + b + e,
        b + b + e,  
        ]
    numbers.append(four)
    
    five = [
        e + e + e,
        e + b + b,
        e + e + e,
        b + b + e,
        e + e + b,  
        ]
    numbers.append(five)
    
    six = [
        b + e + e,
        e + b + b,
        e + e + e,
        e + b + e,
        e + e + e,  
        ]
    numbers.append(six)
    
    seven = [
        e + e + e,
        b + b + e,
        b + e + b,
        e + b + b,
        e + b + b,  
        ]
    numbers.append(seven)
    
    eight = [
        e + e + e,
        e + b + e,
        e + e + e,
        e + b + e,
        e + e + e,  
        ]
    numbers.append(eight)
    
    nine = [
        e + e + e,
        e + b + e,
        e + e + e,
        b + b + e,
        e + e + b,  
        ]
    numbers.append(nine)
    
    blockheight = 5
    for i in range(blockheight):
        line = ''
        for char in text:
            if len(line) != 0:
                line += b
            if char.isalpha():
                block = letters[ord(char.lower()) - ord('a')][i]
                line += block
            elif char.isdigit():
                block = numbers[ord(char) - ord('0')][i]
                line += block
        message += line + '\n'

    return {
        'statusCode': str(200),
        'body': json.dumps({"response_type": "in_channel", 'text': message}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
