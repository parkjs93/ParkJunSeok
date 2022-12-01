import 'package:flutter/material.dart';
import 'package:study_flutter4/screen.dart';

//외부 플러그인 (webview 사용하기)
//1) pubspec.yaml에 cupertino_icons 하단에 pub.dev에서 복사한 내용 붙여넣줌
//2) Flutter/study_flutter4/android/app/build.gradle
// 하단의 defaultConfig의 minSdkVersion 20으로 변경 필요
//3) android-app-src-build.gradle의 compileSdkVersion 32로 변경
void main() {
  runApp(MaterialApp(
    home: HomeScreen(),
  ));
}
