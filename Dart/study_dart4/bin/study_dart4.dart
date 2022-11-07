import 'package:study_dart4/study_dart4.dart' as study_dart4;

void main(List<String> arguments) {
  print("=======method override=======");
  TimesTwo tt = new TimesTwo(2);
  print(tt.claculate());

  TimesFour tf = new TimesFour(3);
  print(tf.claculate());

  print("=======static=======");
  Employee em1 = new Employee("first");
  em1.bildingAndNamePrint();

  Employee em2 = new Employee("second");
  em2.bildingAndNamePrint();

  //class의 static 값 변경
  //static으로 선언된 변수, 함수는 클래스에 붙어서 사용한다.
  print("Employee static 값을 변경함");
  Employee.bilding = "unicore";
  Employee.bildingPrint();

  em1.bildingAndNamePrint();
  em2.bildingAndNamePrint();

  //인터페이스
  print("===========interface===========");
  exInterface1 ex1 = new exInterface1("park");
  ex1.printName();

  exInterface2 ex2 = new exInterface2("ohgo");
  ex2.printName();

  //abstract로 선언하여 아래와 같이 인스트럭트로 선언할 수 없다.
  //FirstInterface test = new FirstInterface("에러 나옵니다");

  print("===========getneric===========");
  Lecture<String, String> emLe1 = new Lecture("123", "park");
  emLe1.printType();

  Lecture<int, String> emLe2 = new Lecture(321, "oh");
  emLe2.printType();
}

///////////////////
//메소드 오버라이딩
//method : function (class 내부에 있는 함수)
// override : 덮어쓰다 (우선시하다)
class TimesTwo {
  final int number;

  TimesTwo(this.number);

  int claculate() {
    return number * 2;
  }
}

class TimesFour extends TimesTwo {
  //자식 생성자를 부모 생성자에 상속받아 넣는 과정
  TimesFour(int numbers) : super(numbers);

  //부모 클래스의 method를 가져와 덮어쓰기하여 사용
  @override
  int claculate() {
    //부모 클래스의 변수를 가지고 오기 때문에 super로 선언 (삭제해도 무방하나 써주는 것이 정석)
    //부모 메소드를 가져와서 자식 메소드에서 추가 작업 가능(this가 될 경우 무한루프에 빠짐)
    return super.claculate() * 2;
  }
}

///////////////////
///Static 키워드
class Employee {
  //static은 instance에 귀속되지 않고 class에 귀속된다.
  static String? bilding;
  String name;

  Employee(this.name);

  void bildingAndNamePrint() {
    print("name : $name, bilding $bilding");
  }

  static void bildingPrint() {
    print("bilding : $bilding ");
  }
}

///////////////////
///interface
///abstract : 추상적, 인스턴스로 만들 수 없다. 설계만 가능하다.
abstract class FirstInterface {
  String name;
  FirstInterface(this.name);

  void printName() {}
}

//인터페이스 사용 :implements
//시그니처 interface로 선언한 클래스 형태를 맞추어야 에러가 발생하지 않는다. (강제)
class exInterface1 implements FirstInterface {
  String name;
  exInterface1(this.name);
  void printName() {
    print("ex1 : $name");
  }
}

class exInterface2 implements FirstInterface {
  String name;
  exInterface2(this.name);
  void printName() {
    print("ex2 : $name");
  }
}

///////////////////
///generic - 타입을 외부에서 받을 때 사용
class Lecture<T, X> {
  final T id; //id의 변수 타입을 외부에서 받아서 결정한다.
  final X name; //string의 변수 타입을 외부에서 받아 결정한다.

  Lecture(this.id, this.name);
  void printType() {
    print(id.runtimeType);
    print(name.runtimeType);
  }
}
