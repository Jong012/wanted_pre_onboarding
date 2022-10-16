# 프리온보딩 코스 - 백엔드 사전과제
- [사전과제](https://bow-hair-db3.notion.site/5-1850bca26fda4e0ca1410df270c03409)

## git commit 컨벤션 정의
### message
1. 템플릿
{행위} {목적어} - {커밋 요약}

{메시지 상세 내용}

2. 설명
    - 행위
        1. INIT: 최초 생성   
        2. ADD: 내용을 추가함
        3. UPDATE: 내용을 변경함
    - 목적어
      : 행위의 대상을 의미함 실행 파일명이 될수도 있고, 라이브러리명 등이 될 수 있다.
    - 커밋 요약
      : 커밋 내용을 요약한다.
      
## 모델 스키마 정의
1. 회사(Company)
    - ID(pk - serial)
    - 회사명(varchar)
    - 국가(varchar)
    - 지역(varchar)
2. 사용자(Applicant)
    - id(pk - serial)
    - 사용자명(varchar)
    - 이메일(varchar)
    - 사용기술(varchar)
3. 채용공고(JobPosting)
    - ID(pk)
    - 채용 제목(varchar)
    - 채용포지션(varchar)
    - 채용 보상금(int)
    - 사용기술(varchar)
    - 채용내용(varchar) 
4. 지원내역(ApplicationDetails)   
    - 제약사항: 채용공고당 1회만 지원 가능함
    - 채용공고_id(fk)
    - 사용자_id(fk)
