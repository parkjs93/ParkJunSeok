import 'package:study_dart3/study_dart3.dart' as study_dart3;

void main(List<String> arguments) {
  print("-------first--------");
  TestInheritance first = new TestInheritance(name: "fist", membersCount: 5);
  first.namePrint();
  first.membersPrint();

  print("-------extends first-------");
  FirstExtends firstExtend = new FirstExtends("parkjs", 93);
  //TestInheritance 클래스를 상속받았기 때문에 사용 가능
  firstExtend.namePrint();
  firstExtend.membersPrint();
  firstExtend.extendsPrint();

  print("-------extends second-------");
  SecondExtends secondEtend = new SecondExtends("Ohgaon", 01);
  secondEtend.namePrint();
  secondEtend.membersPrint();

  print("--------type comparison------");
  print(first is TestInheritance);
  print(firstExtend is TestInheritance);
  print(firstExtend is SecondExtends);

  print(secondEtend is TestInheritance);
  print(secondEtend is SecondExtends);
}

//상속 - inheritance
//부모 클래스의 모든 속성을 자식 클래스가 부여받는다.

class TestInheritance {
  String name;
  int membersCount;

  //네임드 파라미터 생성자 선언
  TestInheritance({required this.name, required this.membersCount});

  void namePrint() {
    print("name : ${this.name}");
  }

  void membersPrint() {
    print("members : ${this.membersCount}");
  }
}

//상속받는 클래스 생성 후 extends 상속받을 클래스 선언
class FirstExtends extends TestInheritance {
  //생성자 생성(파라미터 선언):super(부모클래스에서 받을 값 선언 부모:자식 )
  FirstExtends(String named, int membersCounted)
      : super(name: named, membersCount: membersCounted);

  //자식 클래스에서 선언한 함수 및 변수는 부모 클래스에서 사용할 수 없다.
  void extendsPrint() {
    print("FirstEntends print");
  }
}

class SecondExtends extends TestInheritance {
  SecondExtends(String named, int membersCounted)
      : super(name: named, membersCount: membersCounted);
}
