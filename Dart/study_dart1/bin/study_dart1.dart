import 'package:study_dart1/study_dart1.dart' as study_dart1;

enum Status {
  approved, //승인
  pending,  //대기
  rejected  //거절
}

void main(List<String> arguments) {

  //////////////////*변수 선언 (변수명 중복 선언은 불가)*//////////////////
  var name = 'codefactoy';
  print(name);
  //변수 타입 출력
  print(name.runtimeType);
  
  //변수 타입
  //정수 integer
  int num1 = 10;
  print(num1);
  
  //실수
  // double
  double num2 = 1.2;
  print(num2);
  
  //참 거짓
  //boolean
  bool isTrue = true; //or false
  print(isTrue);
  
  //글자 타입
  //String
  String name1 = 'Parkjs';
  String name2 = "is";
  
  print(name1 + name2);
  print(name1 + ' ' + name2);
  // "" 내에 함수 사용하여 출력 할 때
  print('${name1} ${name2}');
  // "" 내에 변수 하나만 출력 할 때
  print("$name1 $name2");
  
  
  //////////////////*var*//////////////////
  // -> 자동으로 오른쪽, 값의 속성을 자동으로 설정
  // 데이터 값을 바꿈에 따라 데이터 타입을 변경 할 수 없음
  var vnum = 10;
  var vname = "parkjs";
  
  print(vnum);
  print(vname);
  
  //////////////////*dynamic : 어떠한 데이터 타입도 넣을 수 있다*//////////////////
  // var과 다른점 : 데이터 값을 바꿀 경우 데이터 타입도 변경 할 수 있음
  dynamic ddata = "park";
  print("${ddata} ${ddata.runtimeType}");
  
  ddata = 10;
  print("${ddata} ${ddata.runtimeType}");
  
  //////////////////*null*//////////////////
  //nullable : null이 될 수 있다. (?)
  //non-nullable : null이 될 수 없다. (!)
  //null : 아무런 값이 없다
  
  String sName = "박준석"; //non-nullable
  String? sName2 = null; //nullable (변수 타입 명에 ?를 넣어준다)
  
  print(sName!); // sName의 변수는 절대 null 값이 들어갈 수 없는 타입
  print(sName2);

  //////////////////*final, const : 일반적으로 변수를 선언 할 때 맨 앞에 선언*//////////////////
  // 변수를 선언한 이후 값을 변경할 수 없다.
  // 데이터 타입 생략도 가능
  final fName = "오가온 바보";
  const fName2 = "오가온 진짜 바보";
  //DateTime : 현재 시간 저장 
  DateTime now = DateTime.now();  //해당 줄의 코드가 실행되는 시간이 저장
  print(now);

  final DateTime now2 = DateTime.now();  //빌드 타임이 필요하지 않음
  print(now2);

  /*const*/ DateTime now3 = DateTime.now();  //절대적으로 빌드 타임이 필요함 (코드를 실행하는 시간을 알 수 없어서 error, 이 명령어가 어느 시간에 사용될 지 알 수 없음)
  print(now3);
  
  //////////////////*operater*//////////////////
  int oNum1 = 2;
  //기본 연산
  print(oNum1 % 2); // 나머지 값 구하기
  //값 1씩 증감
  oNum1++; //값 +1 하기
  oNum1--;

  double? oNum2 = 4.0;
  //값에 원하는 값 연산 후 재저장
  oNum2 += 1; // oNum2 값에 1을 더 해줌

  //??= : 만약 변수가 null이면 값을 바꾸기
  oNum2 = null;
  print(oNum2);
  oNum2 ??= 3.0;
  print(oNum2);

  //값 비교 ( < , > , <=, >=, ==, !=)
  print(oNum1 < oNum2);

  //타입을 비교 구문
  print(oNum1 is int); //oNum1의 변수 타입이 int 타입인지 확인해라 (bool)
  print(oNum2 is! int); //oNum2의 변수 타입이 int가 아닌지 확인해라

  //and 조건
  bool result = 12 > 10 && 1 > 0; // 둘 다 참일 때 True

  //or 조건
  bool result2 = 12 > 10 || 1 > 0;  // 둘 중 하나만 참이어도 True


  //////////////////*list*//////////////////
  ///List<데이터 타입> 리스트변수명 = [값,값,값];
  List<String> nameList = ["park", "jun", "seok"];
  List<int> numList = [10,9,78];

  print(nameList);
  print(numList);

  //List의 특정 인덱스의 값 출력
  print(nameList[0]);

  //List의 길이 (변수명.length)
  print(nameList.length);

  //List에 값 추가
  nameList.add("value");

  //List의 값 제거
  nameList.remove("value");

  //특정 값이 몇번째 인덱스에 존재하는지 알아내기 ( 변수명.indexof("값"); )
  print(nameList.indexOf("park"));

  //////////////////*map*//////////////////
  ///key / value (python의 딕셔너리와 비슷한 듯)
  
  Map<String, String> dictionary = {
    "parkjs":"30",
    "ohgaon":"22",
    "parkjs2":"32"
  };
  print(dictionary);

  Map<String, bool> isName = {
    "parkjs":true,
    "ohgaon":false,
    "parkjs2":true
  };
  //Map에 키와 값 추가하기
  isName.addAll({"othoer": false}); //1번
  isName["what"] = false;           //2번
  print(isName);

  //가져오고 깊은 값을 가져오는 법 (인덱스에 키 값 입력)
  print(isName["parkjs"]);

  //이미 저장된 키의 값을 변경하기
  isName["othoer"] = true;
  print(isName);

  //삭제하기
  isName.remove("othoer");
  print(isName);

  //키 또는 값만 출력하기
  print(isName.keys);
  print(isName.values);

//////////////////*Set*//////////////////
///리스트처럼 하나의 값만 저장할 수 있음. 리스트와 같으나 중복된 값을 넣을 수 없다.
 final Set<String> nameSet = {
  'code', 'python', 'java','js','code'
 };

  print(nameSet);

  //값 추가하기
  nameSet.add("C#");
  print(nameSet);

  //값 지우기 
  nameSet.remove("C#");
  print(nameSet);
  
  //값 유무 확인
  print(nameSet.contains("js"));

 
//////////////////*IF*//////////////////
  int numif = 4;

  if (numif % 3 == 0) {
    print("나머지 0");
  } else if(numif % 3== 1) {
    print("나머지 1");
  } else {
    print("나머지 2");
  }


//////////////////*switch*//////////////////
  int numSwitch = 3;
  switch (numSwitch % 3){
    case 0:
      print("0");
      break;

    case 1:
      print("1");
      break;

    default:  //if문의 else와 같은 역할
      print("2");
      break;
  }

//////////////////*for*//////////////////
///(시작 ; 조건 ; 증감)
 for (int i = 0 ; i < 10 ; i++){    //i가 0 부터 10보다 작을 때 까지 1씩 증가 시키며 반복
  print(i);
 }

 //리스트에 있는 값 모두 더하기 (방법 1)
 int total = 0;
 List<int> numfors = [1,2,3,4,5,6,7];
 for(int i = 0; i < numfors.length; i++) {
  total += numfors[i];
 }
 print(total);

//리스트에 있는 값 모두 더하기 (방법 2) 파이썬 for문이랑 비슷한 듯
 total = 0;
 for (int numfor in numfors) {
  total += numfor;
 }
 print(total);

 //////////////////*while*//////////////////
 ///조건을 먼저 확인 후 동작
 int total2 = 0;
 while (total2 < 10) {
  total2 += 1;
 }
 print(total2);

//break : 반복문 탈출
 int numWhile = 0;
 while (numWhile < 10) {
  numWhile+=1;
  if (numWhile == 5) {
    break;
  }
 }
 print(numWhile);

 int numFor = 0;
 for (int i = 0; i <10 ; i++) {
  numFor += 1;
  if (numFor == 5) {
    break;
  }
 }
 print(numFor);

//continue : 현재 루프만 건너띄기
 for (int i = 0; i < 10 ; i++) {
  if(i == 5){
    continue;
  }
  print(i);
 }

//////////////////*do while*//////////////////
///동작 먼저 실행 후 조건 판단 (사용 잘 안함)
 total2 = 0;
 do{
  total2+=1;
  } 
 while(total2 < 10);
 print(total2);

//////////////////*eNum*//////////////////
///main 함수 밖에 선언하여 사용해서 타입 설정, main 함수 이전에 선언
 Status status = Status.pending;
 if (status == Status.approved) {
  print("승인");
 } else if(status == Status.pending) {
  print("대기");
 } else {
  print("거절");
 }

//////////////////*함수 선언*//////////////////
int resultF1 = addNumbers(10, 2, 4);
resultF1 += addNumbers(1);
print("return : ${resultF1}");

int resultF2 = addNumbers2(5, z: 1, y: 10);
resultF2 += addNumbers2(1, y: 10);
print("return2 : $resultF2");


//////////////////*typedef 함수 선언*//////////////////
Operation oper = add;   //typedef로 선언한 Operation 타입에 해당되는 함수를 넣어줌 (대신 모든 데이터 타입의 형태가 같아야 한다.)
int result_oper = oper(10, 20, 30);
print (result_oper);

oper = subtract;
result_oper = oper(10, 20, 30);
print(result_oper);

int result_oper3 = calculator(10, 2, 3,subtract);
print(result_oper3);


} // main 함수의 끝



