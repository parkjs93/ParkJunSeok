import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: HomeScreen()));
}

//Scaffold의 부분 = 스크린 화면 부분
// 그 부분을 클래스로 만들기, StatelessWidget을 상속받아 위젯을 생성할 수 있다.
// 핫리로드는 build 함수 내에 있는 내용만 핫리로드 가능하다.
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xff5a7a4b),
      body: Column(
        //자식 위젯 여러개 넣을 수 있음
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset(
            'asset/img/okhee.png',
          ),
          CircularProgressIndicator(
            color: Colors.white,
          ),
        ],
      ),
    );
  }
}
