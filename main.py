from loader import app
import routing  # Импорт всех ссылок
import uvicorn


class A(list):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(A)


a = A()


if __name__ == '__main__':
    uvicorn.run(app)
