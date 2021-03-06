'''
PYTHON Algorithm

입출력---------
\' : 작은따옴표 출력 => '
\" : 큰따옴표 출력 => "
\\ : 역슬래시 출력 => \
c = input() : c라는 변수에 키보드로 입력한 값을 대입, 기본값은 문자열!!!
c = int(input()) : 변수 c에 키보드로 입력한 값을 정수로 바꿔서 대입
c = float(input()) : 변수 c에 키보드로 입력한 값을 실수로 바꿔서 대입
a, b = input().split() : 입력된 값을 공백 기준으로 나누어 변수 a, b에 대입
print(c2, c1) : 변수 여러개를 쉼표를 기준으로 공백을 두고 출력
print(s, s, s) :한 줄에 공백을 두고 여러번 출력
input().split(':') : 입력 받은 값을 콜론 기호를 기준으로 자름
print(a, b, sep=':') : 콜론 기호를 사이에 두고 a와 b 출력
for i in range(len(s)):
    print(s[i])
        : s의 글자 수만큼 i번째 글자를 한 줄씩 출력
s[a:b] : s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분
print('%x' % n) : n을 16진수 소문자 형태 문자열('%x')로 출력
print('%o' % n) : n을 8진수 소문자 형태 문자열('%o')로 출력

연산----------
ord() : 유니코드 문자를 10진수 값으로 변환
chr() : 유니코드 문자(chracter)로 변환
print(-n) : n의 부호(+/-) 바꿔서 출력
print(w * int(n)) : 문자열 w를 n번만큼 출력
print(a ** b) : a를 b만큼 거듭제곱한 값 출력 (^ 아님 주의!)
print(a // b) : a를 b로 나눈 몫 출력
print(a % b) : a를 b로 나눈 나머지 출력
print(format(a, ".2f")) : 실수 a를 소수점 두 번째 자리(".2f")까지 반올림한 값 출력
비트시프트 연산
    실수에서는 허용되지 않음.
    print(n<<1) : 10을 2배 한 값인 20이 출력된다.
    print(n>>1) : 10을 반으로 나눈 값인 5가 출력된다.
    print(n<<2) : 10을 4배 한 값인 40이 출력된다.
    print(n>>2) : 10을 반으로 나눈 후 다시 반으로 나눈 값인 2가 출력된다.
print(bool(a)) : a가 0이면 False, 0이 아니면 True 출력
print(not a) : a가 False이면 반대인 True 출력, True면 False 출력
print(~ a) : a를 비트단위로 참/거짓을 바꾼 후 정수로 출력
print(a & b) : a와 b를 비트단위로 and 연산(둘 다 1인 부분의 자리만 1로 변경)한 후 그 결과를 정수로 출력
print(a | b) : a와 b를 비트단위로 or 연산(둘 중 하나라도 1인 자리를 1로 변경)한 후 그 결과를 정수로 출력
print(a ^ b) : a와 b를 비트단위로 xor 연산(서로 다를 때 1)한 후 그 결과를 정수로 출력
print(a if (a>=b) else b) : a와 b 중에 큰 값 출력
while문을 사용할 때 input을 받는다면, 처음 조건 검사를 통과하기 위한 값을 while문 앞에서 임의로 저장하기
print(ch, end = ' ') : 조건문을 돌면서 줄바꿈 없이 한 줄에 공백을 두고 출력
print(ch, end = '') : 조건문을 돌면서 줄바꿈 없이 한 줄에 공백을 없이 출력
n = int(input(), 16) : 입력되는 값을 16진수로 변환
'''