//세개의 숫자를 함수의 매개변수로 입력 받아 더하고 짝수인지 홀수인지 알려주는 함수
//함수 리턴 타입 (함수명 앞에 작성)
//parameter  /  argument - 매개변수
//positional parameter - 순서가 중요한 파라미터
//optional parameter - 있어도 되고 없어도 되는 파라미터 : 함수 선언 시 매개변수에 [] 표시 (대신 값이 없을 경우 계산이 안될때도 있기 때문에 기본 값을 넣어줘야 함)
int addNumbers(int x, [int y = 0, int z = 0]) {
  print("함수 로드");
  int sum = x + y + z;
  if (sum % 2 == 0){
    print("짝수임");
  } else {
    print("홀수임");
  }
  return sum; //반환 시킬 값 
}

//함수 리턴 타입 설정 (함수명 앞에 작성)
//named parameter - 이름이 있는 파라미터 (순서가 중요하지 않다)
//optional parameter 설정하기 - 해당 매개변수의 required 구문 지워버리면 가능
//positional parameter와 동시에 사용하려면 중괄호 앞부분에는 포지셔닝 파라미터 사용하면 가능
int addNumbers2(int x,{required int y, int z = 0}) {
  print("함수2 로드");
  int sum = x + y + z;
  if (sum % 2 == 0){
    print("짝수임");
  } else {
    print("홀수임");
  }
  return sum;
}

//arrow function - 화살표 함수
//addNumbers2 함수의 return sum과 같은 기능을 하는 구문 => 반환값 
int addNumbers3 (int x, {required int y, int z = 0})=> x + y + z; 


//////////////////*typedef 함수 선언*//////////////////
//signature
typedef Operation = int Function(int x, int y, int z);

int add(int x, int y, int z) => x+y+z;
int subtract(int x, int y, int z) => x-y-z;
int calculator(int x, int y, int z, Operation oper) {
  return oper(x, y, z);
}