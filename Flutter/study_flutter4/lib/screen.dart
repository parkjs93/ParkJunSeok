import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class HomeScreen extends StatelessWidget {
  WebViewController? controller;
  final homeUrl = 'https://terms.naver.com/entry.naver?docId=1112025&cid=40942&categoryId=32707';
  HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar( //상단의 appbar 생성
        backgroundColor: Colors.black,
        title: Text('study4'),
        centerTitle: true, //appbar 내에 텍스트 가운데 정렬
        actions: [
          //아이콘을 버튼으로 만드는 함수
          IconButton(onPressed: () {
            if(controller==null){
              return;
            }
            //http or https를 사용할 지에 따라 설정을 다르게 해야함
            //ios - runner - info.plist  맨 하당 </dict> 위에 <key>NSAppTransportSecurity</key>...</dict> 들여쓰기한 부분까지 입력
            //android - app -src - main - AndroidManifest.xml  <manifest ...> 이후 인터넷 권한 입력 : <uses-permission android:name ="android.permission.INTERNET"/>
            //
            controller!.loadUrl(homeUrl);
          }, icon: Icon(Icons.home,))
        ],
      ),
      body: WebView(
        //webview 컨트롤러 설정
        //webview가 생성될 때 : 컨트롤러를 함수에서 받을 수 있다. 마음대로 webview 마음대로 조종 가능
        //class 상단에 선언 필요
        onWebViewCreated: (WebViewController controller) {
          this.controller = controller;
        },
        initialUrl:
        homeUrl,
        //웹뷰를 띄웠을 때 어떤 사이트를 가장 먼저 띄울것인가
        javascriptMode:
        JavascriptMode.unrestricted, //웹 페이지의 자바스크립트 동작을 허용해주는 작업
      ),
    );
  }
}
