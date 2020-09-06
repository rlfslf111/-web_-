

## 5. 배포서버 URL

- front : https://inmin.netlify.app/
- back : http://inmin.herokuapp.com/

## 6. 기타

- 기타 참고

  - 서버 요청 url

  | HTTP Methods | url                          | 기능                                           | 기타                                      |
  | ------------ | ---------------------------- | ---------------------------------------------- | ----------------------------------------- |
  | post         | /rest-auth/signup/           | 회원가입                                       |                                           |
  | post         | /rest-auth/login/            | 로그인                                         | 토큰                                      |
  | post         | /rest-auth/logout/           | 로그아웃                                       | 로그인 필요                               |
  | put          | /accounts/12/                | 12번 유저 수정                                 | 본인, 관리자만                            |
  | delete       | /accounts/12/                | 12번 유저 삭제                                 | 본인, 관리자만                            |
  | get          | /articles/?page=3            | 게시글 목록 3 페이지 조회                      | 로그인 필요 / default: page=1             |
  | post         | /articles/                   | 게시글 생성                                    | 로그인 필요                               |
  | get          | /articles/12/                | 12번 게시글 조회                               | 로그인 필요                               |
  | put          | /articles/12/                | 12번 게시글 수정                               | 본인만 / title,content 필요               |
  | delete       | /articles/12/                | 12번 게시글 삭제                               | 본인만                                    |
  | get          | /articles/12/user            | 지금 요청한 유저가 12번글의 작성자인지 확인    | 로그인 필요/{status:OK/FAIL}              |
  | get          | /articles/12/comments/       | 12번글 댓글 조회                               | 로그인 필요                               |
  | post         | /articles/12/comments/       | 12번글 댓글 생성                               | 로그인 필요                               |
  | put          | /articles/12/comments/2/     | 12번글 2번째 댓글 수정                         | 로그인 필요 / content 필요                |
  | delete       | /articles/12/comments/2/     | 12번글 2번째 댓글 삭제                         | 로그인 필요                               |
  | get          | /articles/12/comments/2/user | 지금 요청한 유저가 12번 댓글의 작성자인지 확인 | 로그인 필요/{status:OK/FAIL}              |
  | get          | /articles/count/             | 게시글 총 페이지 조회                          | 로그인 필요                               |
  | get          | /movies/?page=3              | 영화 리스트 3페이지 조회                       | default: page=1                           |
  | post         | /movies/                     | 영화 생성                                      | 어드민만                                  |
  | get          | /movies/12/                  | 12번 영화 조회                                 |                                           |
  | put          | /movies/12/                  | 12번 영화 수정                                 | 어드민만                                  |
  | delete       | /movies/12/                  | 12번 영화 삭제                                 | 어드민만                                  |
  | get          | /movies/12/rate/             | 유저가 이전에 작성한 포인트 조회               | 로그인 필요 / {status:OK/FAIL,point:0~10} |
  | post         | /movies/12/rate/             | 12번 영회에 평점 작성/수정                     | 로그인 필요 / point 필요(0~10)            |
  | delete       | /movies/12/rate/             | 12번 영회에 평점 삭제                          | 로그인 필요                               |
  | get          | /movies/recommand/           | 영화 추천                                      | 로그인 필요                               |
  | get          | /movies/search/              | 자동완성을 위한 id, title                      | 로그인 필요                               |
  | get          | /movies/count/               | 영화 총 페이지 조회                            |                                           |

  - 데이터시딩

    ```shell
    # shell plus
    Genre.get_genre() # 장르데이터 가져오기
    Movie.get_movie() # 영화데이터 가져오기
    Article.dummy(n) # 게시글 n개 생성
    ```

    

