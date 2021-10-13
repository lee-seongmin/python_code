#%%
movie_rank=['닥터레인지', "스플릿", "럭키"]
movie_rank.append("배트맨")
movie_rank.insert(1,"슈퍼맨")
del movie_rank[3]
movie_rank.remove("배트맨")
movie_rank.pop()
print(movie_rank)
#%%
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)
# %%
nums = [1, 2, 3, 4, 5, 6, 7]
print("max : ",max(nums))
print("min : ",min(nums))
print(sum(nums))
nums_aver = sum(nums) / len(nums)
print(nums_aver)
# %%
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
# %%
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
# %%
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
# %%
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)
# %%
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0],interest[2])
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))
# %%
string = "삼성전자/LG전자/Naver"
interest = string.split("/") #리스트로 바로 왜 되냐
print(interest)
# %%
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
# %%
data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data, reverse=True)
print(data2)
# %%
