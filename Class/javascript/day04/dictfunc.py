# 람다 대신 이걸 넣는 것도 가능
def poop():
    return "poop"

donghoon = {
    'name': 'donghoon',
    # 'poop': poop
    'poop': lambda : 'poop'
}

print(donghoon['poop']())