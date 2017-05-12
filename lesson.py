#-*- encoding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def qiushibaike():
    contet = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(contet, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())

def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')
    strb = ' \n\rhello \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')

def demo_operation():
    print 1, 1+2, 5/2, 5*2,5-2
    print 2, True, not True
    print 3, 1<2, 5>2, 1>4
    print 4, 2<<3
    print 5, 5|3, 5&3, 5^3
    x=2
    y=3.3
    print x, y, type(x), type(y)

def demo_buildinfunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1,2,3])
    print 3, abs(-2) #fabs,Math,fabs
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x+3')
    print 7, chr(97), ord('a')

def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    score=65

    # for(int i = 0; i<10; ++i)
    # continue ,break, pass
    for i in range(0, 10, 2):
        if i == 0:
            pass #do_special
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break

def demo_list():
    lista = [1,2,3]   #vector Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'wwww')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb*2

if __name__ == '__main__':
    print('hello world')
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    demo_list()