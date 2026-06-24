## 금융회사 API 상세
요청URL
http://finlife.fss.or.kr/finlifeapi/companySearch.{응답방식}
요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) companySearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/companySearch.xml?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1
예제 요청결과(XML)
<result>
<err_cd>000</err_cd>
<err_msg>정상</err_msg>
<total_count>17</total_count>
<max_page_no>4</max_page_no>
<now_page_no>1</now_page_no>
	<products>
		<product>
			<baseinfo>
<dcls_month>201511</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<dcls_chrg_man>영업기획팀 02-6950-7976</dcls_chrg_man>
<homp_url>http://www.shinhancard.co.kr</homp_url>
<cal_tel>15447000</cal_tel>
			</baseinfo>
			<options>
				<option>
<area_cd>01</area_cd>
<area_nm>서울</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>02</area_cd>
<area_nm>부산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>03</area_cd>
<area_nm>대구</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>04</area_cd>
<area_nm>인천</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>05</area_cd>
<area_nm>광주</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>06</area_cd>
<area_nm>대전</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>07</area_cd>
<area_nm>울산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>08</area_cd>
<area_nm>세종</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>09</area_cd>
<area_nm>경기</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>10</area_cd>
<area_nm>강원</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>11</area_cd>
<area_nm>충북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>12</area_cd>
<area_nm>충남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>13</area_cd>
<area_nm>전북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>14</area_cd>
<area_nm>전남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>15</area_cd>
<area_nm>경북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>16</area_cd>
<area_nm>경남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>17</area_cd>
<area_nm>제주</area_nm>
<exis_yn>Y</exis_yn>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201511</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<dcls_chrg_man>카드상품부 02-3702-4718</dcls_chrg_man>
<homp_url>http://www.standardchartered.co.kr</homp_url>
<cal_tel>15881599</cal_tel>
			</baseinfo>
			<options>
				<option>
<area_cd>01</area_cd>
<area_nm>서울</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>02</area_cd>
<area_nm>부산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>03</area_cd>
<area_nm>대구</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>04</area_cd>
<area_nm>인천</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>05</area_cd>
<area_nm>광주</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>06</area_cd>
<area_nm>대전</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>07</area_cd>
<area_nm>울산</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>08</area_cd>
<area_nm>세종</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>09</area_cd>
<area_nm>경기</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>10</area_cd>
<area_nm>강원</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>11</area_cd>
<area_nm>충북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>12</area_cd>
<area_nm>충남</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>13</area_cd>
<area_nm>전북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>14</area_cd>
<area_nm>전남</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>15</area_cd>
<area_nm>경북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>16</area_cd>
<area_nm>경남</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>17</area_cd>
<area_nm>제주</area_nm>
<exis_yn>N</exis_yn>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201511</dcls_month>
<fin_co_no>0010006</fin_co_no>
<kor_co_nm>한국씨티은행</kor_co_nm>
<dcls_chrg_man>카드포트폴리오부 02-2004-1224</dcls_chrg_man>
<homp_url>http://www.citibank.co.kr</homp_url>
<cal_tel>15660777</cal_tel>
			</baseinfo>
			<options>
				<option>
<area_cd>01</area_cd>
<area_nm>서울</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>02</area_cd>
<area_nm>부산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>03</area_cd>
<area_nm>대구</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>04</area_cd>
<area_nm>인천</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>05</area_cd>
<area_nm>광주</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>06</area_cd>
<area_nm>대전</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>07</area_cd>
<area_nm>울산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>08</area_cd>
<area_nm>세종</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>09</area_cd>
<area_nm>경기</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>10</area_cd>
<area_nm>강원</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>11</area_cd>
<area_nm>충북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>12</area_cd>
<area_nm>충남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>13</area_cd>
<area_nm>전북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>14</area_cd>
<area_nm>전남</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>15</area_cd>
<area_nm>경북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>16</area_cd>
<area_nm>경남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>17</area_cd>
<area_nm>제주</area_nm>
<exis_yn>Y</exis_yn>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201511</dcls_month>
<fin_co_no>0010013</fin_co_no>
<kor_co_nm>한국외환은행</kor_co_nm>
<dcls_chrg_man>기업공시국 02-222-3333</dcls_chrg_man>
<homp_url>http://www.kfb.or.kr</homp_url>
<cal_tel>0237055000</cal_tel>
			</baseinfo>
			<options>
				<option>
<area_cd>01</area_cd>
<area_nm>서울</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>02</area_cd>
<area_nm>부산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>03</area_cd>
<area_nm>대구</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>04</area_cd>
<area_nm>인천</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>05</area_cd>
<area_nm>광주</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>06</area_cd>
<area_nm>대전</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>07</area_cd>
<area_nm>울산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>08</area_cd>
<area_nm>세종</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>09</area_cd>
<area_nm>경기</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>10</area_cd>
<area_nm>강원</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>11</area_cd>
<area_nm>충북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>12</area_cd>
<area_nm>충남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>13</area_cd>
<area_nm>전북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>14</area_cd>
<area_nm>전남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>15</area_cd>
<area_nm>경북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>16</area_cd>
<area_nm>경남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>17</area_cd>
<area_nm>제주</area_nm>
<exis_yn>N</exis_yn>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201511</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<dcls_chrg_man>카드사업부 053-740-2915</dcls_chrg_man>
<homp_url>http://www.dgb.co.kr</homp_url>
<cal_tel>15665050</cal_tel>
			</baseinfo>
			<options>
				<option>
<area_cd>01</area_cd>
<area_nm>서울</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>02</area_cd>
<area_nm>부산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>03</area_cd>
<area_nm>대구</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>04</area_cd>
<area_nm>인천</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>05</area_cd>
<area_nm>광주</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>06</area_cd>
<area_nm>대전</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>07</area_cd>
<area_nm>울산</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>08</area_cd>
<area_nm>세종</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>09</area_cd>
<area_nm>경기</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>10</area_cd>
<area_nm>강원</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>11</area_cd>
<area_nm>충북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>12</area_cd>
<area_nm>충남</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>13</area_cd>
<area_nm>전북</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>14</area_cd>
<area_nm>전남</area_nm>
<exis_yn>N</exis_yn>
				</option>
				<option>
<area_cd>15</area_cd>
<area_nm>경북</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>16</area_cd>
<area_nm>경남</area_nm>
<exis_yn>Y</exis_yn>
				</option>
				<option>
<area_cd>17</area_cd>
<area_nm>제주</area_nm>
<exis_yn>N</exis_yn>
				</option>
			</options>
		</product>
	</products>
</result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1
예제 요청결과(JSON)
{"result":{"prdt_div":"F","total_count":"17","max_page_no":"4","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"201511","fin_co_no":"0010001","kor_co_nm":"우리은행","dcls_chrg_man":"영업기획팀 02-6950-7976","homp_url":"http://www.shinhancard.co.kr","cal_tel":"15447000"},{"dcls_month":"201511","fin_co_no":"0010002","kor_co_nm":"한국스탠다드차타드은행","dcls_chrg_man":"카드상품부 02-3702-4718","homp_url":"http://www.standardchartered.co.kr","cal_tel":"15881599"},{"dcls_month":"201511","fin_co_no":"0010006","kor_co_nm":"한국씨티은행","dcls_chrg_man":"카드포트폴리오부 02-2004-1224","homp_url":"http://www.citibank.co.kr","cal_tel":"15660777"},{"dcls_month":"201511","fin_co_no":"0010013","kor_co_nm":"한국외환은행","dcls_chrg_man":"기업공시국 02-222-3333","homp_url":"http://www.kfb.or.kr","cal_tel":"0237055000"},{"dcls_month":"201511","fin_co_no":"0010016","kor_co_nm":"대구은행","dcls_chrg_man":"카드사업부 053-740-2915","homp_url":"http://www.dgb.co.kr","cal_tel":"15665050"}],"optionList":[{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"01","area_nm":"서울","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"02","area_nm":"부산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"03","area_nm":"대구","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"04","area_nm":"인천","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"05","area_nm":"광주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"06","area_nm":"대전","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"07","area_nm":"울산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"08","area_nm":"세종","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"09","area_nm":"경기","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"10","area_nm":"강원","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"11","area_nm":"충북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"12","area_nm":"충남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"13","area_nm":"전북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"14","area_nm":"전남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"15","area_nm":"경북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"16","area_nm":"경남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010001","area_cd":"17","area_nm":"제주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"01","area_nm":"서울","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"02","area_nm":"부산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"03","area_nm":"대구","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"04","area_nm":"인천","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"05","area_nm":"광주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"06","area_nm":"대전","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"07","area_nm":"울산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"08","area_nm":"세종","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"09","area_nm":"경기","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"10","area_nm":"강원","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"11","area_nm":"충북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"12","area_nm":"충남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"13","area_nm":"전북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"14","area_nm":"전남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"15","area_nm":"경북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"16","area_nm":"경남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010002","area_cd":"17","area_nm":"제주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"01","area_nm":"서울","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"02","area_nm":"부산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"03","area_nm":"대구","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"04","area_nm":"인천","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"05","area_nm":"광주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"06","area_nm":"대전","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"07","area_nm":"울산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"08","area_nm":"세종","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"09","area_nm":"경기","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"10","area_nm":"강원","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"11","area_nm":"충북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"12","area_nm":"충남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"13","area_nm":"전북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"14","area_nm":"전남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"15","area_nm":"경북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"16","area_nm":"경남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010006","area_cd":"17","area_nm":"제주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"01","area_nm":"서울","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"02","area_nm":"부산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"03","area_nm":"대구","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"04","area_nm":"인천","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"05","area_nm":"광주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"06","area_nm":"대전","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"07","area_nm":"울산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"08","area_nm":"세종","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"09","area_nm":"경기","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"10","area_nm":"강원","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"11","area_nm":"충북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"12","area_nm":"충남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"13","area_nm":"전북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"14","area_nm":"전남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"15","area_nm":"경북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"16","area_nm":"경남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010013","area_cd":"17","area_nm":"제주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"01","area_nm":"서울","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"02","area_nm":"부산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"03","area_nm":"대구","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"04","area_nm":"인천","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"05","area_nm":"광주","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"06","area_nm":"대전","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"07","area_nm":"울산","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"08","area_nm":"세종","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"09","area_nm":"경기","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"10","area_nm":"강원","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"11","area_nm":"충북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"12","area_nm":"충남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"13","area_nm":"전북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"14","area_nm":"전남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"15","area_nm":"경북","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"16","area_nm":"경남","exis_yn":"N"},{"dcls_month":"201511","fin_co_no":"0010016","area_cd":"17","area_nm":"제주","exis_yn":"N"}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사코드
kor_co_nm	금융회사 명
dcls_chrg_man	공시담당자
homp_url	홈페이지주소
cal_tel	콜센터전화번호
options	옵션목록
options	옵션
area_cd	지역구분
area_nm	지역이름
exis_yn	점포소재여부
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
No	응답코드	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

## 정기예금 API 상세
요청URL
http://finlife.fss.or.kr/finlife/fdrmDpstApi/list.{응답방식}
요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) depositProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1
예제 요청결과(XML)
<result>
		<err_cd>000</err_cd>
		<err_msg>정상</err_msg>
		<total_count>79</total_count>
		<max_page_no>1</max_page_no>
		<now_page_no>1</now_page_no>
			<products>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>WR0001A</fin_prdt_cd>
		<fin_prdt_nm>우리웰리치 주거래예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후
		- 1개월이내 : 만기시점약정이율×50%
		- 1개월초과 6개월이내: 만기시점약정이율×30%
		- 6개월초과 : 만기시점약정이율×20%

		※ 만기시점 약정이율 : 일반정기예금 금리</mtrt_int>
		<spcl_cnd>다음 중 하나 충족한 입금건에 대해  최고 연0.2%p
		1. 순신규고객
		2. 가계대출이용고객
		3. 입금일 전월 주거래우대조건 2가지이상
		4. 건별3천만원이상
		5. 건별 만기 자동재예치</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인</join_member>
		<etc_note>-추가입금은 신규가입 시 선택한 예치기간을 각 입금건별 입금일로부터 적용
		-재예치는 입금건별 최초 입금일로부터 최장 10년간 가능</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201028</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>WR0001B</fin_prdt_cd>
		<fin_prdt_nm>우리웰리치100예금(회전형)</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후
		- 1개월이내 : 만기시점약정이율×50%
		- 1개월초과 6개월이내: 만기시점약정이율×30%
		- 6개월초과 : 만기시점약정이율×20%

		※ 만기시점 약정이율 : 일반정기예금 금리</mtrt_int>
		<spcl_cnd>최고 연 0.2%p우대이율
		1. 연금이체실적보유 : 연0.1%p
		2. 신용/체크카드 보유 : 연0.1%p
		3. 당일 적금/예금/펀드 해지 후 신규시  : 연0.1%p
		4. 인터넷/스마트뱅킹으로 신규시 : 연 0.1%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인</join_member>
		<etc_note>-가입자가 환갑, 칠순, 팔순, 구순, 백순 사유로 중도해지 시 기본이자율을 중도해지 이자율 적용
		※ 주민등록번호 기준으로 사유발생 전후3개월간 혜택제공</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201028</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>WR0001C</fin_prdt_cd>
		<fin_prdt_nm>Red Monkey
		스마트 정기예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>만기 후
		- 1개월이내 : 만기시점약정이율×50%
		- 1개월초과 6개월이내: 만기시점약정이율×30%
		- 6개월초과 : 만기시점약정이율×20%

		※ 만기시점 약정이율 : 일반정기예금 금리</mtrt_int>
		<spcl_cnd>최고 연0.3%p
		1. 위비앱/위비모바일통장 연0.1%p
		2. 최고 연0.2%p
		 - 스마트간편신규 연0.1%p, 펀드/적금/대출보유 연0.1%p, 예적금만기재예치 연0.1%p
		3. 친구번호등록 연0.2%p
		4. 첫거래 연0.2%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit>20000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201028</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>WR0001D</fin_prdt_cd>
		<fin_prdt_nm>우리로모아
		정기예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>만기 후
		- 1개월이내 : 만기시점약정이율×50%
		- 1개월초과 6개월이내: 만기시점약정이율×30%
		- 6개월초과 : 만기시점약정이율×20%

		※ 만기시점 약정이율 : 일반정기예금 금리</mtrt_int>
		<spcl_cnd>최고 연 0.2%p 적용
		1. 우리닷컴통장에서 신규된 경우 : 연 0.2%p
		2. 모바일뱅킹에 가입한 고객 : 연 0.2%p
		3. WIN-CMS에 가입한 고객  : 연 0.2%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>인터넷뱅킹가입고객</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201028</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.95</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>WR0001E</fin_prdt_cd>
		<fin_prdt_nm>iTouch
		우리예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>만기 후
		- 1개월이내 : 만기시점약정이율×50%
		- 1개월초과 6개월이내: 만기시점약정이율×30%
		- 6개월초과 : 만기시점약정이율×20%

		※ 만기시점 약정이율 : 일반정기예금 금리</mtrt_int>
		<spcl_cnd>최고 연 0.2%p
		1. 최종 모집잔액에 따라 : 연 0.1%
		2. iTouch우리통장 연결가입 : 연 0.1%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201028</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010002</fin_co_no>
		<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
		<fin_prdt_cd>00320301</fin_prdt_cd>
		<fin_prdt_nm>홈앤세이브예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기 후 1개월: 0.7%
		만기 후 1개월 초과 1년 이내: 0.3%
		만기 후 1년 초과: 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200944</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010002</fin_co_no>
		<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
		<fin_prdt_cd>00320342</fin_prdt_cd>
		<fin_prdt_nm>e-그린세이브예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰,모집인</join_way>
		<mtrt_int>만기 후 1개월: 0.7%
		만기 후 1개월 초과 1년 이내: 0.3%
		만기 후 1년 초과: 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200944</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010002</fin_co_no>
		<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
		<fin_prdt_cd>00320396</fin_prdt_cd>
		<fin_prdt_nm>퍼스트정기예금</fin_prdt_nm>
		<join_way>영업점,모집인,전화(텔레뱅킹)</join_way>
		<mtrt_int>만기 후 1개월: 0.7%
		만기 후 1개월 초과 1년 이내: 0.3%
		만기 후 1년 초과: 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200944</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010006</fin_co_no>
		<kor_co_nm>한국씨티은행</kor_co_nm>
		<fin_prdt_cd>3127</fin_prdt_cd>
		<fin_prdt_nm>프리스타일예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 고시한 1개월 정기예금 이율
		만기 후 1개월 초과 : 연 1.0%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입금액은 1백만원 이상 가입 가능
		2. 가입기간은 1개월 이상 3년 이내 일단위 가입 가능</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201001</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010006</fin_co_no>
		<kor_co_nm>한국씨티은행</kor_co_nm>
		<fin_prdt_cd>3129</fin_prdt_cd>
		<fin_prdt_nm>자유회전예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 고시한 1개월 정기예금 이율
		만기 후 1개월 초과 : 연 1.0%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입금액은 1백만원 이상 가입 가능
		2. 가입기간은 1개월 이상 30년 이내 일단위 가입 가능</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201001</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010016</fin_co_no>
		<kor_co_nm>대구은행</kor_co_nm>
		<fin_prdt_cd>10511008000845001</fin_prdt_cd>
		<fin_prdt_nm>내손안에 예금</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
		만기 후 3개월 미만 경과: 약정이자율 x 25%
		만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
		<spcl_cnd>* 최고우대금리 : 0.2%
		 - 최초가입 우대 : 0.1%
		 - 공과금 실적 우대 : 0.1%

		※ 단위는 연%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 1계좌당 가입최저한도 : 100만원 (최대 5천만원 이내)
		2. 스마트폰 가입 전용상품
		3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201120</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.42</intr_rate>
		<intr_rate2>1.62</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.46</intr_rate>
		<intr_rate2>1.66</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.48</intr_rate>
		<intr_rate2>1.68</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010016</fin_co_no>
		<kor_co_nm>대구은행</kor_co_nm>
		<fin_prdt_cd>10511008000958002</fin_prdt_cd>
		<fin_prdt_nm>최강삼성V9 예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
		만기 후 3개월 미만 경과: 약정이자율 x 25%
		만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
		<spcl_cnd>* 최고우대금리 : 0.25%
		 - 신규시 주택청약상품 보유 우대 : 0.1%
		 - 신규시 공과금 2건이상 보유 우대 : 0.05%
		 - 삼성라이온즈 정규시즌 우승 우대 : 0.05%
		 - 삼성라이온즈 한국시리즈 우승 우대 : 0.1%
		 - 만기시 공과금 2건이상 보유 우대 : 0.05%

		※ 단위는 연%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 1계좌당 가입최저한도 : 100만원  (최대 5천만원 이내)
		2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201120</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.16</intr_rate>
		<intr_rate2>1.41</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010016</fin_co_no>
		<kor_co_nm>대구은행</kor_co_nm>
		<fin_prdt_cd>10511008000996000</fin_prdt_cd>
		<fin_prdt_nm>DGB주거래우대예금(첫만남고객형)</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
		만기 후 3개월 미만 경과: 약정이자율 x 25%
		만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
		<spcl_cnd>* 최고우대금리 : 0.2%
		 - 최초가입 우대 : 0.1%
		 - 신용(체크)카드 발급 우대 : 0.05%
		 - 인터넷,폰,스마트뱅킹 가입우대 : 0.05%

		※ 단위는 연%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 1계좌당 가입최저한도 : 300만원
		2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201120</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.12</intr_rate>
		<intr_rate2>1.32</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.16</intr_rate>
		<intr_rate2>1.36</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.18</intr_rate>
		<intr_rate2>1.38</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010016</fin_co_no>
		<kor_co_nm>대구은행</kor_co_nm>
		<fin_prdt_cd>10511008001109001</fin_prdt_cd>
		<fin_prdt_nm>ISA플러스 예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
		만기 후 3개월 미만 경과: 약정이자율 x 25%
		만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
		<spcl_cnd>* 최고우대금리 : 0.4%
		 - 신규시 ISA계좌 30만원 이상보유 우대 : 0.1%
		 - 신규시 공과금 3건이상 보유 우대 : 0.1%
		 - 만기시 ISA계좌 30만원 이상 보유 우대 : 0.1%
		 - 만기시 공과금 3건이상 보유 우대 : 0.1%

		※ 단위는 연%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 1계좌당 가입최저한도 : 100만원 (최대 5천만원 이내)
		2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201120</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.16</intr_rate>
		<intr_rate2>1.56</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010016</fin_co_no>
		<kor_co_nm>대구은행</kor_co_nm>
		<fin_prdt_cd>10511014000001001</fin_prdt_cd>
		<fin_prdt_nm>e-U(이유)예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
		만기 후 3개월 미만 경과: 약정이자율 x 25%
		만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
		<spcl_cnd>* 최고우대금리 : 0.5%
		 - 최초가입 우대 : 0.1%
		 - 재예치 우대 : 0.1%
		 - 거래실적 우대 : 0.2%
		 - 주택청약상품 보유 우대 : 0.1%

		※ 단위는 연%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 1계좌당 가입최저한도 : 100만원 (최대 1억원 이내)
		2. 인터넷뱅킹 및 스마트폰 가입 전용상품
		3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201120</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.12</intr_rate>
		<intr_rate2>1.62</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.16</intr_rate>
		<intr_rate2>1.66</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.18</intr_rate>
		<intr_rate2>1.68</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010017</fin_co_no>
		<kor_co_nm>부산은행</kor_co_nm>
		<fin_prdt_cd>01030500130002</fin_prdt_cd>
		<fin_prdt_nm>메리트정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,
		- 만기후1년초과:가입기간별 일반정기예금이율 x 20%</mtrt_int>
		<spcl_cnd>- 1년제, 1천만원이상: 1.10%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>제한없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201336</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.7</intr_rate>
		<intr_rate2>.7</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>.9</intr_rate>
		<intr_rate2>.9</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010017</fin_co_no>
		<kor_co_nm>부산은행</kor_co_nm>
		<fin_prdt_cd>01030500290002</fin_prdt_cd>
		<fin_prdt_nm>e-푸른바다정기예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,
		- 만기후1년초과:가입기간별 일반정기예금이율 x 20%</mtrt_int>
		<spcl_cnd>우대조건 없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입채널: 인터넷,스마트뱅킹,고객센터</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201336</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010017</fin_co_no>
		<kor_co_nm>부산은행</kor_co_nm>
		<fin_prdt_cd>01030500400002</fin_prdt_cd>
		<fin_prdt_nm>BNKe스마트정기예금</fin_prdt_nm>
		<join_way>스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,
		- 만기후1년초과:가입기간별 일반정기예금이율 x 20%</mtrt_int>
		<spcl_cnd>우대조건 없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 개인및 개인사업자 가입가능
		2. 가입한도:3천만원이하
		3. 가입채널: 스마트,고객센터</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201336</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010017</fin_co_no>
		<kor_co_nm>부산은행</kor_co_nm>
		<fin_prdt_cd>01030500460002</fin_prdt_cd>
		<fin_prdt_nm>굿-초이스</fin_prdt_nm>
		<join_way>영업점,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,
		- 만기후1년초과:가입기간별 일반정기예금이율 x 20%</mtrt_int>
		<spcl_cnd>-비대면 여수신 신규우대: 0.10%
		-그룹우대: 0.10%
		-홍보우대: 0.10%
		-교차판매 우대: 0.3%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 개인및 개인사업자 가입가능
		2. 가입채널: 인터넷,스마트,고객센터</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201336</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.8</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010017</fin_co_no>
		<kor_co_nm>부산은행</kor_co_nm>
		<fin_prdt_cd>01030500490002</fin_prdt_cd>
		<fin_prdt_nm>MY SUM</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,
		- 만기후1년초과:가입기간별 일반정기예금이율 x 20%</mtrt_int>
		<spcl_cnd>-10백만원 이상 신규시 : 0.10%
		-썸뱅크간편송금 20회이상: 0.10%
		-SUM모바일통장 기중평잔 30만원 이상: 0.10%
		-SUM모바일통장 결제계좌로 롯데카드 결제실적 300만원 이상 : 0.10%
		-썸뱅크를 통한 외화 환전실적 1회이상: 0.10%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 개인및 개인사업자 가입가능
		2. 가입한도: 1억원이하
		3. 가입채널: 당행 썸뱅크(모바일) 통해 가입가능</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201336</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.7</intr_rate>
		<intr_rate2>2.2</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010017</fin_co_no>
		<kor_co_nm>부산은행</kor_co_nm>
		<fin_prdt_cd>01030500500002</fin_prdt_cd>
		<fin_prdt_nm>BNK어울림</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,
		- 만기후1년초과:가입기간별 일반정기예금이율 x 20%</mtrt_int>
		<spcl_cnd>-예적금 동시보유 : 0.10%
		-ISA가입: 0.05%
		-신규 및 장기고객우대: 0.10%
		-자동이체실적 등 : 0.10%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 개인및 개인사업자 가입가능
		2. 가입한도: 1억원이하</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201336</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.55</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.65</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010019</fin_co_no>
		<kor_co_nm>광주은행</kor_co_nm>
		<fin_prdt_cd>TD11300021000</fin_prdt_cd>
		<fin_prdt_nm>플러스다모아예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 최초 가입
		기간별 일반정기예금 고시금리의 1/2
		만기 후 1개월 초과 : 0.10%</mtrt_int>
		<spcl_cnd>1. 1천만원 이상 가입시 최대 0.3%우대
		2. 최고 0.2% 우대(개인)
		- 적립식예금 6회 이상 납입 : 0.1%
		- 급여통장 보유 : 0.1%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 최소가입금액 : 100만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261219</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.91</intr_rate>
		<intr_rate2>1.41</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.01</intr_rate>
		<intr_rate2>1.51</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.03</intr_rate>
		<intr_rate2>1.53</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>.87</intr_rate>
		<intr_rate2>1.37</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010019</fin_co_no>
		<kor_co_nm>광주은행</kor_co_nm>
		<fin_prdt_cd>TD11300025000</fin_prdt_cd>
		<fin_prdt_nm>아파트사랑정기예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 최초 가입
		기간별 일반정기예금 고시금리의 1/2
		만기 후 1개월 초과 : 0.10%</mtrt_int>
		<spcl_cnd>1. 1천만원 이상 가입시 0.3%우대
		2. 조건 충족시 최대 0.25% 우대(개인)
		- 아파트관리비 6회 이상 자동이체: 0.1%
		- 자녀용돈통장개설: 0.05%
		- 정액적립식 6회 이상 납입: 최대 0.1%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 최소가입금액 : 100만원 이상
		2. 영업점 방문 가입만 가능
		3. 가입기간 : 1년 이상 3년 이내</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261219</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.01</intr_rate>
		<intr_rate2>1.51</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.03</intr_rate>
		<intr_rate2>1.53</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>.87</intr_rate>
		<intr_rate2>1.37</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010019</fin_co_no>
		<kor_co_nm>광주은행</kor_co_nm>
		<fin_prdt_cd>TD11300027000</fin_prdt_cd>
		<fin_prdt_nm>미즈월복리정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 최초 가입
		기간별 일반정기예금 고시금리의 1/2
		만기 후 1개월 초과 : 0.10%</mtrt_int>
		<spcl_cnd>*최대 0.2%우대
		1. 요구불평잔 300만원 이상: 최대 0.2%
		2. 신용카드 결제실적 월 300만원 이상 : 최대 0.1%
		3, 가입자의 자녀출산 또는 결혼시 : 0.1%</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>만 18세 이상 여성고객</join_member>
		<etc_note>1. 1인당 가입한도 : 5천만원
		2. 최소가입금액 : 500만원 이상
		3. 가입기간 : 1년 이상 3년 이내</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261219</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.21</intr_rate>
		<intr_rate2>1.41</intr_rate2>
						</option>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.23</intr_rate>
		<intr_rate2>1.43</intr_rate2>
						</option>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.07</intr_rate>
		<intr_rate2>1.27</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010019</fin_co_no>
		<kor_co_nm>광주은행</kor_co_nm>
		<fin_prdt_cd>TD11300028000</fin_prdt_cd>
		<fin_prdt_nm>스마트모아Dream정기예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 최초 가입
		기간별 일반정기예금 고시금리의 1/2
		만기 후 1개월 초과 : 0.10%</mtrt_int>
		<spcl_cnd>1. 1천만원 이상 가입시 0.3%우대
		2. 스마트뱅킹 신규시 0.2% 우대 : 고객당 2천만원까지</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인고객</join_member>
		<etc_note>1. 인터넷/스마트폰뱅킹 가입 전용상품
		2. 최소가입금액 : 100만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261219</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.01</intr_rate>
		<intr_rate2>1.51</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.11</intr_rate>
		<intr_rate2>1.61</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.13</intr_rate>
		<intr_rate2>1.63</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>.97</intr_rate>
		<intr_rate2>1.47</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010019</fin_co_no>
		<kor_co_nm>광주은행</kor_co_nm>
		<fin_prdt_cd>TD11300029000</fin_prdt_cd>
		<fin_prdt_nm>평생대박정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 최초 가입
		기간별 일반정기예금 고시금리의 1/2
		만기 후 1개월 초과 : 0.10%</mtrt_int>
		<spcl_cnd>1. 500만원 이상 가입시 0.3%우대
		2. 조건충족시, 최대 0.2%우대
		- 4대연금수급실적 : 0.1%
		- 급여이체실적: 0.1%
		- 요구불 평잔 500만원 이상 : 최대 0.1%</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>만 50세 이상 고객</join_member>
		<etc_note>1.최소가입금액 : 500만원 이상
		2.가입기간 : 1년 이상 3년 이내</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261219</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.01</intr_rate>
		<intr_rate2>1.51</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.03</intr_rate>
		<intr_rate2>1.53</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>.87</intr_rate>
		<intr_rate2>1.37</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010019</fin_co_no>
		<kor_co_nm>광주은행</kor_co_nm>
		<fin_prdt_cd>TD11300032000</fin_prdt_cd>
		<fin_prdt_nm>쏠쏠한마이쿨예금</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>만기 후 1개월 이내 : 만기일 당시 최초 가입
		기간별 일반정기예금 고시금리의 1/2
		만기 후 1개월 초과 : 0.10%</mtrt_int>
		<spcl_cnd>해당없음</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>가입일 기준 최근 1년간 당행 거치식예금, 적</join_member>
		<etc_note>1.최소가입금액 : 100만원 이상
		2.가입기간 : 1년</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261219</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.75</intr_rate>
		<intr_rate2>1.75</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010020</fin_co_no>
		<kor_co_nm>제주은행</kor_co_nm>
		<fin_prdt_cd>200000301</fin_prdt_cd>
		<fin_prdt_nm>제주Dream정기예금(개인/만기지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>- 만기후 1개월 이내 : (일반)정기예금 기본이자율의 50%
		- 만기후 1개월 초과 3개월 이내 : (일반)정기예금 기본이자율의 30%
		- 만기후 3개월 초과 : 0.25%</mtrt_int>
		<spcl_cnd>최고 연 0.1%p(항목별 0.1%p)
		①급여이체
		②적립식예금 잔액 10만원 이상 보유
		③탑스, 주거래 고객
		④결제계좌(가맹점) 전월 입금액 10만원 이상
		⑤비과세종합저축 대상 고객
		⑥다자녀(3인이상 자녀)가정</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 : 1백만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200947</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010020</fin_co_no>
		<kor_co_nm>제주은행</kor_co_nm>
		<fin_prdt_cd>200000302</fin_prdt_cd>
		<fin_prdt_nm>사이버우대정기예금(개인/만기지급식)</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>- 만기후 1개월 이내 : (일반)정기예금 기본이자율의 50%
		- 만기후 1개월 초과 3개월 이내 : (일반)정기예금 기본이자율의 30%
		- 만기후 3개월 초과 : 0.25%</mtrt_int>
		<spcl_cnd>최고 연 0.1%p(중복불가)
		①탐나는 J 직장인 통장 가입 고객이 기본우대 요건 충족 후 이 상품 가입시 : 0.1%p
		②탐나는 J 주거래 통장 가입 고객이 기본우대 요건 충족 후 이 상품 가입시 : 0.1%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 : 30만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200947</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.58</intr_rate>
		<intr_rate2>1.68</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.6</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.63</intr_rate>
		<intr_rate2>1.73</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0001-0000</fin_prdt_cd>
		<fin_prdt_nm>정기예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.7</intr_rate>
		<intr_rate2>.7</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.05</intr_rate>
		<intr_rate2>1.05</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.2</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0008-0000</fin_prdt_cd>
		<fin_prdt_nm>맞춤형자유만기정기예금(월이자지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 5백만원이상
		(비과세종합저축은 1백만원이상)</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.05</intr_rate>
		<intr_rate2>1.05</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0009-0000</fin_prdt_cd>
		<fin_prdt_nm>맞춤형자유만기정기예금(만기일시지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 5백만원이상
		(비과세종합저축은 1백만원이상)</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0016-0000</fin_prdt_cd>
		<fin_prdt_nm>전북아이나라예금
		(월이자지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>전라북도에 주소지를 둔 만 3세이하 개인</join_member>
		<etc_note>가입금액 10만원이상 15백만원이하</etc_note>
		<max_limit>15000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0017-0000</fin_prdt_cd>
		<fin_prdt_nm>전북아이나라예금
		(만기일시지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>전라북도에 주소지를 둔 만 3세이하 개인</join_member>
		<etc_note>가입금액 10만원이상 15백만원이하</etc_note>
		<max_limit>15000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.55</intr_rate>
		<intr_rate2>1.55</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0029-0000</fin_prdt_cd>
		<fin_prdt_nm>실버보금자리예금
		(월이자지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>만60세이상 실명의 개인으로
		전라북도 소재 영업점 : 주민등록상 주소지가 전라북도인 경우
		전라북도 소재 이외 영업점 : 주민등록상 주소지, 원적지, 본적지가 전라북도인 경우</join_member>
		<etc_note>가입금액 1백만원이상,
		1인당 3억원이내</etc_note>
		<max_limit>300000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0030-0000</fin_prdt_cd>
		<fin_prdt_nm>실버보금자리예금
		(만기일시지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>만60세이상 실명의 개인으로
		전라북도 소재 영업점 : 주민등록상 주소지가 전라북도인 경우
		전라북도 소재 이외 영업점 : 주민등록상 주소지, 원적지, 본적지가 전라북도인 경우</join_member>
		<etc_note>가입금액 1백만원이상, 1인당 3억원이내</etc_note>
		<max_limit>300000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0037-0000</fin_prdt_cd>
		<fin_prdt_nm>시장금리부정기예금
		(월이자지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 3백만원이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.05</intr_rate>
		<intr_rate2>1.05</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0038-0000</fin_prdt_cd>
		<fin_prdt_nm>시장금리부정기예금
		(만기일시지급식)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 3백만원이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0041-0000</fin_prdt_cd>
		<fin_prdt_nm>인터넷정기예금
		(월이자지급식)</fin_prdt_nm>
		<join_way>인터넷</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 3백만원이상 1억원이하,
		인터넷뱅킹 가입상품</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0042-0000</fin_prdt_cd>
		<fin_prdt_nm>인터넷정기예금
		(만기일시지급식)</fin_prdt_nm>
		<join_way>인터넷</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 3백만원이상 1억원이하,
		인터넷뱅킹 가입상품</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.55</intr_rate>
		<intr_rate2>1.55</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0042-0021</fin_prdt_cd>
		<fin_prdt_nm>스마트정기예금
		(만기일시지급식)</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>1.가입시JB급여플러스통장보유 연0.1%, 2.최근1개월이내신용카드사용고객 연0.1%,3.예금가입기간별우대금리:2년이상연0,1%,3년이상연0.2%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>가입금액 3백만원이상 5천만원이하,
		스마트폰뱅킹 가입상품</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.34</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.44</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.54</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.6</intr_rate>
		<intr_rate2>1.64</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010022</fin_co_no>
		<kor_co_nm>전북은행</kor_co_nm>
		<fin_prdt_cd>10-01-20-024-0046-0000</fin_prdt_cd>
		<fin_prdt_nm>JB 다이렉트예금통장
		(만기일시지급식)</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2
		만기후 1개월 초과 : 연 0.1%</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인(임의단체 제외)</join_member>
		<etc_note>가입금액 1계좌당 1백만원이상,
		1인당  총 3억원 이하,
		인터넷/스마트폰뱅킹 가입상품</etc_note>
		<max_limit>300000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201044</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.7</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010024</fin_co_no>
		<kor_co_nm>경남은행</kor_co_nm>
		<fin_prdt_cd>21000087</fin_prdt_cd>
		<fin_prdt_nm>마니마니정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%
		만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%</mtrt_int>
		<spcl_cnd>우대조건에 따른 우대금리 없음
		계약기간은 최소 1개월 이상부터 가능</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>거래대상자는 제한을 두지 아니한다. 다만, 국가 및 지방자치단체는 이 예금을 거래할 수 없다.</join_member>
		<etc_note>1. 계약기간은 1개월 이상 2년까지로 하되 예금주의 편의에 따라 임의로 정할 수 있다.
		2. 가입금액 최소 5백만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201041</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.05</intr_rate>
		<intr_rate2>1.05</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010024</fin_co_no>
		<kor_co_nm>경남은행</kor_co_nm>
		<fin_prdt_cd>21000093</fin_prdt_cd>
		<fin_prdt_nm>스마트
		정기예금</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%
		만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%</mtrt_int>
		<spcl_cnd>▶추천이율: 최대0.15%
		가입시마다 추천번호제공하며 해당추천번호를 타인이 입력하는 경우</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>스마트폰뱅킹을 가입한 개인 및 개인사업자</join_member>
		<etc_note>1. 이 예금은 스마트폰뱅킹을 통해서만 가입할 수 있으며, 해지는 스마트폰뱅킹, 영업점 창구에서 할 수 있다.
		2. 계약기간은 1개월 이상 12개월 이내 월단위로 한다.
		3. 가입금액 최소 1백만원 이상~최대 5천만원 이하</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201041</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010024</fin_co_no>
		<kor_co_nm>경남은행</kor_co_nm>
		<fin_prdt_cd>21000101</fin_prdt_cd>
		<fin_prdt_nm>e-Money
		정기예금</fin_prdt_nm>
		<join_way>인터넷,전화(텔레뱅킹)</join_way>
		<mtrt_int>만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%
		만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%</mtrt_int>
		<spcl_cnd>▶계약기간 만기전에 만기해지 포함 총 3회까지 분할인출이 가능하다.</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인 및 개인사업자</join_member>
		<etc_note>1. 이 예금은 인터넷뱅킹, 고객센터를 통하여 가입하고, 해지는 인터넷뱅킹, 고객센터, 영업점 창구에서 할 수 있다.
		2. 계약기간은 1개월 이상 12개월 이내 월단위로 한다.
		3. 가입금액 최소 1백만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201041</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010024</fin_co_no>
		<kor_co_nm>경남은행</kor_co_nm>
		<fin_prdt_cd>21001049</fin_prdt_cd>
		<fin_prdt_nm>다모아
		정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%
		만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%</mtrt_int>
		<spcl_cnd>①(핵심예금 평균잔액 증가액X1.6%)/이 예금의 신규가입 금액
		②(신용카드 결제실적 증가액X0.7%)/이 예금의 신규가입 금액
		▶①및②의 금리를 합하여 최고1.0%우대이율 제공</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>거래대상자는 제한을 두지 아니한다. 다만, 국가 및 지방자치단체는 이 예금을 거래할 수 없다.</join_member>
		<etc_note>1. 계약기간은 12개월로 한다.
		2. 최저가입금액은 5백만원 이상으로 하며, 이 예금은 1인 1계좌에 한하여 가입 가능하다.</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201041</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>2.25</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010024</fin_co_no>
		<kor_co_nm>경남은행</kor_co_nm>
		<fin_prdt_cd>21001057</fin_prdt_cd>
		<fin_prdt_nm>다이아몬드
		정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%
		만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%</mtrt_int>
		<spcl_cnd>①비대면채널가입시0.05%
		②여성우대이율 0.10%
		 - 가입기간중 결혼, 임신, 출산, 자녀결혼, 손자출생시 우대금리를 지급하며, 해당 예금의 만기해지전까지 영업점 창구에 증빙서류를 제출하는 경우
		③소개이율 0.05%
		▶①~③의 최고 우대금리 합계는 0.10%</spcl_cnd>
		<join_deny>3</join_deny>
		<join_member>실명의 개인인 여성</join_member>
		<etc_note>1. 계약기간은 6개월 이상 24개월 이내로 한다.
		2. 가입금액 최소 3백만원 이상~최대 1억원 이하</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201041</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.05</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010024</fin_co_no>
		<kor_co_nm>경남은행</kor_co_nm>
		<fin_prdt_cd>21001105</fin_prdt_cd>
		<fin_prdt_nm>BNK사랑방
		정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%
		만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%</mtrt_int>
		<spcl_cnd>①가입일 기준 과거 1년간 당행 정기예금 신규이력이 없는 고객 0.10%
		②아래 항목 중 한가지 이상 충족시 0.10%
		- 입출금이자유로운예금 평잔 2백만원 이상, 신용카드 결제금액이 5백만원 이상
		③주거래우대금리 0.10%
		④비대면채널가입 우대이율 0.05%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인 및 개인사업자</join_member>
		<etc_note>1. 이 예금은 1인 1계좌만 가입 가능하고, 계약기간은 12개월로 한다.
		2. 가입금액 최소 1백만원 이상~최대 5천만원 이하</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201041</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010026</fin_co_no>
		<kor_co_nm>중소기업은행</kor_co_nm>
		<fin_prdt_cd>01211310073</fin_prdt_cd>
		<fin_prdt_nm>新서민섬김통장 실세금리정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기일 당시 실세금리정기예금의 만기후금리 적용
		- 1개월 이내: 만기일 당시 약정금리×50%
		- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
		- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
		<spcl_cnd>최고 연 0.3%p
		1. 신규고객 우대금리 : 연 0.1%p
		2. 거래심화 우대금리 : 연 0.2%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인(개인사업자 제외)</join_member>
		<etc_note>1인당 통합한도(적립식 계약원금+거치식 가입금액) 3천만원</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201030</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.55</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010026</fin_co_no>
		<kor_co_nm>중소기업은행</kor_co_nm>
		<fin_prdt_cd>01211310108</fin_prdt_cd>
		<fin_prdt_nm>IBK흔들어예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기일 당시 실세금리정기예금의 만기후금리 적용
		- 1개월 이내: 만기일 당시 약정금리×50%
		- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
		- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
		<spcl_cnd>최고 연0.4%p
		1. I-ONE뱅크 또는 흔들어예금 앱으로 가입하고 별도로 정한상품 1개이상 신규가입(연0.2%p)
		2. 흔들어예금 앱으로 만보기미션 달성(최고 연0.2%p)</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인(개인사업자 제외)</join_member>
		<etc_note>1인당 가입한도 1억원</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201030</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.65</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010026</fin_co_no>
		<kor_co_nm>중소기업은행</kor_co_nm>
		<fin_prdt_cd>01211310121</fin_prdt_cd>
		<fin_prdt_nm>IBK평생한가족통장 실세금리정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기일 당시 실세금리정기예금의 만기후금리 적용
		- 1개월 이내: 만기일 당시 약정금리×50%
		- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
		- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
		<spcl_cnd>최고 연 0.2%p
		1. 고객별 우대금리: 연 0.05%p
		2. 주거래 우대금리: 연 0.15%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인(개인사업자 제외)</join_member>
		<etc_note>1인당 통합한도 1억원</etc_note>
		<max_limit>100000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201030</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.55</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010028</fin_co_no>
		<kor_co_nm>수협은행</kor_co_nm>
		<fin_prdt_cd>10120102800011</fin_prdt_cd>
		<fin_prdt_nm>사랑해정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>* 만기후 1년 이내
		만기당시 정기예금(월이자지급식) 계약기간별 약정이율 1/2
		* 만기후 1년 초과
		만기당시 보통예금 이율</mtrt_int>
		<spcl_cnd>우대조건없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201529</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.9</intr_rate>
		<intr_rate2>.9</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010028</fin_co_no>
		<kor_co_nm>수협은행</kor_co_nm>
		<fin_prdt_cd>10120104400021</fin_prdt_cd>
		<fin_prdt_nm>사랑해나누리예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>* 만기후 1년 이내
		만기당시 정기예금(월이자지급식) 계약기간별 약정이율 1/2
		* 만기후 1년 초과
		만기당시 보통예금 이율</mtrt_int>
		<spcl_cnd>0.1%
		기부금납부자
		헌혈증서 보유자
		자원봉사증보유자
		어업종사자
		어업인</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201529</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010030</fin_co_no>
		<kor_co_nm>한국산업은행</kor_co_nm>
		<fin_prdt_cd>05100</fin_prdt_cd>
		<fin_prdt_nm>정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>지급일 현재 고시된
		이 예금의 만기후 이율</mtrt_int>
		<spcl_cnd>해당없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261020</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.85</intr_rate>
		<intr_rate2>.85</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>.9</intr_rate>
		<intr_rate2>.9</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>.99</intr_rate>
		<intr_rate2>.99</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.08</intr_rate>
		<intr_rate2>1.08</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010030</fin_co_no>
		<kor_co_nm>한국산업은행</kor_co_nm>
		<fin_prdt_cd>05702</fin_prdt_cd>
		<fin_prdt_nm>KDBdream 정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>* 만기후 1년 이내 :
		 만기일 현재 고시된 일반 정기예금 해당기간 기본이자유의 1/2
		* 만기후 1년 초과 :
		만기일 현재 고시된 보통예금 이자율</mtrt_int>
		<spcl_cnd>KDBdream Account 가입고객이 이 예금을 가입하는 경우, 0.10%P 가산</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인(개인사업자 및 임의단체 포함)</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200933</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.45</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010030</fin_co_no>
		<kor_co_nm>한국산업은행</kor_co_nm>
		<fin_prdt_cd>05705</fin_prdt_cd>
		<fin_prdt_nm>KDB Hi 정기예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>* 만기후 1년 이내 :
		 만기일 현재 고시된 일반 정기예금 해당기간 기본이자유의 1/2
		* 만기후 1년 초과 :
		만기일 현재 고시된 보통예금 이자율</mtrt_int>
		<spcl_cnd>해당없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>KDB Hi 입출금통장에 가입한 개인(개인사업자 및 임의단체 제외)
		단, 국민인 거주자에 한함</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160926</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609261020</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.6</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010927</fin_co_no>
		<kor_co_nm>국민은행</kor_co_nm>
		<fin_prdt_cd>010300100072</fin_prdt_cd>
		<fin_prdt_nm>국민수퍼고정금리형-만기일시지급식</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>- 만기후 1개월이내 : 약정이율 X 50%
		- 만기후 1개월초과~3개월이내 : 약정이율 X 30%
		- 만기후 3개월초과 : 0.2%

		※ 단위 : 연%
		   약정이율 : 고객이 만기시점에 받기로 한 이율</mtrt_int>
		<spcl_cnd>※ 우대이율 최고 : 연0.4%p
		1. 영업점장 우대금리 : 연0.1%p
		   (※ 비대면 신규 시에는 자동 적용)
		2. 평생고객사은 이율 : 연0.1%p
		3. 가입상품 금리우대(인터넷신규시) : 연0.3%p
		   (※ 2번, 3번 우대금리는 중복불가)</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201032</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>.9</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010927</fin_co_no>
		<kor_co_nm>국민은행</kor_co_nm>
		<fin_prdt_cd>010300100209</fin_prdt_cd>
		<fin_prdt_nm>e-파워정기예금</fin_prdt_nm>
		<join_way>인터넷,전화(텔레뱅킹)</join_way>
		<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
		- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
		- 만기후 3개월초과 : 0.2%

		※ 단위 : 연%</mtrt_int>
		<spcl_cnd>※ 우대이율 최고 연0.3%p
		- KB star*t통장 or KB樂Star통장
		  or KB나라사랑우대통장 가입자
		  우대이율 : 연0.3%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>인터넷 전용 상품</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201032</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010927</fin_co_no>
		<kor_co_nm>국민은행</kor_co_nm>
		<fin_prdt_cd>010300100226</fin_prdt_cd>
		<fin_prdt_nm>KB Smart★폰 예금</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
		- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
		- 만기후 3개월초과 : 0.2%

		※ 단위 : 연%</mtrt_int>
		<spcl_cnd>※ 우대이율 최고 연0.6%p
		- 추천 우대이율 : 최대 연0.3%p
		- KB樂Star통장 우대이율 : 연0.3%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 1인당 가입한도 : 3천만원
		2. 스마트폰 전용 상품</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201032</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.8</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010927</fin_co_no>
		<kor_co_nm>국민은행</kor_co_nm>
		<fin_prdt_cd>010300100293</fin_prdt_cd>
		<fin_prdt_nm>KB골든라이프연금우대예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>- 연 0.2%p</mtrt_int>
		<spcl_cnd>※ 우대이율 최고 연0.2%p
		- 연금실적 우대이율 : 연0.1%p
		- 한가족사랑 우대이율 : 연0.1%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201032</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010927</fin_co_no>
		<kor_co_nm>국민은행</kor_co_nm>
		<fin_prdt_cd>010300100297</fin_prdt_cd>
		<fin_prdt_nm>KB창조금융예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
		- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
		- 만기후 3개월초과 : 0.2%

		※ 단위 : 연%</mtrt_int>
		<spcl_cnd>※ 우대이율 최고 연0.1%p
		- 창조경제실천 우대이율 : 연0.1%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1인당가입한도 : 3천만원</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201032</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0010927</fin_co_no>
		<kor_co_nm>국민은행</kor_co_nm>
		<fin_prdt_cd>010300100312</fin_prdt_cd>
		<fin_prdt_nm>KB주니어라이프증여예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>- 연 0.2%p</mtrt_int>
		<spcl_cnd>※ 우대이율 최고 연0.1%p
		- 주니어라이프체크카드 우대이율 : 연0.1%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201032</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0011625</fin_co_no>
		<kor_co_nm>신한은행</kor_co_nm>
		<fin_prdt_cd>200-0037-15</fin_prdt_cd>
		<fin_prdt_nm>미래설계 크레바스 연금예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>-1개월 이하:(일반) 정기예금 기본금리 1/2

		-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4

		-6개월 초과 0.2%</mtrt_int>
		<spcl_cnd>해당사항없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입한도 : 300만원 이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201329</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.2</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.35</intr_rate>
		<intr_rate2>1.35</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0011625</fin_co_no>
		<kor_co_nm>신한은행</kor_co_nm>
		<fin_prdt_cd>200-0121-28</fin_prdt_cd>
		<fin_prdt_nm>신한 플러스 월복리 정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>-1개월 이하:(일반) 정기예금 기본금리 1/2

		-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4

		-6개월 초과 0.2%</mtrt_int>
		<spcl_cnd>※가산금리 최고 0.2%
		-ISA 또는 노란우산공제를 보유시
		-예금주의 입출금통장에서 개인형IRP 및 연금저축상품으로 50만원 이상 누적 이체실적 보유시
		-만 62세 이상
		-비과세 종합저축 가입자격자</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입한도 : 300만원 이상~3천만원 이하</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201329</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.22</intr_rate>
		<intr_rate2>1.42</intr_rate2>
						</option>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.23</intr_rate>
		<intr_rate2>1.43</intr_rate2>
						</option>
						<option>
		<intr_rate_type>M</intr_rate_type>
		<intr_rate_type_nm>복리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.26</intr_rate>
		<intr_rate2>1.46</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0011625</fin_co_no>
		<kor_co_nm>신한은행</kor_co_nm>
		<fin_prdt_cd>200-0134-01</fin_prdt_cd>
		<fin_prdt_nm>U드림 정기예금(온라인전용)</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>-1개월 이하:(일반) 정기예금 기본금리 1/2

		-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4

		-6개월 초과 0.2%</mtrt_int>
		<spcl_cnd>※가산금리 최고 0.3%
		-U드림 저축예금 또는 U드림 READY高통장 연동가입시 0.2%
		-온라인예적금 해지후 15일이내 가입시 0.1%
		-신한주거래 우대통장 추가우대고객 가입시 0.1%
		-신한 S뱅크 가입시 0.1%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입한도 : 50만원이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201329</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1.19</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.23</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.27</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.31</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0011625</fin_co_no>
		<kor_co_nm>신한은행</kor_co_nm>
		<fin_prdt_cd>200-0135-03</fin_prdt_cd>
		<fin_prdt_nm>신한 스마트 정기예금(S뱅크전용)</fin_prdt_nm>
		<join_way>스마트폰</join_way>
		<mtrt_int>-1개월 이하:(일반) 정기예금 기본금리 1/2

		-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4

		-6개월 초과 0.2%</mtrt_int>
		<spcl_cnd>-고객별 3천만원 한도
		 (한도내에서 복수계좌 개설 가능)</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입한도 : 50만원이상 3천만원 이하</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201329</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1.44</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.48</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0011625</fin_co_no>
		<kor_co_nm>신한은행</kor_co_nm>
		<fin_prdt_cd>200-0136-01</fin_prdt_cd>
		<fin_prdt_nm>신한 S드림 정기예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>-1개월 이하:(일반) 정기예금 기본금리 1/2

		-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4

		-6개월 초과 0.2%</mtrt_int>
		<spcl_cnd>해당사항없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입한도 : 300만원이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201329</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.1</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.15</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.25</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0011625</fin_co_no>
		<kor_co_nm>신한은행</kor_co_nm>
		<fin_prdt_cd>200-0136-06</fin_prdt_cd>
		<fin_prdt_nm>신한 S드림 정기예금(온라인전용)</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>-1개월 이하:(일반) 정기예금 기본금리 1/2

		-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4

		-6개월 초과 0.2%</mtrt_int>
		<spcl_cnd>해당사항없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>제한없음</join_member>
		<etc_note>1. 가입한도 : 50만원이상</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201329</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1</intr_rate>
		<intr_rate2>1.34</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.38</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.42</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.46</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-003-01225-0001</fin_prdt_cd>
		<fin_prdt_nm>NH왈츠회전예금 II</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 3개월 : 기본금리의 50%
		만기 후 6개월 : 기본금리의 20%
		만기 후  6개월 초과 : 기본금리의 10%

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. 급여이체실적(50만원 이상)이 있는 경우 : 0.1%p
		2.  NH채움카드 보유 및 결제계좌로 이용 : 0.1%p
		3. 3년 이상 거래고객 : 0.1%p
		4. 틀리플 회전 우대이율 :  4회전기간부터 0.1%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.21</intr_rate>
		<intr_rate2>1.51</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.27</intr_rate>
		<intr_rate2>1.57</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-003-1228-0006</fin_prdt_cd>
		<fin_prdt_nm>법사랑플러스(채움정기예금)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기 후  3개월이내 : 기본금리의 50%
		만기 후 6개월이내 : 기본금리 20%
		만기 후 6개월 초과 : 기본금리의 10%

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. 계약기간이 2년이상 3년미만인 고객 : 0.05%p
		2. 계약기간이 3년이상인 고객 0.1%p
		3. NH채움신용(체크) 월 평균
		10만원 이상 사용 또는청약저축 6개월 이상 보유자 : 0.1%p
		4. 최초고객 : 0.2%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.28</intr_rate>
		<intr_rate2>1.73</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.34</intr_rate>
		<intr_rate2>1.79</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.37</intr_rate>
		<intr_rate2>1.82</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.85</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-003-1267-0001</fin_prdt_cd>
		<fin_prdt_nm>e-금리우대 예금</fin_prdt_nm>
		<join_way>인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 3개월이내 : 만기시점의 국고채 1년물 금리
		만기 후 6개월이내 : 기본금리의 20%p
		만기 후 6개월 초과 :  기본금리의 10%p

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. NH채움카드 이용실적 100만원 : 0.1%p
		2. 추천계좌와 피추천계좌에 각각 : 0.1 %p, 최대 0.3%p
		※ 추천 및 피추천 횟수 5회
		※ 3억원이하</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>1. 1인당 가입한도 : 3억원
		2. 인터넷/스마트뱅킹 전용상품</etc_note>
		<max_limit>300000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.39</intr_rate>
		<intr_rate2>1.79</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.42</intr_rate>
		<intr_rate2>1.82</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.45</intr_rate>
		<intr_rate2>1.85</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-003-1283-0001</fin_prdt_cd>
		<fin_prdt_nm>내생애아름다운예금(채움정기예금)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기 후 3개월 : 만기시점의 국고채 1년물 금리
		만기 후 6개월 : 기본금리의  20%
		만기 후 6개월초과 : 기본금리의 10%

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. 신용(체크)카드 월평균 30만원이상 사용 : 0.1%p
		2. 신용(체크)카드 월평균이용액 80만원 이상인 경우에는 0.2%p
		3. 만45세이상 가입고객 : 0.1%P
		3. 손자,손녀 동일한 날 함께 가입(각각 우대)  : 0.2%P</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>1인당 가입한도 : 5억원</etc_note>
		<max_limit>500000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.34</intr_rate>
		<intr_rate2>1.84</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.37</intr_rate>
		<intr_rate2>1.87</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.9</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-003-1299-0001</fin_prdt_cd>
		<fin_prdt_nm>NH통일대박정기예금</fin_prdt_nm>
		<join_way>영업점,인터넷</join_way>
		<mtrt_int>만기 후 3개월이내 : 만기시점의 국고채 1년물 금리
		만기 후 6개월이내 :  기본금리의 20%p
		만기 후 6개월 초과 : 기본금리의 10%p

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. 실향민 또는 새터민 또는 통일부 허가 법인 임직원 또는 개성공단기업임직원 :  0.1%p
		2. 통일염원 활동에 참여 또는 주최한 개인 및 법인 :  0.1%p
		3. BC/채움(체크)카드 월 평균 50만원 이상 사용 :  0.2%p</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>1인당 가입한도 : 5억원</etc_note>
		<max_limit>500000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.15</intr_rate>
		<intr_rate2>1.55</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.65</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-003-1313-0001</fin_prdt_cd>
		<fin_prdt_nm>NH All100플랜연금예금</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>만기 후 3개월이내 : 만기시점의 국고채 1년물 금리
		만기 후 6개월이내 : 기본금리의 20%p
		만기 후 6개월 초과 :  기본금리의 10%p

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. NH All100플랜 통장 보유시 : 0.1%p
		2. 부부동시 신규금액 각 1천만원 이상 : 0.1%p
		3. 총 기간 3년 이상, 1천만원 이상 : 0.1%p
		4. All100플랜 적금 만기 후 해지일로부터 5영업일 이내 이 예금 신규 시 0.2%P</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>1인당 가입한도 : 10억원</etc_note>
		<max_limit>1000000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.25</intr_rate>
		<intr_rate2>1.75</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.29</intr_rate>
		<intr_rate2>1.79</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.33</intr_rate>
		<intr_rate2>1.83</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013175</fin_co_no>
		<kor_co_nm>농협은행</kor_co_nm>
		<fin_prdt_cd>10-059-1273-0001</fin_prdt_cd>
		<fin_prdt_nm>더나은미래예금</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>만기 후 3개월이내 : 만기시점의 국고채 1년물 금리
		만기 후 6개월이내 : 기본금리의 20%p
		만기 후 6개월 초과 :  기본금리의 10%p

		* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리</mtrt_int>
		<spcl_cnd>1. 최초 거래 고객 : 0.2%p
		2. NH채움카드 신용.체크 이용액 100만원 이상 : 0.1%p
		3. 「더나은미래통장」에서 적립식펀드 자</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>개인</join_member>
		<etc_note>해당없음</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609200941</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.34</intr_rate>
		<intr_rate2>1.84</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.37</intr_rate>
		<intr_rate2>1.87</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.9</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013909</fin_co_no>
		<kor_co_nm>KEB하나은행</kor_co_nm>
		<fin_prdt_cd>1</fin_prdt_cd>
		<fin_prdt_nm>행복Together정기예금

		영업점,인터넷뱅킹,스마트폰뱅킹</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리
		1개월초과 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리 1/2</mtrt_int>
		<spcl_cnd>온라인뱅킹에서 주거래은행 약속 메시지 작성 시 연 0.3% 우대</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인
		또는 개인사업자</join_member>
		<etc_note>1. 가입금액 : 1백만원이상 5천만원이하
		 (인터넷뱅킹,스마트폰뱅킹으로 가입시
		  1만원 가입가능)
		2. 1인 최고가입한도 5천만원</etc_note>
		<max_limit>50000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201518</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.1</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013909</fin_co_no>
		<kor_co_nm>KEB하나은행</kor_co_nm>
		<fin_prdt_cd>2</fin_prdt_cd>
		<fin_prdt_nm>e-플러스정기예금

		인터넷뱅킹,스마트폰뱅킹,콜센터</fin_prdt_nm>
		<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
		<mtrt_int>1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리
		1개월초과 : 지급시점 해당기간 일반정기예금월이자지급식 기본금리 1/2</mtrt_int>
		<spcl_cnd>하나 멤버스 앱 로그인 시 연0.1% 우대</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인
		또는 개인사업자</join_member>
		<etc_note>1. 가입금액: 1만원이상 원단위가입가능</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201518</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>6</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.5</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.5</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.6</intr_rate>
		<intr_rate2>1.7</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013909</fin_co_no>
		<kor_co_nm>KEB하나은행</kor_co_nm>
		<fin_prdt_cd>4</fin_prdt_cd>
		<fin_prdt_nm>행복knowhow 연금예금

		영업점</fin_prdt_nm>
		<join_way>영업점</join_way>
		<mtrt_int>1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리
		1개월초과 : 지급시점 해당기간 일반정기예금월이자지급식 기본금리 1/2</mtrt_int>
		<spcl_cnd>없음</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인
		또는 개인사업자</join_member>
		<etc_note>1. 가입금액 : 1백만원이상 원단위가입가능</etc_note>
		<max_limit></max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201518</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.2</intr_rate>
		<intr_rate2>1.2</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>24</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.3</intr_rate2>
						</option>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>36</save_trm>
		<intr_rate>1.4</intr_rate>
		<intr_rate2>1.4</intr_rate2>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201609</dcls_month>
		<fin_co_no>0013909</fin_co_no>
		<kor_co_nm>KEB하나은행</kor_co_nm>
		<fin_prdt_cd>5</fin_prdt_cd>
		<fin_prdt_nm>두리하나 정기예금

		영업점,인터넷뱅킹,스마트폰뱅킹</fin_prdt_nm>
		<join_way>영업점,인터넷,스마트폰</join_way>
		<mtrt_int>1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리
		1개월초과 : 지급시점 해당기간 일반정기예금월이자지급식 기본금리 1/2</mtrt_int>
		<spcl_cnd>최대 연0.3% 우대
		 - 나도 하나 우대 연0.2%
		 - 모두 하나 우대 연0.1%
		 - 더불어 하나 우대 연0.1%
		 - 두리하나 우대 연0.1%</spcl_cnd>
		<join_deny>1</join_deny>
		<join_member>실명의 개인
		또는 개인사업자</join_member>
		<etc_note>1. 가입금액: 1백만원이상 3천만원이하
		2. 1인 최고가입한도 3천만원</etc_note>
		<max_limit>30000000</max_limit>
		<dcls_strt_day>20160920</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201609201518</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<intr_rate_type>S</intr_rate_type>
		<intr_rate_type_nm>단리</intr_rate_type_nm>
		<save_trm>12</save_trm>
		<intr_rate>1.3</intr_rate>
		<intr_rate2>1.6</intr_rate2>
						</option>
					</options>
				</product>
			</products>
	</result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1
예제 요청결과(JSON)
{"result":{"prdt_div":"D","total_count":"79","max_page_no":"1","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","kor_co_nm":"우리은행","fin_prdt_nm":"우리웰리치 주거래예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리","spcl_cnd":"다음 중 하나 충족한 입금건에 대해  최고 연0.2%p\n1. 순신규고객\n2. 가계대출이용고객\n3. 입금일 전월 주거래우대조건 2가지이상\n4. 건별3천만원이상\n5. 건별 만기 자동재예치","join_deny":"1","join_member":"실명의 개인","etc_note":"-추가입금은 신규가입 시 선택한 예치기간을 각 입금건별 입금일로부터 적용\n-재예치는 입금건별 최초 입금일로부터 최장 10년간 가능","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201028"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001B","kor_co_nm":"우리은행","fin_prdt_nm":"우리웰리치100예금(회전형)","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리","spcl_cnd":"최고 연 0.2%p우대이율\n1. 연금이체실적보유 : 연0.1%p\n2. 신용/체크카드 보유 : 연0.1%p\n3. 당일 적금/예금/펀드 해지 후 신규시  : 연0.1%p\n4. 인터넷/스마트뱅킹으로 신규시 : 연 0.1%","join_deny":"1","join_member":"실명의 개인","etc_note":"-가입자가 환갑, 칠순, 팔순, 구순, 백순 사유로 중도해지 시 기본이자율을 중도해지 이자율 적용\n※ 주민등록번호 기준으로 사유발생 전후3개월간 혜택제공","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201028"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001C","kor_co_nm":"우리은행","fin_prdt_nm":"Red Monkey\n스마트 정기예금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리","spcl_cnd":"최고 연0.3%p \n1. 위비앱/위비모바일통장 연0.1%p \n2. 최고 연0.2%p  \n - 스마트간편신규 연0.1%p, 펀드/적금/대출보유 연0.1%p, 예적금만기재예치 연0.1%p \n3. 친구번호등록 연0.2%p\n4. 첫거래 연0.2%p","join_deny":"1","join_member":"실명의 개인","etc_note":"해당없음","max_limit":20000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201028"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001D","kor_co_nm":"우리은행","fin_prdt_nm":"우리로모아\n정기예금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리","spcl_cnd":"최고 연 0.2%p 적용 \n1. 우리닷컴통장에서 신규된 경우 : 연 0.2%p\n2. 모바일뱅킹에 가입한 고객 : 연 0.2%p\n3. WIN-CMS에 가입한 고객  : 연 0.2%p","join_deny":"1","join_member":"인터넷뱅킹가입고객","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201028"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001E","kor_co_nm":"우리은행","fin_prdt_nm":"iTouch\n우리예금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리","spcl_cnd":"최고 연 0.2%p\n1. 최종 모집잔액에 따라 : 연 0.1%\n2. iTouch우리통장 연결가입 : 연 0.1%p","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201028"},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320301","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"홈앤세이브예금","join_way":"영업점","mtrt_int":"만기 후 1개월: 0.7%\n만기 후 1개월 초과 1년 이내: 0.3%\n만기 후 1년 초과: 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200944"},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320342","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"e-그린세이브예금","join_way":"인터넷,스마트폰,모집인","mtrt_int":"만기 후 1개월: 0.7%\n만기 후 1개월 초과 1년 이내: 0.3%\n만기 후 1년 초과: 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200944"},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320396","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"퍼스트정기예금","join_way":"영업점,모집인,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월: 0.7%\n만기 후 1개월 초과 1년 이내: 0.3%\n만기 후 1년 초과: 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200944"},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3127","kor_co_nm":"한국씨티은행","fin_prdt_nm":"프리스타일예금","join_way":"영업점,인터넷","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 고시한 1개월 정기예금 이율\n만기 후 1개월 초과 : 연 1.0%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입금액은 1백만원 이상 가입 가능\n2. 가입기간은 1개월 이상 3년 이내 일단위 가입 가능","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201001"},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3129","kor_co_nm":"한국씨티은행","fin_prdt_nm":"자유회전예금","join_way":"영업점,인터넷","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 고시한 1개월 정기예금 이율\n만기 후 1개월 초과 : 연 1.0%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입금액은 1백만원 이상 가입 가능\n2. 가입기간은 1개월 이상 30년 이내 일단위 가입 가능","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201001"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000845001","kor_co_nm":"대구은행","fin_prdt_nm":"내손안에 예금","join_way":"스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.2%\n - 최초가입 우대 : 0.1%\n - 공과금 실적 우대 : 0.1%\n \n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 100만원 (최대 5천만원 이내)\n2. 스마트폰 가입 전용상품 \n3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201120"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000958002","kor_co_nm":"대구은행","fin_prdt_nm":"최강삼성V9 예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.25%\n - 신규시 주택청약상품 보유 우대 : 0.1%\n - 신규시 공과금 2건이상 보유 우대 : 0.05%\n - 삼성라이온즈 정규시즌 우승 우대 : 0.05%\n - 삼성라이온즈 한국시리즈 우승 우대 : 0.1%\n - 만기시 공과금 2건이상 보유 우대 : 0.05%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 100만원  (최대 5천만원 이내)\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201120"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000996000","kor_co_nm":"대구은행","fin_prdt_nm":"DGB주거래우대예금(첫만남고객형)","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.2%\n - 최초가입 우대 : 0.1%\n - 신용(체크)카드 발급 우대 : 0.05%\n - 인터넷,폰,스마트뱅킹 가입우대 : 0.05%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 300만원\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201120"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008001109001","kor_co_nm":"대구은행","fin_prdt_nm":"ISA플러스 예금","join_way":"영업점","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.4%\n - 신규시 ISA계좌 30만원 이상보유 우대 : 0.1%\n - 신규시 공과금 3건이상 보유 우대 : 0.1%\n - 만기시 ISA계좌 30만원 이상 보유 우대 : 0.1%\n - 만기시 공과금 3건이상 보유 우대 : 0.1%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 100만원 (최대 5천만원 이내)\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201120"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511014000001001","kor_co_nm":"대구은행","fin_prdt_nm":"e-U(이유)예금","join_way":"인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.5%\n - 최초가입 우대 : 0.1%\n - 재예치 우대 : 0.1%\n - 거래실적 우대 : 0.2%\n - 주택청약상품 보유 우대 : 0.1%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 100만원 (최대 1억원 이내)\n2. 인터넷뱅킹 및 스마트폰 가입 전용상품 \n3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201120"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500130002","kor_co_nm":"부산은행","fin_prdt_nm":"메리트정기예금","join_way":"영업점,인터넷","mtrt_int":"- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,\n- 만기후1년초과:가입기간별 일반정기예금이율 x 20%","spcl_cnd":"- 1년제, 1천만원이상: 1.10%","join_deny":"1","join_member":"제한없음","etc_note":"제한없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201336"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500290002","kor_co_nm":"부산은행","fin_prdt_nm":"e-푸른바다정기예금","join_way":"인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,\n- 만기후1년초과:가입기간별 일반정기예금이율 x 20%","spcl_cnd":"우대조건 없음","join_deny":"1","join_member":"제한없음","etc_note":"가입채널: 인터넷,스마트뱅킹,고객센터","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201336"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500400002","kor_co_nm":"부산은행","fin_prdt_nm":"BNKe스마트정기예금","join_way":"스마트폰,전화(텔레뱅킹)","mtrt_int":"- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,\n- 만기후1년초과:가입기간별 일반정기예금이율 x 20%","spcl_cnd":"우대조건 없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 개인및 개인사업자 가입가능\n2. 가입한도:3천만원이하\n3. 가입채널: 스마트,고객센터","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201336"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500460002","kor_co_nm":"부산은행","fin_prdt_nm":"굿-초이스","join_way":"영업점,스마트폰,전화(텔레뱅킹)","mtrt_int":"- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,\n- 만기후1년초과:가입기간별 일반정기예금이율 x 20%","spcl_cnd":"-비대면 여수신 신규우대: 0.10%\n-그룹우대: 0.10%\n-홍보우대: 0.10%\n-교차판매 우대: 0.3%","join_deny":"1","join_member":"제한없음","etc_note":"1. 개인및 개인사업자 가입가능\n2. 가입채널: 인터넷,스마트,고객센터","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201336"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500490002","kor_co_nm":"부산은행","fin_prdt_nm":"MY SUM","join_way":"스마트폰","mtrt_int":"- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,\n- 만기후1년초과:가입기간별 일반정기예금이율 x 20%","spcl_cnd":"-10백만원 이상 신규시 : 0.10%\n-썸뱅크간편송금 20회이상: 0.10%\n-SUM모바일통장 기중평잔 30만원 이상: 0.10%\n-SUM모바일통장 결제계좌로 롯데카드 결제실적 300만원 이상 : 0.10% \n-썸뱅크를 통한 외화 환전실적 1회이상: 0.10%","join_deny":"1","join_member":"제한없음","etc_note":"1. 개인및 개인사업자 가입가능\n2. 가입한도: 1억원이하\n3. 가입채널: 당행 썸뱅크(모바일) 통해 가입가능","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201336"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500500002","kor_co_nm":"부산은행","fin_prdt_nm":"BNK어울림","join_way":"영업점,인터넷,스마트폰","mtrt_int":"- 만기후1년내: 가입기간별 일반정기예금이율 x 50%,\n- 만기후1년초과:가입기간별 일반정기예금이율 x 20%","spcl_cnd":"-예적금 동시보유 : 0.10%\n-ISA가입: 0.05%\n-신규 및 장기고객우대: 0.10%\n-자동이체실적 등 : 0.10%","join_deny":"1","join_member":"제한없음","etc_note":"1. 개인및 개인사업자 가입가능\n2. 가입한도: 1억원이하","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201336"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300021000","kor_co_nm":"광주은행","fin_prdt_nm":"플러스다모아예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 최초 가입\n기간별 일반정기예금 고시금리의 1/2\n만기 후 1개월 초과 : 0.10%","spcl_cnd":"1. 1천만원 이상 가입시 최대 0.3%우대\n2. 최고 0.2% 우대(개인)\n- 적립식예금 6회 이상 납입 : 0.1%\n- 급여통장 보유 : 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"1. 최소가입금액 : 100만원 이상","max_limit":null,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261219"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300025000","kor_co_nm":"광주은행","fin_prdt_nm":"아파트사랑정기예금","join_way":"영업점","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 최초 가입\n기간별 일반정기예금 고시금리의 1/2\n만기 후 1개월 초과 : 0.10%","spcl_cnd":"1. 1천만원 이상 가입시 0.3%우대\n2. 조건 충족시 최대 0.25% 우대(개인)\n- 아파트관리비 6회 이상 자동이체: 0.1%\n- 자녀용돈통장개설: 0.05%\n- 정액적립식 6회 이상 납입: 최대 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"1. 최소가입금액 : 100만원 이상\n2. 영업점 방문 가입만 가능\n3. 가입기간 : 1년 이상 3년 이내","max_limit":null,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261219"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300027000","kor_co_nm":"광주은행","fin_prdt_nm":"미즈월복리정기예금","join_way":"영업점,인터넷","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 최초 가입\n기간별 일반정기예금 고시금리의 1/2\n만기 후 1개월 초과 : 0.10%","spcl_cnd":"*최대 0.2%우대\n1. 요구불평잔 300만원 이상: 최대 0.2%\n2. 신용카드 결제실적 월 300만원 이상 : 최대 0.1%\n3, 가입자의 자녀출산 또는 결혼시 : 0.1%","join_deny":"3","join_member":"만 18세 이상 여성고객","etc_note":"1. 1인당 가입한도 : 5천만원\n2. 최소가입금액 : 500만원 이상\n3. 가입기간 : 1년 이상 3년 이내","max_limit":50000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261219"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300028000","kor_co_nm":"광주은행","fin_prdt_nm":"스마트모아Dream정기예금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 최초 가입\n기간별 일반정기예금 고시금리의 1/2\n만기 후 1개월 초과 : 0.10%","spcl_cnd":"1. 1천만원 이상 가입시 0.3%우대\n2. 스마트뱅킹 신규시 0.2% 우대 : 고객당 2천만원까지","join_deny":"1","join_member":"개인고객","etc_note":"1. 인터넷/스마트폰뱅킹 가입 전용상품\n2. 최소가입금액 : 100만원 이상","max_limit":null,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261219"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300029000","kor_co_nm":"광주은행","fin_prdt_nm":"평생대박정기예금","join_way":"영업점,인터넷","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 최초 가입\n기간별 일반정기예금 고시금리의 1/2\n만기 후 1개월 초과 : 0.10%","spcl_cnd":"1. 500만원 이상 가입시 0.3%우대\n2. 조건충족시, 최대 0.2%우대\n- 4대연금수급실적 : 0.1%\n- 급여이체실적: 0.1%\n- 요구불 평잔 500만원 이상 : 최대 0.1%","join_deny":"3","join_member":"만 50세 이상 고객","etc_note":"1.최소가입금액 : 500만원 이상\n2.가입기간 : 1년 이상 3년 이내","max_limit":null,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261219"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300032000","kor_co_nm":"광주은행","fin_prdt_nm":"쏠쏠한마이쿨예금","join_way":"스마트폰","mtrt_int":"만기 후 1개월 이내 : 만기일 당시 최초 가입\n기간별 일반정기예금 고시금리의 1/2\n만기 후 1개월 초과 : 0.10%","spcl_cnd":"해당없음","join_deny":"3","join_member":"가입일 기준 최근 1년간 당행 거치식예금, 적","etc_note":"1.최소가입금액 : 100만원 이상\n2.가입기간 : 1년","max_limit":50000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261219"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000301","kor_co_nm":"제주은행","fin_prdt_nm":"제주Dream정기예금(개인/만기지급식)","join_way":"영업점","mtrt_int":"- 만기후 1개월 이내 : (일반)정기예금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기예금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"최고 연 0.1%p(항목별 0.1%p)\n①급여이체\n②적립식예금 잔액 10만원 이상 보유\n③탑스, 주거래 고객\n④결제계좌(가맹점) 전월 입금액 10만원 이상 \n⑤비과세종합저축 대상 고객\n⑥다자녀(3인이상 자녀)가정","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 : 1백만원 이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200947"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000302","kor_co_nm":"제주은행","fin_prdt_nm":"사이버우대정기예금(개인/만기지급식)","join_way":"인터넷,스마트폰","mtrt_int":"- 만기후 1개월 이내 : (일반)정기예금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기예금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"최고 연 0.1%p(중복불가)\n①탐나는 J 직장인 통장 가입 고객이 기본우대 요건 충족 후 이 상품 가입시 : 0.1%p\n②탐나는 J 주거래 통장 가입 고객이 기본우대 요건 충족 후 이 상품 가입시 : 0.1%p","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 : 30만원 이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200947"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0001-0000","kor_co_nm":"전북은행","fin_prdt_nm":"정기예금","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0008-0000","kor_co_nm":"전북은행","fin_prdt_nm":"맞춤형자유만기정기예금(월이자지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 5백만원이상\n(비과세종합저축은 1백만원이상)","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0009-0000","kor_co_nm":"전북은행","fin_prdt_nm":"맞춤형자유만기정기예금(만기일시지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 5백만원이상\n(비과세종합저축은 1백만원이상)","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0016-0000","kor_co_nm":"전북은행","fin_prdt_nm":"전북아이나라예금\n(월이자지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"3","join_member":"전라북도에 주소지를 둔 만 3세이하 개인","etc_note":"가입금액 10만원이상 15백만원이하","max_limit":15000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0017-0000","kor_co_nm":"전북은행","fin_prdt_nm":"전북아이나라예금\n(만기일시지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"3","join_member":"전라북도에 주소지를 둔 만 3세이하 개인","etc_note":"가입금액 10만원이상 15백만원이하","max_limit":15000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0029-0000","kor_co_nm":"전북은행","fin_prdt_nm":"실버보금자리예금\n(월이자지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"3","join_member":"만60세이상 실명의 개인으로\n전라북도 소재 영업점 : 주민등록상 주소지가 전라북도인 경우 \n전라북도 소재 이외 영업점 : 주민등록상 주소지, 원적지, 본적지가 전라북도인 경우","etc_note":"가입금액 1백만원이상, \n1인당 3억원이내","max_limit":300000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0030-0000","kor_co_nm":"전북은행","fin_prdt_nm":"실버보금자리예금\n(만기일시지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"3","join_member":"만60세이상 실명의 개인으로\n전라북도 소재 영업점 : 주민등록상 주소지가 전라북도인 경우 \n전라북도 소재 이외 영업점 : 주민등록상 주소지, 원적지, 본적지가 전라북도인 경우","etc_note":"가입금액 1백만원이상, 1인당 3억원이내","max_limit":300000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0037-0000","kor_co_nm":"전북은행","fin_prdt_nm":"시장금리부정기예금\n(월이자지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 3백만원이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0038-0000","kor_co_nm":"전북은행","fin_prdt_nm":"시장금리부정기예금\n(만기일시지급식)","join_way":"영업점","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 3백만원이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0041-0000","kor_co_nm":"전북은행","fin_prdt_nm":"인터넷정기예금\n(월이자지급식)","join_way":"인터넷","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 3백만원이상 1억원이하, \n인터넷뱅킹 가입상품","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0000","kor_co_nm":"전북은행","fin_prdt_nm":"인터넷정기예금\n(만기일시지급식)","join_way":"인터넷","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 3백만원이상 1억원이하,\n인터넷뱅킹 가입상품","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0021","kor_co_nm":"전북은행","fin_prdt_nm":"스마트정기예금\n(만기일시지급식)","join_way":"스마트폰","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"1.가입시JB급여플러스통장보유 연0.1%, 2.최근1개월이내신용카드사용고객 연0.1%,3.예금가입기간별우대금리:2년이상연0,1%,3년이상연0.2%","join_deny":"1","join_member":"제한없음","etc_note":"가입금액 3백만원이상 5천만원이하,\n스마트폰뱅킹 가입상품","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0046-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB 다이렉트예금통장\n(만기일시지급식)","join_way":"인터넷,스마트폰","mtrt_int":"만기후 1개월 이하 : 만기일 현재 계약기간별 정기예금 실행이율 1/2\n만기후 1개월 초과 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"실명의 개인(임의단체 제외)","etc_note":"가입금액 1계좌당 1백만원이상,\n1인당  총 3억원 이하,\n인터넷/스마트폰뱅킹 가입상품","max_limit":300000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201044"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000087","kor_co_nm":"경남은행","fin_prdt_nm":"마니마니정기예금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%\n만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%","spcl_cnd":"우대조건에 따른 우대금리 없음\n계약기간은 최소 1개월 이상부터 가능","join_deny":"1","join_member":"거래대상자는 제한을 두지 아니한다. 다만, 국가 및 지방자치단체는 이 예금을 거래할 수 없다.","etc_note":"1. 계약기간은 1개월 이상 2년까지로 하되 예금주의 편의에 따라 임의로 정할 수 있다.\n2. 가입금액 최소 5백만원 이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201041"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000093","kor_co_nm":"경남은행","fin_prdt_nm":"스마트\n정기예금","join_way":"스마트폰","mtrt_int":"만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%\n만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%","spcl_cnd":"▶추천이율: 최대0.15%\n가입시마다 추천번호제공하며 해당추천번호를 타인이 입력하는 경우","join_deny":"1","join_member":"스마트폰뱅킹을 가입한 개인 및 개인사업자","etc_note":"1. 이 예금은 스마트폰뱅킹을 통해서만 가입할 수 있으며, 해지는 스마트폰뱅킹, 영업점 창구에서 할 수 있다.\n2. 계약기간은 1개월 이상 12개월 이내 월단위로 한다.\n3. 가입금액 최소 1백만원 이상~최대 5천만원 이하","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201041"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000101","kor_co_nm":"경남은행","fin_prdt_nm":"e-Money\n정기예금","join_way":"인터넷,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%\n만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%","spcl_cnd":"▶계약기간 만기전에 만기해지 포함 총 3회까지 분할인출이 가능하다.","join_deny":"1","join_member":"개인 및 개인사업자","etc_note":"1. 이 예금은 인터넷뱅킹, 고객센터를 통하여 가입하고, 해지는 인터넷뱅킹, 고객센터, 영업점 창구에서 할 수 있다.\n2. 계약기간은 1개월 이상 12개월 이내 월단위로 한다.\n3. 가입금액 최소 1백만원 이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201041"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001049","kor_co_nm":"경남은행","fin_prdt_nm":"다모아\n정기예금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%\n만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%","spcl_cnd":"①(핵심예금 평균잔액 증가액X1.6%)/이 예금의 신규가입 금액\n②(신용카드 결제실적 증가액X0.7%)/이 예금의 신규가입 금액\n▶①및②의 금리를 합하여 최고1.0%우대이율 제공","join_deny":"1","join_member":"거래대상자는 제한을 두지 아니한다. 다만, 국가 및 지방자치단체는 이 예금을 거래할 수 없다.","etc_note":"1. 계약기간은 12개월로 한다.\n2. 최저가입금액은 5백만원 이상으로 하며, 이 예금은 1인 1계좌에 한하여 가입 가능하다.","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201041"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001057","kor_co_nm":"경남은행","fin_prdt_nm":"다이아몬드\n정기예금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%\n만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%","spcl_cnd":"①비대면채널가입시0.05%\n②여성우대이율 0.10%\n - 가입기간중 결혼, 임신, 출산, 자녀결혼, 손자출생시 우대금리를 지급하며, 해당 예금의 만기해지전까지 영업점 창구에 증빙서류를 제출하는 경우 \n③소개이율 0.05%\n▶①~③의 최고 우대금리 합계는 0.10%","join_deny":"3","join_member":"실명의 개인인 여성","etc_note":"1. 계약기간은 6개월 이상 24개월 이내로 한다.\n2. 가입금액 최소 3백만원 이상~최대 1억원 이하","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201041"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001105","kor_co_nm":"경남은행","fin_prdt_nm":"BNK사랑방\n정기예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만: 일반정기예금 기본이율 Ⅹ50%\n만기 후 1개월 이상: 일반정기예금 기본이율 Ⅹ20%","spcl_cnd":"①가입일 기준 과거 1년간 당행 정기예금 신규이력이 없는 고객 0.10%\n②아래 항목 중 한가지 이상 충족시 0.10%\n- 입출금이자유로운예금 평잔 2백만원 이상, 신용카드 결제금액이 5백만원 이상\n③주거래우대금리 0.10%\n④비대면채널가입 우대이율 0.05%","join_deny":"1","join_member":"개인 및 개인사업자","etc_note":"1. 이 예금은 1인 1계좌만 가입 가능하고, 계약기간은 12개월로 한다.\n2. 가입금액 최소 1백만원 이상~최대 5천만원 이하","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201041"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310073","kor_co_nm":"중소기업은행","fin_prdt_nm":"新서민섬김통장 실세금리정기예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 실세금리정기예금의 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30% \n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.3%p\n1. 신규고객 우대금리 : 연 0.1%p\n2. 거래심화 우대금리 : 연 0.2%p","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"1인당 통합한도(적립식 계약원금+거치식 가입금액) 3천만원","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201030"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310108","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK흔들어예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 실세금리정기예금의 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30% \n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연0.4%p\n1. I-ONE뱅크 또는 흔들어예금 앱으로 가입하고 별도로 정한상품 1개이상 신규가입(연0.2%p)\n2. 흔들어예금 앱으로 만보기미션 달성(최고 연0.2%p)","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"1인당 가입한도 1억원","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201030"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310121","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK평생한가족통장 실세금리정기예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 실세금리정기예금의 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30% \n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.2%p\n1. 고객별 우대금리: 연 0.05%p\n2. 주거래 우대금리: 연 0.15%p","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"1인당 통합한도 1억원","max_limit":100000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201030"},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10120102800011","kor_co_nm":"수협은행","fin_prdt_nm":"사랑해정기예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"* 만기후 1년 이내\n만기당시 정기예금(월이자지급식) 계약기간별 약정이율 1/2\n* 만기후 1년 초과\n만기당시 보통예금 이율","spcl_cnd":"우대조건없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201529"},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10120104400021","kor_co_nm":"수협은행","fin_prdt_nm":"사랑해나누리예금","join_way":"영업점","mtrt_int":"* 만기후 1년 이내\n만기당시 정기예금(월이자지급식) 계약기간별 약정이율 1/2\n* 만기후 1년 초과\n만기당시 보통예금 이율","spcl_cnd":"0.1%\n기부금납부자\n헌혈증서 보유자\n자원봉사증보유자\n어업종사자\n어업인","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201529"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05100","kor_co_nm":"한국산업은행","fin_prdt_nm":"정기예금","join_way":"영업점,인터넷","mtrt_int":"지급일 현재 고시된 \n이 예금의 만기후 이율","spcl_cnd":"해당없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261020"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05702","kor_co_nm":"한국산업은행","fin_prdt_nm":"KDBdream 정기예금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"* 만기후 1년 이내 :\n 만기일 현재 고시된 일반 정기예금 해당기간 기본이자유의 1/2\n* 만기후 1년 초과 :\n만기일 현재 고시된 보통예금 이자율","spcl_cnd":"KDBdream Account 가입고객이 이 예금을 가입하는 경우, 0.10%P 가산","join_deny":"1","join_member":"개인(개인사업자 및 임의단체 포함)","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200933"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05705","kor_co_nm":"한국산업은행","fin_prdt_nm":"KDB Hi 정기예금","join_way":"인터넷,스마트폰","mtrt_int":"* 만기후 1년 이내 :\n 만기일 현재 고시된 일반 정기예금 해당기간 기본이자유의 1/2\n* 만기후 1년 초과 :\n만기일 현재 고시된 보통예금 이자율","spcl_cnd":"해당없음","join_deny":"1","join_member":"KDB Hi 입출금통장에 가입한 개인(개인사업자 및 임의단체 제외)\n단, 국민인 거주자에 한함","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261020"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100072","kor_co_nm":"국민은행","fin_prdt_nm":"국민수퍼고정금리형-만기일시지급식","join_way":"영업점,인터넷,스마트폰","mtrt_int":"- 만기후 1개월이내 : 약정이율 X 50%\n- 만기후 1개월초과~3개월이내 : 약정이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%\n   약정이율 : 고객이 만기시점에 받기로 한 이율","spcl_cnd":"※ 우대이율 최고 : 연0.4%p\n1. 영업점장 우대금리 : 연0.1%p\n   (※ 비대면 신규 시에는 자동 적용)\n2. 평생고객사은 이율 : 연0.1%p\n3. 가입상품 금리우대(인터넷신규시) : 연0.3%p\n   (※ 2번, 3번 우대금리는 중복불가)","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201032"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100209","kor_co_nm":"국민은행","fin_prdt_nm":"e-파워정기예금","join_way":"인터넷,전화(텔레뱅킹)","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연0.3%p\n- KB star*t통장 or KB樂Star통장 \n  or KB나라사랑우대통장 가입자\n  우대이율 : 연0.3%p","join_deny":"1","join_member":"제한없음","etc_note":"인터넷 전용 상품","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201032"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100226","kor_co_nm":"국민은행","fin_prdt_nm":"KB Smart★폰 예금","join_way":"스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연0.6%p\n- 추천 우대이율 : 최대 연0.3%p\n- KB樂Star통장 우대이율 : 연0.3%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1인당 가입한도 : 3천만원\n2. 스마트폰 전용 상품","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201032"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100293","kor_co_nm":"국민은행","fin_prdt_nm":"KB골든라이프연금우대예금","join_way":"영업점","mtrt_int":"- 연 0.2%p","spcl_cnd":"※ 우대이율 최고 연0.2%p\n- 연금실적 우대이율 : 연0.1%p\n- 한가족사랑 우대이율 : 연0.1%p","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201032"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100297","kor_co_nm":"국민은행","fin_prdt_nm":"KB창조금융예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연0.1%p\n- 창조경제실천 우대이율 : 연0.1%p","join_deny":"1","join_member":"제한없음","etc_note":"1인당가입한도 : 3천만원","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201032"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100312","kor_co_nm":"국민은행","fin_prdt_nm":"KB주니어라이프증여예금","join_way":"영업점","mtrt_int":"- 연 0.2%p","spcl_cnd":"※ 우대이율 최고 연0.1%p\n- 주니어라이프체크카드 우대이율 : 연0.1%p","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201032"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0037-15","kor_co_nm":"신한은행","fin_prdt_nm":"미래설계 크레바스 연금예금","join_way":"영업점","mtrt_int":"-1개월 이하:(일반) 정기예금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"해당사항없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 300만원 이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201329"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0121-28","kor_co_nm":"신한은행","fin_prdt_nm":"신한 플러스 월복리 정기예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기예금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.2%\n-ISA 또는 노란우산공제를 보유시\n-예금주의 입출금통장에서 개인형IRP 및 연금저축상품으로 50만원 이상 누적 이체실적 보유시\n-만 62세 이상\n-비과세 종합저축 가입자격자","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 300만원 이상~3천만원 이하","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201329"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0134-01","kor_co_nm":"신한은행","fin_prdt_nm":"U드림 정기예금(온라인전용)","join_way":"인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기예금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.3%\n-U드림 저축예금 또는 U드림 READY高통장 연동가입시 0.2%\n-온라인예적금 해지후 15일이내 가입시 0.1%\n-신한주거래 우대통장 추가우대고객 가입시 0.1%\n-신한 S뱅크 가입시 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 50만원이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201329"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0135-03","kor_co_nm":"신한은행","fin_prdt_nm":"신한 스마트 정기예금(S뱅크전용)","join_way":"스마트폰","mtrt_int":"-1개월 이하:(일반) 정기예금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"-고객별 3천만원 한도\n (한도내에서 복수계좌 개설 가능)","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 50만원이상 3천만원 이하","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201329"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-01","kor_co_nm":"신한은행","fin_prdt_nm":"신한 S드림 정기예금","join_way":"영업점","mtrt_int":"-1개월 이하:(일반) 정기예금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"해당사항없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 300만원이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201329"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-06","kor_co_nm":"신한은행","fin_prdt_nm":"신한 S드림 정기예금(온라인전용)","join_way":"인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기예금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기예금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"해당사항없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 50만원이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201329"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-01225-0001","kor_co_nm":"농협은행","fin_prdt_nm":"NH왈츠회전예금 II","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 3개월 : 기본금리의 50%\n만기 후 6개월 : 기본금리의 20%\n만기 후  6개월 초과 : 기본금리의 10%\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. 급여이체실적(50만원 이상)이 있는 경우 : 0.1%p\n2.  NH채움카드 보유 및 결제계좌로 이용 : 0.1%p\n3. 3년 이상 거래고객 : 0.1%p\n4. 틀리플 회전 우대이율 :  4회전기간부터 0.1%p","join_deny":"1","join_member":"개인","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1228-0006","kor_co_nm":"농협은행","fin_prdt_nm":"법사랑플러스(채움정기예금)","join_way":"영업점","mtrt_int":"만기 후  3개월이내 : 기본금리의 50%\n만기 후 6개월이내 : 기본금리 20%\n만기 후 6개월 초과 : 기본금리의 10%\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. 계약기간이 2년이상 3년미만인 고객 : 0.05%p\n2. 계약기간이 3년이상인 고객 0.1%p\n3. NH채움신용(체크) 월 평균\n10만원 이상 사용 또는청약저축 6개월 이상 보유자 : 0.1%p\n4. 최초고객 : 0.2%p","join_deny":"1","join_member":"개인","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1267-0001","kor_co_nm":"농협은행","fin_prdt_nm":"e-금리우대 예금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후 3개월이내 : 만기시점의 국고채 1년물 금리\n만기 후 6개월이내 : 기본금리의 20%p\n만기 후 6개월 초과 :  기본금리의 10%p\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. NH채움카드 이용실적 100만원 : 0.1%p\n2. 추천계좌와 피추천계좌에 각각 : 0.1 %p, 최대 0.3%p\n※ 추천 및 피추천 횟수 5회\n※ 3억원이하","join_deny":"1","join_member":"개인","etc_note":"1. 1인당 가입한도 : 3억원\n2. 인터넷/스마트뱅킹 전용상품","max_limit":300000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1283-0001","kor_co_nm":"농협은행","fin_prdt_nm":"내생애아름다운예금(채움정기예금)","join_way":"영업점","mtrt_int":"만기 후 3개월 : 만기시점의 국고채 1년물 금리\n만기 후 6개월 : 기본금리의  20%\n만기 후 6개월초과 : 기본금리의 10%\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. 신용(체크)카드 월평균 30만원이상 사용 : 0.1%p\n2. 신용(체크)카드 월평균이용액 80만원 이상인 경우에는 0.2%p\n3. 만45세이상 가입고객 : 0.1%P\n3. 손자,손녀 동일한 날 함께 가입(각각 우대)  : 0.2%P","join_deny":"1","join_member":"개인","etc_note":"1인당 가입한도 : 5억원","max_limit":500000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1299-0001","kor_co_nm":"농협은행","fin_prdt_nm":"NH통일대박정기예금","join_way":"영업점,인터넷","mtrt_int":"만기 후 3개월이내 : 만기시점의 국고채 1년물 금리\n만기 후 6개월이내 :  기본금리의 20%p\n만기 후 6개월 초과 : 기본금리의 10%p\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. 실향민 또는 새터민 또는 통일부 허가 법인 임직원 또는 개성공단기업임직원 :  0.1%p\n2. 통일염원 활동에 참여 또는 주최한 개인 및 법인 :  0.1%p\n3. BC/채움(체크)카드 월 평균 50만원 이상 사용 :  0.2%p","join_deny":"1","join_member":"개인","etc_note":"1인당 가입한도 : 5억원","max_limit":500000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1313-0001","kor_co_nm":"농협은행","fin_prdt_nm":"NH All100플랜연금예금","join_way":"영업점","mtrt_int":"만기 후 3개월이내 : 만기시점의 국고채 1년물 금리\n만기 후 6개월이내 : 기본금리의 20%p\n만기 후 6개월 초과 :  기본금리의 10%p\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. NH All100플랜 통장 보유시 : 0.1%p\n2. 부부동시 신규금액 각 1천만원 이상 : 0.1%p\n3. 총 기간 3년 이상, 1천만원 이상 : 0.1%p\n4. All100플랜 적금 만기 후 해지일로부터 5영업일 이내 이 예금 신규 시 0.2%P","join_deny":"1","join_member":"개인","etc_note":"1인당 가입한도 : 10억원","max_limit":1000000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-059-1273-0001","kor_co_nm":"농협은행","fin_prdt_nm":"더나은미래예금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 3개월이내 : 만기시점의 국고채 1년물 금리\n만기 후 6개월이내 : 기본금리의 20%p\n만기 후 6개월 초과 :  기본금리의 10%p\n\n* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리","spcl_cnd":"1. 최초 거래 고객 : 0.2%p\n2. NH채움카드 신용.체크 이용액 100만원 이상 : 0.1%p\n3. 「더나은미래통장」에서 적립식펀드 자","join_deny":"1","join_member":"개인","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200941"},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"1","kor_co_nm":"KEB하나은행","fin_prdt_nm":"행복Together정기예금\n\n영업점,인터넷뱅킹,스마트폰뱅킹","join_way":"영업점,인터넷,스마트폰","mtrt_int":"1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리\n1개월초과 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리 1/2","spcl_cnd":"온라인뱅킹에서 주거래은행 약속 메시지 작성 시 연 0.3% 우대","join_deny":"1","join_member":"실명의 개인\n또는 개인사업자","etc_note":"1. 가입금액 : 1백만원이상 5천만원이하\n (인터넷뱅킹,스마트폰뱅킹으로 가입시\n  1만원 가입가능)\n2. 1인 최고가입한도 5천만원","max_limit":50000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201518"},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"2","kor_co_nm":"KEB하나은행","fin_prdt_nm":"e-플러스정기예금\n\n인터넷뱅킹,스마트폰뱅킹,콜센터","join_way":"인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리\n1개월초과 : 지급시점 해당기간 일반정기예금월이자지급식 기본금리 1/2","spcl_cnd":"하나 멤버스 앱 로그인 시 연0.1% 우대","join_deny":"1","join_member":"실명의 개인\n또는 개인사업자","etc_note":"1. 가입금액: 1만원이상 원단위가입가능","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201518"},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"4","kor_co_nm":"KEB하나은행","fin_prdt_nm":"행복knowhow 연금예금\n\n영업점","join_way":"영업점","mtrt_int":"1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리\n1개월초과 : 지급시점 해당기간 일반정기예금월이자지급식 기본금리 1/2","spcl_cnd":"없음","join_deny":"1","join_member":"실명의 개인\n또는 개인사업자","etc_note":"1. 가입금액 : 1백만원이상 원단위가입가능","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201518"},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"5","kor_co_nm":"KEB하나은행","fin_prdt_nm":"두리하나 정기예금\n\n영업점,인터넷뱅킹,스마트폰뱅킹","join_way":"영업점,인터넷,스마트폰","mtrt_int":"1개월이내 : 지급시점 해당기간 일반정기예금 월이자지급식 기본금리\n1개월초과 : 지급시점 해당기간 일반정기예금월이자지급식 기본금리 1/2","spcl_cnd":"최대 연0.3% 우대\n - 나도 하나 우대 연0.2%\n - 모두 하나 우대 연0.1%\n - 더불어 하나 우대 연0.1%\n - 두리하나 우대 연0.1%","join_deny":"1","join_member":"실명의 개인\n또는 개인사업자","etc_note":"1. 가입금액: 1백만원이상 3천만원이하\n2. 1인 최고가입한도 3천만원","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201518"}],"optionList":[{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001B","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001C","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001C","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001D","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.95,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001D","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001E","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.2,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001E","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320301","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320342","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320342","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320396","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1,"intr_rate2":1},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320396","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320396","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00320396","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3127","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3127","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3127","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3127","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3129","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3129","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3129","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"3129","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000845001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.42,"intr_rate2":1.62},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000845001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.46,"intr_rate2":1.66},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000845001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.48,"intr_rate2":1.68},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000845001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.5,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000958002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.16,"intr_rate2":1.41},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000996000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.12,"intr_rate2":1.32},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000996000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.16,"intr_rate2":1.36},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000996000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.18,"intr_rate2":1.38},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008000996000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.2,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511008001109001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.16,"intr_rate2":1.56},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511014000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.12,"intr_rate2":1.62},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511014000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.16,"intr_rate2":1.66},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511014000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.18,"intr_rate2":1.68},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10511014000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.2,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500130002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.7,"intr_rate2":0.7},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500130002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":0.9,"intr_rate2":0.9},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500290002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500290002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500290002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500290002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500400002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500400002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500460002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500490002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500490002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.7,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500500002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500500002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.2,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01030500500002","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.3,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300021000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.91,"intr_rate2":1.41},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300021000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.01,"intr_rate2":1.51},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300021000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.03,"intr_rate2":1.53},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300021000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":0.87,"intr_rate2":1.37},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300025000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.01,"intr_rate2":1.51},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300025000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.03,"intr_rate2":1.53},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300025000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":0.87,"intr_rate2":1.37},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300027000","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"12","intr_rate":1.21,"intr_rate2":1.41},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300027000","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"24","intr_rate":1.23,"intr_rate2":1.43},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300027000","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"36","intr_rate":1.07,"intr_rate2":1.27},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300028000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.01,"intr_rate2":1.51},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300028000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.11,"intr_rate2":1.61},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300028000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.13,"intr_rate2":1.63},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300028000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":0.97,"intr_rate2":1.47},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300029000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.01,"intr_rate2":1.51},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300029000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.03,"intr_rate2":1.53},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300029000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":0.87,"intr_rate2":1.37},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11300032000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.75,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000301","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.2,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000301","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.35,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000301","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.4,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000301","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.5,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000302","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.4,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000302","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.58,"intr_rate2":1.68},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000302","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.6,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"200000302","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.63,"intr_rate2":1.73},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.7,"intr_rate2":0.7},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.05,"intr_rate2":1.05},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0008-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.05,"intr_rate2":1.05},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0008-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0009-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0009-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0016-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0017-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.55,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0029-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0030-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0037-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.05,"intr_rate2":1.05},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0037-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0037-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0037-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0038-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0038-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0038-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0038-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0041-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0041-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0041-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0041-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.55,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.3,"intr_rate2":1.34},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.4,"intr_rate2":1.44},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.5,"intr_rate2":1.54},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0042-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.6,"intr_rate2":1.64},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-20-024-0046-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.7,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000087","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.05,"intr_rate2":1.05},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000087","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000087","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000093","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000093","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.35,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000101","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000101","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001049","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":2.25},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001057","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.05,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001057","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001057","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.3,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001105","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310073","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310073","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.25,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310073","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.3,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310108","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.25,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310108","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310121","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310121","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.35,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211310121","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10120102800011","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.9,"intr_rate2":0.9},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10120102800011","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10120104400021","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.3,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10120104400021","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.5,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05100","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.85,"intr_rate2":0.85},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05100","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":0.9,"intr_rate2":0.9},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05100","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":0.99,"intr_rate2":0.99},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05100","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.08,"intr_rate2":1.08},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05702","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.25,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05702","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.35,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05702","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.4,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"05705","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.6,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100072","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":0.9,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100072","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100072","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100072","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.2,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100209","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100209","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100226","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.1,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100226","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100293","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100297","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.15,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100297","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010300100312","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0037-15","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0037-15","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0037-15","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0121-28","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"12","intr_rate":1.22,"intr_rate2":1.42},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0121-28","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"24","intr_rate":1.23,"intr_rate2":1.43},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0121-28","intr_rate_type":"M","intr_rate_type_nm":"복리","save_trm":"36","intr_rate":1.26,"intr_rate2":1.46},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0134-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1,"intr_rate2":1.19},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0134-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.23},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0134-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.15,"intr_rate2":1.27},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0134-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.25,"intr_rate2":1.31},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0135-03","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1,"intr_rate2":1.44},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0135-03","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.48},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1,"intr_rate2":1},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.15,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-01","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-06","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1,"intr_rate2":1.34},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-06","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.38},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-06","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.15,"intr_rate2":1.42},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"200-0136-06","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.25,"intr_rate2":1.46},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-01225-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.21,"intr_rate2":1.51},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-01225-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.27,"intr_rate2":1.57},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1228-0006","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.28,"intr_rate2":1.73},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1228-0006","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.34,"intr_rate2":1.79},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1228-0006","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.37,"intr_rate2":1.82},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1228-0006","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1267-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.39,"intr_rate2":1.79},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1267-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.42,"intr_rate2":1.82},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1267-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.45,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1283-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.34,"intr_rate2":1.84},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1283-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.37,"intr_rate2":1.87},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1283-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1299-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.15,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1299-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.2,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1299-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.25,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1313-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.25,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1313-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.29,"intr_rate2":1.79},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-003-1313-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.33,"intr_rate2":1.83},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-059-1273-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.34,"intr_rate2":1.84},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-059-1273-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.37,"intr_rate2":1.87},{"dcls_month":"201609","fin_co_no":"0013175","fin_prdt_cd":"10-059-1273-0001","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"1","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"2","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"6","intr_rate":1.3,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"2","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.4,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"2","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.5,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"2","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.6,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"4","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"4","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"24","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"4","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"36","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0013909","fin_prdt_cd":"5","intr_rate_type":"S","intr_rate_type_nm":"단리","save_trm":"12","intr_rate":1.3,"intr_rate2":1.6}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd **	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
mtrt_int	만기 후 이자율
spcl_cnd	우대조건
join_deny	가입제한
Ex) 1:제한없음, 2:서민전용, 3:일부제한
join_member	가입대상
etc_note	기타 유의사항
max_limit	최고한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
intr_rate_type	저축 금리 유형
intr_rate_type_nm	저축 금리 유형명
save_trm	저축 기간 [단위: 개월]
intr_rate	저축 금리 [소수점 2자리]
intr_rate2	최고 우대금리 [소수점 2자리]
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
응답코드	No	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

## 적금 API 상세
요청URL
http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.{응답방식}

요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) savingProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1

예제 요청결과(XML)
<result>
<err_cd>000</err_cd>
<err_msg>정상</err_msg>
<total_count>113</total_count>
<max_page_no>2</max_page_no>
<now_page_no>1</now_page_no>
	<products>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001A</fin_prdt_cd>
<fin_prdt_nm>올포미 적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 신규 시 아래항목 충족 시 최고 연0.2%p
1. 올포미 신용 카드 보유 및 우리은행 결제계좌 지정 연 0.2%p
2. 우리은행 첫거래 고객 연 0.1%p
3. 급여/연금치에 고객 연0.1%p
4. 통신비/공과금 자동이체 고객 연0.1%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001B</fin_prdt_cd>
<fin_prdt_nm>우리웰리치100적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 신규 시 아래항목 충족 시 최고 연0.2%p
1. 연금이체 실적 보유 연 0.1%p
2. 우리웰리치100연금통장에서 자동이체 연 0.1%p
3. 우리신용/체크카드 보유 연0.1%p
4. 인터넷/스마트뱅킹으로 가입 연0.1%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001C</fin_prdt_cd>
<fin_prdt_nm>우리아이행복적금(12개월회전식)</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 아래 조건 충족 시 최고 연0.2%p
1. 부모와 자녀 동시가입 연0.1%p
2. 유후/아이행복 통장에서 자동이체등록 연0.1%p
3. 직전회전기간동안 100만원이상 납입 연0.1%p
4. 인터넷/스마트뱅킹으로 가입 연0.1%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001D</fin_prdt_cd>
<fin_prdt_nm>우리스마트폰적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 우리 꿈통장으로 연결하여 가입 시 연 0.2%p 우대금리 적용</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001E</fin_prdt_cd>
<fin_prdt_nm>위비꿀적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 최고 연 0.5%p
1. 우리신용카드 최초가입 ＆ 만기해지시까지 신용카드 보유 연 0.1%p
2. 우리카드 결제계좌 등록 ＆ 만기해지시까지 유지 연0.2%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001F</fin_prdt_cd>
<fin_prdt_nm>우리꿈적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 최고 연 0.6%p
1. 스마트뱅킹가입 연 0.2%p
2. 우리은행 또는 제휴업체 발급 금리우대쿠폰 등록 연 0.1%p
3. 친구번호 등록(연 0.1%p), 지인이 내 친구번호 등록(각 연 0.1%p), 최고 연 0.3%p 추가이율</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>.85</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.05</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001G</fin_prdt_cd>
<fin_prdt_nm>수요일이 즐거운 iTouch 문화적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 매주 수요일 입금 금액 연 0.3%p 적용</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001I</fin_prdt_cd>
<fin_prdt_nm>우리사랑플러스적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>1. 우대이자율 최고 연 0.5%p
   (순신규 / 공과금 및 관리비 자동이체 / ISA 가입 / 신용카드 가맹점 결제계좌/5인이상단체가입)
2. 특별이자율 최고 연 1.5%p[0.5%p 기부]
   (우리카드 연간 5백만원 이상 사용)</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001K</fin_prdt_cd>
<fin_prdt_nm>위비꿀모아정기적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>위비멤버스 서비스 가입 고객인 경우 적립액에 대하여 최대 1%의 위비꿀머니 적립
1. 중간적립 : 가입기간 중 매월 신규 적립액의          0.5%P
 2. 만기적립 : 만기해지 시 전체 누적 적립액의 0.5%P</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate></intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001L</fin_prdt_cd>
<fin_prdt_nm>톡톡쇼핑적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>최고 연 0.8%p
1. 금리우대쿠폰 연0.2%p
2. 위비톡 앱 설치 후 바로가입 메뉴 신규 연0.2%p
3. 우리카드결제실적 3개월 이상 보유 연0.2%p
4. 위비톡 매월 10회 이상 메시지 보내기 연 0.2%P</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001M</fin_prdt_cd>
<fin_prdt_nm>우리희망드림적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>만기해지 시 연 2%p 우대이율 적용</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>00266451</fin_prdt_cd>
<fin_prdt_nm>퍼스트가계적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹)</join_way>
<mtrt_int>만기 후 1개월: 0.7%
만기 후 1개월 초과 1년 이내: 0.3%
만기 후 1년 초과: 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200954</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>00266472</fin_prdt_cd>
<fin_prdt_nm>SC행복적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후 1개월: 0.7%
만기 후 1개월 초과 1년 이내: 0.3%
만기 후 1년 초과: 0.1%</mtrt_int>
<spcl_cnd>만기 시점을 기준으로 SC제일은행 입출금통장을 출금 계좌로 하여
SC행복적금으로 자동이체 5회 이상 실적이 있는 경우</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200954</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010006</fin_co_no>
<kor_co_nm>한국씨티은행</kor_co_nm>
<fin_prdt_cd>1800</fin_prdt_cd>
<fin_prdt_nm>정기적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기 후 1년 이내 : 만기일 당시 1년제 정기적금 이율의 1/2
만기 후 1년 초과 : 연 1.0%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201002</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010006</fin_co_no>
<kor_co_nm>한국씨티은행</kor_co_nm>
<fin_prdt_cd>1813</fin_prdt_cd>
<fin_prdt_nm>원더풀라이프적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기 후 1년 이내 : 만기일 당시 1년제 정기적금 이율의 1/2
만기 후 1년 초과 : 연 1.0%</mtrt_int>
<spcl_cnd>적금 가입 기간 중 은행이 고지한 Event 발생시 발생일로부터 추가우대이율 가산
(추가우대이율 최대적용범위는 0.5%)
(각 Event 항목별 연 0.1%[세전] 추가우대이율 적용)</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201002</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001000846001</fin_prdt_cd>
<fin_prdt_nm>내손안에 적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.3%
 - 최초가입 우대 : 0.2%
 - 비대면채널 거래실적 우대 : 0.1%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.46</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.48</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001000861003</fin_prdt_cd>
<fin_prdt_nm>DGB희망더하기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 2.0%
 - 자동이체 우대 : 2.0%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001000958002</fin_prdt_cd>
<fin_prdt_nm>최강삼성V9 적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.25%
 - 신규시 주택청약상품 보유 우대 : 0.1%
 - 신규시 공과금 2건이상 보유 우대 : 0.05%
 - 삼성라이온즈 정규시즌 우승 우대 : 0.05%
 - 삼성라이온즈 한국시리즈 우승 우대 : 0.1%
 - 만기시 공과금 2건이상 보유 우대 : 0.05%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.16</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001001046000</fin_prdt_cd>
<fin_prdt_nm>DGB여(女)러분적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.5%
 - 거래실적 우대 : 0.2%
 - 힐링 우대 : 0.2%
 - 상품 소개 우대 : 0.1%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.16</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.28</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001001058000</fin_prdt_cd>
<fin_prdt_nm>쓰담쓰담적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 1.4%
 - 첫예금 우대 : 0.1%
 - 패키지 우대 : 0.1%
 - 급여이체 우대 : 0.1%
 - 재예치 우대 : 0.3%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001001109001</fin_prdt_cd>
<fin_prdt_nm>ISA플러스 적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.4%
 - 신규시 ISA계좌 10만원 이상 보유 우대 : 0.1%
 - 신규시 공과금 3건이상 보유 우대 : 0.1%
 - 만기시 ISA계좌 10만원 이상 보유 우대 : 0.1%
 - 만기시 공과금 3건이상 보유 우대 : 0.1%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.16</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10527001001143000</fin_prdt_cd>
<fin_prdt_nm>청춘희망적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.5%
 - 신규시 주택청약상품 보유 우대 : 0.1%
 - 신용카드 실적 우대 : 0.1%
 - 만기시 목표 불입액 달성 우대 : 0.1%
 - 상품 소개 우대: 0.2%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.02</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.26</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.28</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10527036000001001</fin_prdt_cd>
<fin_prdt_nm>e-U(이유)적금</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.6%
 - 재예치 우대 : 0.2%
 - 비대면채널 거래실적 우대 : 0.1%
 - 3개월 평잔 30만원 보유  우대 : 0.1%
 - 주택청약상품 보유 우대 : 0.2%

※ 단위는 연%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.26</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.28</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400110001</fin_prdt_cd>
<fin_prdt_nm>갈맷길정기적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-걷기실천우대 : 0.05~0.20%
-인터넷가입우대: 0.10%
-장애인(걷기 동반자 1인): 0.10%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400210001</fin_prdt_cd>
<fin_prdt_nm>e-푸른바다 자유적금</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>우대조건 없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400240001</fin_prdt_cd>
<fin_prdt_nm>달콤한인생적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-자동재예치시: 0.10%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400270001</fin_prdt_cd>
<fin_prdt_nm>BNK희망가꾸기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-월간불입한도 금액내에서
우대이율 2.5%우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>2.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>2.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400340001</fin_prdt_cd>
<fin_prdt_nm>굿-초이스</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-스마트 우대: 0.10%
-팔로워 우대: 0.10%
-목돈마련 우대: 0.10%
-신용카드, 교차판매 우대: 0.70%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400360001</fin_prdt_cd>
<fin_prdt_nm>MySUM포인트적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>- 모바일 통장 자동이체 8회차 이상 불입 시: 0.10%
- 10만원 이상 스윙서비스 입금건수 6회 이상: 0.1%
- 모바일 통장 기중평잔 30만원 이상: 0.10%
- 당행 신용카드 및 롯데카드 결제 실적 우대: 0.10%
- 계좌이동 건수 2건 이상: 0.10%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01021400020002</fin_prdt_cd>
<fin_prdt_nm>가계우대정기적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>우대조건 없음.</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330018000</fin_prdt_cd>
<fin_prdt_nm>파워월복리적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>*최고 우대금리 : 0.7%
1.요구불 평잔 우대 : 0.2%
2. 자녀명의「KJB아이사랑월복리 적금」가입 실적 : 0.1%
3. 신용카드실적우대: 최대 0.2%
4. 급여통장보유: 0.1%
5. 가맹점 결제계좌우대: 0.1%</spcl_cnd>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330021000</fin_prdt_cd>
<fin_prdt_nm>스마트모아Dream정기적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>- 스마트뱅킹 1년제 정액적립식 가입 : 0.1%우대</spcl_cnd>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.9</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330023000</fin_prdt_cd>
<fin_prdt_nm>KJB주거래적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>* 최고 우대금리: 1.3%
- 신규고객 : 0.3%
- 당행대출보유 : 0.2%
- 만18세 이하 : 0.2%
- 자동이체실적우대 : 최고 0.4%
- 신용(체크)카드 사용우대 : 최고 0.3%</spcl_cnd>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330024000</fin_prdt_cd>
<fin_prdt_nm>꿈모아매일적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>*최고 우대금리 : 0.4%
1.「목표설정」우대금리 : 0.1%
2.「우등상」 우대금리 : 0.1%
3.「친구소개」우대금리 : 최대 0.2%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201122</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330025000</fin_prdt_cd>
<fin_prdt_nm>해피라이프_여행스케치적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>* 최고 우대금리 : 0.2%
- 신용(체크)카드 사용 : 최대 0.1%
- 비대면채널 이용우대 : 0.1%</spcl_cnd>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330027000</fin_prdt_cd>
<fin_prdt_nm>쏠쏠한마이쿨적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.9</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD1330024000</fin_prdt_cd>
<fin_prdt_nm>꿈모아매일적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>*최고 우대금리 : 0.4%
1.목표설정우대금리 : 0.1%
2. 우등상 우대금리 : 0.1%
3. 친구소개우대금리 : 최대 0.2%</spcl_cnd>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220000801</fin_prdt_cd>
<fin_prdt_nm>제주Tops허니문통장</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.6%p
①자동대체 등록 거래 0.1%p
②적금 계약기간 중 자녀 출산시 0.2%p
③적금 계약기간 중 결혼시 0.3%p
- 인터넷뱅킹 등 비대면매체 신규 우대 연 0.1%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220000901</fin_prdt_cd>
<fin_prdt_nm>만덕사랑적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 여성 최고  연 0.6%p(남성  연0.5%p) (항목별 연 0.1%p)
①매 저축 건별 자동대체 거래
②미성년자
③여성
④다자녀고객(3자녀 이상)
⑤자원봉사인증서 or 헌혈증서 지참
⑥복지단체후원금 or 기부금영수증 지참
⑦복지카드소지</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220001201</fin_prdt_cd>
<fin_prdt_nm>모아모아월복리적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.3%p(항목별 연 0.1%p)
①유동성예금 가입
②거치식,적립식예금, 방카,펀드 가입
③고객정보(CIF) 최초 등록
④자동대체 등록
- 추가우대(최고 0.1%p)
①탐나는J직장인통장 or 주거래통장 가입(기본요건충족)</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.9</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220001301</fin_prdt_cd>
<fin_prdt_nm>제주SOHO적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.3%p(항목별 연 0.1%p)
①탐나는 J 사업자통장 가입
②제주은행 계좌로 카드가맹점 대금 이체 실적 有
③종업원 급여이체
④비 활동성 고객
⑤SOHO 전용 패키지 가입</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220001701</fin_prdt_cd>
<fin_prdt_nm>새희망키움적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 3.0%p
①만기해지시 2.5%p
②유동성계좌에서 자동이체 등록시 0.5%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>230000202</fin_prdt_cd>
<fin_prdt_nm>사이버우대매일부금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.1%p
①탐나는 J 직장인통장 가입 고객이 기본우대 요건 충족후 이 상품 가입시 : 0.1%p
②탐나는 J 주거래통장 가입고객이 기본우대 요건 충족후 이 상품 가입시 : 0.1%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.75</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.85</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0004-0000</fin_prdt_cd>
<fin_prdt_nm>정기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0018-0000</fin_prdt_cd>
<fin_prdt_nm>JB 다이렉트적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 정기적금(자유적립식) 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 :
당행 계좌간 자동이체를 통해 이 예금으로 자동이체 된 금액에 0.1% 금리 우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.85</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.95</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0019-0000</fin_prdt_cd>
<fin_prdt_nm>JB 행복투어적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 0.3% 우대
- 첫회제외 모든회차 자동이체 불입시 연 0.1% 우대
- 인터넷뱅킹 계좌 신규시 연 0.1% 우대
- 만기까지 정상 불입시 연 0.1% 우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0020-0000</fin_prdt_cd>
<fin_prdt_nm>JB 행복결혼적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 0.3% 우대
- 첫회제외 모든회차 자동이체 불입시 연 0.1% 우대
- 인터넷뱅킹 계좌 신규시 연 0.1% 우대
- 만기까지 정상 불입시 연 0.1% 우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0021-0000</fin_prdt_cd>
<fin_prdt_nm>JB 행복드림적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 정기적금(자유적립식) 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 3.0% 우대(서류제출시)
- 기초생활수급자,        - 한부모 가정
- 소녀소녀가장세대주   - 근로장려금 수급자
- 다문화가정
- 차상위계층이하 만65세이상 고령자</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0022-0000</fin_prdt_cd>
<fin_prdt_nm>JB 온과빛함께적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대:최고 연0.8%우대 1.전북은행최초거래시 연0.2% 우대, 2.만18세이하가입시 연0.2%우대, 3.자동이체로납입시(계약기간1/2이상) 연0.2%우대, 4.만기전6개월내신용카드사용금액에 따라 연0.1%~0.2%우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0023-0000</fin_prdt_cd>
<fin_prdt_nm>JB퍼스트주거래적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대:최고연0.4%우대1.JB퍼스트통장가입후적금신규시연0.1%우대,2.기간이3년이상인경우연0.1%우대,3.기간중3개월이상펀드상품보유시연0.1%우대,4.만기일최근6개월내카드매입실적이50만원이상인경우연0.1%우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0001-0000</fin_prdt_cd>
<fin_prdt_nm>상호부금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0005-0000</fin_prdt_cd>
<fin_prdt_nm>시장금리부 상호부금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0007-0000</fin_prdt_cd>
<fin_prdt_nm>인터넷상호부금</fin_prdt_nm>
<join_way>인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0007-0021</fin_prdt_cd>
<fin_prdt_nm>스마트상호부금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 0.3% 우대
- 가입시 JB플러스급여통장 보유시 연 0.1% 우대
- 최근 1개월이내 신용카드 사용고객 연 0.1% 우대
- 상호부금 가입기간 1년이상인 경우 연 0.1% 우대</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000111</fin_prdt_cd>
<fin_prdt_nm>행복드림적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷적립식예금신규가입우대: 0.05%
▷신용카드신규가입 우대: 0.10%
▷고액적립액우대이율:30만원 이상: 0.05%, 60만원 이상: 0.10%
▷자동이체 우대이율: 0.05%
▷행복 우대이율:최대 0.15%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000112</fin_prdt_cd>
<fin_prdt_nm>행복드림여행적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷자동이체 우대금리
-정기적립식: 전체 적립회수의 2/3이상을 월10만원 이상 자동이체 입금시 0.05%
-자유적립식: 창구외 채널(인터넷뱅킹, 텔레뱅킹 등)로 10만원 이상 입금시 0.05%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.15</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000114</fin_prdt_cd>
<fin_prdt_nm>월복리솔솔적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>※아래 조건 충족시 최대 0.20% 우대금리 지급
▷예금 가입전 당행 거래가족수에 따른 우대금리 최고 0.10%, 직장인우대통장 가입 0.05%, 자녀명의로 아이드림자유적금 가입한 경우, 공과금자동이체 등록고객 각 0.05%
▷예금 가입전 3개월 이내 당행 신용(체크)카드 10만원 이상 이용시 0.05%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000118</fin_prdt_cd>
<fin_prdt_nm>희망모아적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷정기적립식의 경우, 이 예금을 전회차 납입하고 만기해지하는 경우 우대금리 3.00%
▷자유적립식의 경우 만기해지시 우대금리 2.00%
※특별중도해지 우대 : 가입후 6개월 이상 경과한 계좌로써, 가입기간 중 주택구입(임차), 결혼, 출산, 입원, 입학시</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000120</fin_prdt_cd>
<fin_prdt_nm>탄탄성공적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷입출금예금평잔에 따른 우대금리 0.10%~0.15%
▷퇴직연금가입시 우대금리 0.05%
▷월부금 2/3 이상 자동이체 입금시 우대금리 0.05%
▷이노비즈(Inno-Biz) 선정 사업자 우대금리 0.05%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000122</fin_prdt_cd>
<fin_prdt_nm>아이드림자유적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷출생년도 입금분 0.05%
▷입학년도 입금분(유치원, 초,중,고) 0.05%
▷설날, 추석, 생일 이후 5영업일 이내 입금분 0.05%
▷자동재예치 우대 0.05%
▷창구거래 외 입금 0.05%
▷예금주 또는 부모가 경남(울산)사랑통장 주거래고객인 경우 0.05%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000124</fin_prdt_cd>
<fin_prdt_nm>스마트자유적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷추천번호 입력 우대금리: 추천시 0.10%, 최대 3회 0.30% 제공</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000131</fin_prdt_cd>
<fin_prdt_nm>e-money 자유적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷특정입출금상품에서 인출하여 신규시 우대금리
  - 직장인우대통장: 0.15%
  - 공직자우대통장: 0.15%
▷월부금 30만원 이상 자동이체 입금시 우대금리: 0.10%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000158</fin_prdt_cd>
<fin_prdt_nm>상조적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷차상위계층 이하 65세 이상 고령자가 가입할 경우 연 1.00%의 우대금리 지급
▷계약기간 중 본인, 배우자, 본인 및 배우자의 직계존비속 상사시 연 0.10% 우대금리</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001044</fin_prdt_cd>
<fin_prdt_nm>캠퍼스드림적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷전회차를 납입하고 만기해지하는 경우 우대금리 1.50%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001053</fin_prdt_cd>
<fin_prdt_nm>카드플러스적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷신용카드결제증가액 우대이율: 최대 2.50%
▷거래실적 우대이율: 최대 0.10%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001058</fin_prdt_cd>
<fin_prdt_nm>에메랄드적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷인터넷뱅킹, 스마트뱅킹, 고객센터를 통해 신규시 0.05%
▷아래 항목별 0.10%를 우대금리로 제공하며 최대 0.20%
- 가입자의 결혼, 임신, 출산, 가입자 자녀의 결혼, 손자 출생
▷신규가입고객이 다른 고객 1인을 소개시 0.05% 우대금리 제공하며 최대 0.10%까지 인정</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001070</fin_prdt_cd>
<fin_prdt_nm>BNK연리지적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷BNK투자증권,BNK캐피탈,BNK저축은행거래 여부에 따른 우대금리0.20%~0.30%
▷첫거래자 0.10%
▷계좌이동서비스로자동이체변경0.10%
▷평생통장자동이체0.10%
▷연결고리0.10%
▷종이통장미발행0.05%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.15</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210078</fin_prdt_cd>
<fin_prdt_nm>新서민섬김통장 가계우대정기적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.5%p
1. 신규고객 우대금리 : 연 0.1%p
2. 거래심화 우대금리 : 연 0.4%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210082</fin_prdt_cd>
<fin_prdt_nm>IBK국군희망준비적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.20%p
1. 급여이체우대 : 연 0.20%p
2. 신용(체크)카드 우대 : 최고 연 0.20%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate></intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>5.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>5.25</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>3.8</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210095</fin_prdt_cd>
<fin_prdt_nm>IBK사랑나눔적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 1.80%p
(계약기간별 고시금리와 동일한 금리를 우대금리로 제공)</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210097</fin_prdt_cd>
<fin_prdt_nm>IBK평생든든자유적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.3%p(1~4번 각 연0.1%p)
1. 평생설계저금통서비스 납입 실적
2. 급여, 4대연금, 보훈, 장해, 기초(노령)연금
3. 당행 연금관련상품의 가입실적
4. 비대면채널을 통해 이 상품을 가입했을 경우</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.25</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210102</fin_prdt_cd>
<fin_prdt_nm>IBK평생한가족통장 자유적립식</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.4%p
1. 고객별 우대금리: 연 0.1%p
2. 주거래 우대금리: 연 0.3%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210103</fin_prdt_cd>
<fin_prdt_nm>IBK평생한가족통장 정액적립식</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.4%p
1. 고객별 우대금리: 연 0.1%p
2. 주거래 우대금리: 연 0.3%p</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010028</fin_co_no>
<kor_co_nm>수협은행</kor_co_nm>
<fin_prdt_cd>10140108700011</fin_prdt_cd>
<fin_prdt_nm>더플러스정액적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>* 1년이하
정기적금 만기일 계약(해당)기간 약정금리 1/2
* 1년초과
만기후 해당구간시작일 보통예금 금리</mtrt_int>
<spcl_cnd>최고0.9%우대금리
-첫거래고객최대0.4%
-2인이상동시가입0.1%
-급여이체0.2%
-카드거래최대0.3%
-정기예금0.1%
-대출거래0.1%
-정액적립식거래0.2%
-인터넷뱅킹적금신규0.1%
-아파트관리비자동이체0.2%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201530</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010028</fin_co_no>
<kor_co_nm>수협은행</kor_co_nm>
<fin_prdt_cd>10141109800011</fin_prdt_cd>
<fin_prdt_nm>SH월복리자유적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>* 1년이하
상호부금 만기일 계약(해당)기간 약정금리 1/2
* 1년초과
만기후 해당구간시작일 보통예금 금리</mtrt_int>
<spcl_cnd>최고0.7%우대금리
-첫거래고객0.3%
-카드거래고객최대0.3%
-복수거래0.1%
-요구불거래최대0.2%
-인터넷뱅킹고객0.1%
-자동이체신청0.1%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201530</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010028</fin_co_no>
<kor_co_nm>수협은행</kor_co_nm>
<fin_prdt_cd>10141110500011</fin_prdt_cd>
<fin_prdt_nm>SH100세만기자유적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>* 1년이하
상호부금 만기일 계약(해당)기간 약정금리 1/2
* 1년초과
만기후 해당구간시작일 보통예금 금리</mtrt_int>
<spcl_cnd>최고0.3%우대금리
-계좌이동제이동고객0.1%
-복수거래고객0.1%
-자동이체고객0.1%
-SH평생주거래통장고객0.1%
-칠순팔순고객0.1%
서민고객0.1%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201530</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.65</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03100</fin_prdt_cd>
<fin_prdt_nm>정기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>지급일 현재 고시된 일반정기예금 만기후 이자율 적용</mtrt_int>
<spcl_cnd>해당없음</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.25</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.35</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03202</fin_prdt_cd>
<fin_prdt_nm>KDBdream 자유적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>*만기후 1년 이내:
만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2
* 만기후 1년 초과:
만기일 현재 보통예금 이자율</mtrt_int>
<spcl_cnd>KDBdream Account 계좌에서 자동이체방법으로 납입하는 경우, 연 0.10% 가산</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.49</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.59</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.74</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03204</fin_prdt_cd>
<fin_prdt_nm>KDB Hi 자유적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>*만기후 1년 이내:
만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2
* 만기후 1년 초과:
만기일 현재 보통예금 이자율</mtrt_int>
<spcl_cnd>KDB Hi 입출금통장에서 자동이체방법으로 납입하는 경우, 연 0.10% 가산</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.78</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.63</intr_rate>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.53</intr_rate>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03205</fin_prdt_cd>
<fin_prdt_nm>주거래플러스 적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>*만기후 1년 이내:
만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2
* 만기후 1년 초과:
만기일 현재 보통예금 이자율</mtrt_int>
<spcl_cnd>* 온라인 가입 : 0.1%
* 산업은행 정기예금 또는 산금채 가입 : 0.1%
* 체크카드 사용실적 또는 자동이체 : 0.5%
* 입금 실적(월 건당 50만원 이상) : 0.3%
* 펀드 자동이체 : 0.2%</spcl_cnd>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<sav<result>
<err_cd>000</err_cd>
<err_msg>정상</err_msg>
<total_count>113</total_count>
<max_page_no>2</max_page_no>
<now_page_no>1</now_page_no>
	<products>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001A</fin_prdt_cd>
<fin_prdt_nm>올포미 적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 신규 시 아래항목 충족 시 최고 연0.2%p
1. 올포미 신용 카드 보유 및 우리은행 결제계좌 지정 연 0.2%p
2. 우리은행 첫거래 고객 연 0.1%p
3. 급여/연금치에 고객 연0.1%p
4. 통신비/공과금 자동이체 고객 연0.1%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인,개인사업자</join_member>
<etc_note>해당없음</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>1.55</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001B</fin_prdt_cd>
<fin_prdt_nm>우리웰리치100적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 신규 시 아래항목 충족 시 최고 연0.2%p
1. 연금이체 실적 보유 연 0.1%p
2. 우리웰리치100연금통장에서 자동이체 연 0.1%p
3. 우리신용/체크카드 보유 연0.1%p
4. 인터넷/스마트뱅킹으로 가입 연0.1%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001C</fin_prdt_cd>
<fin_prdt_nm>우리아이행복적금(12개월회전식)</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 아래 조건 충족 시 최고 연0.2%p
1. 부모와 자녀 동시가입 연0.1%p
2. 유후/아이행복 통장에서 자동이체등록 연0.1%p
3. 직전회전기간동안 100만원이상 납입 연0.1%p
4. 인터넷/스마트뱅킹으로 가입 연0.1%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001D</fin_prdt_cd>
<fin_prdt_nm>우리스마트폰적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 우리 꿈통장으로 연결하여 가입 시 연 0.2%p 우대금리 적용</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001E</fin_prdt_cd>
<fin_prdt_nm>위비꿀적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 최고 연 0.5%p
1. 우리신용카드 최초가입 ＆ 만기해지시까지 신용카드 보유 연 0.1%p
2. 우리카드 결제계좌 등록 ＆ 만기해지시까지 유지 연0.2%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001F</fin_prdt_cd>
<fin_prdt_nm>우리꿈적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 최고 연 0.6%p
1. 스마트뱅킹가입 연 0.2%p
2. 우리은행 또는 제휴업체 발급 금리우대쿠폰 등록 연 0.1%p
3. 친구번호 등록(연 0.1%p), 지인이 내 친구번호 등록(각 연 0.1%p), 최고 연 0.3%p 추가이율</spcl_cnd>
<join_deny>1</join_deny>
<join_member>국내거주자인 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>.85</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>2.15</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.05</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001G</fin_prdt_cd>
<fin_prdt_nm>수요일이 즐거운 iTouch 문화적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>- 매주 수요일 입금 금액 연 0.3%p 적용</spcl_cnd>
<join_deny>1</join_deny>
<join_member>국내거주자인 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001I</fin_prdt_cd>
<fin_prdt_nm>우리사랑플러스적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>1. 우대이자율 최고 연 0.5%p
   (순신규 / 공과금 및 관리비 자동이체 / ISA 가입 / 신용카드 가맹점 결제계좌/5인이상단체가입)
2. 특별이자율 최고 연 1.5%p[0.5%p 기부]
   (우리카드 연간 5백만원 이상 사용)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>3.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001K</fin_prdt_cd>
<fin_prdt_nm>위비꿀모아정기적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>위비멤버스 서비스 가입 고객인 경우 적립액에 대하여 최대 1%의 위비꿀머니 적립
1. 중간적립 : 가입기간 중 매월 신규 적립액의          0.5%P
 2. 만기적립 : 만기해지 시 전체 누적 적립액의 0.5%P</spcl_cnd>
<join_deny>1</join_deny>
<join_member>14세 이상 실명의 개인</join_member>
<etc_note>해당없음</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2></intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate></intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001L</fin_prdt_cd>
<fin_prdt_nm>톡톡쇼핑적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>최고 연 0.8%p
1. 금리우대쿠폰 연0.2%p
2. 위비톡 앱 설치 후 바로가입 메뉴 신규 연0.2%p
3. 우리카드결제실적 3개월 이상 보유 연0.2%p
4. 위비톡 매월 10회 이상 메시지 보내기 연 0.2%P</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인 및 개인사업자</join_member>
<etc_note>해당없음</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>WR0001M</fin_prdt_cd>
<fin_prdt_nm>우리희망드림적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기적금 금리</mtrt_int>
<spcl_cnd>만기해지 시 연 2%p 우대이율 적용</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자, 만 65세 이상 차상위계층, 소년소녀가장, 결혼이민자, 북한 이탈주민, 근로장려금수급자</join_member>
<etc_note>기초생활수급자, 만 65세 이상 차상위계층, 소년소녀가장, 결혼이민자, 북한 이탈주민, 근로장려금 수급자
(단, 1인 1계좌에 한하여 가입 가능)
주1)결혼이민자란 외국국적을 가진자가 대한민국 국적을 가진자와 결혼한 사람을 의미</etc_note>
<max_limit>200000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201049</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2</intr_rate>
<intr_rate2>4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2</intr_rate>
<intr_rate2>4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>00266451</fin_prdt_cd>
<fin_prdt_nm>퍼스트가계적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹)</join_way>
<mtrt_int>만기 후 1개월: 0.7%
만기 후 1개월 초과 1년 이내: 0.3%
만기 후 1년 초과: 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200954</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>00266472</fin_prdt_cd>
<fin_prdt_nm>SC행복적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후 1개월: 0.7%
만기 후 1개월 초과 1년 이내: 0.3%
만기 후 1년 초과: 0.1%</mtrt_int>
<spcl_cnd>만기 시점을 기준으로 SC제일은행 입출금통장을 출금 계좌로 하여
SC행복적금으로 자동이체 5회 이상 실적이 있는 경우</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자, 소년소녀가장, 북한이탈주민, 결혼이민자, 근로장려금수급자, 한부모가족지원 보호대상자, 차상위계층 대상자(만 65세이상)</join_member>
<etc_note>1. 1인당 가입한도 : 월 30만원
2. 월 적립액은 예금을 가입하는 때에 정하며, 계약기간 중에 변경할 수 없음
3. 가입 시 가입자격 증빙을 위한 증빙서류 징구</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200954</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3.5</intr_rate>
<intr_rate2>3.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010006</fin_co_no>
<kor_co_nm>한국씨티은행</kor_co_nm>
<fin_prdt_cd>1800</fin_prdt_cd>
<fin_prdt_nm>정기적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기 후 1년 이내 : 만기일 당시 1년제 정기적금 이율의 1/2
만기 후 1년 초과 : 연 1.0%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입기간은 6개월 이상 5년 이하 월단위 가입 가능 (3년을 초과하여 계약하고자 하는 경우 5년으로 함)</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201002</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1</intr_rate>
<intr_rate2>1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010006</fin_co_no>
<kor_co_nm>한국씨티은행</kor_co_nm>
<fin_prdt_cd>1813</fin_prdt_cd>
<fin_prdt_nm>원더풀라이프적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기 후 1년 이내 : 만기일 당시 1년제 정기적금 이율의 1/2
만기 후 1년 초과 : 연 1.0%</mtrt_int>
<spcl_cnd>적금 가입 기간 중 은행이 고지한 Event 발생시 발생일로부터 추가우대이율 가산
(추가우대이율 최대적용범위는 0.5%)
(각 Event 항목별 연 0.1%[세전] 추가우대이율 적용)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입기간은 1년 이상 3년 이하 월단위 가입 가능
2. 가입금액은 1만원 이상 최고 1천만원 이내(단, 매월 1천만원 범위 내)이며, 계약기간의 3/4이 경과한 경우 적립할 수 있는 금액의 합계는 그 이전 적립금액의 50%를 초과할 수 없음 (매월의 기준은 1일부터 말일을 의미)</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201002</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001000846001</fin_prdt_cd>
<fin_prdt_nm>내손안에 적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.3%
 - 최초가입 우대 : 0.2%
 - 비대면채널 거래실적 우대 : 0.1%

※ 단위는 연%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1계좌당 가입한도 : 월 100만원 (최저 10만원 이상)
2. 스마트폰 가입 전용상품
3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.46</intr_rate>
<intr_rate2>1.76</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.48</intr_rate>
<intr_rate2>1.78</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001000861003</fin_prdt_cd>
<fin_prdt_nm>DGB희망더하기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 2.0%
 - 자동이체 우대 : 2.0%

※ 단위는 연%p</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자, 등록장애인(1급 ~ 3급), 소년소녀가장, 결혼이민여성, 근로장려금수급자, 한부모가족지원 보호대상자, 차상위계층(단, 만65세이상 고령자에 한함)</join_member>
<etc_note>1. 1계좌당 가입한도 : 월 30만원 (최저 1만원 이상)
2. 저축기간 중 적용금리 변동 : 고시금리 기준 변동금리 적용</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3</intr_rate>
<intr_rate2>5</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001000958002</fin_prdt_cd>
<fin_prdt_nm>최강삼성V9 적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.25%
 - 신규시 주택청약상품 보유 우대 : 0.1%
 - 신규시 공과금 2건이상 보유 우대 : 0.05%
 - 삼성라이온즈 정규시즌 우승 우대 : 0.05%
 - 삼성라이온즈 한국시리즈 우승 우대 : 0.1%
 - 만기시 공과금 2건이상 보유 우대 : 0.05%

※ 단위는 연%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1계좌당 가입최저한도 : 10만원
2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.16</intr_rate>
<intr_rate2>1.56</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001001046000</fin_prdt_cd>
<fin_prdt_nm>DGB여(女)러분적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.5%
 - 거래실적 우대 : 0.2%
 - 힐링 우대 : 0.2%
 - 상품 소개 우대 : 0.1%

※ 단위는 연%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>만18세 이상의 여성</join_member>
<etc_note>1. 1계좌당 가입한도 : 월 50만원 (최저 10만원 이상)
2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.16</intr_rate>
<intr_rate2>1.66</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.28</intr_rate>
<intr_rate2>1.78</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001001058000</fin_prdt_cd>
<fin_prdt_nm>쓰담쓰담적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 1.4%
 - 첫예금 우대 : 0.1%
 - 패키지 우대 : 0.1%
 - 급여이체 우대 : 0.1%
 - 재예치 우대 : 0.3%

※ 단위는 연%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1계좌당 가입한도 : 월 100만원 (최저 10만원 이상)
2. 저축기간 중 적용금리 변동 : 고시금리 기준 변동금리 적용</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>2.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>2.75</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10521001001109001</fin_prdt_cd>
<fin_prdt_nm>ISA플러스 적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.4%
 - 신규시 ISA계좌 10만원 이상 보유 우대 : 0.1%
 - 신규시 공과금 3건이상 보유 우대 : 0.1%
 - 만기시 ISA계좌 10만원 이상 보유 우대 : 0.1%
 - 만기시 공과금 3건이상 보유 우대 : 0.1%

※ 단위는 연%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1계좌당 가입최저한도 : 10만원
2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.16</intr_rate>
<intr_rate2>1.46</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10527001001143000</fin_prdt_cd>
<fin_prdt_nm>청춘희망적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.5%
 - 신규시 주택청약상품 보유 우대 : 0.1%
 - 신용카드 실적 우대 : 0.1%
 - 만기시 목표 불입액 달성 우대 : 0.1%
 - 상품 소개 우대: 0.2%

※ 단위는 연%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>만19세 이상 만40세 이하 개인</join_member>
<etc_note>1. 1계좌당 가입한도 : 월 100만원 (최저 1만원 이상)
2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.02</intr_rate>
<intr_rate2>1.52</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.26</intr_rate>
<intr_rate2>1.76</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.28</intr_rate>
<intr_rate2>1.78</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010016</fin_co_no>
<kor_co_nm>대구은행</kor_co_nm>
<fin_prdt_cd>10527036000001001</fin_prdt_cd>
<fin_prdt_nm>e-U(이유)적금</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>만기 후 1개월 미만 경과: 약정이자율 x 50%
만기 후 3개월 미만 경과: 약정이자율 x 25%
만기 후 3개월 이상 경과: 약정이자율 x 10%</mtrt_int>
<spcl_cnd>* 최고우대금리 : 0.6%
 - 재예치 우대 : 0.2%
 - 비대면채널 거래실적 우대 : 0.1%
 - 3개월 평잔 30만원 보유  우대 : 0.1%
 - 주택청약상품 보유 우대 : 0.2%

※ 단위는 연%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1계좌당 가입한도 : 월 200만원 (최저 10만원 이상)
2. 인터넷뱅킹 및 스마트폰 가입 전용상품
3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용</etc_note>
<max_limit>2000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201130</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.26</intr_rate>
<intr_rate2>1.86</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.28</intr_rate>
<intr_rate2>1.88</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400110001</fin_prdt_cd>
<fin_prdt_nm>갈맷길정기적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-걷기실천우대 : 0.05~0.20%
-인터넷가입우대: 0.10%
-장애인(걷기 동반자 1인): 0.10%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>제한없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400210001</fin_prdt_cd>
<fin_prdt_nm>e-푸른바다 자유적금</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>우대조건 없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1.1인당 가입한도: 월 500만원</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400240001</fin_prdt_cd>
<fin_prdt_nm>달콤한인생적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-자동재예치시: 0.10%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>제한없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400270001</fin_prdt_cd>
<fin_prdt_nm>BNK희망가꾸기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-월간불입한도 금액내에서
우대이율 2.5%우대</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급권자 본인(독거노인포함),
소년소녀가장 본인, 북한이탈주민 본인,
다문화가정(결혼이민자 본인,그 배우자 및 자녀),
한부모가정(한부모가족지원법에 따른 지원대상),
장애인</join_member>
<etc_note>1.1인당 가입한도: 월 25만원</etc_note>
<max_limit>250000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2</intr_rate>
<intr_rate2>4.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>2.2</intr_rate>
<intr_rate2>4.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>2.4</intr_rate>
<intr_rate2>4.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400340001</fin_prdt_cd>
<fin_prdt_nm>굿-초이스</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>-스마트 우대: 0.10%
-팔로워 우대: 0.10%
-목돈마련 우대: 0.10%
-신용카드, 교차판매 우대: 0.70%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1인당 가입한도: 월 100만원</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01020400360001</fin_prdt_cd>
<fin_prdt_nm>MySUM포인트적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>- 모바일 통장 자동이체 8회차 이상 불입 시: 0.10%
- 10만원 이상 스윙서비스 입금건수 6회 이상: 0.1%
- 모바일 통장 기중평잔 30만원 이상: 0.10%
- 당행 신용카드 및 롯데카드 결제 실적 우대: 0.10%
- 계좌이동 건수 2건 이상: 0.10%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1인당 가입한도: 월 100만원
2. 가입채널: 당행 썸뱅크(모바일) 통해 가입가능
3. MySUM모바일통장과 패키지로 개설</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010017</fin_co_no>
<kor_co_nm>부산은행</kor_co_nm>
<fin_prdt_cd>01021400020002</fin_prdt_cd>
<fin_prdt_nm>가계우대정기적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%
- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%</mtrt_int>
<spcl_cnd>우대조건 없음.</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1.1인당 가입한도: 월 270만원(총 1억원이내)</etc_note>
<max_limit>2700000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201338</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330018000</fin_prdt_cd>
<fin_prdt_nm>파워월복리적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>*최고 우대금리 : 0.7%
1.요구불 평잔 우대 : 0.2%
2. 자녀명의「KJB아이사랑월복리 적금」가입 실적 : 0.1%
3. 신용카드실적우대: 최대 0.2%
4. 급여통장보유: 0.1%
5. 가맹점 결제계좌우대: 0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인</join_member>
<etc_note>1. 가입금액 : 1만원 이상 ~5천만원 이하
2. 분기당 납입금액 : 1천만원 이하
3. 자유적립식</etc_note>
<max_limit>50000000</max_limit>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330021000</fin_prdt_cd>
<fin_prdt_nm>스마트모아Dream정기적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>- 스마트뱅킹 1년제 정액적립식 가입 : 0.1%우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인</join_member>
<etc_note>1. 월입금한도 : 매회 1만원 ~ 월 1천만원 이하
2. 비대면실명확인 고객의 경우 정액적립식만 선택가능</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.9</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330023000</fin_prdt_cd>
<fin_prdt_nm>KJB주거래적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>* 최고 우대금리: 1.3%
- 신규고객 : 0.3%
- 당행대출보유 : 0.2%
- 만18세 이하 : 0.2%
- 자동이체실적우대 : 최고 0.4%
- 신용(체크)카드 사용우대 : 최고 0.3%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인</join_member>
<etc_note>1. 1인당 가입한도 : 월 50만원
2. 1인 1계좌
3. 정액적립식</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>2.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2.7</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330024000</fin_prdt_cd>
<fin_prdt_nm>꿈모아매일적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>*최고 우대금리 : 0.4%
1.「목표설정」우대금리 : 0.1%
2.「우등상」 우대금리 : 0.1%
3.「친구소개」우대금리 : 최대 0.2%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인</join_member>
<etc_note>1. 가입금액 : 1만원 이상
2. 납입한도 : 월 100만원 이내
3. 자유적립식</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201122</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330025000</fin_prdt_cd>
<fin_prdt_nm>해피라이프_여행스케치적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>* 최고 우대금리 : 0.2%
- 신용(체크)카드 사용 : 최대 0.1%
- 비대면채널 이용우대 : 0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입금액 : 월 5만원 이상 ~10백만원 이하
2. 정액적립식</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD11330027000</fin_prdt_cd>
<fin_prdt_nm>쏠쏠한마이쿨적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>3</join_deny>
<join_member>가입일 기준 최근 1년간 당행 거치식예금, 적</join_member>
<etc_note>1. 가입금액 : 월 1만원 이상 ~ 100만원 이하
2. 1인 1계좌
3. 정액적립식</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.9</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010019</fin_co_no>
<kor_co_nm>광주은행</kor_co_nm>
<fin_prdt_cd>TD1330024000</fin_prdt_cd>
<fin_prdt_nm>꿈모아매일적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>-만기후 1개월 이내
: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2
-만기후 1개월 초과
:0.10%</mtrt_int>
<spcl_cnd>*최고 우대금리 : 0.4%
1.목표설정우대금리 : 0.1%
2. 우등상 우대금리 : 0.1%
3. 친구소개우대금리 : 최대 0.2%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인</join_member>
<etc_note>1. 가입금액: 1만원 이상
2. 납입한도 : 월100만원 이내
3. 자유적립식</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261232</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220000801</fin_prdt_cd>
<fin_prdt_nm>제주Tops허니문통장</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.6%p
①자동대체 등록 거래 0.1%p
②적금 계약기간 중 자녀 출산시 0.2%p
③적금 계약기간 중 결혼시 0.3%p
- 인터넷뱅킹 등 비대면매체 신규 우대 연 0.1%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>미혼 및 결혼한지 3년 이내의 개인</join_member>
<etc_note>월적립금 최소 10만원 이상~ 최대 300만원 이하</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220000901</fin_prdt_cd>
<fin_prdt_nm>만덕사랑적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 여성 최고  연 0.6%p(남성  연0.5%p) (항목별 연 0.1%p)
①매 저축 건별 자동대체 거래
②미성년자
③여성
④다자녀고객(3자녀 이상)
⑤자원봉사인증서 or 헌혈증서 지참
⑥복지단체후원금 or 기부금영수증 지참
⑦복지카드소지</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>자유적립식인 경우 2회차 이후 월1천만원 이내</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220001201</fin_prdt_cd>
<fin_prdt_nm>모아모아월복리적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.3%p(항목별 연 0.1%p)
①유동성예금 가입
②거치식,적립식예금, 방카,펀드 가입
③고객정보(CIF) 최초 등록
④자동대체 등록
- 추가우대(최고 0.1%p)
①탐나는J직장인통장 or 주거래통장 가입(기본요건충족)</spcl_cnd>
<join_deny>3</join_deny>
<join_member>개인 및 개인사업자</join_member>
<etc_note>1. 1인 1계좌
2. 가입금액 : 매 입금건별 1만원 이상 분기별 5백만원 이하</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.9</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220001301</fin_prdt_cd>
<fin_prdt_nm>제주SOHO적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.3%p(항목별 연 0.1%p)
①탐나는 J 사업자통장 가입
②제주은행 계좌로 카드가맹점 대금 이체 실적 有
③종업원 급여이체
④비 활동성 고객
⑤SOHO 전용 패키지 가입</spcl_cnd>
<join_deny>3</join_deny>
<join_member>개인사업자, 법인, 임의단체</join_member>
<etc_note>가입금액 : 1만원 이상</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>220001701</fin_prdt_cd>
<fin_prdt_nm>새희망키움적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 3.0%p
①만기해지시 2.5%p
②유동성계좌에서 자동이체 등록시 0.5%p</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자,소년소녀가장,북한이탈주민,결혼이민자,근로장려금수급자,한부모가족지원보호대상자,만65세이상차상위계층</join_member>
<etc_note>1인당 가입한도: 월 20만원</etc_note>
<max_limit>200000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3</intr_rate>
<intr_rate2>6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010020</fin_co_no>
<kor_co_nm>제주은행</kor_co_nm>
<fin_prdt_cd>230000202</fin_prdt_cd>
<fin_prdt_nm>사이버우대매일부금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%
- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%
- 만기후 3개월 초과 : 0.25%</mtrt_int>
<spcl_cnd>- 교차우대 최고 연 0.1%p
①탐나는 J 직장인통장 가입 고객이 기본우대 요건 충족후 이 상품 가입시 : 0.1%p
②탐나는 J 주거래통장 가입고객이 기본우대 요건 충족후 이 상품 가입시 : 0.1%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>개인 및 개인사업자</join_member>
<etc_note>"해당 없음"</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200957</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.75</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.85</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0004-0000</fin_prdt_cd>
<fin_prdt_nm>정기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 월 불입한도 1천만원 이내
2. 만기직전 1개월간 적립금액 합계는 그 이전 기간동안 적립액을 초과할수 없음</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0018-0000</fin_prdt_cd>
<fin_prdt_nm>JB 다이렉트적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 정기적금(자유적립식) 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 :
당행 계좌간 자동이체를 통해 이 예금으로 자동이체 된 금액에 0.1% 금리 우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인
(임의단체 제외)</join_member>
<etc_note>1. 초회불입금 1만원이상, 1인당 월별 최고 1천만원이내
2. 만기직전 1개월간 적립합계는 이전기간 적립금액을 초과할 수 없음
3. 인터넷뱅킹/스마트폰뱅킹 가입상품</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.85</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.95</intr_rate>
<intr_rate2>2.04</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0019-0000</fin_prdt_cd>
<fin_prdt_nm>JB 행복투어적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 0.3% 우대
- 첫회제외 모든회차 자동이체 불입시 연 0.1% 우대
- 인터넷뱅킹 계좌 신규시 연 0.1% 우대
- 만기까지 정상 불입시 연 0.1% 우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>월 적립액 5만원이상 1천만원이하</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0020-0000</fin_prdt_cd>
<fin_prdt_nm>JB 행복결혼적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 0.3% 우대
- 첫회제외 모든회차 자동이체 불입시 연 0.1% 우대
- 인터넷뱅킹 계좌 신규시 연 0.1% 우대
- 만기까지 정상 불입시 연 0.1% 우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>월 적립액 10만원이상 1천만원이하</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0021-0000</fin_prdt_cd>
<fin_prdt_nm>JB 행복드림적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 정기적금(자유적립식) 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 3.0% 우대(서류제출시)
- 기초생활수급자,        - 한부모 가정
- 소녀소녀가장세대주   - 근로장려금 수급자
- 다문화가정
- 차상위계층이하 만65세이상 고령자</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>월 적립액 1만원이상 50만원이하</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0022-0000</fin_prdt_cd>
<fin_prdt_nm>JB 온과빛함께적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대:최고 연0.8%우대 1.전북은행최초거래시 연0.2% 우대, 2.만18세이하가입시 연0.2%우대, 3.자동이체로납입시(계약기간1/2이상) 연0.2%우대, 4.만기전6개월내신용카드사용금액에 따라 연0.1%~0.2%우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>월 적립액 1만원이상
(단, 만18세이하는 1인당 최대 적립한도 2천만원이하)</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>2.35</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>2.25</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>2.15</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-031-0023-0000</fin_prdt_cd>
<fin_prdt_nm>JB퍼스트주거래적금</fin_prdt_nm>
<join_way>영업점,인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대:최고연0.4%우대1.JB퍼스트통장가입후적금신규시연0.1%우대,2.기간이3년이상인경우연0.1%우대,3.기간중3개월이상펀드상품보유시연0.1%우대,4.만기일최근6개월내카드매입실적이50만원이상인경우연0.1%우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인</join_member>
<etc_note>월 적립액 1만이상 1천만원이하</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0001-0000</fin_prdt_cd>
<fin_prdt_nm>상호부금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0005-0000</fin_prdt_cd>
<fin_prdt_nm>시장금리부 상호부금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.55</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>1.35</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0007-0000</fin_prdt_cd>
<fin_prdt_nm>인터넷상호부금</fin_prdt_nm>
<join_way>인터넷</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 월 적립액 1천만원이하
2. 인터넷뱅킹 가입상품</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.55</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010022</fin_co_no>
<kor_co_nm>전북은행</kor_co_nm>
<fin_prdt_cd>10-01-30-039-0007-0021</fin_prdt_cd>
<fin_prdt_nm>스마트상호부금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2
만기후 1개월초과 경과분 : 연 0.1%</mtrt_int>
<spcl_cnd>추가우대금리 : 최고 연 0.3% 우대
- 가입시 JB플러스급여통장 보유시 연 0.1% 우대
- 최근 1개월이내 신용카드 사용고객 연 0.1% 우대
- 상호부금 가입기간 1년이상인 경우 연 0.1% 우대</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 월 적립액 3백만이하,
2. 스마트폰뱅킹 가입상품</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201055</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
<intr_rate2>2.04</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000111</fin_prdt_cd>
<fin_prdt_nm>행복드림적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷적립식예금신규가입우대: 0.05%
▷신용카드신규가입 우대: 0.10%
▷고액적립액우대이율:30만원 이상: 0.05%, 60만원 이상: 0.10%
▷자동이체 우대이율: 0.05%
▷행복 우대이율:최대 0.15%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의개인</join_member>
<etc_note>1. 계약기간은 12개월 이상 36개월 이내에서 월 단위로 한다.
2. 이 예금은 5만원 이상 매월 정기적립식으로 한다.</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.05</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.15</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000112</fin_prdt_cd>
<fin_prdt_nm>행복드림여행적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷자동이체 우대금리
-정기적립식: 전체 적립회수의 2/3이상을 월10만원 이상 자동이체 입금시 0.05%
-자유적립식: 창구외 채널(인터넷뱅킹, 텔레뱅킹 등)로 10만원 이상 입금시 0.05%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인 및 임의단체(법인제외)</join_member>
<etc_note>1. 계약기간은 6개월 이상 36개월 이내에서 월 단위로 한다.
2. 정기적립식은 5만원 이상 매월 적립
3. 자유적립식은 최초 5만원 이상, 2회차 이후는 1만원 이상 자유롭게 납입하고, 월별 저축한도는 10백만원 이내</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.35</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.25</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.15</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.15</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.15</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000114</fin_prdt_cd>
<fin_prdt_nm>월복리솔솔적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>※아래 조건 충족시 최대 0.20% 우대금리 지급
▷예금 가입전 당행 거래가족수에 따른 우대금리 최고 0.10%, 직장인우대통장 가입 0.05%, 자녀명의로 아이드림자유적금 가입한 경우, 공과금자동이체 등록고객 각 0.05%
▷예금 가입전 3개월 이내 당행 신용(체크)카드 10만원 이상 이용시 0.05%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인 및 개인사업자</join_member>
<etc_note>1. 계약기간은 2년 이상 3년 이내에서 월 단위로 하며, 가입은 1인 1계좌로 제한
2. 적립액은 월 최소 5만원 이상 최대 5백만원 이하</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000118</fin_prdt_cd>
<fin_prdt_nm>희망모아적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷정기적립식의 경우, 이 예금을 전회차 납입하고 만기해지하는 경우 우대금리 3.00%
▷자유적립식의 경우 만기해지시 우대금리 2.00%
※특별중도해지 우대 : 가입후 6개월 이상 경과한 계좌로써, 가입기간 중 주택구입(임차), 결혼, 출산, 입원, 입학시</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자, 소년소녀가장, 근로장려금수급자, 다문화가정(부부),한부모가족지원보호대상자</join_member>
<etc_note>1. 계약기간은 12개월로 하며, 가입은 1인 1계좌로 제한
2. 적립액은 월 최소 1만원 이상 최대 30만원 이하</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>4.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>3.5</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000120</fin_prdt_cd>
<fin_prdt_nm>탄탄성공적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷입출금예금평잔에 따른 우대금리 0.10%~0.15%
▷퇴직연금가입시 우대금리 0.05%
▷월부금 2/3 이상 자동이체 입금시 우대금리 0.05%
▷이노비즈(Inno-Biz) 선정 사업자 우대금리 0.05%</spcl_cnd>
<join_deny>3</join_deny>
<join_member>가입대상은 개인사업자 및 법인에 한함.(다만 국가 및 지방자치단체는 가입할 수 없다.)</join_member>
<etc_note>1. 계약기간은 1년 이상 3년 이내에서 월 단위로 한다.
2. 이 예금은 10만원 이상 정기정액적립식으로 한다.</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000122</fin_prdt_cd>
<fin_prdt_nm>아이드림자유적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷출생년도 입금분 0.05%
▷입학년도 입금분(유치원, 초,중,고) 0.05%
▷설날, 추석, 생일 이후 5영업일 이내 입금분 0.05%
▷자동재예치 우대 0.05%
▷창구거래 외 입금 0.05%
▷예금주 또는 부모가 경남(울산)사랑통장 주거래고객인 경우 0.05%</spcl_cnd>
<join_deny>3</join_deny>
<join_member>26세 이하 개인에 한함
※자녀 전용 자유적립식 상품</join_member>
<etc_note>1. 계약기간은 1년 이상 3년 이내에서 년 단위로 한다.
2. 이 예금은 1인 1계좌에 한함
3. 이 예금은 1만원 이상 원단위로 자유롭게 적립하고 월별 저축한도는 1,000만원 이내</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000124</fin_prdt_cd>
<fin_prdt_nm>스마트자유적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷추천번호 입력 우대금리: 추천시 0.10%, 최대 3회 0.30% 제공</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인 및 개인사업자</join_member>
<etc_note>1. 계약기간은 6개월 이상 12개월 이내 월 단위로 한다.
2. 이 예금은 초입금 1만원 이상 월별 300만원 이내에서 자유롭게 저축(최대 저축횟수는 999회 이내)</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000131</fin_prdt_cd>
<fin_prdt_nm>e-money 자유적금</fin_prdt_nm>
<join_way>영업점,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷특정입출금상품에서 인출하여 신규시 우대금리
  - 직장인우대통장: 0.15%
  - 공직자우대통장: 0.15%
▷월부금 30만원 이상 자동이체 입금시 우대금리: 0.10%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인 및 개인사업자</join_member>
<etc_note>1. 계약기간은 6개월 이상 24개월 이내에서 월 단위로 한다.
2. 이 예금은 1만원 이상 자유롭게 적립
3. 이 예금은 인터넷뱅킹, 고객센터를 통하여 가입</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.55</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21000158</fin_prdt_cd>
<fin_prdt_nm>상조적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷차상위계층 이하 65세 이상 고령자가 가입할 경우 연 1.00%의 우대금리 지급
▷계약기간 중 본인, 배우자, 본인 및 배우자의 직계존비속 상사시 연 0.10% 우대금리</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인 및 개인사업자</join_member>
<etc_note>1. 계약기간은 1년 또는 2년으로 한다.
2. 월 5만원 이상 최대 100만원 이하에서 자유롭게 저축 가능</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001044</fin_prdt_cd>
<fin_prdt_nm>캠퍼스드림적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷전회차를 납입하고 만기해지하는 경우 우대금리 1.50%</spcl_cnd>
<join_deny>3</join_deny>
<join_member>대학생 전용상품으로 가입대상은 만18세 이상 만27세 이하의 개인(개인사업자 제외)</join_member>
<etc_note>1. 계약기간은 3년으로 하며, 1인 1계좌만 가입 가능
2. 적립액은 월 최소 1만원 이상 10만원 이하 정기정액적립식</etc_note>
<max_limit>100000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>2.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001053</fin_prdt_cd>
<fin_prdt_nm>카드플러스적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷신용카드결제증가액 우대이율: 최대 2.50%
▷거래실적 우대이율: 최대 0.10%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인 및 개인사업자</join_member>
<etc_note>1. 계약기간은 12개월로 한다.
2. 이 적금은 1인당 1계좌만 가입가능
3. 정기적립식은 월 최소 10만원 이상 최대 30만원 이하로 한다.</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001058</fin_prdt_cd>
<fin_prdt_nm>에메랄드적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷인터넷뱅킹, 스마트뱅킹, 고객센터를 통해 신규시 0.05%
▷아래 항목별 0.10%를 우대금리로 제공하며 최대 0.20%
- 가입자의 결혼, 임신, 출산, 가입자 자녀의 결혼, 손자 출생
▷신규가입고객이 다른 고객 1인을 소개시 0.05% 우대금리 제공하며 최대 0.10%까지 인정</spcl_cnd>
<join_deny>3</join_deny>
<join_member>여성 전용상품으로 가입대상은 실명의 개인인 여성</join_member>
<etc_note>1. 계약기간은 6개월이상 36개월 이내
2. 적립액은 매월 10만원 이상 100만원 이하</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.05</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010024</fin_co_no>
<kor_co_nm>경남은행</kor_co_nm>
<fin_prdt_cd>21001070</fin_prdt_cd>
<fin_prdt_nm>BNK연리지적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>만기후 1개월 이내: 일반정기예금 기본이율의 50%
만기후 1개월 초과: 일반정기예금 기본이율의 20%</mtrt_int>
<spcl_cnd>▷BNK투자증권,BNK캐피탈,BNK저축은행거래 여부에 따른 우대금리0.20%~0.30%
▷첫거래자 0.10%
▷계좌이동서비스로자동이체변경0.10%
▷평생통장자동이체0.10%
▷연결고리0.10%
▷종이통장미발행0.05%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>거래대상자는 제한을 두지 아니한다. 다만, 국가 및 지방자치단체는 이 예금을 거래할 수 없다.</join_member>
<etc_note>1. 계약기간은 12개월 이상 36개월 이내에서 월 단위로 한다.
2. 이 적금은 1인당 1계좌만 가입가능
3. 정액적립식은 10만원 이상 최대 5백만원 범위 내에서 매월 적립
4. 자유적립식은 초입금 1만원 이상, 분기별 적립금 합계액이 3백만원 이하 범위 내에서 적립</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201057</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2.05</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.15</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.35</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2.15</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210078</fin_prdt_cd>
<fin_prdt_nm>新서민섬김통장 가계우대정기적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.5%p
1. 신규고객 우대금리 : 연 0.1%p
2. 거래심화 우대금리 : 연 0.4%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인(개인사업자 제외)</join_member>
<etc_note>1인당 통합한도(적립식 계약원금+거치식 가입금액) 3천만원</etc_note>
<max_limit>30000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.9</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210082</fin_prdt_cd>
<fin_prdt_nm>IBK국군희망준비적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.20%p
1. 급여이체우대 : 연 0.20%p
2. 신용(체크)카드 우대 : 최고 연 0.20%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>실명의 개인으로 군 의무복무 병사</join_member>
<etc_note>월 1만원 이상 10만원 이하 적립가능</etc_note>
<max_limit>2400000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate></intr_rate>
<intr_rate2>5.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>5.3</intr_rate>
<intr_rate2>5.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>5.25</intr_rate>
<intr_rate2>4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>3.8</intr_rate>
<intr_rate2></intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210095</fin_prdt_cd>
<fin_prdt_nm>IBK사랑나눔적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 1.80%p
(계약기간별 고시금리와 동일한 금리를 우대금리로 제공)</spcl_cnd>
<join_deny>2</join_deny>
<join_member>장애인,기초생활수급자,소년소녀가장,북한이탈주민,결혼이민여성,한부모가족지원보호 대상자,차상위계층 이하 만65세 이상인 실명의 개인(개인사업자 제외)</join_member>
<etc_note>1인당 2계좌 가입가능하며, 계좌당 월적립금액 50만원 이하로 제한</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>3.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>3.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>3.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210097</fin_prdt_cd>
<fin_prdt_nm>IBK평생든든자유적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.3%p(1~4번 각 연0.1%p)
1. 평생설계저금통서비스 납입 실적
2. 급여, 4대연금, 보훈, 장해, 기초(노령)연금
3. 당행 연금관련상품의 가입실적
4. 비대면채널을 통해 이 상품을 가입했을 경우</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인(개인사업자 제외)</join_member>
<etc_note>월 1천원이상 30백만원 이하
※ 단, 초입금제한은 없으며, 월 적립금액 한도에 포함되지 않음</etc_note>
<max_limit>30000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.25</intr_rate>
<intr_rate2>1.55</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210102</fin_prdt_cd>
<fin_prdt_nm>IBK평생한가족통장 자유적립식</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.4%p
1. 고객별 우대금리: 연 0.1%p
2. 주거래 우대금리: 연 0.3%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인(개인사업자 제외)</join_member>
<etc_note>1인당 적립식 월적립한도 200만원</etc_note>
<max_limit>2000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>1.75</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010026</fin_co_no>
<kor_co_nm>중소기업은행</kor_co_nm>
<fin_prdt_cd>01211210103</fin_prdt_cd>
<fin_prdt_nm>IBK평생한가족통장 정액적립식</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기일 당시 가계우대정기적금 만기후금리 적용
- 1개월 이내: 만기일 당시 약정금리×50%
- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%
- 6개월 초과: 만기일 당시 약정금리×20%</mtrt_int>
<spcl_cnd>최고 연 0.4%p
1. 고객별 우대금리: 연 0.1%p
2. 주거래 우대금리: 연 0.3%p</spcl_cnd>
<join_deny>1</join_deny>
<join_member>실명의 개인(개인사업자 제외)</join_member>
<etc_note>1인당 적립식 월적립한도 200만원</etc_note>
<max_limit>2000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201050</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010028</fin_co_no>
<kor_co_nm>수협은행</kor_co_nm>
<fin_prdt_cd>10140108700011</fin_prdt_cd>
<fin_prdt_nm>더플러스정액적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>* 1년이하
정기적금 만기일 계약(해당)기간 약정금리 1/2
* 1년초과
만기후 해당구간시작일 보통예금 금리</mtrt_int>
<spcl_cnd>최고0.9%우대금리
-첫거래고객최대0.4%
-2인이상동시가입0.1%
-급여이체0.2%
-카드거래최대0.3%
-정기예금0.1%
-대출거래0.1%
-정액적립식거래0.2%
-인터넷뱅킹적금신규0.1%
-아파트관리비자동이체0.2%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201530</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>2.7</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010028</fin_co_no>
<kor_co_nm>수협은행</kor_co_nm>
<fin_prdt_cd>10141109800011</fin_prdt_cd>
<fin_prdt_nm>SH월복리자유적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>* 1년이하
상호부금 만기일 계약(해당)기간 약정금리 1/2
* 1년초과
만기후 해당구간시작일 보통예금 금리</mtrt_int>
<spcl_cnd>최고0.7%우대금리
-첫거래고객0.3%
-카드거래고객최대0.3%
-복수거래0.1%
-요구불거래최대0.2%
-인터넷뱅킹고객0.1%
-자동이체신청0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>* 1인당 가입한도 : 월 5백만원</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201530</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010028</fin_co_no>
<kor_co_nm>수협은행</kor_co_nm>
<fin_prdt_cd>10141110500011</fin_prdt_cd>
<fin_prdt_nm>SH100세만기자유적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>* 1년이하
상호부금 만기일 계약(해당)기간 약정금리 1/2
* 1년초과
만기후 해당구간시작일 보통예금 금리</mtrt_int>
<spcl_cnd>최고0.3%우대금리
-계좌이동제이동고객0.1%
-복수거래고객0.1%
-자동이체고객0.1%
-SH평생주거래통장고객0.1%
-칠순팔순고객0.1%
서민고객0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>* 1인당 가입한도 : 월 1천만원</etc_note>
<max_limit>10000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201530</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.65</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03100</fin_prdt_cd>
<fin_prdt_nm>정기적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>지급일 현재 고시된 일반정기예금 만기후 이자율 적용</mtrt_int>
<spcl_cnd>해당없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.25</intr_rate>
<intr_rate2>1.25</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>1.35</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03202</fin_prdt_cd>
<fin_prdt_nm>KDBdream 자유적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>*만기후 1년 이내:
만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2
* 만기후 1년 초과:
만기일 현재 보통예금 이자율</mtrt_int>
<spcl_cnd>KDBdream Account 계좌에서 자동이체방법으로 납입하는 경우, 연 0.10% 가산</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인 및 개인사업자</join_member>
<etc_note>이자율 적용방식 선택 가능
1) 최초납입일 고정금리식
2) 수시납입일 고정금리식</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.49</intr_rate>
<intr_rate2>1.59</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.59</intr_rate>
<intr_rate2>1.69</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.74</intr_rate>
<intr_rate2>1.84</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03204</fin_prdt_cd>
<fin_prdt_nm>KDB Hi 자유적금</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>*만기후 1년 이내:
만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2
* 만기후 1년 초과:
만기일 현재 보통예금 이자율</mtrt_int>
<spcl_cnd>KDB Hi 입출금통장에서 자동이체방법으로 납입하는 경우, 연 0.10% 가산</spcl_cnd>
<join_deny>1</join_deny>
<join_member>KDB Hi 입출금통장에 가입한 개인(개인사업자 및 임의단체 제외)
단, 국민인 거주자에 한함</join_member>
<etc_note>해당없음</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.78</intr_rate>
<intr_rate2>1.88</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.63</intr_rate>
<intr_rate2>1.73</intr_rate2>
				</option>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.53</intr_rate>
<intr_rate2>1.63</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010030</fin_co_no>
<kor_co_nm>한국산업은행</kor_co_nm>
<fin_prdt_cd>03205</fin_prdt_cd>
<fin_prdt_nm>주거래플러스 적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>*만기후 1년 이내:
만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2
* 만기후 1년 초과:
만기일 현재 보통예금 이자율</mtrt_int>
<spcl_cnd>* 온라인 가입 : 0.1%
* 산업은행 정기예금 또는 산금채 가입 : 0.1%
* 체크카드 사용실적 또는 자동이체 : 0.5%
* 입금 실적(월 건당 50만원 이상) : 0.3%
* 펀드 자동이체 : 0.2%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>개인(개인사업자 및 임의단체 제외)</join_member>
<etc_note>해당없음</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609200953</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.45</intr_rate>
<intr_rate2>2.65</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.7</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100054</fin_prdt_cd>
<fin_prdt_nm>KB국민행복적금
(정액적립식)</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※ 우대이율 최고 연2.0%p
- 전 회차 월 저축금 납입하고 만기해지하는 경우 계약기간 동안 적용</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자, 소년소녀가장, 북한이탈주민, 결혼이민여성, 근로장려금수급자, 한부모가족지원보호대상자, 만65세이상 차상위계층</join_member>
<etc_note>1인당가입한도 : 월 50만원</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>4.2</intr_rate>
<intr_rate2>6.2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100055</fin_prdt_cd>
<fin_prdt_nm>KB국민행복적금
(자유적립식)</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※ 우대이율 최고 연1.0%p
- 만기해지하는 경우 계약기간 동안 적용</spcl_cnd>
<join_deny>2</join_deny>
<join_member>기초생활수급자, 소년소녀가장, 북한이탈주민, 결혼이민여성, 근로장려금수급자, 한부모가족지원보호대상자, 만65세이상 차상위계층</join_member>
<etc_note>1인당가입한도 : 월 50만원</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>4.2</intr_rate>
<intr_rate2>5.2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100058</fin_prdt_cd>
<fin_prdt_nm>KB국군장병우대적금
(간부용)</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.5%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※ 우대이율 최고 연0.3%p
- 급여이체 우대이율 : 연0.3%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>군 의무복무 병을 제외한 실명의 개인인 군인</join_member>
<etc_note>1인당가입한도 : 월 50만원</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>4.7</intr_rate>
<intr_rate2>5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>4.8</intr_rate>
<intr_rate2>5.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>4.8</intr_rate>
<intr_rate2>5.1</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100059</fin_prdt_cd>
<fin_prdt_nm>KB국군희망준비적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.5%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※ 우대이율 최고 연0.3%p
- 급여이체 우대이율 : 연0.3%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>군 의무복무병 및 대체 복무자</join_member>
<etc_note>1인당가입한도 : 월 10만원</etc_note>
<max_limit>100000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>4.4</intr_rate>
<intr_rate2>4.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>5.4</intr_rate>
<intr_rate2>5.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>5.5</intr_rate>
<intr_rate2>5.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100062</fin_prdt_cd>
<fin_prdt_nm>KB창조금융적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※우대이율 최고 연1.2%p
-  Welcome 우대이율 : 연0.3
- 창조아이디어등록 우대이율 : 연0.2
- 우수아이디어채택 우대이율 : 연0.5
- 창의인재 우대이율 : 연0.2
(단위:%p)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1인당가입한도 : 월50만원</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.9</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100069</fin_prdt_cd>
<fin_prdt_nm>KB미소드림적금</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>우대이율 없음</spcl_cnd>
<join_deny>3</join_deny>
<join_member>미소금융대출 성실상환자로 재산형성 참여추천을 받은 실명의 개인</join_member>
<etc_note>1인당가입한도 : 월 10만원</etc_note>
<max_limit>100000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>4</intr_rate>
<intr_rate2></intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>3.8</intr_rate>
<intr_rate2></intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>3.6</intr_rate>
<intr_rate2></intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100070</fin_prdt_cd>
<fin_prdt_nm>KB내맘대로적금
(정액적립식)</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※우대이율 최고:연0.6%p
-급여이체:0.1
-카드결제계좌:0.1
-자동이체저축:0.1
-아파트관리비이체:0.1
-KB스타뱅킹 이체:0.1
-장기거래:0.1
-첫 거래:0.1
-주택청약종합저축:0.1
-소중한날:0.1
(단위:%p)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.7</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>2.4</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200100071</fin_prdt_cd>
<fin_prdt_nm>KB내맘대로적금
(자유적립식)</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※우대이율최고:연0.6%p
급여이체:0.1
카드결제계좌:0.1
자동이체저축:0.1
아파트관리비이체:0.1
KB스타뱅킹이체:0.1
장기거래:0.1
첫거래:0.1
주택청약종합저축:0.1
소중한날:0.1
(단위:%p)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1인당가입한도 : 월300만원</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2.1</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200200019</fin_prdt_cd>
<fin_prdt_nm>직장인우대적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※우대이율 최고 연0.5%p
- 직장인우대이율 : 연0.3
- 제휴사통신사 우대이율 : 연0.1 or 연0.2
(단위:%p)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1인당가입한도 : 월300만원</etc_note>
<max_limit>3000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609261500</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate></intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200300066</fin_prdt_cd>
<fin_prdt_nm>e-파워자유적금</fin_prdt_nm>
<join_way>인터넷,전화(텔레뱅킹)</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※우대이율 최고 연0.3%p
- KB star*t통장 or KB樂Star통장
 or KB나라사랑우대통장 가입자
 우대이율 : 연0.3
(단위:%p)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1인당가입한도 : 월 500만원
2. 인터넷 전용상품</etc_note>
<max_limit>5000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1</intr_rate>
<intr_rate2>1.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0010927</fin_co_no>
<kor_co_nm>국민은행</kor_co_nm>
<fin_prdt_cd>010200300071</fin_prdt_cd>
<fin_prdt_nm>KB Smart★폰 적금</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>- 만기후 1개월이내 : 기본이율 X 50%
- 만기후 1개월초과~3개월이내 : 기본이율 X 30%
- 만기후 3개월초과 : 0.2%

※ 단위 : 연%</mtrt_int>
<spcl_cnd>※우대이율 최고 연0.9%p
- 추천우대이율 : 최대 연0.3
- 아이콘적립우대이율 : 최대 연0.2
- 굿다운로더 우대이율 : 연0.1
- KB樂Star통장 우대이율 : 연0.3
(단위:%p)</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 1인당가입한도 : 월 100만원
2.스마트폰 전용상품</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201052</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.4</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>2.2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>.9</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0109-48</fin_prdt_cd>
<fin_prdt_nm>신한월복리적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,전화(텔레뱅킹)</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 연 0.3%(매 입금시 1건이상 충족시)
-주택청약종합저축 가입시
-신한카드결제계좌를 당행으로 지정시
-급여이체 실적, 공과금 이체 실적, 연금이체 실적으로 우대받은경우 중 1건이상</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입한도 : 분기별 100만원 이하
 (1~3월/4~6월/7~9월/10~12월)
2. 1인 1계좌</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>M</intr_rate_type>
<intr_rate_type_nm>복리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.85</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0109-54</fin_prdt_cd>
<fin_prdt_nm>신한 장학적금
(자유적립식)</fin_prdt_nm>
<join_way>영업점</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고0.6%,
-이체에 의한 저축시 0.2%
-체크카드OR 주택청액종합저축 보유 0.2%
-학교단체 신규시 0.2%</spcl_cnd>
<join_deny>3</join_deny>
<join_member>초.중.고등학생
(만 6세~만 18세)</join_member>
<etc_note>1. 가입한도 : 월 30만원 이하
2. 1인 1계좌</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.75</intr_rate>
<intr_rate2>2.35</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0109-64</fin_prdt_cd>
<fin_prdt_nm>신한 롯데백화점  LOVELY 적금 (자유적립식)</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고 0.1%
-신한카드 결제계좌 당행 지정시  0.10%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입한도 : 월 30만원이하
2. 1인 1계좌</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.5</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0118-07</fin_prdt_cd>
<fin_prdt_nm>신한스마트적금(s뱅크)</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>해당사항 없음</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입한도 : 월 100만원이하
2. 가입방법 : 스마트폰
3. 1인 1계좌</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.8</intr_rate>
<intr_rate2>1.8</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0118-31</fin_prdt_cd>
<fin_prdt_nm>신한저축습관만들기적금
(자유적립식)</fin_prdt_nm>
<join_way>스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고 0.4%
-저축습관지원 우대금리 0.3%
-목표달성지원 0.2%
-금리우대쿠폰발급고객 0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입한도 : 월 100만원 이하
2. 가입방법 : 스마트폰
3. 1인 1계좌</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.55</intr_rate>
<intr_rate2>1.95</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1.2</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0119-21</fin_prdt_cd>
<fin_prdt_nm>신한미션플러스 적금
(자유적립식)</fin_prdt_nm>
<join_way>인터넷,스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고 0.7%
-인터넷뱅킹,스마트폰으로 적금가입시 0.1%
-홈페이지 또는 어플리케이션을 통해 미션플러스 접속후 활동한 결과에 따라 최고 0.6%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입한도 : 월 100만원이하
2. 가입방법 : 인터넷, 스마트폰
3. 미션 1개당 1계좌</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>.9</intr_rate>
<intr_rate2>1.6</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.35</intr_rate>
<intr_rate2>2.05</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.6</intr_rate>
<intr_rate2>2.3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0119-41</fin_prdt_cd>
<fin_prdt_nm>신한 헬스플러스 적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고 0.3%
-신한카드 결제실적 월 10만원 이상 5회 이상 이용시 0.1%
-비대면채널 또는 모바일통장으로 신규시 0.1%
-목표 건강관리마일리지 달성 시 0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>1. 가입한도 : 월 100만원이하
2. 1인 1계좌</etc_note>
<max_limit>1000000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.7</intr_rate>
<intr_rate2>2</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0119-52</fin_prdt_cd>
<fin_prdt_nm>신한 청춘드림(DREAM) 적금(자유적립식)</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고 연 1.7%
-첫거래 우대 0.8%
-신한FAN클럽 가입실적 및 신한카드 결제 실적 0.3%
-휴대폰요금 자동이체실적 5개월이상 0.2%
-청약상품 만기유지 0.2%, -비대면채널 신규 0.2%</spcl_cnd>
<join_deny>3</join_deny>
<join_member>만19세~만35세</join_member>
<etc_note>1. 가입한도 : 월 30만원이하
2. 1인 1계좌</etc_note>
<max_limit>300000</max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.3</intr_rate>
<intr_rate2>3</intr_rate2>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201609</dcls_month>
<fin_co_no>0011625</fin_co_no>
<kor_co_nm>신한은행</kor_co_nm>
<fin_prdt_cd>230-0120-01</fin_prdt_cd>
<fin_prdt_nm>신한 S드림(DREAM) 적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>-1개월 이하:(일반) 정기적금 기본금리 1/2

-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4

-6개월 초과 0.2%</mtrt_int>
<spcl_cnd>※가산금리 최고 0.4%
-정기예금 잔액 3백만원 이상 0.2%
-청약상품 잔액 30만원 이상 보유시 0.2%
-적금상품 만기해지후 3개월내 신규시 0.2%
-30만원 이상 신규시 0.1%
-비대면 채널로 신규시 0.1%</spcl_cnd>
<join_deny>1</join_deny>
<join_member>제한없음</join_member>
<etc_note>해당사항 없음</etc_note>
<max_limit></max_limit>
<dcls_strt_day>20160920</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201609201331</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>6</save_trm>
<intr_rate>1</intr_rate>
<intr_rate2>1.4</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>1.05</intr_rate>
<intr_rate2>1.45</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>1.1</intr_rate>
<intr_rate2>1.5</intr_rate2>
				</option>
				<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>S</rsrv_type>
<rsrv_type_nm>정액적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>1.25</intr_rate>
<intr_rate2>1.65</intr_rate2>
				</option>
			</options>
		</product>
	</products>
</result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1

예제 요청결과(JSON)
{"result":{"prdt_div":"S","total_count":"113","max_page_no":"2","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","kor_co_nm":"우리은행","fin_prdt_nm":"올포미 적금","join_way":"영업점","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 신규 시 아래항목 충족 시 최고 연0.2%p\n1. 올포미 신용 카드 보유 및 우리은행 결제계좌 지정 연 0.2%p\n2. 우리은행 첫거래 고객 연 0.1%p\n3. 급여/연금치에 고객 연0.1%p\n4. 통신비/공과금 자동이체 고객 연0.1%p","join_deny":"1","join_member":"개인,개인사업자","etc_note":"해당없음","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001B","kor_co_nm":"우리은행","fin_prdt_nm":"우리웰리치100적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 신규 시 아래항목 충족 시 최고 연0.2%p\n1. 연금이체 실적 보유 연 0.1%p\n2. 우리웰리치100연금통장에서 자동이체 연 0.1%p\n3. 우리신용/체크카드 보유 연0.1%p\n4. 인터넷/스마트뱅킹으로 가입 연0.1%p","join_deny":"1","join_member":"실명의 개인","etc_note":"해당없음","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001C","kor_co_nm":"우리은행","fin_prdt_nm":"우리아이행복적금(12개월회전식)","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 아래 조건 충족 시 최고 연0.2%p\n1. 부모와 자녀 동시가입 연0.1%p\n2. 유후/아이행복 통장에서 자동이체등록 연0.1%p\n3. 직전회전기간동안 100만원이상 납입 연0.1%p\n4. 인터넷/스마트뱅킹으로 가입 연0.1%p","join_deny":"1","join_member":"실명의 개인","etc_note":"해당없음","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001D","kor_co_nm":"우리은행","fin_prdt_nm":"우리스마트폰적금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 우리 꿈통장으로 연결하여 가입 시 연 0.2%p 우대금리 적용","join_deny":"1","join_member":"실명의 개인","etc_note":"해당없음","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001E","kor_co_nm":"우리은행","fin_prdt_nm":"위비꿀적금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 최고 연 0.5%p\n1. 우리신용카드 최초가입 & 만기해지시까지 신용카드 보유 연 0.1%p\n2. 우리카드 결제계좌 등록 & 만기해지시까지 유지 연0.2%p","join_deny":"1","join_member":"실명의 개인","etc_note":"해당없음","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","kor_co_nm":"우리은행","fin_prdt_nm":"우리꿈적금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 최고 연 0.6%p\n1. 스마트뱅킹가입 연 0.2%p\n2. 우리은행 또는 제휴업체 발급 금리우대쿠폰 등록 연 0.1%p\n3. 친구번호 등록(연 0.1%p), 지인이 내 친구번호 등록(각 연 0.1%p), 최고 연 0.3%p 추가이율","join_deny":"1","join_member":"국내거주자인 개인","etc_note":"해당없음","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001G","kor_co_nm":"우리은행","fin_prdt_nm":"수요일이 즐거운 iTouch 문화적금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"- 매주 수요일 입금 금액 연 0.3%p 적용","join_deny":"1","join_member":"국내거주자인 개인","etc_note":"해당없음","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001I","kor_co_nm":"우리은행","fin_prdt_nm":"우리사랑플러스적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"1. 우대이자율 최고 연 0.5%p\n   (순신규 / 공과금 및 관리비 자동이체 / ISA 가입 / 신용카드 가맹점 결제계좌/5인이상단체가입)\n2. 특별이자율 최고 연 1.5%p[0.5%p 기부]\n   (우리카드 연간 5백만원 이상 사용)","join_deny":"1","join_member":"실명의 개인","etc_note":"해당없음","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001K","kor_co_nm":"우리은행","fin_prdt_nm":"위비꿀모아정기적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"위비멤버스 서비스 가입 고객인 경우 적립액에 대하여 최대 1%의 위비꿀머니 적립\n1. 중간적립 : 가입기간 중 매월 신규 적립액의          0.5%P\n 2. 만기적립 : 만기해지 시 전체 누적 적립액의 0.5%P","join_deny":"1","join_member":"14세 이상 실명의 개인","etc_note":"해당없음","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001L","kor_co_nm":"우리은행","fin_prdt_nm":"톡톡쇼핑적금","join_way":"인터넷,스마트폰","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"최고 연 0.8%p\n1. 금리우대쿠폰 연0.2%p\n2. 위비톡 앱 설치 후 바로가입 메뉴 신규 연0.2%p \n3. 우리카드결제실적 3개월 이상 보유 연0.2%p\n4. 위비톡 매월 10회 이상 메시지 보내기 연 0.2%P","join_deny":"1","join_member":"실명의 개인 및 개인사업자","etc_note":"해당없음","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001M","kor_co_nm":"우리은행","fin_prdt_nm":"우리희망드림적금","join_way":"영업점","mtrt_int":"만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리","spcl_cnd":"만기해지 시 연 2%p 우대이율 적용","join_deny":"2","join_member":"기초생활수급자, 만 65세 이상 차상위계층, 소년소녀가장, 결혼이민자, 북한 이탈주민, 근로장려금수급자","etc_note":"기초생활수급자, 만 65세 이상 차상위계층, 소년소녀가장, 결혼이민자, 북한 이탈주민, 근로장려금 수급자\n(단, 1인 1계좌에 한하여 가입 가능) \n주1)결혼이민자란 외국국적을 가진자가 대한민국 국적을 가진자와 결혼한 사람을 의미","max_limit":200000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201049"},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"퍼스트가계적금","join_way":"영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월: 0.7%\n만기 후 1개월 초과 1년 이내: 0.3%\n만기 후 1년 초과: 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200954"},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266472","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"SC행복적금","join_way":"영업점","mtrt_int":"만기 후 1개월: 0.7%\n만기 후 1개월 초과 1년 이내: 0.3%\n만기 후 1년 초과: 0.1%","spcl_cnd":"만기 시점을 기준으로 SC제일은행 입출금통장을 출금 계좌로 하여 \nSC행복적금으로 자동이체 5회 이상 실적이 있는 경우","join_deny":"2","join_member":"기초생활수급자, 소년소녀가장, 북한이탈주민, 결혼이민자, 근로장려금수급자, 한부모가족지원 보호대상자, 차상위계층 대상자(만 65세이상)","etc_note":"1. 1인당 가입한도 : 월 30만원\n2. 월 적립액은 예금을 가입하는 때에 정하며, 계약기간 중에 변경할 수 없음\n3. 가입 시 가입자격 증빙을 위한 증빙서류 징구","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200954"},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1800","kor_co_nm":"한국씨티은행","fin_prdt_nm":"정기적금","join_way":"영업점,인터넷","mtrt_int":"만기 후 1년 이내 : 만기일 당시 1년제 정기적금 이율의 1/2\n만기 후 1년 초과 : 연 1.0%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입기간은 6개월 이상 5년 이하 월단위 가입 가능 (3년을 초과하여 계약하고자 하는 경우 5년으로 함)","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201002"},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1813","kor_co_nm":"한국씨티은행","fin_prdt_nm":"원더풀라이프적금","join_way":"영업점,인터넷","mtrt_int":"만기 후 1년 이내 : 만기일 당시 1년제 정기적금 이율의 1/2\n만기 후 1년 초과 : 연 1.0%","spcl_cnd":"적금 가입 기간 중 은행이 고지한 Event 발생시 발생일로부터 추가우대이율 가산\n(추가우대이율 최대적용범위는 0.5%)\n(각 Event 항목별 연 0.1%[세전] 추가우대이율 적용)","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입기간은 1년 이상 3년 이하 월단위 가입 가능\n2. 가입금액은 1만원 이상 최고 1천만원 이내(단, 매월 1천만원 범위 내)이며, 계약기간의 3/4이 경과한 경우 적립할 수 있는 금액의 합계는 그 이전 적립금액의 50%를 초과할 수 없음 (매월의 기준은 1일부터 말일을 의미)","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201002"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000846001","kor_co_nm":"대구은행","fin_prdt_nm":"내손안에 적금","join_way":"스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.3%\n - 최초가입 우대 : 0.2%\n - 비대면채널 거래실적 우대 : 0.1%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입한도 : 월 100만원 (최저 10만원 이상)\n2. 스마트폰 가입 전용상품 \n3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000861003","kor_co_nm":"대구은행","fin_prdt_nm":"DGB희망더하기적금","join_way":"영업점","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 2.0%\n - 자동이체 우대 : 2.0%\n \n※ 단위는 연%p","join_deny":"2","join_member":"기초생활수급자, 등록장애인(1급 ~ 3급), 소년소녀가장, 결혼이민여성, 근로장려금수급자, 한부모가족지원 보호대상자, 차상위계층(단, 만65세이상 고령자에 한함)","etc_note":"1. 1계좌당 가입한도 : 월 30만원 (최저 1만원 이상)\n2. 저축기간 중 적용금리 변동 : 고시금리 기준 변동금리 적용","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000958002","kor_co_nm":"대구은행","fin_prdt_nm":"최강삼성V9 적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.25%\n - 신규시 주택청약상품 보유 우대 : 0.1%\n - 신규시 공과금 2건이상 보유 우대 : 0.05%\n - 삼성라이온즈 정규시즌 우승 우대 : 0.05%\n - 삼성라이온즈 한국시리즈 우승 우대 : 0.1%\n - 만기시 공과금 2건이상 보유 우대 : 0.05%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 10만원\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001046000","kor_co_nm":"대구은행","fin_prdt_nm":"DGB여(女)러분적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.5%\n - 거래실적 우대 : 0.2%\n - 힐링 우대 : 0.2%\n - 상품 소개 우대 : 0.1%\n\n※ 단위는 연%p","join_deny":"3","join_member":"만18세 이상의 여성","etc_note":"1. 1계좌당 가입한도 : 월 50만원 (최저 10만원 이상)\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001058000","kor_co_nm":"대구은행","fin_prdt_nm":"쓰담쓰담적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 1.4%\n - 첫예금 우대 : 0.1%\n - 패키지 우대 : 0.1%\n - 급여이체 우대 : 0.1%\n - 재예치 우대 : 0.3%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입한도 : 월 100만원 (최저 10만원 이상)\n2. 저축기간 중 적용금리 변동 : 고시금리 기준 변동금리 적용","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001109001","kor_co_nm":"대구은행","fin_prdt_nm":"ISA플러스 적금","join_way":"영업점","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.4%\n - 신규시 ISA계좌 10만원 이상 보유 우대 : 0.1%\n - 신규시 공과금 3건이상 보유 우대 : 0.1%\n - 만기시 ISA계좌 10만원 이상 보유 우대 : 0.1%\n - 만기시 공과금 3건이상 보유 우대 : 0.1%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입최저한도 : 10만원\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527001001143000","kor_co_nm":"대구은행","fin_prdt_nm":"청춘희망적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.5%\n - 신규시 주택청약상품 보유 우대 : 0.1%\n - 신용카드 실적 우대 : 0.1%\n - 만기시 목표 불입액 달성 우대 : 0.1%\n - 상품 소개 우대: 0.2%\n\n※ 단위는 연%p","join_deny":"3","join_member":"만19세 이상 만40세 이하 개인","etc_note":"1. 1계좌당 가입한도 : 월 100만원 (최저 1만원 이상)\n2. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527036000001001","kor_co_nm":"대구은행","fin_prdt_nm":"e-U(이유)적금","join_way":"인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%","spcl_cnd":"* 최고우대금리 : 0.6%\n - 재예치 우대 : 0.2%\n - 비대면채널 거래실적 우대 : 0.1%\n - 3개월 평잔 30만원 보유  우대 : 0.1%\n - 주택청약상품 보유 우대 : 0.2%\n\n※ 단위는 연%p","join_deny":"1","join_member":"제한없음","etc_note":"1. 1계좌당 가입한도 : 월 200만원 (최저 10만원 이상)\n2. 인터넷뱅킹 및 스마트폰 가입 전용상품 \n3. 저축기간 중 적용금리 변동 : 자유적립식예금 기준 변동금리 적용","max_limit":2000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201130"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400110001","kor_co_nm":"부산은행","fin_prdt_nm":"갈맷길정기적금","join_way":"영업점,인터넷","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"-걷기실천우대 : 0.05~0.20%\n-인터넷가입우대: 0.10%\n-장애인(걷기 동반자 1인): 0.10%","join_deny":"1","join_member":"제한없음","etc_note":"제한없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400210001","kor_co_nm":"부산은행","fin_prdt_nm":"e-푸른바다 자유적금","join_way":"인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"우대조건 없음","join_deny":"1","join_member":"제한없음","etc_note":"1.1인당 가입한도: 월 500만원","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400240001","kor_co_nm":"부산은행","fin_prdt_nm":"달콤한인생적금","join_way":"영업점","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"-자동재예치시: 0.10%","join_deny":"1","join_member":"제한없음","etc_note":"제한없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400270001","kor_co_nm":"부산은행","fin_prdt_nm":"BNK희망가꾸기적금","join_way":"영업점","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"-월간불입한도 금액내에서 \n우대이율 2.5%우대","join_deny":"2","join_member":"기초생활수급권자 본인(독거노인포함),\n소년소녀가장 본인, 북한이탈주민 본인,\n다문화가정(결혼이민자 본인,그 배우자 및 자녀),\n한부모가정(한부모가족지원법에 따른 지원대상),\n장애인","etc_note":"1.1인당 가입한도: 월 25만원","max_limit":250000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400340001","kor_co_nm":"부산은행","fin_prdt_nm":"굿-초이스","join_way":"인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"-스마트 우대: 0.10%\n-팔로워 우대: 0.10%\n-목돈마련 우대: 0.10%\n-신용카드, 교차판매 우대: 0.70%","join_deny":"1","join_member":"제한없음","etc_note":"1. 1인당 가입한도: 월 100만원","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400360001","kor_co_nm":"부산은행","fin_prdt_nm":"MySUM포인트적금","join_way":"스마트폰","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"- 모바일 통장 자동이체 8회차 이상 불입 시: 0.10%\n- 10만원 이상 스윙서비스 입금건수 6회 이상: 0.1%\n- 모바일 통장 기중평잔 30만원 이상: 0.10%\n- 당행 신용카드 및 롯데카드 결제 실적 우대: 0.10%\n- 계좌이동 건수 2건 이상: 0.10%","join_deny":"1","join_member":"제한없음","etc_note":"1. 1인당 가입한도: 월 100만원\n2. 가입채널: 당행 썸뱅크(모바일) 통해 가입가능\n3. MySUM모바일통장과 패키지로 개설","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01021400020002","kor_co_nm":"부산은행","fin_prdt_nm":"가계우대정기적금","join_way":"영업점,인터넷","mtrt_int":"- 만기후 1년이내:가입기간별 일반정기적금 기본이율 x 50%\n- 만기후 1년초과:가입기간별 일반정기적금 기본이율 x 20%","spcl_cnd":"우대조건 없음.","join_deny":"1","join_member":"제한없음","etc_note":"1.1인당 가입한도: 월 270만원(총 1억원이내)","max_limit":2700000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201338"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330018000","kor_co_nm":"광주은행","fin_prdt_nm":"파워월복리적금","join_way":"영업점,인터넷","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"*최고 우대금리 : 0.7%\n1.요구불 평잔 우대 : 0.2%\n2. 자녀명의「KJB아이사랑월복리 적금」가입 실적 : 0.1%\n3. 신용카드실적우대: 최대 0.2%\n4. 급여통장보유: 0.1%\n5. 가맹점 결제계좌우대: 0.1%","join_deny":"1","join_member":"개인","etc_note":"1. 가입금액 : 1만원 이상 ~5천만원 이하\n2. 분기당 납입금액 : 1천만원 이하\n3. 자유적립식","max_limit":50000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261232"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","kor_co_nm":"광주은행","fin_prdt_nm":"스마트모아Dream정기적금","join_way":"인터넷,스마트폰","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"- 스마트뱅킹 1년제 정액적립식 가입 : 0.1%우대","join_deny":"1","join_member":"개인","etc_note":"1. 월입금한도 : 매회 1만원 ~ 월 1천만원 이하\n2. 비대면실명확인 고객의 경우 정액적립식만 선택가능","max_limit":10000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261232"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330023000","kor_co_nm":"광주은행","fin_prdt_nm":"KJB주거래적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"* 최고 우대금리: 1.3%\n- 신규고객 : 0.3%\n- 당행대출보유 : 0.2%\n- 만18세 이하 : 0.2%\n- 자동이체실적우대 : 최고 0.4%\n- 신용(체크)카드 사용우대 : 최고 0.3%","join_deny":"1","join_member":"개인","etc_note":"1. 1인당 가입한도 : 월 50만원\n2. 1인 1계좌  \n3. 정액적립식","max_limit":500000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261232"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330024000","kor_co_nm":"광주은행","fin_prdt_nm":"꿈모아매일적금","join_way":"스마트폰","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"*최고 우대금리 : 0.4%\n1.「목표설정」우대금리 : 0.1%\n2.「우등상」 우대금리 : 0.1%\n3.「친구소개」우대금리 : 최대 0.2%","join_deny":"1","join_member":"개인","etc_note":"1. 가입금액 : 1만원 이상 \n2. 납입한도 : 월 100만원 이내\n3. 자유적립식","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201122"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330025000","kor_co_nm":"광주은행","fin_prdt_nm":"해피라이프_여행스케치적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"* 최고 우대금리 : 0.2%\n- 신용(체크)카드 사용 : 최대 0.1%\n- 비대면채널 이용우대 : 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입금액 : 월 5만원 이상 ~10백만원 이하\n2. 정액적립식","max_limit":10000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261232"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330027000","kor_co_nm":"광주은행","fin_prdt_nm":"쏠쏠한마이쿨적금","join_way":"스마트폰","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"없음","join_deny":"3","join_member":"가입일 기준 최근 1년간 당행 거치식예금, 적","etc_note":"1. 가입금액 : 월 1만원 이상 ~ 100만원 이하 \n2. 1인 1계좌 \n3. 정액적립식","max_limit":1000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261232"},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD1330024000","kor_co_nm":"광주은행","fin_prdt_nm":"꿈모아매일적금","join_way":"인터넷,스마트폰","mtrt_int":"-만기후 1개월 이내\n: 만기일당시 해당적금 최초 가입기간별 고시이자율의 1/2\n-만기후 1개월 초과\n:0.10%","spcl_cnd":"*최고 우대금리 : 0.4%\n1.목표설정우대금리 : 0.1%\n2. 우등상 우대금리 : 0.1%\n3. 친구소개우대금리 : 최대 0.2%","join_deny":"1","join_member":"개인","etc_note":"1. 가입금액: 1만원 이상\n2. 납입한도 : 월100만원 이내\n3. 자유적립식","max_limit":1000000,"dcls_strt_day":"20160926","dcls_end_day":null,"fin_co_subm_day":"201609261232"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000801","kor_co_nm":"제주은행","fin_prdt_nm":"제주Tops허니문통장","join_way":"영업점,인터넷,스마트폰","mtrt_int":"- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"- 교차우대 최고 연 0.6%p\n①자동대체 등록 거래 0.1%p\n②적금 계약기간 중 자녀 출산시 0.2%p\n③적금 계약기간 중 결혼시 0.3%p\n- 인터넷뱅킹 등 비대면매체 신규 우대 연 0.1%p","join_deny":"3","join_member":"미혼 및 결혼한지 3년 이내의 개인","etc_note":"월적립금 최소 10만원 이상~ 최대 300만원 이하","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200957"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","kor_co_nm":"제주은행","fin_prdt_nm":"만덕사랑적금","join_way":"영업점","mtrt_int":"- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"- 교차우대 여성 최고  연 0.6%p(남성  연0.5%p) (항목별 연 0.1%p)\n①매 저축 건별 자동대체 거래\n②미성년자\n③여성\n④다자녀고객(3자녀 이상)\n⑤자원봉사인증서 or 헌혈증서 지참\n⑥복지단체후원금 or 기부금영수증 지참\n⑦복지카드소지","join_deny":"1","join_member":"제한없음","etc_note":"자유적립식인 경우 2회차 이후 월1천만원 이내","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200957"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001201","kor_co_nm":"제주은행","fin_prdt_nm":"모아모아월복리적금","join_way":"영업점","mtrt_int":"- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"- 교차우대 최고 연 0.3%p(항목별 연 0.1%p)\n①유동성예금 가입\n②거치식,적립식예금, 방카,펀드 가입\n③고객정보(CIF) 최초 등록\n④자동대체 등록\n- 추가우대(최고 0.1%p)\n①탐나는J직장인통장 or 주거래통장 가입(기본요건충족)","join_deny":"3","join_member":"개인 및 개인사업자","etc_note":"1. 1인 1계좌\n2. 가입금액 : 매 입금건별 1만원 이상 분기별 5백만원 이하","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200957"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","kor_co_nm":"제주은행","fin_prdt_nm":"제주SOHO적금","join_way":"영업점","mtrt_int":"- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"- 교차우대 최고 연 0.3%p(항목별 연 0.1%p)\n①탐나는 J 사업자통장 가입\n②제주은행 계좌로 카드가맹점 대금 이체 실적 有\n③종업원 급여이체\n④비 활동성 고객\n⑤SOHO 전용 패키지 가입","join_deny":"3","join_member":"개인사업자, 법인, 임의단체","etc_note":"가입금액 : 1만원 이상","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200957"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001701","kor_co_nm":"제주은행","fin_prdt_nm":"새희망키움적금","join_way":"영업점","mtrt_int":"- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"- 교차우대 최고 연 3.0%p\n①만기해지시 2.5%p\n②유동성계좌에서 자동이체 등록시 0.5%p","join_deny":"2","join_member":"기초생활수급자,소년소녀가장,북한이탈주민,결혼이민자,근로장려금수급자,한부모가족지원보호대상자,만65세이상차상위계층","etc_note":"1인당 가입한도: 월 20만원","max_limit":200000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200957"},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"230000202","kor_co_nm":"제주은행","fin_prdt_nm":"사이버우대매일부금","join_way":"인터넷,스마트폰","mtrt_int":"- 만기후 1개월 이내 : (일반)정기적금 기본이자율의 50%\n- 만기후 1개월 초과 3개월 이내 : (일반)정기적금 기본이자율의 30%\n- 만기후 3개월 초과 : 0.25%","spcl_cnd":"- 교차우대 최고 연 0.1%p\n①탐나는 J 직장인통장 가입 고객이 기본우대 요건 충족후 이 상품 가입시 : 0.1%p\n②탐나는 J 주거래통장 가입고객이 기본우대 요건 충족후 이 상품 가입시 : 0.1%p","join_deny":"3","join_member":"개인 및 개인사업자","etc_note":"\"해당 없음\"","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200957"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","kor_co_nm":"전북은행","fin_prdt_nm":"정기적금","join_way":"영업점","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 월 불입한도 1천만원 이내 \n2. 만기직전 1개월간 적립금액 합계는 그 이전 기간동안 적립액을 초과할수 없음","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0018-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB 다이렉트적금","join_way":"인터넷,스마트폰","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 정기적금(자유적립식) 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대금리 :\n당행 계좌간 자동이체를 통해 이 예금으로 자동이체 된 금액에 0.1% 금리 우대","join_deny":"1","join_member":"실명의 개인\n(임의단체 제외)","etc_note":"1. 초회불입금 1만원이상, 1인당 월별 최고 1천만원이내\n2. 만기직전 1개월간 적립합계는 이전기간 적립금액을 초과할 수 없음\n3. 인터넷뱅킹/스마트폰뱅킹 가입상품","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0019-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB 행복투어적금","join_way":"영업점,인터넷","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대금리 : 최고 연 0.3% 우대\n- 첫회제외 모든회차 자동이체 불입시 연 0.1% 우대\n- 인터넷뱅킹 계좌 신규시 연 0.1% 우대\n- 만기까지 정상 불입시 연 0.1% 우대","join_deny":"1","join_member":"제한없음","etc_note":"월 적립액 5만원이상 1천만원이하","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0020-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB 행복결혼적금","join_way":"영업점,인터넷","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대금리 : 최고 연 0.3% 우대\n- 첫회제외 모든회차 자동이체 불입시 연 0.1% 우대\n- 인터넷뱅킹 계좌 신규시 연 0.1% 우대\n- 만기까지 정상 불입시 연 0.1% 우대","join_deny":"1","join_member":"실명의 개인","etc_note":"월 적립액 10만원이상 1천만원이하","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0021-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB 행복드림적금","join_way":"영업점","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 정기적금(자유적립식) 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대금리 : 최고 연 3.0% 우대(서류제출시)\n- 기초생활수급자,        - 한부모 가정\n- 소녀소녀가장세대주   - 근로장려금 수급자  \n- 다문화가정\n- 차상위계층이하 만65세이상 고령자","join_deny":"1","join_member":"실명의 개인","etc_note":"월 적립액 1만원이상 50만원이하","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0022-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB 온과빛함께적금","join_way":"영업점,인터넷","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대:최고 연0.8%우대 1.전북은행최초거래시 연0.2% 우대, 2.만18세이하가입시 연0.2%우대, 3.자동이체로납입시(계약기간1/2이상) 연0.2%우대, 4.만기전6개월내신용카드사용금액에 따라 연0.1%~0.2%우대","join_deny":"1","join_member":"실명의 개인","etc_note":"월 적립액 1만원이상\n(단, 만18세이하는 1인당 최대 적립한도 2천만원이하)","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0023-0000","kor_co_nm":"전북은행","fin_prdt_nm":"JB퍼스트주거래적금","join_way":"영업점,인터넷","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대:최고연0.4%우대1.JB퍼스트통장가입후적금신규시연0.1%우대,2.기간이3년이상인경우연0.1%우대,3.기간중3개월이상펀드상품보유시연0.1%우대,4.만기일최근6개월내카드매입실적이50만원이상인경우연0.1%우대","join_deny":"1","join_member":"실명의 개인","etc_note":"월 적립액 1만이상 1천만원이하","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0001-0000","kor_co_nm":"전북은행","fin_prdt_nm":"상호부금","join_way":"영업점","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0005-0000","kor_co_nm":"전북은행","fin_prdt_nm":"시장금리부 상호부금","join_way":"영업점","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0000","kor_co_nm":"전북은행","fin_prdt_nm":"인터넷상호부금","join_way":"인터넷","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 월 적립액 1천만원이하\n2. 인터넷뱅킹 가입상품","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0021","kor_co_nm":"전북은행","fin_prdt_nm":"스마트상호부금","join_way":"스마트폰","mtrt_int":"만기후 1개월이내 경과분 : 만기일 현재 계약기간별 실행이율의 1/2\n만기후 1개월초과 경과분 : 연 0.1%","spcl_cnd":"추가우대금리 : 최고 연 0.3% 우대\n- 가입시 JB플러스급여통장 보유시 연 0.1% 우대\n- 최근 1개월이내 신용카드 사용고객 연 0.1% 우대\n- 상호부금 가입기간 1년이상인 경우 연 0.1% 우대","join_deny":"1","join_member":"제한없음","etc_note":"1. 월 적립액 3백만이하, \n2. 스마트폰뱅킹 가입상품","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201055"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000111","kor_co_nm":"경남은행","fin_prdt_nm":"행복드림적금","join_way":"영업점,전화(텔레뱅킹)","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷적립식예금신규가입우대: 0.05%\n▷신용카드신규가입 우대: 0.10%\n▷고액적립액우대이율:30만원 이상: 0.05%, 60만원 이상: 0.10%\n▷자동이체 우대이율: 0.05%\n▷행복 우대이율:최대 0.15%","join_deny":"1","join_member":"실명의개인","etc_note":"1. 계약기간은 12개월 이상 36개월 이내에서 월 단위로 한다.\n2. 이 예금은 5만원 이상 매월 정기적립식으로 한다.","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","kor_co_nm":"경남은행","fin_prdt_nm":"행복드림여행적금","join_way":"영업점,전화(텔레뱅킹)","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷자동이체 우대금리\n-정기적립식: 전체 적립회수의 2/3이상을 월10만원 이상 자동이체 입금시 0.05%\n-자유적립식: 창구외 채널(인터넷뱅킹, 텔레뱅킹 등)로 10만원 이상 입금시 0.05%","join_deny":"1","join_member":"개인 및 임의단체(법인제외)","etc_note":"1. 계약기간은 6개월 이상 36개월 이내에서 월 단위로 한다.\n2. 정기적립식은 5만원 이상 매월 적립\n3. 자유적립식은 최초 5만원 이상, 2회차 이후는 1만원 이상 자유롭게 납입하고, 월별 저축한도는 10백만원 이내","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000114","kor_co_nm":"경남은행","fin_prdt_nm":"월복리솔솔적금","join_way":"영업점,전화(텔레뱅킹)","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"※아래 조건 충족시 최대 0.20% 우대금리 지급\n▷예금 가입전 당행 거래가족수에 따른 우대금리 최고 0.10%, 직장인우대통장 가입 0.05%, 자녀명의로 아이드림자유적금 가입한 경우, 공과금자동이체 등록고객 각 0.05%\n▷예금 가입전 3개월 이내 당행 신용(체크)카드 10만원 이상 이용시 0.05%","join_deny":"1","join_member":"실명의 개인 및 개인사업자","etc_note":"1. 계약기간은 2년 이상 3년 이내에서 월 단위로 하며, 가입은 1인 1계좌로 제한\n2. 적립액은 월 최소 5만원 이상 최대 5백만원 이하","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000118","kor_co_nm":"경남은행","fin_prdt_nm":"희망모아적금","join_way":"영업점","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷정기적립식의 경우, 이 예금을 전회차 납입하고 만기해지하는 경우 우대금리 3.00%\n▷자유적립식의 경우 만기해지시 우대금리 2.00%\n※특별중도해지 우대 : 가입후 6개월 이상 경과한 계좌로써, 가입기간 중 주택구입(임차), 결혼, 출산, 입원, 입학시","join_deny":"2","join_member":"기초생활수급자, 소년소녀가장, 근로장려금수급자, 다문화가정(부부),한부모가족지원보호대상자","etc_note":"1. 계약기간은 12개월로 하며, 가입은 1인 1계좌로 제한\n2. 적립액은 월 최소 1만원 이상 최대 30만원 이하","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000120","kor_co_nm":"경남은행","fin_prdt_nm":"탄탄성공적금","join_way":"영업점","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷입출금예금평잔에 따른 우대금리 0.10%~0.15%\n▷퇴직연금가입시 우대금리 0.05%\n▷월부금 2/3 이상 자동이체 입금시 우대금리 0.05%\n▷이노비즈(Inno-Biz) 선정 사업자 우대금리 0.05%","join_deny":"3","join_member":"가입대상은 개인사업자 및 법인에 한함.(다만 국가 및 지방자치단체는 가입할 수 없다.)","etc_note":"1. 계약기간은 1년 이상 3년 이내에서 월 단위로 한다.\n2. 이 예금은 10만원 이상 정기정액적립식으로 한다.","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000122","kor_co_nm":"경남은행","fin_prdt_nm":"아이드림자유적금","join_way":"영업점","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷출생년도 입금분 0.05%\n▷입학년도 입금분(유치원, 초,중,고) 0.05%\n▷설날, 추석, 생일 이후 5영업일 이내 입금분 0.05%\n▷자동재예치 우대 0.05%\n▷창구거래 외 입금 0.05%\n▷예금주 또는 부모가 경남(울산)사랑통장 주거래고객인 경우 0.05%","join_deny":"3","join_member":"26세 이하 개인에 한함\n※자녀 전용 자유적립식 상품","etc_note":"1. 계약기간은 1년 이상 3년 이내에서 년 단위로 한다.\n2. 이 예금은 1인 1계좌에 한함\n3. 이 예금은 1만원 이상 원단위로 자유롭게 적립하고 월별 저축한도는 1,000만원 이내","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000124","kor_co_nm":"경남은행","fin_prdt_nm":"스마트자유적금","join_way":"스마트폰","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷추천번호 입력 우대금리: 추천시 0.10%, 최대 3회 0.30% 제공","join_deny":"1","join_member":"개인 및 개인사업자","etc_note":"1. 계약기간은 6개월 이상 12개월 이내 월 단위로 한다.\n2. 이 예금은 초입금 1만원 이상 월별 300만원 이내에서 자유롭게 저축(최대 저축횟수는 999회 이내)","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000131","kor_co_nm":"경남은행","fin_prdt_nm":"e-money 자유적금","join_way":"영업점,전화(텔레뱅킹)","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷특정입출금상품에서 인출하여 신규시 우대금리\n  - 직장인우대통장: 0.15%\n  - 공직자우대통장: 0.15%\n▷월부금 30만원 이상 자동이체 입금시 우대금리: 0.10%","join_deny":"1","join_member":"개인 및 개인사업자","etc_note":"1. 계약기간은 6개월 이상 24개월 이내에서 월 단위로 한다.\n2. 이 예금은 1만원 이상 자유롭게 적립\n3. 이 예금은 인터넷뱅킹, 고객센터를 통하여 가입","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000158","kor_co_nm":"경남은행","fin_prdt_nm":"상조적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷차상위계층 이하 65세 이상 고령자가 가입할 경우 연 1.00%의 우대금리 지급\n▷계약기간 중 본인, 배우자, 본인 및 배우자의 직계존비속 상사시 연 0.10% 우대금리","join_deny":"1","join_member":"개인 및 개인사업자","etc_note":"1. 계약기간은 1년 또는 2년으로 한다.\n2. 월 5만원 이상 최대 100만원 이하에서 자유롭게 저축 가능","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001044","kor_co_nm":"경남은행","fin_prdt_nm":"캠퍼스드림적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷전회차를 납입하고 만기해지하는 경우 우대금리 1.50%","join_deny":"3","join_member":"대학생 전용상품으로 가입대상은 만18세 이상 만27세 이하의 개인(개인사업자 제외)","etc_note":"1. 계약기간은 3년으로 하며, 1인 1계좌만 가입 가능\n2. 적립액은 월 최소 1만원 이상 10만원 이하 정기정액적립식","max_limit":100000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001053","kor_co_nm":"경남은행","fin_prdt_nm":"카드플러스적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷신용카드결제증가액 우대이율: 최대 2.50%\n▷거래실적 우대이율: 최대 0.10%","join_deny":"1","join_member":"실명의 개인 및 개인사업자","etc_note":"1. 계약기간은 12개월로 한다.\n2. 이 적금은 1인당 1계좌만 가입가능\n3. 정기적립식은 월 최소 10만원 이상 최대 30만원 이하로 한다.","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001058","kor_co_nm":"경남은행","fin_prdt_nm":"에메랄드적금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷인터넷뱅킹, 스마트뱅킹, 고객센터를 통해 신규시 0.05%\n▷아래 항목별 0.10%를 우대금리로 제공하며 최대 0.20%\n- 가입자의 결혼, 임신, 출산, 가입자 자녀의 결혼, 손자 출생\n▷신규가입고객이 다른 고객 1인을 소개시 0.05% 우대금리 제공하며 최대 0.10%까지 인정","join_deny":"3","join_member":"여성 전용상품으로 가입대상은 실명의 개인인 여성","etc_note":"1. 계약기간은 6개월이상 36개월 이내\n2. 적립액은 매월 10만원 이상 100만원 이하","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","kor_co_nm":"경남은행","fin_prdt_nm":"BNK연리지적금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"만기후 1개월 이내: 일반정기예금 기본이율의 50%\n만기후 1개월 초과: 일반정기예금 기본이율의 20%","spcl_cnd":"▷BNK투자증권,BNK캐피탈,BNK저축은행거래 여부에 따른 우대금리0.20%~0.30%\n▷첫거래자 0.10%\n▷계좌이동서비스로자동이체변경0.10%\n▷평생통장자동이체0.10%\n▷연결고리0.10%\n▷종이통장미발행0.05%","join_deny":"1","join_member":"거래대상자는 제한을 두지 아니한다. 다만, 국가 및 지방자치단체는 이 예금을 거래할 수 없다.","etc_note":"1. 계약기간은 12개월 이상 36개월 이내에서 월 단위로 한다.\n2. 이 적금은 1인당 1계좌만 가입가능\n3. 정액적립식은 10만원 이상 최대 5백만원 범위 내에서 매월 적립\n4. 자유적립식은 초입금 1만원 이상, 분기별 적립금 합계액이 3백만원 이하 범위 내에서 적립","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201057"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210078","kor_co_nm":"중소기업은행","fin_prdt_nm":"新서민섬김통장 가계우대정기적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 가계우대정기적금 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%\n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.5%p\n1. 신규고객 우대금리 : 연 0.1%p\n2. 거래심화 우대금리 : 연 0.4%p","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"1인당 통합한도(적립식 계약원금+거치식 가입금액) 3천만원","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201050"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210082","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK국군희망준비적금","join_way":"영업점","mtrt_int":"만기일 당시 가계우대정기적금 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%\n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.20%p\n1. 급여이체우대 : 연 0.20%p\n2. 신용(체크)카드 우대 : 최고 연 0.20%p","join_deny":"3","join_member":"실명의 개인으로 군 의무복무 병사","etc_note":"월 1만원 이상 10만원 이하 적립가능","max_limit":2400000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201050"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210095","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK사랑나눔적금","join_way":"영업점","mtrt_int":"만기일 당시 가계우대정기적금 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%\n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 1.80%p\n(계약기간별 고시금리와 동일한 금리를 우대금리로 제공)","join_deny":"2","join_member":"장애인,기초생활수급자,소년소녀가장,북한이탈주민,결혼이민여성,한부모가족지원보호 대상자,차상위계층 이하 만65세 이상인 실명의 개인(개인사업자 제외)","etc_note":"1인당 2계좌 가입가능하며, 계좌당 월적립금액 50만원 이하로 제한","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201050"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210097","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK평생든든자유적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 가계우대정기적금 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%\n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.3%p(1~4번 각 연0.1%p)\n1. 평생설계저금통서비스 납입 실적\n2. 급여, 4대연금, 보훈, 장해, 기초(노령)연금\n3. 당행 연금관련상품의 가입실적\n4. 비대면채널을 통해 이 상품을 가입했을 경우","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"월 1천원이상 30백만원 이하\n※ 단, 초입금제한은 없으며, 월 적립금액 한도에 포함되지 않음","max_limit":30000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201050"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210102","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK평생한가족통장 자유적립식","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 가계우대정기적금 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%\n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.4%p\n1. 고객별 우대금리: 연 0.1%p\n2. 주거래 우대금리: 연 0.3%p","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"1인당 적립식 월적립한도 200만원","max_limit":2000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201050"},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210103","kor_co_nm":"중소기업은행","fin_prdt_nm":"IBK평생한가족통장 정액적립식","join_way":"영업점,인터넷,스마트폰","mtrt_int":"만기일 당시 가계우대정기적금 만기후금리 적용\n- 1개월 이내: 만기일 당시 약정금리×50%\n- 1월 초과 6개월 이내: 만기일 당시 약정금리×30%\n- 6개월 초과: 만기일 당시 약정금리×20%","spcl_cnd":"최고 연 0.4%p\n1. 고객별 우대금리: 연 0.1%p\n2. 주거래 우대금리: 연 0.3%p","join_deny":"1","join_member":"실명의 개인(개인사업자 제외)","etc_note":"1인당 적립식 월적립한도 200만원","max_limit":2000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201050"},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10140108700011","kor_co_nm":"수협은행","fin_prdt_nm":"더플러스정액적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"* 1년이하\n정기적금 만기일 계약(해당)기간 약정금리 1/2\n* 1년초과\n만기후 해당구간시작일 보통예금 금리","spcl_cnd":"최고0.9%우대금리\n-첫거래고객최대0.4%\n-2인이상동시가입0.1%\n-급여이체0.2%\n-카드거래최대0.3%\n-정기예금0.1%\n-대출거래0.1%\n-정액적립식거래0.2%\n-인터넷뱅킹적금신규0.1%\n-아파트관리비자동이체0.2%","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201530"},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141109800011","kor_co_nm":"수협은행","fin_prdt_nm":"SH월복리자유적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"* 1년이하\n상호부금 만기일 계약(해당)기간 약정금리 1/2\n* 1년초과\n만기후 해당구간시작일 보통예금 금리","spcl_cnd":"최고0.7%우대금리\n-첫거래고객0.3%\n-카드거래고객최대0.3%\n-복수거래0.1%\n-요구불거래최대0.2%\n-인터넷뱅킹고객0.1%\n-자동이체신청0.1%","join_deny":"1","join_member":"제한없음","etc_note":"* 1인당 가입한도 : 월 5백만원","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201530"},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141110500011","kor_co_nm":"수협은행","fin_prdt_nm":"SH100세만기자유적금","join_way":"영업점","mtrt_int":"* 1년이하\n상호부금 만기일 계약(해당)기간 약정금리 1/2\n* 1년초과\n만기후 해당구간시작일 보통예금 금리","spcl_cnd":"최고0.3%우대금리\n-계좌이동제이동고객0.1%\n-복수거래고객0.1%\n-자동이체고객0.1%\n-SH평생주거래통장고객0.1%\n-칠순팔순고객0.1%\n서민고객0.1%","join_deny":"1","join_member":"제한없음","etc_note":"* 1인당 가입한도 : 월 1천만원","max_limit":10000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201530"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03100","kor_co_nm":"한국산업은행","fin_prdt_nm":"정기적금","join_way":"영업점","mtrt_int":"지급일 현재 고시된 일반정기예금 만기후 이자율 적용","spcl_cnd":"해당없음","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200953"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03202","kor_co_nm":"한국산업은행","fin_prdt_nm":"KDBdream 자유적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"*만기후 1년 이내:\n만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2\n* 만기후 1년 초과:\n만기일 현재 보통예금 이자율","spcl_cnd":"KDBdream Account 계좌에서 자동이체방법으로 납입하는 경우, 연 0.10% 가산","join_deny":"1","join_member":"개인 및 개인사업자","etc_note":"이자율 적용방식 선택 가능\n1) 최초납입일 고정금리식\n2) 수시납입일 고정금리식","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200953"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03204","kor_co_nm":"한국산업은행","fin_prdt_nm":"KDB Hi 자유적금","join_way":"인터넷,스마트폰","mtrt_int":"*만기후 1년 이내:\n만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2\n* 만기후 1년 초과:\n만기일 현재 보통예금 이자율","spcl_cnd":"KDB Hi 입출금통장에서 자동이체방법으로 납입하는 경우, 연 0.10% 가산","join_deny":"1","join_member":"KDB Hi 입출금통장에 가입한 개인(개인사업자 및 임의단체 제외)\n단, 국민인 거주자에 한함","etc_note":"해당없음","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200953"},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03205","kor_co_nm":"한국산업은행","fin_prdt_nm":"주거래플러스 적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"*만기후 1년 이내:\n만기일 현재 일반정지걱금 해당예금기간 기본이자율의 1/2\n* 만기후 1년 초과:\n만기일 현재 보통예금 이자율","spcl_cnd":"* 온라인 가입 : 0.1%\n* 산업은행 정기예금 또는 산금채 가입 : 0.1%\n* 체크카드 사용실적 또는 자동이체 : 0.5%\n* 입금 실적(월 건당 50만원 이상) : 0.3%\n* 펀드 자동이체 : 0.2%","join_deny":"1","join_member":"개인(개인사업자 및 임의단체 제외)","etc_note":"해당없음","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609200953"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100054","kor_co_nm":"국민은행","fin_prdt_nm":"KB국민행복적금\n(정액적립식)","join_way":"영업점","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연2.0%p\n- 전 회차 월 저축금 납입하고 만기해지하는 경우 계약기간 동안 적용","join_deny":"2","join_member":"기초생활수급자, 소년소녀가장, 북한이탈주민, 결혼이민여성, 근로장려금수급자, 한부모가족지원보호대상자, 만65세이상 차상위계층","etc_note":"1인당가입한도 : 월 50만원","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100055","kor_co_nm":"국민은행","fin_prdt_nm":"KB국민행복적금\n(자유적립식)","join_way":"영업점","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연1.0%p\n- 만기해지하는 경우 계약기간 동안 적용","join_deny":"2","join_member":"기초생활수급자, 소년소녀가장, 북한이탈주민, 결혼이민여성, 근로장려금수급자, 한부모가족지원보호대상자, 만65세이상 차상위계층","etc_note":"1인당가입한도 : 월 50만원","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100058","kor_co_nm":"국민은행","fin_prdt_nm":"KB국군장병우대적금\n(간부용)","join_way":"영업점","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.5%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연0.3%p\n- 급여이체 우대이율 : 연0.3%p","join_deny":"3","join_member":"군 의무복무 병을 제외한 실명의 개인인 군인","etc_note":"1인당가입한도 : 월 50만원","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100059","kor_co_nm":"국민은행","fin_prdt_nm":"KB국군희망준비적금","join_way":"영업점","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.5%\n\n※ 단위 : 연%","spcl_cnd":"※ 우대이율 최고 연0.3%p\n- 급여이체 우대이율 : 연0.3%p","join_deny":"3","join_member":"군 의무복무병 및 대체 복무자","etc_note":"1인당가입한도 : 월 10만원","max_limit":100000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100062","kor_co_nm":"국민은행","fin_prdt_nm":"KB창조금융적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※우대이율 최고 연1.2%p\n-  Welcome 우대이율 : 연0.3\n- 창조아이디어등록 우대이율 : 연0.2\n- 우수아이디어채택 우대이율 : 연0.5\n- 창의인재 우대이율 : 연0.2\n(단위:%p)","join_deny":"1","join_member":"제한없음","etc_note":"1인당가입한도 : 월50만원","max_limit":500000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100069","kor_co_nm":"국민은행","fin_prdt_nm":"KB미소드림적금","join_way":"영업점","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"우대이율 없음","join_deny":"3","join_member":"미소금융대출 성실상환자로 재산형성 참여추천을 받은 실명의 개인","etc_note":"1인당가입한도 : 월 10만원","max_limit":100000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100070","kor_co_nm":"국민은행","fin_prdt_nm":"KB내맘대로적금\n(정액적립식)","join_way":"인터넷,스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※우대이율 최고:연0.6%p\n-급여이체:0.1\n-카드결제계좌:0.1\n-자동이체저축:0.1\n-아파트관리비이체:0.1\n-KB스타뱅킹 이체:0.1\n-장기거래:0.1\n-첫 거래:0.1\n-주택청약종합저축:0.1\n-소중한날:0.1\n(단위:%p)","join_deny":"1","join_member":"제한없음","etc_note":"해당없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100071","kor_co_nm":"국민은행","fin_prdt_nm":"KB내맘대로적금\n(자유적립식)","join_way":"인터넷,스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※우대이율최고:연0.6%p\n급여이체:0.1\n카드결제계좌:0.1\n자동이체저축:0.1\n아파트관리비이체:0.1\nKB스타뱅킹이체:0.1\n장기거래:0.1\n첫거래:0.1\n주택청약종합저축:0.1\n소중한날:0.1\n(단위:%p)","join_deny":"1","join_member":"제한없음","etc_note":"1인당가입한도 : 월300만원","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200200019","kor_co_nm":"국민은행","fin_prdt_nm":"직장인우대적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※우대이율 최고 연0.5%p\n- 직장인우대이율 : 연0.3\n- 제휴사통신사 우대이율 : 연0.1 or 연0.2\n(단위:%p)","join_deny":"1","join_member":"제한없음","etc_note":"1인당가입한도 : 월300만원","max_limit":3000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609261500"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300066","kor_co_nm":"국민은행","fin_prdt_nm":"e-파워자유적금","join_way":"인터넷,전화(텔레뱅킹)","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※우대이율 최고 연0.3%p\n- KB star*t통장 or KB樂Star통장\n or KB나라사랑우대통장 가입자 \n 우대이율 : 연0.3\n(단위:%p)","join_deny":"1","join_member":"제한없음","etc_note":"1. 1인당가입한도 : 월 500만원\n2. 인터넷 전용상품","max_limit":5000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300071","kor_co_nm":"국민은행","fin_prdt_nm":"KB Smart★폰 적금","join_way":"스마트폰","mtrt_int":"- 만기후 1개월이내 : 기본이율 X 50%\n- 만기후 1개월초과~3개월이내 : 기본이율 X 30%\n- 만기후 3개월초과 : 0.2%\n\n※ 단위 : 연%","spcl_cnd":"※우대이율 최고 연0.9%p\n- 추천우대이율 : 최대 연0.3\n- 아이콘적립우대이율 : 최대 연0.2\n- 굿다운로더 우대이율 : 연0.1\n- KB樂Star통장 우대이율 : 연0.3\n(단위:%p)","join_deny":"1","join_member":"제한없음","etc_note":"1. 1인당가입한도 : 월 100만원\n2.스마트폰 전용상품","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201052"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0109-48","kor_co_nm":"신한은행","fin_prdt_nm":"신한월복리적금","join_way":"영업점,인터넷,스마트폰,전화(텔레뱅킹)","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 연 0.3%(매 입금시 1건이상 충족시)\n-주택청약종합저축 가입시 \n-신한카드결제계좌를 당행으로 지정시\n-급여이체 실적, 공과금 이체 실적, 연금이체 실적으로 우대받은경우 중 1건이상","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 분기별 100만원 이하\n (1~3월/4~6월/7~9월/10~12월)\n2. 1인 1계좌","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0109-54","kor_co_nm":"신한은행","fin_prdt_nm":"신한 장학적금\n(자유적립식)","join_way":"영업점","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고0.6%, \n-이체에 의한 저축시 0.2%\n-체크카드OR 주택청액종합저축 보유 0.2%\n-학교단체 신규시 0.2%","join_deny":"3","join_member":"초.중.고등학생\n(만 6세~만 18세)","etc_note":"1. 가입한도 : 월 30만원 이하\n2. 1인 1계좌","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0109-64","kor_co_nm":"신한은행","fin_prdt_nm":"신한 롯데백화점  LOVELY 적금 (자유적립식)","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.1%\n-신한카드 결제계좌 당행 지정시  0.10%","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 월 30만원이하\n2. 1인 1계좌","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-07","kor_co_nm":"신한은행","fin_prdt_nm":"신한스마트적금(s뱅크)","join_way":"스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"해당사항 없음","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 월 100만원이하\n2. 가입방법 : 스마트폰\n3. 1인 1계좌","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-31","kor_co_nm":"신한은행","fin_prdt_nm":"신한저축습관만들기적금\n(자유적립식)","join_way":"스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.4%\n-저축습관지원 우대금리 0.3%\n-목표달성지원 0.2%\n-금리우대쿠폰발급고객 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 월 100만원 이하\n2. 가입방법 : 스마트폰\n3. 1인 1계좌","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-21","kor_co_nm":"신한은행","fin_prdt_nm":"신한미션플러스 적금 \n(자유적립식)","join_way":"인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.7%\n-인터넷뱅킹,스마트폰으로 적금가입시 0.1%\n-홈페이지 또는 어플리케이션을 통해 미션플러스 접속후 활동한 결과에 따라 최고 0.6%","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 월 100만원이하\n2. 가입방법 : 인터넷, 스마트폰\n3. 미션 1개당 1계좌","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-41","kor_co_nm":"신한은행","fin_prdt_nm":"신한 헬스플러스 적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.3%\n-신한카드 결제실적 월 10만원 이상 5회 이상 이용시 0.1%\n-비대면채널 또는 모바일통장으로 신규시 0.1%\n-목표 건강관리마일리지 달성 시 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"1. 가입한도 : 월 100만원이하\n2. 1인 1계좌","max_limit":1000000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-52","kor_co_nm":"신한은행","fin_prdt_nm":"신한 청춘드림(DREAM) 적금(자유적립식)","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 연 1.7%\n-첫거래 우대 0.8%\n-신한FAN클럽 가입실적 및 신한카드 결제 실적 0.3%\n-휴대폰요금 자동이체실적 5개월이상 0.2%\n-청약상품 만기유지 0.2%, -비대면채널 신규 0.2%","join_deny":"3","join_member":"만19세~만35세","etc_note":"1. 가입한도 : 월 30만원이하\n2. 1인 1계좌","max_limit":300000,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0120-01","kor_co_nm":"신한은행","fin_prdt_nm":"신한 S드림(DREAM) 적금","join_way":"영업점,인터넷,스마트폰","mtrt_int":"-1개월 이하:(일반) 정기적금 기본금리 1/2<br>\n-1개월 초과~6개월 이하: (일반) 정기적금 기본금리의 1/4<br>\n-6개월 초과 0.2%","spcl_cnd":"※가산금리 최고 0.4%\n-정기예금 잔액 3백만원 이상 0.2%\n-청약상품 잔액 30만원 이상 보유시 0.2% \n-적금상품 만기해지후 3개월내 신규시 0.2%\n-30만원 이상 신규시 0.1%\n-비대면 채널로 신규시 0.1%","join_deny":"1","join_member":"제한없음","etc_note":"해당사항 없음","max_limit":null,"dcls_strt_day":"20160920","dcls_end_day":null,"fin_co_subm_day":"201609201331"}],"optionList":[{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.7,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.75,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.35,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.45,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.55,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.55,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001A","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.65,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001B","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001B","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001B","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001C","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001D","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.8,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001E","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.5,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.4,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.35,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":0.85,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.55,"intr_rate2":2.15},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001F","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.05,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001G","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001I","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":3.4},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001K","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.6,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001K","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.65,"intr_rate2":null},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001K","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":null,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001L","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.5,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001M","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":2,"intr_rate2":4},{"dcls_month":"201609","fin_co_no":"0010001","fin_prdt_cd":"WR0001M","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":2,"intr_rate2":4},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.65,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.6,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266451","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010002","fin_prdt_cd":"00266472","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":3.5,"intr_rate2":3.8},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1800","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1,"intr_rate2":1},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1800","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1800","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1813","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.4,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1813","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.2,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010006","fin_prdt_cd":"1813","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000846001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.46,"intr_rate2":1.76},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000846001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.48,"intr_rate2":1.78},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000846001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000861003","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":3,"intr_rate2":5},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001000958002","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.16,"intr_rate2":1.56},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001046000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.16,"intr_rate2":1.66},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001046000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.28,"intr_rate2":1.78},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001046000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.4,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001058000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.35,"intr_rate2":2.75},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001058000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.35,"intr_rate2":2.75},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10521001001109001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.16,"intr_rate2":1.46},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527001001143000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.02,"intr_rate2":1.52},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527001001143000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.26,"intr_rate2":1.76},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527001001143000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.28,"intr_rate2":1.78},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527001001143000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.3,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527036000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.26,"intr_rate2":1.86},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527036000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.28,"intr_rate2":1.88},{"dcls_month":"201609","fin_co_no":"0010016","fin_prdt_cd":"10527036000001001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.3,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400110001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400110001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400110001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400210001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400210001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400210001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400210001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400240001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400270001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":2,"intr_rate2":4.5},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400270001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":2.2,"intr_rate2":4.7},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400270001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":2.4,"intr_rate2":4.9},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400340001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01020400360001","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.8,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01021400020002","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01021400020002","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010017","fin_prdt_cd":"01021400020002","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330018000","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330018000","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330018000","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.9,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.8,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.7,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330021000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.4,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330023000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":2.5},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330023000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.3,"intr_rate2":2.6},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330023000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.4,"intr_rate2":2.7},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330025000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330025000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330025000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330025000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD11330027000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.9,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD1330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD1330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD1330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010019","fin_prdt_cd":"TD1330024000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000801","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000801","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000801","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.4},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220000901","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001201","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.9,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.8,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.7,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001301","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.6,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"220001701","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":3,"intr_rate2":6},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"230000202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.55,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"230000202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.65,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"230000202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.75,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010020","fin_prdt_cd":"230000202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.85,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0004-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0018-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.8,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0018-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.85,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0018-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.95,"intr_rate2":2.04},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0019-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0019-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0019-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0019-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0020-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0020-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0020-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0020-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0021-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0021-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0021-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0021-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0022-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.55,"intr_rate2":2.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0022-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.45,"intr_rate2":2.25},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0022-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.35,"intr_rate2":2.15},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0023-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.2,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0023-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-031-0023-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.1},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0001-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0005-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.55,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0005-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0005-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0005-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.3,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.55,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0000","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.65,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.75,"intr_rate2":2.04},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.65,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.55,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010022","fin_prdt_cd":"10-01-30-039-0007-0021","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.4,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000111","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000111","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.05},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000111","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.15},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.3,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.2,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.15,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000112","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.15},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000114","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.55,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000114","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.75,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000118","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":4.5},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000118","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":3.5},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000120","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000120","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000120","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000122","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000122","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000122","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.3,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000124","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000124","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.6,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000131","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000131","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000131","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.65},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000158","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":2.5},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21000158","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":2.4},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001044","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.45,"intr_rate2":2.9},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001053","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":4},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.05},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.3,"intr_rate2":2.05},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.2,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.15,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.45},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.35},{"dcls_month":"201609","fin_co_no":"0010024","fin_prdt_cd":"21001070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":2.15},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210078","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.35,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210078","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":1.9},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210078","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.45,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210082","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":null,"intr_rate2":5.5},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210082","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":5.3,"intr_rate2":5.45},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210082","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":5.25,"intr_rate2":4},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210082","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":3.8,"intr_rate2":null},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210095","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.7,"intr_rate2":3.4},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210095","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.8,"intr_rate2":3.6},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210095","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.8,"intr_rate2":3.6},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210097","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.25,"intr_rate2":1.55},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210102","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210102","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.35,"intr_rate2":1.75},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210102","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.45,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210103","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.55,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210103","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.45,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0010026","fin_prdt_cd":"01211210103","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10140108700011","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.6,"intr_rate2":2.5},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10140108700011","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.7,"intr_rate2":2.6},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10140108700011","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.8,"intr_rate2":2.7},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141109800011","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141109800011","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141109800011","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.4},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141110500011","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.65,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141110500011","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.65,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010028","fin_prdt_cd":"10141110500011","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.65,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03100","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.2},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03100","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.25,"intr_rate2":1.25},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03100","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.35,"intr_rate2":1.35},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03100","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.45,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.49,"intr_rate2":1.59},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.59,"intr_rate2":1.69},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03202","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.74,"intr_rate2":1.84},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03204","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.78,"intr_rate2":1.88},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03204","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.63,"intr_rate2":1.73},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03204","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.53,"intr_rate2":1.63},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03205","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":2.6},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03205","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.45,"intr_rate2":2.65},{"dcls_month":"201609","fin_co_no":"0010030","fin_prdt_cd":"03205","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.5,"intr_rate2":2.7},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100054","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":4.2,"intr_rate2":6.2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100055","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":4.2,"intr_rate2":5.2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":4.7,"intr_rate2":5},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":4.8,"intr_rate2":5.1},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100058","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":4.8,"intr_rate2":5.1},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100059","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":4.4,"intr_rate2":4.7},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100059","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":5.4,"intr_rate2":5.7},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100059","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":5.5,"intr_rate2":5.8},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100062","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":2.5},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100062","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":2.7},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100062","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.9},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100069","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":4,"intr_rate2":null},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100069","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":3.8,"intr_rate2":null},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100069","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":3.6,"intr_rate2":null},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1.1,"intr_rate2":1.7},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.5,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100070","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.8,"intr_rate2":2.4},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.4,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":2.1},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200100071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200200019","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":null,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200200019","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.8,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200200019","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200200019","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300066","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1,"intr_rate2":1.3},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300066","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300066","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.5,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300066","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.7,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":2.5},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.4,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.3,"intr_rate2":2.2},{"dcls_month":"201609","fin_co_no":"0010927","fin_prdt_cd":"010200300071","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":0.9,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0109-48","intr_rate_type":"M","intr_rate_type_nm":"복리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.55,"intr_rate2":1.85},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0109-54","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.75,"intr_rate2":2.35},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0109-64","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.5,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-07","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.8,"intr_rate2":1.8},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-31","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.6,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-31","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.55,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-31","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.55,"intr_rate2":1.95},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0118-31","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":1.2,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-21","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"6","intr_rate":0.9,"intr_rate2":1.6},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-21","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"12","intr_rate":1.35,"intr_rate2":2.05},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-21","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"24","intr_rate":1.6,"intr_rate2":2.3},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-41","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.7,"intr_rate2":2},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0119-52","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"F","rsrv_type_nm":"자유적립식","save_trm":"36","intr_rate":1.3,"intr_rate2":3},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0120-01","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"6","intr_rate":1,"intr_rate2":1.4},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0120-01","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"12","intr_rate":1.05,"intr_rate2":1.45},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0120-01","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"24","intr_rate":1.1,"intr_rate2":1.5},{"dcls_month":"201609","fin_co_no":"0011625","fin_prdt_cd":"230-0120-01","intr_rate_type":"S","intr_rate_type_nm":"단리","rsrv_type":"S","rsrv_type_nm":"정액적립식","save_trm":"36","intr_rate":1.25,"intr_rate2":1.65}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd**	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
mtrt_int	만기 후 이자율
spcl_cnd	우대조건
join_deny	가입제한
Ex) 1:제한없음, 2:서민전용, 3:일부제한
join_member	가입대상
etc_note	기타 유의사항
max_limit	최고한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
intr_rate_type	저축 금리 유형
intr_rate_type_nm	저축 금리 유형명
rsrv_type	적립 유형
rsrv_type_nm	적립 유형명
save_trm	저축 기간 [단위: 개월]
intr_rate	저축 금리 [소수점 2자리]
intr_rate2	최고 우대금리 [소수점 2자리]
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
No	응답코드	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

## 연금저축 API 상세
요청URL
http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.{응답방식}

요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) savingProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=060000&pageNo=1

예제 요청결과(XML)
<result>
<err_cd>000</err_cd>
<err_msg>정상</err_msg>
<total_count>102</total_count>
<max_page_no>21</max_page_no>
<now_page_no>1</now_page_no>
	<products>
		<product>
			<baseinfo>
<dcls_month>201510</dcls_month>
<fin_co_no>0010170</fin_co_no>
<kor_co_nm>하나유비에스자산운용</kor_co_nm>
<fin_prdt_cd>KR5102314204</fin_prdt_cd>
<fin_prdt_nm>하나UBS인Best연금증권투자신탁(제1호)[채권]</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타</join_way>
<pnsn_kind>4</pnsn_kind>
<pnsn_kind_nm>연금저축펀드</pnsn_kind_nm>
<sale_strt_day>20010201</sale_strt_day>
<mntn_cnt>73342945069</mntn_cnt>
<prdt_type>411</prdt_type>
<prdt_type_nm>채권형</prdt_type_nm>
<avg_prft_rate>4.05</avg_prft_rate>
<dcls_rate></dcls_rate>
<guar_rate></guar_rate>
<btrm_prft_rate_1>2.96</btrm_prft_rate_1>
<btrm_prft_rate_2>1.97</btrm_prft_rate_2>
<btrm_prft_rate_3>3.35</btrm_prft_rate_3>
<etc></etc>
<sale_co>KEB하나은행(구.외환은행),KEB하나은행(구.하나은행),우리은행,기업은행,수협중앙회,에스케이증권,현대증권,메리츠종금증권,삼성증권,한양증권,NH투자증권,교보증권,KDB대우증권,신한금융투자,유안타증권,아이비케이투자증권,이베스트투자증권,키움증권,리딩투자증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,미래에셋생명보험,삼성생명보험,한화생명보험,펀드온라인코리아 주식회사,케이티비투자증권,유진투자증권</sale_co>
<dcls_strt_day>20151001</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201510301534</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>229566</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>840868</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>840868</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>623168</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>623168</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>862105</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>862105</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1215635</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1215635</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1681737</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1681737</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1246337</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1246337</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1724211</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1724211</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1823452</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1823452</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2522605</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2522605</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1869505</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1869505</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2586316</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2586316</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>607817</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>607817</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>976825</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>229566</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>317587</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>317587</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>235364</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>235364</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>325608</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>325608</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>459133</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>459133</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>635175</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>635175</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>470729</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>976825</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>706093</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>706093</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>952762</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>952762</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>688699</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>688699</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>651217</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>651217</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>470729</pnsn_recp_amt>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201510</dcls_month>
<fin_co_no>0010170</fin_co_no>
<kor_co_nm>하나유비에스자산운용</kor_co_nm>
<fin_prdt_cd>KR5102314212</fin_prdt_cd>
<fin_prdt_nm>하나UBS인Best연금증권투자신탁(제1호)[주식]</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타</join_way>
<pnsn_kind>4</pnsn_kind>
<pnsn_kind_nm>연금저축펀드</pnsn_kind_nm>
<sale_strt_day>20010201</sale_strt_day>
<mntn_cnt>814160555217</mntn_cnt>
<prdt_type>421</prdt_type>
<prdt_type_nm>주식형</prdt_type_nm>
<avg_prft_rate>8.07</avg_prft_rate>
<dcls_rate></dcls_rate>
<guar_rate></guar_rate>
<btrm_prft_rate_1>-6.24</btrm_prft_rate_1>
<btrm_prft_rate_2>2.26</btrm_prft_rate_2>
<btrm_prft_rate_3>4.26</btrm_prft_rate_3>
<etc></etc>
<sale_co>경남은행,우리은행,부산은행,KEB하나은행(구.외환은행),기업은행,수협중앙회,신영증권,한양증권,NH투자증권,교보증권,대신증권,KDB대우증권,신한금융투자,유안타증권,에스케이증권,삼성생명보험,한화생명보험,펀드온라인코리아 주식회사,케이티비투자증권,엘아이지투자증권,아이비케이투자증권,이베스트투자증권,키움증권,리딩투자증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,현대증권,메리츠종금증권,삼성증권,미래에셋생명보험,KEB하나은행(구.하나은행)</sale_co>
<dcls_strt_day>20151001</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201510301534</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>557199</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>770842</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>770842</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>522570</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>522570</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>722936</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>722936</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1114398</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1114398</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1541683</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1541683</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1045141</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1045141</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1445872</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1445872</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1671597</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1671597</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2312525</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2312525</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1567711</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1567711</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2168807</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2168807</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>557199</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>819136</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>210448</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>210448</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>291139</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>291139</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>197370</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>197370</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>273045</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>273045</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>420897</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>420897</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>582278</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>582278</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>394739</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>819136</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>592109</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>592109</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>873417</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>873417</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>631345</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>631345</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>546091</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>546091</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>394739</pnsn_recp_amt>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201510</dcls_month>
<fin_co_no>0010170</fin_co_no>
<kor_co_nm>하나유비에스자산운용</kor_co_nm>
<fin_prdt_cd>KR5102314352</fin_prdt_cd>
<fin_prdt_nm>하나UBS인Best연금증권투자신탁(제1호)[국공채]</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타</join_way>
<pnsn_kind>4</pnsn_kind>
<pnsn_kind_nm>연금저축펀드</pnsn_kind_nm>
<sale_strt_day>20010202</sale_strt_day>
<mntn_cnt>27342275814</mntn_cnt>
<prdt_type>411</prdt_type>
<prdt_type_nm>채권형</prdt_type_nm>
<avg_prft_rate>4.05</avg_prft_rate>
<dcls_rate></dcls_rate>
<guar_rate></guar_rate>
<btrm_prft_rate_1>2.9</btrm_prft_rate_1>
<btrm_prft_rate_2>2.15</btrm_prft_rate_2>
<btrm_prft_rate_3>3.07</btrm_prft_rate_3>
<etc></etc>
<sale_co>우리은행,에스케이증권,KEB하나은행(구.하나은행),수협중앙회,KDB대우증권,신영증권,이베스트투자증권,키움증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,메리츠종금증권,삼성증권,미래에셋생명보험,삼성생명보험,케이티비투자증권,아이비케이투자증권,NH투자증권</sale_co>
<dcls_strt_day>20151001</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201510301534</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>607960</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>841066</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>841066</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>623466</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>623466</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>862516</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>862516</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1215920</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1215920</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1682132</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1682132</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1246931</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1246931</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1725033</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1725033</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1823881</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1823881</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2523198</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2523198</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1870397</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1870397</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2587549</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2587549</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>607960</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>977291</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>229620</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>229620</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>317662</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>317662</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>235477</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>235477</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>325764</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>325764</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>459241</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>459241</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>635324</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>635324</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>470953</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>977291</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>706430</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>706430</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>952986</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>952986</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>688861</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>688861</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>651527</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>651527</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>470953</pnsn_recp_amt>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201510</dcls_month>
<fin_co_no>0010170</fin_co_no>
<kor_co_nm>하나유비에스자산운용</kor_co_nm>
<fin_prdt_cd>KR5102314733</fin_prdt_cd>
<fin_prdt_nm>하나UBS인Best연금증권투자신탁(제1호)[주식혼합]</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타</join_way>
<pnsn_kind>4</pnsn_kind>
<pnsn_kind_nm>연금저축펀드</pnsn_kind_nm>
<sale_strt_day>20010205</sale_strt_day>
<mntn_cnt>174743666758</mntn_cnt>
<prdt_type>431</prdt_type>
<prdt_type_nm>혼합주식형</prdt_type_nm>
<avg_prft_rate>8.63</avg_prft_rate>
<dcls_rate></dcls_rate>
<guar_rate></guar_rate>
<btrm_prft_rate_1>-2.8</btrm_prft_rate_1>
<btrm_prft_rate_2>1.66</btrm_prft_rate_2>
<btrm_prft_rate_3>4.48</btrm_prft_rate_3>
<etc></etc>
<sale_co>KEB하나은행(구.외환은행),우리은행,기업은행,KEB하나은행(구.하나은행),에스케이증권,메리츠종금증권,삼성증권,신영증권,한양증권,NH투자증권,교보증권,KDB대우증권,신한금융투자,유안타증권,아이비케이투자증권,이베스트투자증권,키움증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,현대증권,미래에셋생명보험,삼성생명보험,한화생명보험,펀드온라인코리아 주식회사,수협중앙회</sale_co>
<dcls_strt_day>20151001</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201510301534</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>570675</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>789485</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>789485</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>548449</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>548449</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>758736</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>758736</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1141350</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1141350</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1578970</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1578970</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1096897</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1096897</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1517473</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1517473</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1712026</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1712026</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2368455</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2368455</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1645346</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1645346</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2276209</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2276209</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>570675</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>859701</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>215538</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>215538</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>298180</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>298180</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>207143</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>207143</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>286567</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>286567</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>431076</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>431076</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>596361</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>596361</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>414287</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>859701</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>621430</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>621430</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>894541</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>894541</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>646615</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>646615</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>573134</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>573134</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>414287</pnsn_recp_amt>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>201510</dcls_month>
<fin_co_no>0010170</fin_co_no>
<kor_co_nm>하나유비에스자산운용</kor_co_nm>
<fin_prdt_cd>KR5102644667</fin_prdt_cd>
<fin_prdt_nm>하나UBSFirstClass연금증권투자신탁(제1호)[주식혼합]</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타</join_way>
<pnsn_kind>4</pnsn_kind>
<pnsn_kind_nm>연금저축펀드</pnsn_kind_nm>
<sale_strt_day>20070125</sale_strt_day>
<mntn_cnt>17189394854</mntn_cnt>
<prdt_type>431</prdt_type>
<prdt_type_nm>혼합주식형</prdt_type_nm>
<avg_prft_rate>1.43</avg_prft_rate>
<dcls_rate></dcls_rate>
<guar_rate></guar_rate>
<btrm_prft_rate_1>-4.66</btrm_prft_rate_1>
<btrm_prft_rate_2>1.94</btrm_prft_rate_2>
<btrm_prft_rate_3>5.33</btrm_prft_rate_3>
<etc></etc>
<sale_co>하나금융투자</sale_co>
<dcls_strt_day>20151001</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>201510301534</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>570947</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>789862</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>789862</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>548978</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>548978</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>759469</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>759469</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1141895</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1141895</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1579723</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1579723</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1097956</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1097956</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1518938</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1518938</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1712842</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1712842</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2369585</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2369585</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>1646934</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>1646934</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>2278406</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>570947</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>860531</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>860531</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>215641</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>215641</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>298323</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>298323</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>207343</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>207343</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>286844</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>286844</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>431282</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>431282</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>596645</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>30</pnsn_entr_age>
<pnsn_entr_age_nm>30세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>596645</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>414687</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>414687</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>573687</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>10</mon_paym_atm>
<mon_paym_atm_nm>100,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>573687</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>646923</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>646923</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>894968</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>20</mon_paym_atm>
<mon_paym_atm_nm>200,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>894968</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>60</pnsn_strt_age>
<pnsn_strt_age_nm>60세</pnsn_strt_age_nm>
<pnsn_recp_amt>622030</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>A</pnsn_recp_trm>
<pnsn_recp_trm_nm>10년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>10</paym_prd>
<paym_prd_nm>10년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>622030</pnsn_recp_amt>
				</option>
				<option>
<pnsn_recp_trm>B</pnsn_recp_trm>
<pnsn_recp_trm_nm>20년확정</pnsn_recp_trm_nm>
<pnsn_entr_age>40</pnsn_entr_age>
<pnsn_entr_age_nm>40세</pnsn_entr_age_nm>
<mon_paym_atm>30</mon_paym_atm>
<mon_paym_atm_nm>300,000원</mon_paym_atm_nm>
<paym_prd>20</paym_prd>
<paym_prd_nm>20년</paym_prd_nm>
<pnsn_strt_age>65</pnsn_strt_age>
<pnsn_strt_age_nm>65세</pnsn_strt_age_nm>
<pnsn_recp_amt>2278406</pnsn_recp_amt>
				</option>
			</options>
		</product>
	</products>
</result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=060000&pageNo=1

예제 요청결과(JSON)
{"result":{"prdt_div":"P","total_count":"102","max_page_no":"21","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","kor_co_nm":"하나유비에스자산운용","fin_prdt_nm":"하나UBS인Best연금증권투자신탁(제1호)[채권]","join_way":"영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타","pnsn_kind":"4","pnsn_kind_nm":"연금저축펀드","sale_strt_day":"20010201","mntn_cnt":73342945069,"prdt_type":"411","prdt_type_nm":"채권형","avg_prft_rate":4.05,"dcls_rate":null,"guar_rate":null,"btrm_prft_rate_1":2.96,"btrm_prft_rate_2":1.97,"btrm_prft_rate_3":3.35,"etc":null,"sale_co":"KEB하나은행(구.외환은행),KEB하나은행(구.하나은행),우리은행,기업은행,수협중앙회,에스케이증권,현대증권,메리츠종금증권,삼성증권,한양증권,NH투자증권,교보증권,KDB대우증권,신한금융투자,유안타증권,아이비케이투자증권,이베스트투자증권,키움증권,리딩투자증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,미래에셋생명보험,삼성생명보험,한화생명보험,펀드온라인코리아 주식회사,케이티비투자증권,유진투자증권","dcls_strt_day":"20151001","dcls_end_day":null,"fin_co_subm_day":"201510301534"},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","kor_co_nm":"하나유비에스자산운용","fin_prdt_nm":"하나UBS인Best연금증권투자신탁(제1호)[주식]","join_way":"영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타","pnsn_kind":"4","pnsn_kind_nm":"연금저축펀드","sale_strt_day":"20010201","mntn_cnt":814160555217,"prdt_type":"421","prdt_type_nm":"주식형","avg_prft_rate":8.07,"dcls_rate":null,"guar_rate":null,"btrm_prft_rate_1":-6.24,"btrm_prft_rate_2":2.26,"btrm_prft_rate_3":4.26,"etc":null,"sale_co":"경남은행,우리은행,부산은행,KEB하나은행(구.외환은행),기업은행,수협중앙회,신영증권,한양증권,NH투자증권,교보증권,대신증권,KDB대우증권,신한금융투자,유안타증권,에스케이증권,삼성생명보험,한화생명보험,펀드온라인코리아 주식회사,케이티비투자증권,엘아이지투자증권,아이비케이투자증권,이베스트투자증권,키움증권,리딩투자증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,현대증권,메리츠종금증권,삼성증권,미래에셋생명보험,KEB하나은행(구.하나은행)","dcls_strt_day":"20151001","dcls_end_day":null,"fin_co_subm_day":"201510301534"},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","kor_co_nm":"하나유비에스자산운용","fin_prdt_nm":"하나UBS인Best연금증권투자신탁(제1호)[국공채]","join_way":"영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타","pnsn_kind":"4","pnsn_kind_nm":"연금저축펀드","sale_strt_day":"20010202","mntn_cnt":27342275814,"prdt_type":"411","prdt_type_nm":"채권형","avg_prft_rate":4.05,"dcls_rate":null,"guar_rate":null,"btrm_prft_rate_1":2.9,"btrm_prft_rate_2":2.15,"btrm_prft_rate_3":3.07,"etc":null,"sale_co":"우리은행,에스케이증권,KEB하나은행(구.하나은행),수협중앙회,KDB대우증권,신영증권,이베스트투자증권,키움증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,메리츠종금증권,삼성증권,미래에셋생명보험,삼성생명보험,케이티비투자증권,아이비케이투자증권,NH투자증권","dcls_strt_day":"20151001","dcls_end_day":null,"fin_co_subm_day":"201510301534"},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","kor_co_nm":"하나유비에스자산운용","fin_prdt_nm":"하나UBS인Best연금증권투자신탁(제1호)[주식혼합]","join_way":"영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타","pnsn_kind":"4","pnsn_kind_nm":"연금저축펀드","sale_strt_day":"20010205","mntn_cnt":174743666758,"prdt_type":"431","prdt_type_nm":"혼합주식형","avg_prft_rate":8.63,"dcls_rate":null,"guar_rate":null,"btrm_prft_rate_1":-2.8,"btrm_prft_rate_2":1.66,"btrm_prft_rate_3":4.48,"etc":null,"sale_co":"KEB하나은행(구.외환은행),우리은행,기업은행,KEB하나은행(구.하나은행),에스케이증권,메리츠종금증권,삼성증권,신영증권,한양증권,NH투자증권,교보증권,KDB대우증권,신한금융투자,유안타증권,아이비케이투자증권,이베스트투자증권,키움증권,하나금융투자,하이투자증권,동부증권,에이치엠씨투자증권,한화투자증권,현대증권,미래에셋생명보험,삼성생명보험,한화생명보험,펀드온라인코리아 주식회사,수협중앙회","dcls_strt_day":"20151001","dcls_end_day":null,"fin_co_subm_day":"201510301534"},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","kor_co_nm":"하나유비에스자산운용","fin_prdt_nm":"하나UBSFirstClass연금증권투자신탁(제1호)[주식혼합]","join_way":"영업점,인터넷,스마트폰,모집인,전화(텔레뱅킹),기타","pnsn_kind":"4","pnsn_kind_nm":"연금저축펀드","sale_strt_day":"20070125","mntn_cnt":17189394854,"prdt_type":"431","prdt_type_nm":"혼합주식형","avg_prft_rate":1.43,"dcls_rate":null,"guar_rate":null,"btrm_prft_rate_1":-4.66,"btrm_prft_rate_2":1.94,"btrm_prft_rate_3":5.33,"etc":null,"sale_co":"하나금융투자","dcls_strt_day":"20151001","dcls_end_day":null,"fin_co_subm_day":"201510301534"}],"optionList":[{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":229566},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":840868},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":840868},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":623168},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":623168},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":862105},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":862105},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1215635},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1215635},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1681737},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1681737},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1246337},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1246337},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1724211},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1724211},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1823452},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1823452},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2522605},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2522605},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1869505},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1869505},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2586316},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2586316},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":607817},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":607817},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":976825},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":229566},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":317587},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":317587},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":235364},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":235364},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":325608},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":325608},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":459133},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":459133},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":635175},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":635175},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":470729},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":976825},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":706093},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":706093},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":952762},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":952762},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":688699},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":688699},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":651217},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":651217},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314204","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":470729},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":557199},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":770842},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":770842},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":522570},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":522570},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":722936},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":722936},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1114398},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1114398},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1541683},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1541683},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1045141},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1045141},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1445872},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1445872},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1671597},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1671597},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2312525},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2312525},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1567711},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1567711},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2168807},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2168807},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":557199},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":819136},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":210448},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":210448},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":291139},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":291139},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":197370},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":197370},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":273045},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":273045},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":420897},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":420897},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":582278},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":582278},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":394739},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":819136},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":592109},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":592109},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":873417},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":873417},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":631345},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":631345},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":546091},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":546091},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314212","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":394739},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":607960},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":841066},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":841066},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":623466},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":623466},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":862516},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":862516},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1215920},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1215920},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1682132},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1682132},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1246931},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1246931},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1725033},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1725033},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1823881},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1823881},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2523198},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2523198},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1870397},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1870397},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2587549},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2587549},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":607960},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":977291},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":229620},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":229620},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":317662},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":317662},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":235477},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":235477},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":325764},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":325764},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":459241},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":459241},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":635324},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":635324},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":470953},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":977291},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":706430},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":706430},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":952986},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":952986},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":688861},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":688861},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":651527},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":651527},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314352","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":470953},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":570675},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":789485},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":789485},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":548449},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":548449},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":758736},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":758736},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1141350},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1141350},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1578970},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1578970},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1096897},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1096897},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1517473},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1517473},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1712026},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1712026},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2368455},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2368455},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1645346},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1645346},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2276209},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2276209},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":570675},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":859701},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":215538},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":215538},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":298180},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":298180},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":207143},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":207143},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":286567},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":286567},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":431076},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":431076},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":596361},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":596361},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":414287},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":859701},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":621430},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":621430},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":894541},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":894541},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":646615},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":646615},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":573134},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":573134},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102314733","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":414287},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":570947},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":789862},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":789862},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":548978},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":548978},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":759469},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":759469},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1141895},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1141895},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1579723},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1579723},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1097956},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1097956},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1518938},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1518938},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1712842},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1712842},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2369585},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2369585},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":1646934},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":1646934},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":2278406},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":570947},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":860531},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":860531},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":215641},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":215641},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":298323},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":298323},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":207343},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":207343},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":286844},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":286844},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":431282},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":431282},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":596645},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"30","pnsn_entr_age_nm":"30세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":596645},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":414687},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":414687},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":573687},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"10","mon_paym_atm_nm":"100,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":573687},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":646923},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":646923},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":894968},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"20","mon_paym_atm_nm":"200,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":894968},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"60","pnsn_strt_age_nm":"60세","pnsn_recp_amt":622030},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"A","pnsn_recp_trm_nm":"10년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"10","paym_prd_nm":"10년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":622030},{"dcls_month":"201510","fin_co_no":"0010170","fin_prdt_cd":"KR5102644667","pnsn_recp_trm":"B","pnsn_recp_trm_nm":"20년확정","pnsn_entr_age":"40","pnsn_entr_age_nm":"40세","mon_paym_atm":"30","mon_paym_atm_nm":"300,000원","paym_prd":"20","paym_prd_nm":"20년","pnsn_strt_age":"65","pnsn_strt_age_nm":"65세","pnsn_recp_amt":2278406}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd**	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
pnsn_kind	연금종류
pnsn_kind_nm	연금종류명
sale_strt_day	판매 개시일
mntn_cnt	유지건수[단위: 건] 또는 설정액 [단위: 원]
prdt_type	상품유형
prdt_type_nm	상품유형명
dcls_rate	공시이율 [소수점 2자리]
guar_rate	최저 보증이율
btrm_prft_rate_1	과거 수익률1(전년도) [소수점 2자리]
btrm_prft_rate_2	과거 수익률2(전전년도) [소수점 2자리]
btrm_prft_rate_3	과거 수익률3(전전전년도) [소수점 2자리]
etc	기타사항
sale_co	판매사
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
intr_rate_type	저축 금리 유형
intr_rate_type_nm	저축 금리 유형명
rsrv_type	적립 유형
rsrv_type_nm	적립 유형명
save_trm	저축 기간 [단위: 개월]
intr_rate	저축 금리 [소수점 2자리]
intr_rate2	최고 우대금리 [소수점 2자리]
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
No	응답코드	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

## 주택담보대출 API 상세
요청URL
http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.{응답방식}

요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) mortgageLoanProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

예제 요청결과(XML)
<result>
		<err_cd>000</err_cd>
		<err_msg>정상</err_msg>
		<total_count>40</total_count>
		<max_page_no>8</max_page_no>
		<now_page_no>1</now_page_no>
			<products>
				<product>
					<baseinfo>
		<dcls_month>201601</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>1054</fin_prdt_cd>
		<fin_prdt_nm>우리아파트론</fin_prdt_nm>
		<join_way>영업점,모집인</join_way>
		<loan_inci_expn>- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)
		- 국민주택채권 매입 : 대출금액 × 120% × 1% × 채권할인율
		- 주택신보출연료(신규 주택구입시에 한함) : 0.09~0.29%</loan_inci_expn>
		<erly_rpay_fee>- 주택상환금액×1.4%×(대출잔액일수÷3년)</erly_rpay_fee>
		<dly_rate>- 3개월 미만 : 정상금리 + 7%
		- 3개월 이상 : 정상금리 + 8%
		  (최고 : 15%)</dly_rate>
		<loan_lmt>LTV 70%</loan_lmt>
		<dcls_strt_day>20160120</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201601191355</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>2.97</lend_rate_min>
		<lend_rate_max>4.78</lend_rate_max>
		<lend_rate_avg>3.2</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.97</lend_rate_min>
		<lend_rate_max>4.78</lend_rate_max>
		<lend_rate_avg>3.51</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.97</lend_rate_min>
		<lend_rate_max>4.78</lend_rate_max>
		<lend_rate_avg>3.21</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>2.97</lend_rate_min>
		<lend_rate_max>4.78</lend_rate_max>
		<lend_rate_avg>4.3</lend_rate_avg>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201601</dcls_month>
		<fin_co_no>0010001</fin_co_no>
		<kor_co_nm>우리은행</kor_co_nm>
		<fin_prdt_cd>1055</fin_prdt_cd>
		<fin_prdt_nm>우리부동산론</fin_prdt_nm>
		<join_way>영업점,모집인</join_way>
		<loan_inci_expn>- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)
		- 국민주택채권 매입 : 대출금액 × 120% × 1% × 채권할인율
		- 주택신보출연료(신규 주택구입시에 한함) : 0.09~0.29%</loan_inci_expn>
		<erly_rpay_fee>- 주택상환금액×1.4%×(대출잔액일수÷3년)</erly_rpay_fee>
		<dly_rate>- 3개월 미만 : 정상금리 + 7%
		- 3개월 이상 : 정상금리 + 8%
		  (최고 : 15%)</dly_rate>
		<loan_lmt>LTV 70%</loan_lmt>
		<dcls_strt_day>20160120</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201601191355</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>3.38</lend_rate_min>
		<lend_rate_max>4.96</lend_rate_max>
		<lend_rate_avg>3.86</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>3.38</lend_rate_min>
		<lend_rate_max>4.96</lend_rate_max>
		<lend_rate_avg>3.55</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>3.38</lend_rate_min>
		<lend_rate_max>4.96</lend_rate_max>
		<lend_rate_avg>3.57</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>3.38</lend_rate_min>
		<lend_rate_max>4.96</lend_rate_max>
		<lend_rate_avg>3.78</lend_rate_avg>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201601</dcls_month>
		<fin_co_no>0010002</fin_co_no>
		<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
		<fin_prdt_cd>SC002111/SC002015</fin_prdt_cd>
		<fin_prdt_nm>주택담보대출</fin_prdt_nm>
		<join_way>영업점</join_way>
		<loan_inci_expn>인지세 : 해당세액의 50% (대출금액 4천만원 미만 시 없음)
		국민주택채권 매입 : 대출금액 * 120% * 1% * 채권할인율
		화재보험료 : 아파트 및 주거용 오피스텔 외 물건지에 한함</loan_inci_expn>
		<erly_rpay_fee>조기상환원금 × 1.5% × [(3년-대출경과일수) / 3년]
		매년 대출잔액의 10% 까지 중도상환수수료 면제</erly_rpay_fee>
		<dly_rate>90일 미만 : 대출금리 + 8%
		90일 이상 : 대출금리 + 9% (최고 연체이자율 : 16%)</dly_rate>
		<loan_lmt>LTV 최대 70%
		최대 대출한도 : 2,000백만원</loan_lmt>
		<dcls_strt_day>20160120</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201601191302</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>3.51</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>3.92</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>3.2</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>2.88</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>3.54</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>3.21</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.46</lend_rate_min>
		<lend_rate_max>4.5</lend_rate_max>
		<lend_rate_avg>3.63</lend_rate_avg>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201601</dcls_month>
		<fin_co_no>0010006</fin_co_no>
		<kor_co_nm>한국씨티은행</kor_co_nm>
		<fin_prdt_cd>CT001M</fin_prdt_cd>
		<fin_prdt_nm>씨티주택담보대출</fin_prdt_nm>
		<join_way>영업점,모집인</join_way>
		<loan_inci_expn>1. 인지세 : 해당세액의 50%
		2. 국민주택채권 매입비용 : 대출금액 × 120% × 1% × 채권할인율
		3. 화재보험료(아파트 외 물건지에 한함)</loan_inci_expn>
		<erly_rpay_fee>중도상환금액×1.5%×(대출잔여일수÷대출기간*)
		* 대출기간이 3년을 초과하는 경우 3년</erly_rpay_fee>
		<dly_rate>1개월미만:대출금리+5%
		3개월미만:대출금리+6%
		3개월이상:대출금리+7%
		(최고 연체이자율 : 16.9%)</dly_rate>
		<loan_lmt>담보인정비율(LTV) 70%</loan_lmt>
		<dcls_strt_day>20160120</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201601191626</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>F</lend_rate_type>
		<lend_rate_type_nm>고정금리</lend_rate_type_nm>
		<lend_rate_min>2.58</lend_rate_min>
		<lend_rate_max>4.15</lend_rate_max>
		<lend_rate_avg>3.35</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.58</lend_rate_min>
		<lend_rate_max>4.15</lend_rate_max>
		<lend_rate_avg>3.12</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>D</rpay_type>
		<rpay_type_nm>분할상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>2.58</lend_rate_min>
		<lend_rate_max>4.15</lend_rate_max>
		<lend_rate_avg>3.31</lend_rate_avg>
						</option>
					</options>
				</product>
				<product>
					<baseinfo>
		<dcls_month>201601</dcls_month>
		<fin_co_no>0010016</fin_co_no>
		<kor_co_nm>대구은행</kor_co_nm>
		<fin_prdt_cd>20282101001040001</fin_prdt_cd>
		<fin_prdt_nm>일반주택담보대출(생활)</fin_prdt_nm>
		<join_way>영업점</join_way>
		<loan_inci_expn>1.인지세:해당세액의 50%
		2.국민주택채권매입비용 : 대출금액×115%×1%×채권할인율</loan_inci_expn>
		<erly_rpay_fee>중도상환수수료×1.0%×(3년-대출경과일수)÷3년(일수)</erly_rpay_fee>
		<dly_rate>3개월미만 : 대출금리+6.0%
		3개월이상 : 대출금리+7.0%
		(최고 연체이자율 : 연 15.0%)</dly_rate>
		<loan_lmt>담보인정비율(LTV) 70%</loan_lmt>
		<dcls_strt_day>20160120</dcls_strt_day>
		<dcls_end_day></dcls_end_day>
		<fin_co_subm_day>201601191910</fin_co_subm_day>
					</baseinfo>
					<options>
						<option>
		<mrtg_type>A</mrtg_type>
		<mrtg_type_nm>아파트</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>3.72</lend_rate_min>
		<lend_rate_max>5.28</lend_rate_max>
		<lend_rate_avg>3.43</lend_rate_avg>
						</option>
						<option>
		<mrtg_type>E</mrtg_type>
		<mrtg_type_nm>아파트외</mrtg_type_nm>
		<rpay_type>S</rpay_type>
		<rpay_type_nm>만기일시상환방식</rpay_type_nm>
		<lend_rate_type>C</lend_rate_type>
		<lend_rate_type_nm>변동금리</lend_rate_type_nm>
		<lend_rate_min>3.72</lend_rate_min>
		<lend_rate_max>5.28</lend_rate_max>
		<lend_rate_avg>3.45</lend_rate_avg>
						</option>
					</options>
				</product>
			</products>
		</result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

예제 요청결과(JSON)
{"result":{"prdt_div":"M","total_count":"40","max_page_no":"8","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1054","kor_co_nm":"우리은행","fin_prdt_nm":"우리아파트론","join_way":"영업점,모집인","loan_inci_expn":"- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)\n- 국민주택채권 매입 : 대출금액 × 120% × 1% × 채권할인율\n- 주택신보출연료(신규 주택구입시에 한함) : 0.09~0.29%","erly_rpay_fee":"- 주택상환금액×1.4%×(대출잔액일수÷3년)","dly_rate":"- 3개월 미만 : 정상금리 + 7%\n- 3개월 이상 : 정상금리 + 8%\n  (최고 : 15%)","loan_lmt":"LTV 70%","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191355"},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1055","kor_co_nm":"우리은행","fin_prdt_nm":"우리부동산론","join_way":"영업점,모집인","loan_inci_expn":"- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)\n- 국민주택채권 매입 : 대출금액 × 120% × 1% × 채권할인율\n- 주택신보출연료(신규 주택구입시에 한함) : 0.09~0.29%","erly_rpay_fee":"- 주택상환금액×1.4%×(대출잔액일수÷3년)","dly_rate":"- 3개월 미만 : 정상금리 + 7%\n- 3개월 이상 : 정상금리 + 8%\n  (최고 : 15%)","loan_lmt":"LTV 70%","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191355"},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"주택담보대출","join_way":"영업점","loan_inci_expn":"인지세 : 해당세액의 50% (대출금액 4천만원 미만 시 없음)\n국민주택채권 매입 : 대출금액 * 120% * 1% * 채권할인율\n화재보험료 : 아파트 및 주거용 오피스텔 외 물건지에 한함","erly_rpay_fee":"조기상환원금 × 1.5% × [(3년-대출경과일수) / 3년]\n매년 대출잔액의 10% 까지 중도상환수수료 면제","dly_rate":"90일 미만 : 대출금리 + 8%\n90일 이상 : 대출금리 + 9% (최고 연체이자율 : 16%)","loan_lmt":"LTV 최대 70%\n최대 대출한도 : 2,000백만원","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191302"},{"dcls_month":"201601","fin_co_no":"0010006","fin_prdt_cd":"CT001M","kor_co_nm":"한국씨티은행","fin_prdt_nm":"씨티주택담보대출","join_way":"영업점,모집인","loan_inci_expn":"1. 인지세 : 해당세액의 50%\n2. 국민주택채권 매입비용 : 대출금액 × 120% × 1% × 채권할인율\n3. 화재보험료(아파트 외 물건지에 한함)","erly_rpay_fee":"중도상환금액×1.5%×(대출잔여일수÷대출기간*)\n* 대출기간이 3년을 초과하는 경우 3년","dly_rate":"1개월미만:대출금리+5%\n3개월미만:대출금리+6%\n3개월이상:대출금리+7%\n(최고 연체이자율 : 16.9%)","loan_lmt":"담보인정비율(LTV) 70%","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191626"},{"dcls_month":"201601","fin_co_no":"0010016","fin_prdt_cd":"20282101001040001","kor_co_nm":"대구은행","fin_prdt_nm":"일반주택담보대출(생활)","join_way":"영업점","loan_inci_expn":"1.인지세:해당세액의 50%\n2.국민주택채권매입비용 : 대출금액×115%×1%×채권할인율","erly_rpay_fee":"중도상환수수료×1.0%×(3년-대출경과일수)÷3년(일수)","dly_rate":"3개월미만 : 대출금리+6.0%\n3개월이상 : 대출금리+7.0%\n(최고 연체이자율 : 연 15.0%)","loan_lmt":"담보인정비율(LTV) 70%","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191910"}],"optionList":[{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1054","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.97,"lend_rate_max":4.78,"lend_rate_avg":3.2},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1054","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.97,"lend_rate_max":4.78,"lend_rate_avg":3.51},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1054","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.97,"lend_rate_max":4.78,"lend_rate_avg":3.21},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1054","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.97,"lend_rate_max":4.78,"lend_rate_avg":4.3},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1055","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":3.38,"lend_rate_max":4.96,"lend_rate_avg":3.86},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1055","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3.38,"lend_rate_max":4.96,"lend_rate_avg":3.55},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1055","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3.38,"lend_rate_max":4.96,"lend_rate_avg":3.57},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"1055","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":3.38,"lend_rate_max":4.96,"lend_rate_avg":3.78},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":3.51},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":3.92},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":3.2},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":2.88},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":3.54},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":3.21},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002111/SC002015","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.46,"lend_rate_max":4.5,"lend_rate_avg":3.63},{"dcls_month":"201601","fin_co_no":"0010006","fin_prdt_cd":"CT001M","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.58,"lend_rate_max":4.15,"lend_rate_avg":3.35},{"dcls_month":"201601","fin_co_no":"0010006","fin_prdt_cd":"CT001M","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.58,"lend_rate_max":4.15,"lend_rate_avg":3.12},{"dcls_month":"201601","fin_co_no":"0010006","fin_prdt_cd":"CT001M","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"D","rpay_type_nm":"분할상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.58,"lend_rate_max":4.15,"lend_rate_avg":3.31},{"dcls_month":"201601","fin_co_no":"0010016","fin_prdt_cd":"20282101001040001","mrtg_type":"A","mrtg_type_nm":"아파트","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3.72,"lend_rate_max":5.28,"lend_rate_avg":3.43},{"dcls_month":"201601","fin_co_no":"0010016","fin_prdt_cd":"20282101001040001","mrtg_type":"E","mrtg_type_nm":"아파트외","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3.72,"lend_rate_max":5.28,"lend_rate_avg":3.45}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month ***	공시 제출월 [YYYYMM]
fin_co_no ***	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd***	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
loan_inci_expn	대출 부대비용
erly_rpay_fee	중도상환 수수료
dly_rate	연체 이자율
loan_lmt	대출한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
mrtg_type	담보유형 코드
mrtg_type_nm	담보유형
rpay_type	대출상환유형 코드
rpay_type_nm	대출상환유형 **
lend_rate_type	대출금리유형 코드
lend_rate_type_nm	대출금리유형
lend_rate_min	대출금리_최저 [소수점 2자리]
lend_rate_max	대출금리_최고 [소수점 2자리]
lend_rate_avg	전월 취급 평균금리 [소수점 2자리]
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** 원리금분할상환과 원금분할상환방식의 금리가 동일하여 상환유형은 분할상환방식과 일시상환방식 2가지로 제공됩니다.

*** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
No	응답코드	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

## 전세자금대출 API 상세
요청URL
http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.{응답방식}

요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) rentHouseLoanProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

예제 요청결과(XML)
        <result>
        <err_cd>000</err_cd>
        <err_msg>정상</err_msg>
        <total_count>30</total_count>
        <max_page_no>6</max_page_no>
        <now_page_no>1</now_page_no>
            <products>
                <product>
                    <baseinfo>
        <dcls_month>201601</dcls_month>
        <fin_co_no>0010001</fin_co_no>
        <kor_co_nm>우리은행</kor_co_nm>
        <fin_prdt_cd>203105601</fin_prdt_cd>
        <fin_prdt_nm>우리전세론(주택보증)</fin_prdt_nm>
        <join_way>영업점,모집인</join_way>
        <loan_inci_expn>- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)
        - 주택신보출연료 : 0.29%
        - 주택신보보증료 : 연 0.18 ~ 연 0.50%</loan_inci_expn>
        <erly_rpay_fee>- 주택상환금액×0.7%×(대출잔액일수÷3년)</erly_rpay_fee>
        <dly_rate>- 3개월 미만 : 정상금리 + 7%
        - 3개월 이상 : 정상금리 + 8%
          (최고: 15%)</dly_rate>
        <loan_lmt>최대2.2억원</loan_lmt>
        <dcls_strt_day>20160120</dcls_strt_day>
        <dcls_end_day></dcls_end_day>
        <fin_co_subm_day>201601191355</fin_co_subm_day>
                    </baseinfo>
                    <options>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>F</lend_rate_type>
        <lend_rate_type_nm>고정금리</lend_rate_type_nm>
        <lend_rate_min>2.97</lend_rate_min>
        <lend_rate_max>4.82</lend_rate_max>
        <lend_rate_avg>4.06</lend_rate_avg>
                        </option>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>C</lend_rate_type>
        <lend_rate_type_nm>변동금리</lend_rate_type_nm>
        <lend_rate_min>2.97</lend_rate_min>
        <lend_rate_max>4.82</lend_rate_max>
        <lend_rate_avg>2.94</lend_rate_avg>
                        </option>
                    </options>
                </product>
                <product>
                    <baseinfo>
        <dcls_month>201601</dcls_month>
        <fin_co_no>0010001</fin_co_no>
        <kor_co_nm>우리은행</kor_co_nm>
        <fin_prdt_cd>203105611</fin_prdt_cd>
        <fin_prdt_nm>우리전세론(서울보증)</fin_prdt_nm>
        <join_way>영업점,모집인</join_way>
        <loan_inci_expn>- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)
        - 주택신보출연료 : 0.29%
        - 질권설정, 채권양도통지 비용 : 3만원</loan_inci_expn>
        <erly_rpay_fee>- 주택상환금액×0.7%×(대출잔액일수÷3년)</erly_rpay_fee>
        <dly_rate>- 3개월 미만 : 정상금리 + 7%
        - 3개월 이상 : 정상금리 + 8%
          (최고: 15%)</dly_rate>
        <loan_lmt>최대3억원</loan_lmt>
        <dcls_strt_day>20160120</dcls_strt_day>
        <dcls_end_day></dcls_end_day>
        <fin_co_subm_day>201601191355</fin_co_subm_day>
                    </baseinfo>
                    <options>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>F</lend_rate_type>
        <lend_rate_type_nm>고정금리</lend_rate_type_nm>
        <lend_rate_min>3.37</lend_rate_min>
        <lend_rate_max>5.22</lend_rate_max>
        <lend_rate_avg>4.43</lend_rate_avg>
                        </option>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>C</lend_rate_type>
        <lend_rate_type_nm>변동금리</lend_rate_type_nm>
        <lend_rate_min>3.37</lend_rate_min>
        <lend_rate_max>5.22</lend_rate_max>
        <lend_rate_avg>3.32</lend_rate_avg>
                        </option>
                    </options>
                </product>
                <product>
                    <baseinfo>
        <dcls_month>201601</dcls_month>
        <fin_co_no>0010002</fin_co_no>
        <kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
        <fin_prdt_cd>SC002013SC002003</fin_prdt_cd>
        <fin_prdt_nm>전세담보대출</fin_prdt_nm>
        <join_way>영업점</join_way>
        <loan_inci_expn>인지세 : 해당세액의 50% (대출금액 4천만원 미만시 없음)</loan_inci_expn>
        <erly_rpay_fee>중도상환금액× 1.5%× (대출잔여일수 ÷ 대출기간 총일수)</erly_rpay_fee>
        <dly_rate>90일 미만 : 대출금리 + 8%
        90일 이상 : 대출금리 + 9% (최고 연체이자율 : 16%)</dly_rate>
        <loan_lmt>최대 3억원</loan_lmt>
        <dcls_strt_day>20160120</dcls_strt_day>
        <dcls_end_day></dcls_end_day>
        <fin_co_subm_day>201601191303</fin_co_subm_day>
                    </baseinfo>
                    <options>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>C</lend_rate_type>
        <lend_rate_type_nm>변동금리</lend_rate_type_nm>
        <lend_rate_min>3</lend_rate_min>
        <lend_rate_max>5.67</lend_rate_max>
        <lend_rate_avg>3.26</lend_rate_avg>
                        </option>
                    </options>
                </product>
                <product>
                    <baseinfo>
        <dcls_month>201601</dcls_month>
        <fin_co_no>0010006</fin_co_no>
        <kor_co_nm>한국씨티은행</kor_co_nm>
        <fin_prdt_cd>CT001K</fin_prdt_cd>
        <fin_prdt_nm>씨티전세담보대출</fin_prdt_nm>
        <join_way>영업점,모집인</join_way>
        <loan_inci_expn>1. 인지세 : 해당세액의 50%
        2. 질권설정 통지 수수료</loan_inci_expn>
        <erly_rpay_fee>중도상환금액×1.5%×(대출잔여일수÷대출기간*)
        * 대출기간이 3년을 초과하는 경우 3년</erly_rpay_fee>
        <dly_rate>1개월미만:대출금리+5%
        3개월미만:대출금리+6%
        3개월이상:대출금리+7%
        (최고 연체이자율 : 16.9%)</dly_rate>
        <loan_lmt>3억원</loan_lmt>
        <dcls_strt_day>20160120</dcls_strt_day>
        <dcls_end_day></dcls_end_day>
        <fin_co_subm_day>201601191626</fin_co_subm_day>
                    </baseinfo>
                    <options>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>C</lend_rate_type>
        <lend_rate_type_nm>변동금리</lend_rate_type_nm>
        <lend_rate_min>3.71</lend_rate_min>
        <lend_rate_max>3.91</lend_rate_max>
        <lend_rate_avg>3.78</lend_rate_avg>
                        </option>
                    </options>
                </product>
                <product>
                    <baseinfo>
        <dcls_month>201601</dcls_month>
        <fin_co_no>0010016</fin_co_no>
        <kor_co_nm>대구은행</kor_co_nm>
        <fin_prdt_cd>20460801000001001</fin_prdt_cd>
        <fin_prdt_nm>DGB전세보증대출</fin_prdt_nm>
        <join_way>영업점</join_way>
        <loan_inci_expn>1.인지세:해당세액의 50%
        2.보증료
          1억이하:연0.18%
          1억초과~4억이하:연0.28%
          4억초과~6억이하:연0.5%</loan_inci_expn>
        <erly_rpay_fee>중도상환금액x1.0%x(대출잔여일수 ÷ 3년)</erly_rpay_fee>
        <dly_rate>3개월미만 : 대출금리+6.0%
        3개월이상 : 대출금리+7.0%
        (최고 연체이자율 : 연 15.0%)</dly_rate>
        <loan_lmt>200백만원</loan_lmt>
        <dcls_strt_day>20160120</dcls_strt_day>
        <dcls_end_day></dcls_end_day>
        <fin_co_subm_day>201601191849</fin_co_subm_day>
                    </baseinfo>
                    <options>
                        <option>
        <rpay_type>S</rpay_type>
        <rpay_type_nm>만기일시상환방식</rpay_type_nm>
        <lend_rate_type>C</lend_rate_type>
        <lend_rate_type_nm>변동금리</lend_rate_type_nm>
        <lend_rate_min>2.78</lend_rate_min>
        <lend_rate_max>7.09</lend_rate_max>
        <lend_rate_avg>3.31</lend_rate_avg>
                        </option>
                    </options>
                </product>
            </products>
        </result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

예제 요청결과(JSON)
{"result":{"prdt_div":"R","total_count":"30","max_page_no":"6","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"203105601","kor_co_nm":"우리은행","fin_prdt_nm":"우리전세론(주택보증)","join_way":"영업점,모집인","loan_inci_expn":"- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)\n- 주택신보출연료 : 0.29%\n- 주택신보보증료 : 연 0.18 ~ 연 0.50%","erly_rpay_fee":"- 주택상환금액×0.7%×(대출잔액일수÷3년)","dly_rate":"- 3개월 미만 : 정상금리 + 7%\n- 3개월 이상 : 정상금리 + 8%\n  (최고: 15%)","loan_lmt":"최대2.2억원","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191355"},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"203105611","kor_co_nm":"우리은행","fin_prdt_nm":"우리전세론(서울보증)","join_way":"영업점,모집인","loan_inci_expn":"- 인지세 : 해당세액의 50%(대출금액 4천만원 이하시 없음)\n- 주택신보출연료 : 0.29%\n- 질권설정, 채권양도통지 비용 : 3만원","erly_rpay_fee":"- 주택상환금액×0.7%×(대출잔액일수÷3년)","dly_rate":"- 3개월 미만 : 정상금리 + 7%\n- 3개월 이상 : 정상금리 + 8%\n  (최고: 15%)","loan_lmt":"최대3억원","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191355"},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002013SC002003","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"전세담보대출","join_way":"영업점","loan_inci_expn":"인지세 : 해당세액의 50% (대출금액 4천만원 미만시 없음)","erly_rpay_fee":"중도상환금액× 1.5%× (대출잔여일수 ÷ 대출기간 총일수)","dly_rate":"90일 미만 : 대출금리 + 8%\n90일 이상 : 대출금리 + 9% (최고 연체이자율 : 16%)","loan_lmt":"최대 3억원","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191303"},{"dcls_month":"201601","fin_co_no":"0010006","fin_prdt_cd":"CT001K","kor_co_nm":"한국씨티은행","fin_prdt_nm":"씨티전세담보대출","join_way":"영업점,모집인","loan_inci_expn":"1. 인지세 : 해당세액의 50%\n2. 질권설정 통지 수수료","erly_rpay_fee":"중도상환금액×1.5%×(대출잔여일수÷대출기간*)\n* 대출기간이 3년을 초과하는 경우 3년","dly_rate":"1개월미만:대출금리+5%\n3개월미만:대출금리+6%\n3개월이상:대출금리+7%\n(최고 연체이자율 : 16.9%)","loan_lmt":"3억원","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191626"},{"dcls_month":"201601","fin_co_no":"0010016","fin_prdt_cd":"20460801000001001","kor_co_nm":"대구은행","fin_prdt_nm":"DGB전세보증대출","join_way":"영업점","loan_inci_expn":"1.인지세:해당세액의 50%\n2.보증료 \n  1억이하:연0.18%\n  1억초과~4억이하:연0.28%\n  4억초과~6억이하:연0.5%","erly_rpay_fee":"중도상환금액x1.0%x(대출잔여일수 ÷ 3년)","dly_rate":"3개월미만 : 대출금리+6.0%\n3개월이상 : 대출금리+7.0%\n(최고 연체이자율 : 연 15.0%)","loan_lmt":"200백만원","dcls_strt_day":"20160120","dcls_end_day":null,"fin_co_subm_day":"201601191849"}],"optionList":[{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"203105601","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":2.97,"lend_rate_max":4.82,"lend_rate_avg":4.06},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"203105601","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.97,"lend_rate_max":4.82,"lend_rate_avg":2.94},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"203105611","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"F","lend_rate_type_nm":"고정금리","lend_rate_min":3.37,"lend_rate_max":5.22,"lend_rate_avg":4.43},{"dcls_month":"201601","fin_co_no":"0010001","fin_prdt_cd":"203105611","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3.37,"lend_rate_max":5.22,"lend_rate_avg":3.32},{"dcls_month":"201601","fin_co_no":"0010002","fin_prdt_cd":"SC002013SC002003","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3,"lend_rate_max":5.67,"lend_rate_avg":3.26},{"dcls_month":"201601","fin_co_no":"0010006","fin_prdt_cd":"CT001K","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":3.71,"lend_rate_max":3.91,"lend_rate_avg":3.78},{"dcls_month":"201601","fin_co_no":"0010016","fin_prdt_cd":"20460801000001001","rpay_type":"S","rpay_type_nm":"만기일시상환방식","lend_rate_type":"C","lend_rate_type_nm":"변동금리","lend_rate_min":2.78,"lend_rate_max":7.09,"lend_rate_avg":3.31}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month ***	공시 제출월 [YYYYMM]
fin_co_no ***	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd***	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
loan_inci_expn	대출 부대비용
erly_rpay_fee	중도상환 수수료
dly_rate	연체 이자율
loan_lmt	대출한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
rpay_type	대출상환유형 코드
rpay_type_nm	대출상환유형 **
lend_rate_type	대출금리유형 코드
lend_rate_type_nm	대출금리유형
lend_rate_min	대출금리_최저 [소수점 2자리]
lend_rate_max	대출금리_최고 [소수점 2자리]
lend_rate_avg	전월 취급 평균금리 [소수점 2자리]
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** 원리금분할상환과 원금분할상환방식의 금리가 동일하여 상환유형은 분할상환방식과 일시상환방식 2가지로 제공됩니다.

*** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
No	응답코드	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

## 개인신용대출 API 상세
요청URL
http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.{응답방식}

요청변수
요청변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) creditLoanProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나
예제 URL(XML)
http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

예제 요청결과(XML)
<result>
<err_cd>000</err_cd>
<err_msg>정상</err_msg>
<total_count>45</total_count>
<max_page_no>9</max_page_no>
<now_page_no>1</now_page_no>
	<products>
		<product>
			<baseinfo>
<dcls_month>202102</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>CR0001A</fin_prdt_cd>
<fin_prdt_nm>개인신용대출</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<cb_name>KCB</cb_name>
<crdt_prdt_type>1</crdt_prdt_type>
<crdt_prdt_type_nm>일반신용대출</crdt_prdt_type_nm>
<dcls_strt_day>20210222</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>202102171438</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<crdt_lend_rate_type>A</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>대출금리</crdt_lend_rate_type_nm>
<crdt_grad_1>2.62</crdt_grad_1>
<crdt_grad_4>2.89</crdt_grad_4>
<crdt_grad_5>3.1</crdt_grad_5>
<crdt_grad_6>3.51</crdt_grad_6>
<crdt_grad_10>4.83</crdt_grad_10>
<crdt_grad_11>4.44</crdt_grad_11>
<crdt_grad_12>2.48</crdt_grad_12>
<crdt_grad_13>10.87</crdt_grad_13>
<crdt_grad_avg>2.93</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>B</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>기준금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.78</crdt_grad_1>
<crdt_grad_4>.83</crdt_grad_4>
<crdt_grad_5>.83</crdt_grad_5>
<crdt_grad_6>.83</crdt_grad_6>
<crdt_grad_10>.84</crdt_grad_10>
<crdt_grad_11>.75</crdt_grad_11>
<crdt_grad_12>.68</crdt_grad_12>
<crdt_grad_13>1.42</crdt_grad_13>
<crdt_grad_avg>.81</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>C</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가산금리</crdt_lend_rate_type_nm>
<crdt_grad_1>2.44</crdt_grad_1>
<crdt_grad_4>2.47</crdt_grad_4>
<crdt_grad_5>2.71</crdt_grad_5>
<crdt_grad_6>3.09</crdt_grad_6>
<crdt_grad_10>4.2</crdt_grad_10>
<crdt_grad_11>3.75</crdt_grad_11>
<crdt_grad_12>1.8</crdt_grad_12>
<crdt_grad_13>9.45</crdt_grad_13>
<crdt_grad_avg>2.59</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>D</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가감조정금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.6</crdt_grad_1>
<crdt_grad_4>.41</crdt_grad_4>
<crdt_grad_5>.44</crdt_grad_5>
<crdt_grad_6>.41</crdt_grad_6>
<crdt_grad_10>.21</crdt_grad_10>
<crdt_grad_11>.06</crdt_grad_11>
<crdt_grad_12>0</crdt_grad_12>
<crdt_grad_13>0</crdt_grad_13>
<crdt_grad_avg>.47</crdt_grad_avg>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>202102</dcls_month>
<fin_co_no>0010001</fin_co_no>
<kor_co_nm>우리은행</kor_co_nm>
<fin_prdt_cd>CR0001B</fin_prdt_cd>
<fin_prdt_nm>개인신용대출</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<cb_name>KCB</cb_name>
<crdt_prdt_type>2</crdt_prdt_type>
<crdt_prdt_type_nm>마이너스한도대출</crdt_prdt_type_nm>
<dcls_strt_day>20210222</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>202102171438</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<crdt_lend_rate_type>A</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>대출금리</crdt_lend_rate_type_nm>
<crdt_grad_1>3.12</crdt_grad_1>
<crdt_grad_4>3.25</crdt_grad_4>
<crdt_grad_5>3.34</crdt_grad_5>
<crdt_grad_6>3.61</crdt_grad_6>
<crdt_grad_10>4.09</crdt_grad_10>
<crdt_grad_11>5.86</crdt_grad_11>
<crdt_grad_12>2.56</crdt_grad_12>
<crdt_grad_13>12</crdt_grad_13>
<crdt_grad_avg>3.22</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>B</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>기준금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.8</crdt_grad_1>
<crdt_grad_4>.82</crdt_grad_4>
<crdt_grad_5>.81</crdt_grad_5>
<crdt_grad_6>.81</crdt_grad_6>
<crdt_grad_10>.83</crdt_grad_10>
<crdt_grad_11>.87</crdt_grad_11>
<crdt_grad_12>1.2</crdt_grad_12>
<crdt_grad_13>.89</crdt_grad_13>
<crdt_grad_avg>.81</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>C</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가산금리</crdt_lend_rate_type_nm>
<crdt_grad_1>2.54</crdt_grad_1>
<crdt_grad_4>2.5</crdt_grad_4>
<crdt_grad_5>2.68</crdt_grad_5>
<crdt_grad_6>2.92</crdt_grad_6>
<crdt_grad_10>3.17</crdt_grad_10>
<crdt_grad_11>4.89</crdt_grad_11>
<crdt_grad_12>1.36</crdt_grad_12>
<crdt_grad_13>10.81</crdt_grad_13>
<crdt_grad_avg>2.56</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>D</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가감조정금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.22</crdt_grad_1>
<crdt_grad_4>.07</crdt_grad_4>
<crdt_grad_5>.15</crdt_grad_5>
<crdt_grad_6>.12</crdt_grad_6>
<crdt_grad_10>-.09</crdt_grad_10>
<crdt_grad_11>.1</crdt_grad_11>
<crdt_grad_12>0</crdt_grad_12>
<crdt_grad_13>.3</crdt_grad_13>
<crdt_grad_avg>.15</crdt_grad_avg>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>202102</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>SC001217</fin_prdt_cd>
<fin_prdt_nm>개인신용대출</fin_prdt_nm>
<join_way>영업점,스마트폰</join_way>
<cb_name>NICE</cb_name>
<crdt_prdt_type>1</crdt_prdt_type>
<crdt_prdt_type_nm>일반신용대출</crdt_prdt_type_nm>
<dcls_strt_day>20210222</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>202102221605</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<crdt_lend_rate_type>D</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가감조정금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.49</crdt_grad_1>
<crdt_grad_4>.36</crdt_grad_4>
<crdt_grad_5>.23</crdt_grad_5>
<crdt_grad_6>.07</crdt_grad_6>
<crdt_grad_10>0</crdt_grad_10>
<crdt_grad_11>0</crdt_grad_11>
<crdt_grad_12>.03</crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>.42</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>C</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가산금리</crdt_lend_rate_type_nm>
<crdt_grad_1>3.64</crdt_grad_1>
<crdt_grad_4>5.11</crdt_grad_4>
<crdt_grad_5>6.99</crdt_grad_5>
<crdt_grad_6>6.9</crdt_grad_6>
<crdt_grad_10>5.91</crdt_grad_10>
<crdt_grad_11>5.67</crdt_grad_11>
<crdt_grad_12>7.36</crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>4.44</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>B</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>기준금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.67</crdt_grad_1>
<crdt_grad_4>.67</crdt_grad_4>
<crdt_grad_5>.67</crdt_grad_5>
<crdt_grad_6>.67</crdt_grad_6>
<crdt_grad_10>.66</crdt_grad_10>
<crdt_grad_11>.67</crdt_grad_11>
<crdt_grad_12>.66</crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>.67</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>A</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>대출금리</crdt_lend_rate_type_nm>
<crdt_grad_1>3.82</crdt_grad_1>
<crdt_grad_4>5.42</crdt_grad_4>
<crdt_grad_5>7.43</crdt_grad_5>
<crdt_grad_6>7.5</crdt_grad_6>
<crdt_grad_10>6.57</crdt_grad_10>
<crdt_grad_11>6.34</crdt_grad_11>
<crdt_grad_12>7.99</crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>4.69</crdt_grad_avg>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>202102</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>SC001217_1</fin_prdt_cd>
<fin_prdt_nm>개인신용대출</fin_prdt_nm>
<join_way>영업점,스마트폰</join_way>
<cb_name>NICE</cb_name>
<crdt_prdt_type>2</crdt_prdt_type>
<crdt_prdt_type_nm>마이너스한도대출</crdt_prdt_type_nm>
<dcls_strt_day>20210222</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>202102221605</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<crdt_lend_rate_type>A</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>대출금리</crdt_lend_rate_type_nm>
<crdt_grad_1>4.49</crdt_grad_1>
<crdt_grad_4>5.08</crdt_grad_4>
<crdt_grad_5>6.67</crdt_grad_5>
<crdt_grad_6>6.79</crdt_grad_6>
<crdt_grad_10></crdt_grad_10>
<crdt_grad_11></crdt_grad_11>
<crdt_grad_12></crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>4.62</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>B</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>기준금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.67</crdt_grad_1>
<crdt_grad_4>.67</crdt_grad_4>
<crdt_grad_5>.67</crdt_grad_5>
<crdt_grad_6>.66</crdt_grad_6>
<crdt_grad_10></crdt_grad_10>
<crdt_grad_11></crdt_grad_11>
<crdt_grad_12></crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>.67</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>C</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가산금리</crdt_lend_rate_type_nm>
<crdt_grad_1>4.1</crdt_grad_1>
<crdt_grad_4>4.63</crdt_grad_4>
<crdt_grad_5>6</crdt_grad_5>
<crdt_grad_6>6.24</crdt_grad_6>
<crdt_grad_10></crdt_grad_10>
<crdt_grad_11></crdt_grad_11>
<crdt_grad_12></crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>4.22</crdt_grad_avg>
				</option>
				<option>
<crdt_lend_rate_type>D</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>가감조정금리</crdt_lend_rate_type_nm>
<crdt_grad_1>.28</crdt_grad_1>
<crdt_grad_4>.22</crdt_grad_4>
<crdt_grad_5>0</crdt_grad_5>
<crdt_grad_6>.11</crdt_grad_6>
<crdt_grad_10></crdt_grad_10>
<crdt_grad_11></crdt_grad_11>
<crdt_grad_12></crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>.27</crdt_grad_avg>
				</option>
			</options>
		</product>
		<product>
			<baseinfo>
<dcls_month>202102</dcls_month>
<fin_co_no>0010002</fin_co_no>
<kor_co_nm>한국스탠다드차타드은행</kor_co_nm>
<fin_prdt_cd>WR0002F</fin_prdt_cd>
<fin_prdt_nm>장기카드대출</fin_prdt_nm>
<join_way>인터넷,스마트폰,전화(텔레뱅킹),기타</join_way>
<cb_name>KCB</cb_name>
<crdt_prdt_type>3</crdt_prdt_type>
<crdt_prdt_type_nm>장기카드대출(카드론)</crdt_prdt_type_nm>
<dcls_strt_day>20210221</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>202102100935</fin_co_subm_day>
			</baseinfo>
			<options>
				<option>
<crdt_lend_rate_type>A</crdt_lend_rate_type>
<crdt_lend_rate_type_nm>대출금리</crdt_lend_rate_type_nm>
<crdt_grad_1>8.7</crdt_grad_1>
<crdt_grad_4>9.58</crdt_grad_4>
<crdt_grad_5>11.93</crdt_grad_5>
<crdt_grad_6>13.13</crdt_grad_6>
<crdt_grad_10>13.64</crdt_grad_10>
<crdt_grad_11></crdt_grad_11>
<crdt_grad_12></crdt_grad_12>
<crdt_grad_13></crdt_grad_13>
<crdt_grad_avg>10.67</crdt_grad_avg>
				</option>
			</options>
		</product>
	</products>
</result>
예제 URL(JSON)
http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

예제 요청결과(JSON)
{"result":{"prdt_div":"C","total_count":"45","max_page_no":"9","now_page_no":"1","err_cd":"000","err_msg":"정상","baseList":[{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001A","crdt_prdt_type":"1","kor_co_nm":"우리은행","fin_prdt_nm":"개인신용대출","join_way":"영업점,인터넷,스마트폰","cb_name":"KCB","crdt_prdt_type_nm":"일반신용대출","dcls_strt_day":"20210222","dcls_end_day":null,"fin_co_subm_day":"202102171438"},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001B","crdt_prdt_type":"2","kor_co_nm":"우리은행","fin_prdt_nm":"개인신용대출","join_way":"영업점,인터넷,스마트폰","cb_name":"KCB","crdt_prdt_type_nm":"마이너스한도대출","dcls_strt_day":"20210222","dcls_end_day":null,"fin_co_subm_day":"202102171438"},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217","crdt_prdt_type":"1","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"개인신용대출","join_way":"영업점,스마트폰","cb_name":"NICE","crdt_prdt_type_nm":"일반신용대출","dcls_strt_day":"20210222","dcls_end_day":null,"fin_co_subm_day":"202102221605"},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217_1","crdt_prdt_type":"2","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"개인신용대출","join_way":"영업점,스마트폰","cb_name":"NICE","crdt_prdt_type_nm":"마이너스한도대출","dcls_strt_day":"20210222","dcls_end_day":null,"fin_co_subm_day":"202102221605"},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"WR0002F","crdt_prdt_type":"3","kor_co_nm":"한국스탠다드차타드은행","fin_prdt_nm":"장기카드대출","join_way":"인터넷,스마트폰,전화(텔레뱅킹),기타","cb_name":"KCB","crdt_prdt_type_nm":"장기카드대출(카드론)","dcls_strt_day":"20210221","dcls_end_day":null,"fin_co_subm_day":"202102100935"}],"optionList":[{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001A","crdt_prdt_type":"1","crdt_lend_rate_type":"A","crdt_lend_rate_type_nm":"대출금리","crdt_grad_1":2.62,"crdt_grad_4":2.89,"crdt_grad_5":3.1,"crdt_grad_6":3.51,"crdt_grad_10":4.83,"crdt_grad_11":4.44,"crdt_grad_12":2.48,"crdt_grad_13":10.87,"crdt_grad_avg":2.93},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001A","crdt_prdt_type":"1","crdt_lend_rate_type":"B","crdt_lend_rate_type_nm":"기준금리","crdt_grad_1":0.78,"crdt_grad_4":0.83,"crdt_grad_5":0.83,"crdt_grad_6":0.83,"crdt_grad_10":0.84,"crdt_grad_11":0.75,"crdt_grad_12":0.68,"crdt_grad_13":1.42,"crdt_grad_avg":0.81},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001A","crdt_prdt_type":"1","crdt_lend_rate_type":"C","crdt_lend_rate_type_nm":"가산금리","crdt_grad_1":2.44,"crdt_grad_4":2.47,"crdt_grad_5":2.71,"crdt_grad_6":3.09,"crdt_grad_10":4.2,"crdt_grad_11":3.75,"crdt_grad_12":1.8,"crdt_grad_13":9.45,"crdt_grad_avg":2.59},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001A","crdt_prdt_type":"1","crdt_lend_rate_type":"D","crdt_lend_rate_type_nm":"가감조정금리","crdt_grad_1":0.6,"crdt_grad_4":0.41,"crdt_grad_5":0.44,"crdt_grad_6":0.41,"crdt_grad_10":0.21,"crdt_grad_11":0.06,"crdt_grad_12":0,"crdt_grad_13":0,"crdt_grad_avg":0.47},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001B","crdt_prdt_type":"2","crdt_lend_rate_type":"A","crdt_lend_rate_type_nm":"대출금리","crdt_grad_1":3.12,"crdt_grad_4":3.25,"crdt_grad_5":3.34,"crdt_grad_6":3.61,"crdt_grad_10":4.09,"crdt_grad_11":5.86,"crdt_grad_12":2.56,"crdt_grad_13":12,"crdt_grad_avg":3.22},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001B","crdt_prdt_type":"2","crdt_lend_rate_type":"B","crdt_lend_rate_type_nm":"기준금리","crdt_grad_1":0.8,"crdt_grad_4":0.82,"crdt_grad_5":0.81,"crdt_grad_6":0.81,"crdt_grad_10":0.83,"crdt_grad_11":0.87,"crdt_grad_12":1.2,"crdt_grad_13":0.89,"crdt_grad_avg":0.81},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001B","crdt_prdt_type":"2","crdt_lend_rate_type":"C","crdt_lend_rate_type_nm":"가산금리","crdt_grad_1":2.54,"crdt_grad_4":2.5,"crdt_grad_5":2.68,"crdt_grad_6":2.92,"crdt_grad_10":3.17,"crdt_grad_11":4.89,"crdt_grad_12":1.36,"crdt_grad_13":10.81,"crdt_grad_avg":2.56},{"dcls_month":"202102","fin_co_no":"0010001","fin_prdt_cd":"CR0001B","crdt_prdt_type":"2","crdt_lend_rate_type":"D","crdt_lend_rate_type_nm":"가감조정금리","crdt_grad_1":0.22,"crdt_grad_4":0.07,"crdt_grad_5":0.15,"crdt_grad_6":0.12,"crdt_grad_10":-0.09,"crdt_grad_11":0.1,"crdt_grad_12":0,"crdt_grad_13":0.3,"crdt_grad_avg":0.15},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217","crdt_prdt_type":"1","crdt_lend_rate_type":"D","crdt_lend_rate_type_nm":"가감조정금리","crdt_grad_1":0.49,"crdt_grad_4":0.36,"crdt_grad_5":0.23,"crdt_grad_6":0.07,"crdt_grad_10":0,"crdt_grad_11":0,"crdt_grad_12":0.03,"crdt_grad_13":null,"crdt_grad_avg":0.42},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217","crdt_prdt_type":"1","crdt_lend_rate_type":"C","crdt_lend_rate_type_nm":"가산금리","crdt_grad_1":3.64,"crdt_grad_4":5.11,"crdt_grad_5":6.99,"crdt_grad_6":6.9,"crdt_grad_10":5.91,"crdt_grad_11":5.67,"crdt_grad_12":7.36,"crdt_grad_13":null,"crdt_grad_avg":4.44},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217","crdt_prdt_type":"1","crdt_lend_rate_type":"B","crdt_lend_rate_type_nm":"기준금리","crdt_grad_1":0.67,"crdt_grad_4":0.67,"crdt_grad_5":0.67,"crdt_grad_6":0.67,"crdt_grad_10":0.66,"crdt_grad_11":0.67,"crdt_grad_12":0.66,"crdt_grad_13":null,"crdt_grad_avg":0.67},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217","crdt_prdt_type":"1","crdt_lend_rate_type":"A","crdt_lend_rate_type_nm":"대출금리","crdt_grad_1":3.82,"crdt_grad_4":5.42,"crdt_grad_5":7.43,"crdt_grad_6":7.5,"crdt_grad_10":6.57,"crdt_grad_11":6.34,"crdt_grad_12":7.99,"crdt_grad_13":null,"crdt_grad_avg":4.69},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217_1","crdt_prdt_type":"2","crdt_lend_rate_type":"A","crdt_lend_rate_type_nm":"대출금리","crdt_grad_1":4.49,"crdt_grad_4":5.08,"crdt_grad_5":6.67,"crdt_grad_6":6.79,"crdt_grad_10":null,"crdt_grad_11":null,"crdt_grad_12":null,"crdt_grad_13":null,"crdt_grad_avg":4.62},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217_1","crdt_prdt_type":"2","crdt_lend_rate_type":"B","crdt_lend_rate_type_nm":"기준금리","crdt_grad_1":0.67,"crdt_grad_4":0.67,"crdt_grad_5":0.67,"crdt_grad_6":0.66,"crdt_grad_10":null,"crdt_grad_11":null,"crdt_grad_12":null,"crdt_grad_13":null,"crdt_grad_avg":0.67},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217_1","crdt_prdt_type":"2","crdt_lend_rate_type":"C","crdt_lend_rate_type_nm":"가산금리","crdt_grad_1":4.1,"crdt_grad_4":4.63,"crdt_grad_5":6,"crdt_grad_6":6.24,"crdt_grad_10":null,"crdt_grad_11":null,"crdt_grad_12":null,"crdt_grad_13":null,"crdt_grad_avg":4.22},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"SC001217_1","crdt_prdt_type":"2","crdt_lend_rate_type":"D","crdt_lend_rate_type_nm":"가감조정금리","crdt_grad_1":0.28,"crdt_grad_4":0.22,"crdt_grad_5":0,"crdt_grad_6":0.11,"crdt_grad_10":null,"crdt_grad_11":null,"crdt_grad_12":null,"crdt_grad_13":null,"crdt_grad_avg":0.27},{"dcls_month":"202102","fin_co_no":"0010002","fin_prdt_cd":"WR0002F","crdt_prdt_type":"3","crdt_lend_rate_type":"A","crdt_lend_rate_type_nm":"대출금리","crdt_grad_1":8.7,"crdt_grad_4":9.58,"crdt_grad_5":11.93,"crdt_grad_6":13.13,"crdt_grad_10":13.64,"crdt_grad_11":null,"crdt_grad_12":null,"crdt_grad_13":null,"crdt_grad_avg":10.67}]}}
결과변수
결과변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd**	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
crdt_prdt_type	대출종류 코드
crdt_prdt_type_nm	대출종류명
cb_name	CB 회사명
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
crdt_lend_rate_type	금리구분 코드
crdt_lend_rate_type_nm	금리구분
crdt_grad_1	900점 초과 [소수점 2자리]
crdt_grad_4	801~900점 [소수점 2자리]
crdt_grad_5	701~800점 [소수점 2자리]
crdt_grad_6	601~700점 [소수점 2자리]
crdt_grad_10	501~600점 [소수점 2자리]
crdt_grad_11	401~500점 [소수점 2자리]
crdt_grad_12	301~400점 [소수점 2자리]
crdt_grad_13	300점 이하 [소수점 2자리]
crdt_grad_avg	평균 금리 [소수점 2자리]
* 1회 조회 개수: 페이징 처리를 위한 1회 조회 제한 개수이며, 기본적으로 1회 조회 시 100개로 제한되지만 개인 사용자의 경우 관리자 판단에 의해 조절될 수 있다.

** Info와 연결되는 상품별 옵션 테이블 키값입니다.

응답메시지
응답메시지
No	응답코드	응답 메시지	설명
1	000	정상	정상적으로 처리되는 경우
2	010	미등록 인증키	등록되지 않은 인증키(auth)를 입력한 경우
3	011	중지된 인증키	중지 처리된 인증키(auth)를 입력한 경우
4	012	삭제된 인증키	삭제 처리된 인증키(auth)를 입력한 경우
5	013	샘플 인증키	샘플 인증키(auth)를 입력한 경우
6	020	일일검색 허용횟수 초과	개인의 경우로, 일일허용횟수를 초과하여 사용한 경우
7	021	허용된 IP가 아닙니다.	단체의 경우로, 인증키 신청시와 다른 IP를 사용한 경우
8	100	{요청변수ID} 누락	요청변수값을 입력하지 않은 경우
9	101	{요청변수ID}의 부적절한 값	부적절한 요청변수값을 사용한 경우
10	900	정의되지 않은 오류	Open API 서비스 내부 시스템 에러

