
world = [[], []]

def add_object(o, depth = 0): # 게임 내 객체들을 추가하는 함수
    world[depth].append(o)

def add_objects(ol, depth = 0): # 게임 내 객체들을 여러 개 추가하는 함수
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise Exception("월드에 존재하지 않는 객체를 삭제하려고 합니다.")

# 게임 월드의 모든 객체들을 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

# 게임 월드의 모든 객체들을 그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()
