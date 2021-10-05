#연락처 관리 프로그램

menu=[i for i in range(1,6)]
friends = []
name=''

def print_list():
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 친구 이름 변경')
    print('5. 종료')

while menu !=5:
    print_list()
    
    menu=int(input("메뉴를 선택하세요. "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("이름을 입력하세요. ")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제할 이름을 입력하세요. ")
        if del_name in friends:
            friends.remove(name)
        else:
            print("삭제하려는 이름이 없습니다.")
    elif menu == 4:
        change_name = input("변경하고 싶은 이름을 입력하세요. ")
        if change_name in friends:
            index = friends.index(change_name)
            new_name = input("새로 입력할 이름을 입력하세요")
            friends[index] = new_name
        else:
            print("바꿀 이름이 없습니다.")