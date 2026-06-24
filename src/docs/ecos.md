› 상세주소https://ecos.bok.or.kr/api/   (https와 http 모두 사용 가능합니다.)

요청인자
항목명(국문)	필수여부	샘플데이터	항목설명
서비스명	Y	StatisticTableList	API서비스명
인증키	Y	sample	한국은행에서 발급받은 오픈API 인증키
요청유형	Y	xml	결과값의 파일 형식 - xml, json
언어구분	Y	kr	결과값의 언어 - kr(국문), en(영문)
요청시작건수	Y	1	전체 결과값 중 시작 번호
요청종료건수	Y	10	전체 결과값 중 끝 번호
통계표코드	N	102Y004	통계표코드
메시지 설명
에러 및 정보배치
정보-100 : 인증키가 유효하지 않습니다. 인증키를 확인하십시오! 인증키가 없는 경우 인증키를 신청하십시오!

정보-200 : 해당하는 데이터가 없습니다.

에러-100 : 필수 값이 누락되어 있습니다. 필수 값을 확인하십시오! 필수 값이 누락되어 있으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-101 : 주기와 다른 형식의 날짜 형식입니다.

에러-200 : 파일타입 값이 누락 혹은 유효하지 않습니다. 파일타입 값을 확인하십시오! 파일타입 값이 누락 혹은 유효하지 않으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-300 : 조회건수 값이 누락되어 있습니다. 조회시작건수/조회종료건수 값을 확인하십시오! 조회시작건수/조회종료건수 값이 누락되어 있으면 오류를 발생합니다.

에러-301 : 조회건수 값의 타입이 유효하지 않습니다. 조회건수 값을 확인하십시오! 조회건수 값의 타입이 유효하지 않으면 오류를 발생합니다. 정수를 입력하세요.

에러-400 : 검색범위가 적정범위를 초과하여 60초 TIMEOUT이 발생하였습니다. 요청조건 조정하여 다시 요청하시기 바랍니다.

에러-500 : 서버 오류입니다. OpenAPI 호출시 서버에서 오류가 발생하였습니다. 해당 서비스를 찾을 수 없습니다.

에러-600 : DB Connection 오류입니다. OpenAPI 호출시 서버에서 DB접속 오류가 발생했습니다.

에러-601 : SQL 오류입니다. OpenAPI 호출시 서버에서 SQL 오류가 발생했습니다.

에러-602 : 과도한 OpenAPI호출로 이용이 제한되었습니다. 잠시후 이용해주시기 바랍니다.

출력값(Out Result)
항목명(국문)	항목명(영문)	항목크기	샘플데이터	항목설명
상위통계표코드	P_STAT_CODE	8	0000000442	상위통계표코드
통계표코드	STAT_CODE	8	102Y004	통계표코드
통계명	STAT_NAME	200	1.1.1.1.2. 본원통화 구성내역(평잔, 원계열)	통계명
주기	CYCLE	2	M	주기(년, 분기, 월)
검색가능여부	SRCH_YN	1	Y	검색가능여부
출처	ORG_NAME	50	한국은행	출처

샘플 URL (Sample 위치에 인증키 값을 입력)
https://ecos.bok.or.kr/api/StatisticTableList/sample/xml/kr/1/10/102Y004
예제
<?xml version="1.0" encoding="UTF-8"?>
<StatisticTableList>
  <list_total_count number="true">1</list_total_count>
  <row array="true">
    <P_STAT_CODE>0000000622</P_STAT_CODE>
    <STAT_CODE>102Y004</STAT_CODE>
    <STAT_NAME>1.1.1.1.1. 본원통화 구성내역(평잔, 계절조정계열)</STAT_NAME>
    <CYCLE>M</CYCLE>
    <SRCH_YN>Y</SRCH_YN>
    <ORG_NAME/>
  </row>
</StatisticTableList>

## 통계용어사전

