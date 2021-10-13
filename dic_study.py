a, b, *c = (0, 1, 2, 3, 4, 5, 6)
print(a,b,c)
#%%
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, c, d, e, f, g, h, *i = scores
valid_scores = a,b,c,d,e,f,g,h
print(valid_scores)
# %%
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_scores, _, _ =scores
print(valid_scores)
a, b , *valid_scores = scores
print(valid_scores)
c, *valid_scores, d = scores
print(valid_scores)
# %%
temp = {}
print(type(temp))
# %%
icecream = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800}
print(icecream)
icecream['죠스바'], icecream['월드콘'] = 1200, 1500 
#icecream['월드콘'] = 1500
print(icecream)
print("메로나 가격은 : ", icecream['메로나'])
icecream['메로나'] =1300
print(icecream)
del[icecream['메로나']]
print(icecream)
print(icecream.keys())
print(icecream.values())
print(sum(icecream.values()))
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
# %%
inventory = {'메로나' : [300, 20], '비비빅' : [400, 3], '죠스바' : [250, 100]}
print(inventory)
print(inventory['메로나'][0],"원")
print(inventory['메로나'][1], "개")
inventory['월드콘'] = [500, 7]
print(inventory)
# %%
# zip()함수를 몰랐을 때
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = {keys[0] : vals[0], keys[1] : vals[1], keys[2] : vals[2]}
print(result)
# %%
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
results = dict(zip(keys, vals))
re = list(zip(keys, vals))
print(result)
key1 , val1 =zip(*re)
key2, val2 =zip(*result)
print(key1, val1)

# %%
