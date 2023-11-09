from app import create_app
from app.main import views

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#디버크 켜져있는지 확인하기