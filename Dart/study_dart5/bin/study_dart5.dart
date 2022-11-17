import 'package:study_dart5/study_dart5.dart' as study_dart5;

//Functional Programming (함수형 프로그래밍)
void main(List<String> arguments) {
  /////////List/////////
  List<String> parkjs = ['park', 'js', '93', '93'];
  print(parkjs);

  //Map으로 형변환하기 (asMap() : list에서 제공하는 함수)
  print(parkjs.asMap());

  //set으로 형변환하기 (toSet() : list에서 제공하는 함수)s
  print(parkjs.toSet());

  Map parkjsMap = parkjs.asMap();
  print(parkjsMap.keys.toList()); //Map의 key값을 리스트형태로
  print(parkjsMap.values.toList()); //Map의 value값을 리스트형태로

  //list를 set으로 변경하는 방법
  Set parkjsSet = Set.from(parkjs);
  print(parkjsSet.toList());

  final newParkjs = parkjs.map((e) => '9308$e');
  print(parkjs);
  print(newParkjs.toList());

  //.map으로 선언하여 새로운 List를 만들 경우 값이 같더라도 다른 리스트가 된다
  final newParkjs2 = parkjs.map((e) => '9308$e');
  print(newParkjs == newParkjs2);

  //문자열 리스트로 변경 후 문자 바꾼 뒤 리스트로 변경하기
  String numder = '13579';
  final parsed = numder.split("").map((e) => "$e.jpg").toList();
  print(parsed);

  /////////Map/////////
  //Map을 maping하기
  Map<String, String> name = {'park': '박', 'jun': '준', 'seok': '석'};
  final nameMap =
      name.map((key, value) => MapEntry("nameENG : $key", "nameKor : $value "));

  print(nameMap);

  //Map의 key값을 매핑하기
  final keys = name.keys.map((e) => 'key : $e').toList();
  final values = name.values.map((e) => 'values : $e').toList();
  print(keys);
  print(values);

  /////////set/////////
  ///set mapping하기
  Set nameSet = {'park', 'jun', 'seok'};
  final newName = nameSet.map((e) => 'set $e').toSet();
  print(newName);

  /////////where/////////
  List<Map<String, String>> namePeople = [
    {'name': 'parkjs', 'age': '93'},
    {'name': 'ohgaon', 'age': '23'},
    {'name': 'noname', 'age': '23'},
    {'name': 'noname2', 'age': '93'}
  ];
  //x['age'] == '93'의 결과가 true인 경우만 저장됨
  final namePeoplePrint = namePeople.where((x) => x['age'] == '93').toList();
  print(namePeoplePrint);

  /////////reduce/////////
  ///최초 1회 : prev에는 list의 첫번째 값이 할당됨 / next에는 2번째 값이 할당됨
  ///2회 : 1회 이후 returne된 prev + next 값이 prev 값이 된다.
  ///return 되어야 하는 값의 타입이 동일해야 한다.
  List<int> numbersReduce = [1, 3, 5, 7, 9];
  numbersReduce.reduce((prev, next) {
    print("==============");
    print('prev : $prev');
    print('next : $next');
    print('total : ${prev + next}');

    return prev + next;
  });

  ///위 내용과 동일한 상태, 표시 방법만 다름
  List<int> numbersReduce2 = [1, 3, 5, 7, 9];
  final reduceResult = numbersReduce2.reduce((prev, next) => prev + next);
  print(reduceResult);

  ///문자 붙이기
  List<String> words = ["name ", "parkjs ", "age ", "93"];
  final sentence = words.reduce((value, element) => value + element);
  print(sentence);

  /////////fold/////////
  ///return 된 값의 형태가 같지 않아도 사용 가능
  List<int> numbersFold = [1, 3, 5, 7, 9];
  //최초 1회 : 초기 값이 0으로 진행(시작값),  prev : 초기 값 , next : list의 첫번째 값
  //다음 2회 이후 : prev : 이전 리턴값, next : 다음 list의 값
  final foldSum = numbersFold.fold<int>(0, (prev, next) => prev + next);
  print(foldSum);

  List<String> wordsFold = ['name', 'parkjs', '93'];
  final resultWordFold = wordsFold.fold<String>(
      "", (previousValue, element) => previousValue + element);
  print(resultWordFold);

  final resultWordFoldLence = wordsFold.fold<int>(
      0, (previousValue, element) => previousValue + element.length);
  print(resultWordFoldLence);

  ///////cascading operator///////
  ///여러개의 리스트를 하나로 합치는 것
  ///...리스트명 => 완전히 새로운 리스트에 값을 풀어넣은 것
  List<int> even = [1, 2, 3, 4];
  List<int> odd = [5, 6, 7, 8];
  print([...even, ...odd]); // 리스트 두개 붙이기 ([...리스트1, ...리스트2])

  ///////실제 함수형 프로그래밍///////
  ///test + class Person 포함
  ///구조화 해서 다루는 방법
  final List<Map<String, String>> people = [
    {"name": "parkjs", "age": "30"},
    {"name": "ohgaon", "age": "22"},
    {"name": "who", "age": "NoData"}
  ];

  final parsePeople =
      people.map((e) => Person(name: e["name"]!, age: e["age"]!)).toList();
  //! 에러 없음을 강제로 처리하는 것

  print(parsePeople);

  //활용 예시1 : parsePeople의 갯수만큼 반복해서 name과 age 값 출력
  for (Person person in parsePeople) {
    print(person.name);
    print(person.age);
    print("=====");
  }

  //활용 예시2 : parsePeople 중 name이 parkjs인 항목 출력
  final parkjsName = parsePeople.where((element) => element.name == "parkjs");
  print(parkjsName);

  //한번에 선언하고 활용하기
  final resultPerson = people
      .map((e) => Person(name: e["name"]!, age: e["age"]!))
      .where((element) => element.name == "parkjs");

  print(resultPerson);
}

class Person {
  final String name;
  final String age;

  Person({required this.name, required this.age});

  @override //오버라이드 없이 그냥 출력했을 경우 parsePeople 출력 시 클래스 기본 값만 출력됨
  String toString() {
    return "Person(name:$name, age:$age)";
  }
}