요청인자
항목명(국문)	필수여부	샘플데이터	항목설명
서비스명	Y	StatisticWord	API서비스명
인증키	Y	sample	한국은행에서 발급받은 오픈API 인증키
요청유형	Y	xml	결과값의 파일 형식 - xml, json
언어구분	Y	kr	결과값의 언어 - kr(국문), en(영문)
요청시작건수	Y	1	전체 결과값 중 시작 번호
요청종료건수	Y	10	전체 결과값 중 끝 번호
용어	Y	소비자동향지수	용어
메시지 설명
에러 및 정보배치
정보-100 : 인증키가 유효하지 않습니다. 인증키를 확인하십시오! 인증키가 없는 경우 인증키를 신청하십시오!

정보-200 : 해당하는 데이터가 없습니다.

에러-100 : 필수 값이 누락되어 있습니다. 필수 값을 확인하십시오! 필수 값이 누락되어 있으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-101 : 주기와 다른 형식의 날짜 형식입니다.

에러-200 : 파일타입 값이 누락 혹은 유효하지 않습니다. 파일타입 값을 확인하십시오! 파일타입 값이 누락 혹은 유효하지 않으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-300 : 조회건수 값이 누락되어 있습니다. 조회시작건수/조회종료건수 값을 확인하십시오! 조회시작건수/조회종료건수 값이 누락되어 있으면 오류를 발생합니다.

에러-301 : 조회건수 값의 타입이 유효하지 않습니다. 조회건수 값을 확인하십시오! 조회건수 값의 타입이 유효하지 않으면 오류를 발생합니다. 정수를 입력하세요.

에러-400 : 검색범위가 적정범위를 초과하여 60초 TIMEOUT이 발생하였습니다. 요청조건 조정하여 다시 요청하시기 바랍니다.

에러-500 : 서버 오류입니다. OpenAPI 호출시 서버에서 오류가 발생하였습니다. 해당 서비스를 찾을 수 없습니다.

에러-600 : DB Connection 오류입니다. OpenAPI 호출시 서버에서 DB접속 오류가 발생했습니다.

에러-601 : SQL 오류입니다. OpenAPI 호출시 서버에서 SQL 오류가 발생했습니다.

에러-602 : 과도한 OpenAPI호출로 이용이 제한되었습니다. 잠시후 이용해주시기 바랍니다.

출력값(Out Result)
항목명(국문)	항목명(영문)	항목크기	샘플데이터	항목설명
용어	WORD	100	소비자동향지수	용어
용어설명	CONTENT	4000	소비자들이 느끼는 경기, 소비지출계획, 생활형편 등 경제에 대한 전반적인 인식을 조사하여 지수화함으로써 소비 및 경기를 파악하는 지표로 활용된다. 소비자동향지수는 1964년 미국 미시간대학이 최초로 작성하였으며 그 이후 우리나라를 비롯한 세계 각국에서 편제하여 공표하고 있다. 한국은행의 소비자동향지수는 매월 초～중순에 걸쳐 조사하여 하순에 결과를 발표하고 있다.	용어설명

플 URL (Sample 위치에 인증키 값을 입력)
https://ecos.bok.or.kr/api/StatisticWord/sample/xml/kr/1/10/소비자동향지수
예제
<?xml version="1.0" encoding="UTF-8"?>
<StatisticWord>
  <list_total_count number="true">1</list_total_count>
  <row array="true">
    <WORD>소비자동향지수</WORD>
    <CONTENT>소비자들이 느끼는 경기, 소비지출계획, 생활형편 등 경제에 대한 전반적인 인식을 조사하여 지수화함으로써 소비 및 경기를 파악하는 지표로 활용된다. 소비자동향지수는 1964년 미국 미시간대학이 최초로 작성하였으며 그 이후 우리나라를 비롯한 세계 각국에서 편제하여 공표하고 있다. 한국은행의 소비자동향지수는 매월 초～중순에 걸쳐 조사하여 하순에 결과를 발표하고 있다. </CONTENT>
  </row>
</StatisticWord>

## 통계 세부항목 목록

