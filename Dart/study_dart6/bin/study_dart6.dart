import 'package:study_dart6/study_dart6.dart' as study_dart6;

void main(List<String> arguments) {
  /////// 비동기 프로그래밍(Asynchronous Programming) ////////
  /// CPU 8코어 16쓰레드 / 쓰레드 : 프로그램을 실행하는 가장 작은 유닛
  /// 1 스레드 기준
  /// CPU는 하나의 함수를 하나의 작업만 가능하다.
  /// 서버를 요청할 경우 cpu를 사용하지 않지만 cpu 사용이 불가능하다.
  /// 비동기 프로그래밍을 통해 해결 가능
  /// 작업1이 cpu를 사용하지 않는 작업일 경우 작업1 동작하자마자 cpu사용 불가가 풀린다
  /// 작업1이 끝나지 않은 상태에서 작업2 시작 가능
  /// CPU를 효율적으로 사용하는 것

  /// Future - 미래
  /// 미래에 받아올 값
  Future<String> name = Future.value("parkjs");
  Future<int> number = Future.value(93);
  Future<bool> isTrue = Future.value(true);

  print("함수 시작");

  //2개의 파라미터
  //delay - 지연
  // 1번 파라미터 : 지연할 시간 (얼마나 지연시킬건지) Duration
  // 2번 파라미터 : 지연 시간이 지난 후 실행할 함수.
  Future.delayed(Duration(seconds: 2), () {
    print("Delay 끝");
  }); // -> 1번째 파라미터만큼 지연시킨 후 2번째 파라미터의 함수를 실행시킨다

  addNumbers(1, 2);
}

//계산 시작 후 계산된 결과가 계산 완료 보다 늦게 출력된다. (2초 대기하는 동안 다른 함수가 실행된다는 증거)
void addNumbers(int num1, int num2) {
  print('계산 시작');
  Future.delayed(Duration(seconds: 3), () {
    print("$num1+$num2");
  });
  print("계산 완료");
}
