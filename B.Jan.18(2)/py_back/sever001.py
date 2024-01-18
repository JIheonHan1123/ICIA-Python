from flask import Flask, request

# cf) class -> 사용자 정의 자료형을 만드는 방법. 파이썬의 모든 타입은 클래스
x = int()

# 1. __name__은 현재 파일의 이름 -> Flask 웹서버 객체를 생성
# 서버는 사용자 요청을 기다리다가 요청이 들어오면 처리해주는 프로그램이다
# Flask 웹서버는 5000번 포트로 사용자 요청을 대기한다
# Flask는 임포트 해줘야함
# 지금 이 코드치는 이런 파일 하나가 서버 하나임
# => 그래서 다른 서버 열 때는 지금 서버 끄고해야 5000번 포트 충돌이 안난다
app = Flask(__name__)


# flask는 터미널이 아니라 브라우저에서 실행함 => 주소를 줘야한다.
# 주소 주는 방식은 어노테이션(@)을 주면 된다
# @ = decorator (자바로 치면 어노테이션(annotation)) -추노에 노비낙인 같은거
# 서버 실행키는 동일 (F5 -> ! Ctrl+F5는 안먹음 주의 !)
@app.route("/hello")
def hello():
    return "hello flask"
    # 터미널에 뜨는 주소에 /hello 붙여줘야함


@app.route("/hello2")
def insa():
    return "헤이모두들안녕"


@app.route("/hello3")
def add():
    # request: 사용자가 요청한 정보를 담고있는 변수(자동으로 담겨있음)
    # request도 import 해와야 함
    '''
    print(request)
    return "까~꿍"
    '''

    # 터미널에 뜨는 주소에 /hello3 붙여주고 ?val=10을 붙여주면
    # http://127.0.0.1:5000/hello3?val=10 이렇게 되는데
    # 이걸 파이썬에서 받아오면 {'val':'10'}임 (인터넷에서 왔다갔다 하는건 다 문자 =request로 전달받은 값은 무조건 문자)
    # 코드로 표현하면 request.args['val'] (위 주소에 ?가 자동으로 딕셔너리를 만듬)
    val = request.args['val']
    return val


@app.route("/hello4")
def square():
    val = int(request.args['val'])
    result = val*val
    # request로 전달받은 값은 무조건 문자
    # => 리턴도 무조건 문자로
    return f'제곱결과는 {result}입니다'


# ex 1) 적정체중 = 키-105 로 가정
# 키를 입력받아 적정체중을 출력하는 서버 프로그램을 작성하시오
@app.route('/health')
def health():
    # 양 옆에 변수 이름이 똑같아야 함 ex) height = int...['val'] 이러면 안됨
    # request로 받아오는 key값이랑 그 key값을 담는 변수의 이름은 같아야한다.
    height = int(request.args['height'])
    result = height - 105
    return f'적정체중은 {result}입니다'


app.run()
# app.run(debug=True)
# 이거로 하면 서버 안끄고 계속 수정해도 됨
# 컴 뒤질수도 있응께 알아서 쓰기