요청인자
항목명(국문)	필수여부	샘플데이터	항목설명
서비스명	Y	StatisticItemList	API서비스명
인증키	Y	sample	한국은행에서 발급받은 오픈API 인증키
요청유형	Y	xml	결과값의 파일 형식 - xml, json
언어구분	Y	kr	결과값의 언어 - kr(국문), en(영문)
요청시작건수	Y	1	전체 결과값 중 시작 번호
요청종료건수	Y	10	전체 결과값 중 끝 번호
통계표코드	Y	601Y002	통계표코드
메시지 설명
에러 및 정보배치
정보-100 : 인증키가 유효하지 않습니다. 인증키를 확인하십시오! 인증키가 없는 경우 인증키를 신청하십시오!

정보-200 : 해당하는 데이터가 없습니다.

에러-100 : 필수 값이 누락되어 있습니다. 필수 값을 확인하십시오! 필수 값이 누락되어 있으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-101 : 주기와 다른 형식의 날짜 형식입니다.

에러-200 : 파일타입 값이 누락 혹은 유효하지 않습니다. 파일타입 값을 확인하십시오! 파일타입 값이 누락 혹은 유효하지 않으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-300 : 조회건수 값이 누락되어 있습니다. 조회시작건수/조회종료건수 값을 확인하십시오! 조회시작건수/조회종료건수 값이 누락되어 있으면 오류를 발생합니다.

에러-301 : 조회건수 값의 타입이 유효하지 않습니다. 조회건수 값을 확인하십시오! 조회건수 값의 타입이 유효하지 않으면 오류를 발생합니다. 정수를 입력하세요.

에러-400 : 검색범위가 적정범위를 초과하여 60초 TIMEOUT이 발생하였습니다. 요청조건 조정하여 다시 요청하시기 바랍니다.

에러-500 : 서버 오류입니다. OpenAPI 호출시 서버에서 오류가 발생하였습니다. 해당 서비스를 찾을 수 없습니다.

에러-600 : DB Connection 오류입니다. OpenAPI 호출시 서버에서 DB접속 오류가 발생했습니다.

에러-601 : SQL 오류입니다. OpenAPI 호출시 서버에서 SQL 오류가 발생했습니다.

에러-602 : 과도한 OpenAPI호출로 이용이 제한되었습니다. 잠시후 이용해주시기 바랍니다.

출력값(Out Result)
항목명(국문)	항목명(영문)	항목크기	샘플데이터	항목설명
통계표코드	STAT_CODE	8	601Y002	통계표코드
통계명	STAT_NAME	200	7.5.2. 지역별 소비유형별 개인 신용카드	통계명
항목그룹코드	GRP_CODE	20	Group1	항목그룹코드
항목그룹명	GRP_NAME	60	지역코드	항목그룹명
통계항목코드	ITEM_CODE	20	A	통계항목코드
통계항목명	ITEM_NAME	200	서울	통계항목명
상위통계항목코드	P_ITEM_CODE	8	null	상위통계항목코드
상위통계항목명	P_ITEM_NAME	200	null	상위통계항목명
주기	CYCLE	2	M	주기
수록시작일자	START_TIME	8	200912	수록시작일자
수록종료일자	END_TIME	8	202112	수록종료일자
자료수	DATA_CNT	22	145	자료수
단위	UNIT_NAME	200	십억원	단위
가중치	WEIGHT	22	null	가중치

샘플 URL (Sample 위치에 인증키 값을 입력)
https://ecos.bok.or.kr/api/StatisticItemList/sample/xml/kr/1/10/601Y002
예제
<?xml version="1.0" encoding="UTF-8"?>
<StatisticItemList>
  <list_total_count number="true">61</list_total_count>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>A</ITEM_CODE>
    <ITEM_NAME>서울</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>B</ITEM_CODE>
    <ITEM_NAME>부산</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>C</ITEM_CODE>
    <ITEM_NAME>대구</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>D</ITEM_CODE>
    <ITEM_NAME>인천</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>E</ITEM_CODE>
    <ITEM_NAME>광주</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>F</ITEM_CODE>
    <ITEM_NAME>대전</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>G</ITEM_CODE>
    <ITEM_NAME>울산</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>L</ITEM_CODE>
    <ITEM_NAME>경기</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>M</ITEM_CODE>
    <ITEM_NAME>강원</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
  <row>
    <STAT_CODE>601Y002</STAT_CODE>
    <STAT_NAME>7.5.2. 지역별 소비유형별 개인 신용카드</STAT_NAME>
    <GRP_CODE>Group1</GRP_CODE>
    <GRP_NAME>지역코드</GRP_NAME>
    <ITEM_CODE>N</ITEM_CODE>
    <ITEM_NAME>충북</ITEM_NAME>
    <P_ITEM_CODE/>
    <P_ITEM_NAME/>
    <CYCLE>M</CYCLE>
    <START_TIME>200912</START_TIME>
    <END_TIME>202308</END_TIME>
    <DATA_CNT number="true">13530</DATA_CNT>
    <UNIT_NAME/>
    <WEIGHT/>
  </row>
