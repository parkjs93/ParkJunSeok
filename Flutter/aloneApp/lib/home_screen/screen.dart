import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.yellow,

      //최상단(시간, 배터리 등등)과 최하단(홈버튼바) 부분은 적용되지 않도록 하는 것
      body: SafeArea(
        child: Column(
          //화면 중앙에 출력
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              color: Colors.white,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Container(
                    width: 100,
                  ),
                  Container(
                    child: Text(
                      "OKHEE App",
                    ),
                  ),
                  Container(
                    width: 100,
                  )
                ],
              ),
            ),
            Container(
                width: 250.0,
                height: 250.0,
                child: Image.asset('asset/img/okhee.png')),
            Container(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Container(
                    child: Text(
                      "Park Jun Seok"
                    ),
                  ),
                  Container(
                    child: Text(
                      "Oh Ga On"
                    ),
                  )
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}
