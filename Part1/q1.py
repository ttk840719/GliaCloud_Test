urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png"
]
def couting(urls):
    dct = {}
    for url in urls:
        name = url.rsplit('/', 1)[-1] ## get file name, put into dictionary
        if name in dct:
            dct[name] += 1
        else:
            dct[name] = 1
    sort_lst = sorted(dct, key = dct.get, reverse = True)
    print(sort_lst[:3]) ## get the top 3 in the list

couting(urls)    