</StatisticItemList>

## 통계 조회 조건 설정

요청인자
항목명(국문)	필수여부	샘플데이터	항목설명
서비스명	Y	StatisticSearch	API서비스명
인증키	Y	sample	한국은행에서 발급받은 오픈API 인증키
요청유형	Y	xml	결과값의 파일 형식 - xml, json
언어구분	Y	kr	결과값의 언어 - kr(국문), en(영문)
요청시작건수	Y	1	전체 결과값 중 시작 번호
요청종료건수	Y	10	전체 결과값 중 끝 번호
통계표코드	Y	200Y101	통계표코드
주기	Y	A	주기(년:A, 반년:S, 분기:Q, 월:M, 반월:SM, 일: D)
검색시작일자	Y	2020	검색시작일자(주기에 맞는 형식으로 입력: 2020, 2020Q1, 202001, 20200101 등)
검색종료일자	Y	2023	검색시작일자(주기에 맞는 형식으로 입력: 2023, 2023Q1, 202301, 20230101 등)
통계항목코드1	N	10101	통계항목코드1
통계항목코드2	N	?	통계항목코드2
통계항목코드3	N	?	통계항목코드3
통계항목코드4	N	?	통계항목코드4
메시지 설명
에러 및 정보배치
정보-100 : 인증키가 유효하지 않습니다. 인증키를 확인하십시오! 인증키가 없는 경우 인증키를 신청하십시오!

정보-200 : 해당하는 데이터가 없습니다.

에러-100 : 필수 값이 누락되어 있습니다. 필수 값을 확인하십시오! 필수 값이 누락되어 있으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-101 : 주기와 다른 형식의 날짜 형식입니다.

에러-200 : 파일타입 값이 누락 혹은 유효하지 않습니다. 파일타입 값을 확인하십시오! 파일타입 값이 누락 혹은 유효하지 않으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-300 : 조회건수 값이 누락되어 있습니다. 조회시작건수/조회종료건수 값을 확인하십시오! 조회시작건수/조회종료건수 값이 누락되어 있으면 오류를 발생합니다.

에러-301 : 조회건수 값의 타입이 유효하지 않습니다. 조회건수 값을 확인하십시오! 조회건수 값의 타입이 유효하지 않으면 오류를 발생합니다. 정수를 입력하세요.

에러-400 : 검색범위가 적정범위를 초과하여 60초 TIMEOUT이 발생하였습니다. 요청조건 조정하여 다시 요청하시기 바랍니다.

에러-500 : 서버 오류입니다. OpenAPI 호출시 서버에서 오류가 발생하였습니다. 해당 서비스를 찾을 수 없습니다.

에러-600 : DB Connection 오류입니다. OpenAPI 호출시 서버에서 DB접속 오류가 발생했습니다.

에러-601 : SQL 오류입니다. OpenAPI 호출시 서버에서 SQL 오류가 발생했습니다.

에러-602 : 과도한 OpenAPI호출로 이용이 제한되었습니다. 잠시후 이용해주시기 바랍니다.

