def get_profile(name):
    while True:
        try:
            user = api.get_user(screen_name = name)
            js = json.dumps(user[0].__json)
            print(js)
        except:
            print('error')