from fastapi import FastAPI

from main07 import insert_board_list

# 1. FastAPI앱 만들기
app = FastAPI()

# 2. 앤드포인트(주소) 등록하기
@app.get("/api/boards") #데코레이터 get 요청 들어오면 바로 아래 함수 실행해라.
def get_board():
    return insert_board_list() #리스트, 딕셔너리면 바로 json 형식으로 변환해줌

# 3. 서버실행하기
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main_api:app', host="0.0.0.0", port=8000, reload=True)