출력값(Out Result)
항목명(국문)	항목명(영문)	항목크기	샘플데이터	항목설명
통계표코드	STAT_CODE	8	200Y101	통계표코드
통계명	STAT_NAME	200	2.1.1.1. 주요지표(연간지표)	통계명
통계항목코드1	ITEM_CODE1	20	10101	통계항목코드1
통계항목명1	ITEM_NAME1	200	국내총생산(명목, 원화표시)	통계항목명1
통계항목코드2	ITEM_CODE2	20	null	통계항목코드2
통계항목명2	ITEM_NAME2	200	null	통계항목명2
통계항목코드3	ITEM_CODE3	20	null	통계항목코드3
통계항목명3	ITEM_NAME3	200	null	통계항목명3
통계항목코드4	ITEM_CODE4	20	null	통계항목코드3
통계항목명4	ITEM_NAME4	200	null	통계항목명4
단위	UNIT_NAME	200	십억원	단위
가중치	WGT	22	null	가중치
시점	TIME	8	2020	시점
값	DATA_VALUE	23	1658020.4	값

샘플 URL (Sample 위치에 인증키 값을 입력)
https://ecos.bok.or.kr/api/StatisticSearch/sample/xml/kr/1/10/200Y101/A/2020/2023/10101/?/?/?
예제
<?xml version="1.0" encoding="UTF-8"?>
<StatisticSearch>
  <list_total_count number="true">4</list_total_count>
  <row>
    <STAT_CODE>200Y101</STAT_CODE>
    <STAT_NAME>2.1.1.1. 주요지표(연간지표)</STAT_NAME>
    <ITEM_CODE1>10101</ITEM_CODE1>
    <ITEM_NAME1>국내총생산(명목, 원화표시)</ITEM_NAME1>
    <ITEM_CODE2/>
    <ITEM_NAME2/>
    <ITEM_CODE3/>
    <ITEM_NAME3/>
    <ITEM_CODE4/>
    <ITEM_NAME4/>
    <UNIT_NAME>십억원</UNIT_NAME>
    <WGT/>
    <TIME>2020</TIME>
    <DATA_VALUE>2058466.5</DATA_VALUE>
  </row>
  <row>
    <STAT_CODE>200Y101</STAT_CODE>
    <STAT_NAME>2.1.1.1. 주요지표(연간지표)</STAT_NAME>
    <ITEM_CODE1>10101</ITEM_CODE1>
    <ITEM_NAME1>국내총생산(명목, 원화표시)</ITEM_NAME1>
    <ITEM_CODE2/>
    <ITEM_NAME2/>
    <ITEM_CODE3/>
    <ITEM_NAME3/>
    <ITEM_CODE4/>
    <ITEM_NAME4/>
    <UNIT_NAME>십억원</UNIT_NAME>
    <WGT/>
    <TIME>2021</TIME>
    <DATA_VALUE>2223719.9</DATA_VALUE>
  </row>
  <row>
    <STAT_CODE>200Y101</STAT_CODE>
    <STAT_NAME>2.1.1.1. 주요지표(연간지표)</STAT_NAME>
    <ITEM_CODE1>10101</ITEM_CODE1>
    <ITEM_NAME1>국내총생산(명목, 원화표시)</ITEM_NAME1>
    <ITEM_CODE2/>
    <ITEM_NAME2/>
    <ITEM_CODE3/>
    <ITEM_NAME3/>
    <ITEM_CODE4/>
    <ITEM_NAME4/>
    <UNIT_NAME>십억원</UNIT_NAME>
    <WGT/>
    <TIME>2022</TIME>
    <DATA_VALUE>2328169</DATA_VALUE>
  </row>
  <row>
    <STAT_CODE>200Y101</STAT_CODE>
    <STAT_NAME>2.1.1.1. 주요지표(연간지표)</STAT_NAME>
    <ITEM_CODE1>10101</ITEM_CODE1>
    <ITEM_NAME1>국내총생산(명목, 원화표시)</ITEM_NAME1>
    <ITEM_CODE2/>
    <ITEM_NAME2/>
    <ITEM_CODE3/>
    <ITEM_NAME3/>
    <ITEM_CODE4/>
    <ITEM_NAME4/>
    <UNIT_NAME>십억원</UNIT_NAME>
    <WGT/>
    <TIME>2023</TIME>
    <DATA_VALUE>2407575.8</DATA_VALUE>
  </row>
</StatisticSearch>

## 100대 통계지표

