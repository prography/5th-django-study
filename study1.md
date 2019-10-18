
# Tutorial 1: Serialization


## Model - Serializer 관계
1. 모델 생성
2. Serializer 에 모델/쿼리 전달
* serializer의 data 속성은 python dict

## 직렬화
content = JSONRenderer().render(serializer.data)

뷰 함수에서
return JsonResponse(serializer.data)

## 역직렬화
stream = io.BytesIO(content) # json 전달
data = JSONParser().parse(stream)
data를 Serializer에 전달하여 객체 인스턴스로 복원



# Tutorial 2: Requests and Responses

... (vscode)

format_suffix_patterns(urlpatterns)
이건 뭔지 모르겠다

