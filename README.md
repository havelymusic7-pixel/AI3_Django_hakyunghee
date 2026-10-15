# Django Todo List

MySQL과 Django를 사용한 Todo List CRUD 프로젝트입니다.

## 주요 기능

- 할 일 등록, 목록 조회, 수정, 삭제
- 진행 및 완료 상태 변경
- 완료 항목 취소선 표시
- 입력값 유효성 검사와 오류 메시지
- Django 관리자 페이지에서 Todo 관리

## 실행 준비

1. `pip install -r requirements.txt`
2. MySQL에 `todo_db` 데이터베이스를 생성합니다.
3. `TODO_DB_USER`, `TODO_DB_PASSWORD`, `TODO_DB_HOST`, `TODO_DB_PORT` 환경변수를 설정합니다. 또는 Git에 올리지 않는 `config/local_settings.py`에 `MYSQL_PASSWORD = "내 비밀번호"`를 지정할 수 있습니다.
4. `python manage.py migrate`를 실행해 Django 기본 테이블과 Todo 테이블을 생성합니다.
5. `python manage.py createsuperuser`로 관리자 계정을 만들고 `python manage.py runserver`를 실행합니다.

`schema.sql`은 과제 제출용 Todo 테이블 DDL입니다. 실행 준비에서는 이 테이블을 직접 만들지 말고 Django 마이그레이션을 사용하세요.