요청인자
항목명(국문)	필수여부	샘플데이터	항목설명
서비스명	Y	KeyStatisticList	API서비스명
인증키	Y	sample	한국은행에서 발급받은 오픈API 인증키
요청유형	Y	xml	결과값의 파일 형식 - xml, json
언어구분	Y	kr	결과값의 언어 - kr(국문), en(영문)
요청시작건수	Y	1	전체 결과값 중 시작 번호
요청종료건수	Y	10	전체 결과값 중 끝 번호
메시지 설명
에러 및 정보배치
정보-100 : 인증키가 유효하지 않습니다. 인증키를 확인하십시오! 인증키가 없는 경우 인증키를 신청하십시오!

정보-200 : 해당하는 데이터가 없습니다.

에러-100 : 필수 값이 누락되어 있습니다. 필수 값을 확인하십시오! 필수 값이 누락되어 있으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-101 : 주기와 다른 형식의 날짜 형식입니다.

에러-200 : 파일타입 값이 누락 혹은 유효하지 않습니다. 파일타입 값을 확인하십시오! 파일타입 값이 누락 혹은 유효하지 않으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-300 : 조회건수 값이 누락되어 있습니다. 조회시작건수/조회종료건수 값을 확인하십시오! 조회시작건수/조회종료건수 값이 누락되어 있으면 오류를 발생합니다.

에러-301 : 조회건수 값의 타입이 유효하지 않습니다. 조회건수 값을 확인하십시오! 조회건수 값의 타입이 유효하지 않으면 오류를 발생합니다. 정수를 입력하세요.

에러-400 : 검색범위가 적정범위를 초과하여 60초 TIMEOUT이 발생하였습니다. 요청조건 조정하여 다시 요청하시기 바랍니다.

에러-500 : 서버 오류입니다. OpenAPI 호출시 서버에서 오류가 발생하였습니다. 해당 서비스를 찾을 수 없습니다.

에러-600 : DB Connection 오류입니다. OpenAPI 호출시 서버에서 DB접속 오류가 발생했습니다.

에러-601 : SQL 오류입니다. OpenAPI 호출시 서버에서 SQL 오류가 발생했습니다.

에러-602 : 과도한 OpenAPI호출로 이용이 제한되었습니다. 잠시후 이용해주시기 바랍니다.

출력값(Out Result)
항목명(국문)	항목명(영문)	항목크기	샘플데이터	항목설명
통계그룹명	CLASS_NAME	400	국민소득 · 경기 · 기업경영	통계그룹명
통계명	KEYSTAT_NAME	200	경제성장률(전기대비)	통계명
값	DATA_VALUE	23	1.9	값
시점	CYCLE	13	202003	통계의 최근 수록 시점
단위	UNIT_NAME	200	%, 달러, 십억원 등	단위

