# 8-13 用户简介 ：复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介；调用这个函数时，指定你的
# 名和姓，以及三个描述你的键-值对。
def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Yanliang', 'einstein',
                             location='princeton',
                             field='physics',
                             degree='PHD')
print(user_profile)