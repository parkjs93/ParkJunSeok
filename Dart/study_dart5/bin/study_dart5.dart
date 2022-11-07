import 'package:study_dart5/study_dart5.dart' as study_dart5;

//Functional Programming (함수형 프로그래밍)
void main(List<String> arguments) {
  /////////List/////////
  List<String> parkjs = ['park', 'js', '93', '93'];
  print(parkjs);

  //Map으로 형변환하기 (asMap() : list에서 제공하는 함수)
  print(parkjs.asMap());

  //set으로 형변환하기 (toSet() : list에서 제공하는 함수)
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
}
