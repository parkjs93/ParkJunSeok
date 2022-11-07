import 'package:study_dart2/study_dart2.dart' as study_dart2;

void main(List<String> arguments) {
  //Idol 클래스의 black 인스턴스 생성
  //생성자 선언을 했기 때문에 인스턴스 생성시 값을 넣어줘야 한다
  Idol black = new Idol("오가온", ['박', '준', '석']);

  //black.name = "박준석"; //클래스 내 변수를 final로 선언했기 때문에 값 변경 불가.
  print(black.name);
  print(black.members);
  black.sayHello();

  //클래스 Idol의 2번째 인스턴스 생성
  Idol yellow = new Idol('박준석', ['오', '가', '온']);

  print(yellow.name);
  print(yellow.members);
  yellow.sayHello();
  yellow.introduce();

  //named-constructor를 사용한 인스턴스 선언
  Idol blue = new Idol.formList([
    '박준석',
    ['박준석', '오가온', '어렵']
  ]);

  print(blue.name);
  print(blue.members);
  blue.sayHello();
  blue.introduce();

  //constructor를 const로 선언한 경우 red 인스턴스 선언 시 매개 변수 값을 변경할 수 없다.
  //const : 빌드 타임에 값을 알고 있어야 오류가 발생하지 않는다.
  Idol red = const Idol("red", ["1", "2", "3"]);

  print(red.name);
  print(red.members);
  red.sayHello();
  red.introduce();

  //const로 선언하지 않은 red2 인스턴스
  //red 인스턴스와 값은 같지만 값이 생성될 때 마다 값이 올라가기 때문에 다른 값이라고 함
  Idol red2 = new Idol("red", ["1", "2", "3"]);
  print(red == red2); //const로 선언하지 않아 false

  Idol red3 = const Idol("red", ["1", "2", "3"]);
  print(red == red3); // const로 선언하여 같은 인스턴스가 될 수 있다.

  //---------------------------------------------------------
  //getter, setter
  GetSetIdol getsetName =
      new GetSetIdol("getter", ["parkjs", "ohgaon", "list"]);

  print(getsetName.firstMember);
  getsetName.firstMember = "setter";
  print(getsetName.firstMember);
}

//class class명
//name (이름) -> 변수
//members (멤버들) -> 변수
//sayhello(인사) -> 함수
//introduce(자기소개)
class Idol {
  //클래스 내에 변수 생성
  //final로 선언하여 인스턴스 선언 때 입력한 값 이 외 값으로 변경할 수 없도록 한다 (중요!)
  final String name;
  final List<String> members;

  //생성자(constructor 선언)
  //방법 1.
  /*
  Idol(String name, List<String> members)
      : this.name = name, //this는 현재 클래스 내에 있음을 가리킴, this.name은 맨처음 선언한 name
        this.members = members; //생성자를 통해 받아온 매개 변수를 현재 클래스 내에 변수에 대입
  */

  //방법 2.
  //인스턴스 생성 시 받아온 값을 현재 클래스 내에 변수에 값을 저장한다. (간단하고 좋음)
  const Idol(this.name, this.members);

  //named-constructor 선언
  //기본 constructor과 동시에 사용이 가능하다.
  //class명.원하는이름()
  Idol.formList(List value)
      : this.name = value[0], //value 인덱스는 파라미터의 선언 위치로 보임,,, 그래서 네임드,,
        this.members = value[1];

  //클래스 내에 함수 생성
  void sayHello() {
    //this. -> 현재 클래스를 가리키는 것
    print("name 출력 : ${this.name}");
  }

  void introduce() {
    print("members 출력 : ${this.members}");
  }
}

//getter : 값을 가져올 떄 사용하는 것
//setter : 데이터를 설정 할 때 사용하는 것
//데이터를 간단하게 가공할 때 사용
class GetSetIdol {
  final String name;
  final List<String> menbers;

  GetSetIdol(this.name, this.menbers);

  void sayHello() {
    print("name : ${this.name}");
  }

  void introuduce() {
    print("members : ${this.menbers}");
  }

  //getter (String을 리턴해주는 getter이다.)
  String get firstMember {
    return this.menbers[0];
  }

  //setter : 하나의 파라미터만 설정 가능
  //main 함수에서 받은 값을 파라미터로 받게 되는 것
  // 클래스에서 변수를 선언할 때 대부분 final로 선언하여 변경할 수 없게 하지만
  // 리스트 값을 변경할 수 있어 자주 사용하지 않는다.
  set firstMember(String name) {
    this.menbers[0] = name;
  }
}
