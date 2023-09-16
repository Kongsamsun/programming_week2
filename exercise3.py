import re
while True:
    enter_email = input("텍스트를 입력하세요: ")
    if enter_email == 'done':
        print("프로그램 중지")
        break
    elif len(enter_email) <= 0:
        print("최소 한 개 이상의 텍스트를 입력하세요")
        continue
    else:
        x = re.findall("[a-zA-Z0-9-_]+@[a-zA-Z0-9-]+.[a-zA-Z]{3}", enter_email)
        if len(x) > 0:
            print("추출된 이메일 주소:")
            for email in x:
                print(email)
        else:
            print("메일 이름이 올바르지 않습니다")
            continue
