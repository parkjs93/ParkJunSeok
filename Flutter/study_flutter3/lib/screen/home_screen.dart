import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        bottom: false,
        child: Container(
          color: Colors.black,
          //현재 핸드폰의 사이즈 전체를 가져오는 방법
          //height: MediaQuery.of(context).size.height,
          //Column : 세로, Row : 가
          child: Row(
            //주축 정렬하기 (차지할 수 있는 공간을 모두 차지한다.)
            //spaceBetween - 위젯과 위젯의 사이가 동일하게 배치
            //spaceEvenly - 위젯을 같은 간격으로 배치하지만 끝에도 위젯이 아닌 빈 간격으로 시작
            //spaceAround - 위젯을 같은 간격으로 배치하고 끝과 끝에는 그 반 만큼의 빈 간격으로 시작,
            mainAxisAlignment: MainAxisAlignment.start,

            //CrossAxisAlignment : 반대축 정럴 (ex. 주축 : 가로, 반대축 : 새로)
            //baseline : 글자의 윗 부분
            //stretch : 강제로 최대한의 범위로 넓힌다
            crossAxisAlignment: CrossAxisAlignment.start,

            //max : 최대 사이즈로 세팅
            //min : 최소 사이즈로 세팅
            mainAxisSize: MainAxisSize.max,

            children: [
              //Expanded  /  Flexible : children 내에서만 사용할 수 있다.

              Expanded( //남은 부분을 Expanded 끼리 전체 차지한다.
                flex: 2,    //Expanded 중 비율을 변경
                child: Container(
                  color: Colors.pink,
                  width: 40.0,
                  height: 40.0,
                ),
              ),
              Expanded(
                child: Container(
                  color: Colors.red,
                  width: 40.0,
                  height: 40.0,
                ),
              ),
              Expanded(
                child: Container(
                  color: Colors.blue,
                  width: 40.0,
                  height: 40.0,
                ),
              ),
              Expanded(
                child: Container(
                  color: Colors.yellow,
                  width: 40.0,
                  height: 40.0,
                ),
              ),
              Flexible( //Expanded로 인해 할당 받은 범위 중 width, height 지정 범위 외는 빈 공간으로 둔다
                child: Container(
                  color: Colors.green,
                  width: 20.0,
                  height: 40.0,
                ),
              ),
            ],
          ),
        ),
      )
    );
  }
}