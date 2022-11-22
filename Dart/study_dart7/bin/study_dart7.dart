import 'package:study_dart7/study_dart7.dart' as study_dart7;
//Stream 패키지 불러와야 함
import 'dart:async';

void main(List<String> arguments) {
  // [Future - await] : 하나에서 완료될 때 까지 하나의 값만 반환 받을 수 있다.
  //여러 순간에 여러번 받을 수 없다.

  //Stream : aysnc에서 사용하는 함수
  //flutter에서 가장 많이 사용
  //Stream : 실행 후 완료 순간을 지정할 수 있다.
  // yield를 통해 반환값을 지속적으로 받을 수 있다. Stream을 닫을 때 까지

  //stream을 가져오기 위해 선언
  final controller = StreamController();
  //final stream = controller.stream; //listen을 한번만 사용 할 수 있음

  final streamTwo = controller.stream.asBroadcastStream(); // lisen을 여러번 사용 가능

  //기본적인 방법 (1개)
  //listen 동안 첫번째 매개변수(함수) 실행
  /*
  final streamListener1 = stream.listen((val) {
    print("listen 1 : $val");
  });
  */
  //controller가 listen되는 동안 add라는 함수를 전달하는 것
  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);

  //여러번 listen을 하는 방법
  //1에서는 짝수만 (기능을 추가할 수 있다.)
  final streamTwoListener1 = streamTwo.where((e) => e % 2 == 0).listen((event) {
    print("Listen 1 : $event");
  });
  //2에서는 홀수만
  final streamTwoListener2 = streamTwo.where((e) => e % 2 == 1).listen((event) {
    print("Listen 2 : $event");
  });

  controller.sink.add(4);
  controller.sink.add(5);
  controller.sink.add(6);

  print("==============");

  calculate(1).listen((event) {
    print("calculate(1) : $event");
  });

  calculate(2).listen((event) {
    print("calculate(2) : $event");
  });

  print("==============");
  playAllStream().listen((event) {
    print(event);
  });
}

//yield가 실행될 때 마다 calculate 함수를 listening하고 있는 listener에 뿌려 줄 수 있다
Stream<int> calculate(int num) async* {
  for (int i = 1; i < 5; i++) {
    yield i * num;

    await Future.delayed(Duration(seconds: 3));
    //1초마다 출력
  }
}

Stream<int> playAllStream() async* {
  yield* calculate(3); //동시에 진행하지 않고 끝날 때 까지 다음 함수 시작되지 않음
  yield* calculate(100);
}