샘플 URL (Sample 위치에 인증키 값을 입력)
https://ecos.bok.or.kr/api/KeyStatisticList/sample/xml/kr/1/10
예제
<?xml version="1.0" encoding="UTF-8"?>
<KeyStatisticList>
  <list_total_count number="true">101</list_total_count>
  <row_count number="true">10</row_count>
  <row>
    <CLASS_NAME>통화량</CLASS_NAME>
    <KEYSTAT_NAME>M1(협의통화, 평잔)</KEYSTAT_NAME>
    <DATA_VALUE>1381957.1</DATA_VALUE>
    <CYCLE>202604</CYCLE>
    <UNIT_NAME>십억원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>통화량</CLASS_NAME>
    <KEYSTAT_NAME>M2(광의통화, 평잔)</KEYSTAT_NAME>
    <DATA_VALUE>4160887.5</DATA_VALUE>
    <CYCLE>202604</CYCLE>
    <UNIT_NAME>십억원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>환율</CLASS_NAME>
    <KEYSTAT_NAME>원/달러 환율(종가)</KEYSTAT_NAME>
    <DATA_VALUE>1539.1</DATA_VALUE>
    <CYCLE>20260623</CYCLE>
    <UNIT_NAME>원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>환율</CLASS_NAME>
    <KEYSTAT_NAME>원/엔(100엔) 환율(매매기준율)</KEYSTAT_NAME>
    <DATA_VALUE>951.53</DATA_VALUE>
    <CYCLE>20260624</CYCLE>
    <UNIT_NAME>원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>환율</CLASS_NAME>
    <KEYSTAT_NAME>원/유로 환율(매매기준율)</KEYSTAT_NAME>
    <DATA_VALUE>1749.64</DATA_VALUE>
    <CYCLE>20260624</CYCLE>
    <UNIT_NAME>원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>환율</CLASS_NAME>
    <KEYSTAT_NAME>원/위안 환율(종가)</KEYSTAT_NAME>
    <DATA_VALUE>227.06</DATA_VALUE>
    <CYCLE>20260623</CYCLE>
    <UNIT_NAME>원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>채권</CLASS_NAME>
    <KEYSTAT_NAME>국고채발행액</KEYSTAT_NAME>
    <DATA_VALUE>19582</DATA_VALUE>
    <CYCLE>202604</CYCLE>
    <UNIT_NAME>십억원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>소득</CLASS_NAME>
    <KEYSTAT_NAME>GDP(명목, 계절조정)</KEYSTAT_NAME>
    <DATA_VALUE>764882.3</DATA_VALUE>
    <CYCLE>2026Q1</CYCLE>
    <UNIT_NAME>십억원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>소비</CLASS_NAME>
    <KEYSTAT_NAME>개인신용카드사용액</KEYSTAT_NAME>
    <DATA_VALUE>78674829</DATA_VALUE>
    <CYCLE>202603</CYCLE>
    <UNIT_NAME>백만원</UNIT_NAME>
  </row>
  <row>
    <CLASS_NAME>가계</CLASS_NAME>
    <KEYSTAT_NAME>가구당월평균소득</KEYSTAT_NAME>
    <DATA_VALUE>6969.4</DATA_VALUE>
    <CYCLE>2024Q4</CYCLE>
    <UNIT_NAME>천원</UNIT_NAME>
  </row>
</KeyStatisticList>

요청인자
항목명(국문)	필수여부	샘플데이터	항목설명
서비스명	Y	StatisticMeta	API서비스명
인증키	Y	sample	한국은행에서 발급받은 오픈API 인증키
요청유형	Y	xml	결과값의 파일 형식 - xml, json
언어구분	Y	kr	결과값의 언어 - kr(국문), en(영문)
요청시작건수	Y	1	전체 결과값 중 시작 번호
요청종료건수	Y	10	전체 결과값 중 끝 번호
데이터명	Y	경제심리지수	데이터명
메시지 설명
에러 및 정보배치
정보-100 : 인증키가 유효하지 않습니다. 인증키를 확인하십시오! 인증키가 없는 경우 인증키를 신청하십시오!

정보-200 : 해당하는 데이터가 없습니다.

에러-100 : 필수 값이 누락되어 있습니다. 필수 값을 확인하십시오! 필수 값이 누락되어 있으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-101 : 주기와 다른 형식의 날짜 형식입니다.

에러-200 : 파일타입 값이 누락 혹은 유효하지 않습니다. 파일타입 값을 확인하십시오! 파일타입 값이 누락 혹은 유효하지 않으면 오류를 발생합니다. 요청 변수를 참고 하십시오!

에러-300 : 조회건수 값이 누락되어 있습니다. 조회시작건수/조회종료건수 값을 확인하십시오! 조회시작건수/조회종료건수 값이 누락되어 있으면 오류를 발생합니다.

에러-301 : 조회건수 값의 타입이 유효하지 않습니다. 조회건수 값을 확인하십시오! 조회건수 값의 타입이 유효하지 않으면 오류를 발생합니다. 정수를 입력하세요.

에러-400 : 검색범위가 적정범위를 초과하여 60초 TIMEOUT이 발생하였습니다. 요청조건 조정하여 다시 요청하시기 바랍니다.

에러-500 : 서버 오류입니다. OpenAPI 호출시 서버에서 오류가 발생하였습니다. 해당 서비스를 찾을 수 없습니다.

에러-600 : DB Connection 오류입니다. OpenAPI 호출시 서버에서 DB접속 오류가 발생했습니다.

에러-601 : SQL 오류입니다. OpenAPI 호출시 서버에서 SQL 오류가 발생했습니다.

에러-602 : 과도한 OpenAPI호출로 이용이 제한되었습니다. 잠시후 이용해주시기 바랍니다.

출력값(Out Result)
항목명(국문)	항목명(영문)	항목크기	샘플데이터	항목설명
레벨	LVL	2	2	레벨
상위통계항목코드	P_CONT_CODE	8	1	부모통계항목코드
통계항목코드	CONT_CODE	8	0000000003	통계항목코드
통계항목명	CONT_NAME	200	최초작성연도	통계항목명
메타데이터	META_DATA	200	2012.6월 최초 작성(과거 시계열은 2003.1월부터 제공)	메타데이터

샘플 URL (Sample 위치에 인증키 값을 입력)
https://ecos.bok.or.kr/api/StatisticMeta/sample/xml/kr/1/10/경제심리지수
예제
<?xml version="1.0" encoding="UTF-8"?>
<StatisticMeta>
  <list_total_count number="true">53</list_total_count>
  <row>
    <LVL>2</LVL>
    <P_CONT_CODE>0000000108</P_CONT_CODE>
    <CONT_CODE>N13</CONT_CODE>
    <CONT_NAME>참고 자료</CONT_NAME>
    <META_DATA/>
  </row>
  <row>
    <LVL>3</LVL>
    <P_CONT_CODE>N13</P_CONT_CODE>
    <CONT_CODE>0000000107</CONT_CODE>
    <CONT_NAME>기타 참고 자료</CONT_NAME>
    <META_DATA/>
  </row>
  <row>
    <LVL>1</LVL>
    <P_CONT_CODE/>
    <CONT_CODE>0000000108</CONT_CODE>
    <CONT_NAME>기타</CONT_NAME>
    <META_DATA/>
  </row>
  <row>
    <LVL>1</LVL>
    <P_CONT_CODE/>
    <CONT_CODE>0000000001</CONT_CODE>
    <CONT_NAME>기본정보</CONT_NAME>
    <META_DATA/>
  </row>
  <row>
    <LVL>4</LVL>
    <P_CONT_CODE>N031</P_CONT_CODE>
    <CONT_CODE>0000000002</CONT_CODE>
    <CONT_NAME>통계명</CONT_NAME>
    <META_DATA>경제심리지수</META_DATA>
  </row>
  <row>
    <LVL>4</LVL>
    <P_CONT_CODE>N031</P_CONT_CODE>
    <CONT_CODE>0000000006</CONT_CODE>
    <CONT_NAME>조사(작성)목적 </CONT_NAME>
    <META_DATA>기업과 소비자 모두를 포함한 민간의 경제상황에 대한 심리를 종합적으로 파악하기 위하여 BSI 및 CSI 지수를 합성하여 경제심리지수(ESI : Economic Sentiment Index)를 작성</META_DATA>
  </row>
  <row>
    <LVL>4</LVL>
    <P_CONT_CODE>N123</P_CONT_CODE>
    <CONT_CODE>0000000017</CONT_CODE>
    <CONT_NAME>조사(작성)대상기간/시점 </CONT_NAME>
    <META_DATA>매월</META_DATA>
  </row>
  <row>
    <LVL>4</LVL>
    <P_CONT_CODE>N031</P_CONT_CODE>
    <CONT_CODE>0000000025</CONT_CODE>
    <CONT_NAME>계속여부</CONT_NAME>
    <META_DATA>Y</META_DATA>
  </row>
  <row>
    <LVL>3</LVL>
    <P_CONT_CODE>N01</P_CONT_CODE>
    <CONT_CODE>N011</CONT_CODE>
    <CONT_NAME>담당기관</CONT_NAME>
    <META_DATA>한국은행</META_DATA>
  </row>
  <row>
    <LVL>3</LVL>
    <P_CONT_CODE>N01</P_CONT_CODE>
    <CONT_CODE>N012</CONT_CODE>
    <CONT_NAME>담당부서</CONT_NAME>
    <META_DATA>경제통계1국 경제심리조사팀</META_DATA>
  </row>
</StatisticMeta>

