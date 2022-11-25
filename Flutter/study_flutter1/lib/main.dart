import 'package:flutter/material.dart';

void main() {
  runApp(
    //무조건 외워야 하는 사항
    //시작하는 것
    MaterialApp(
        home: Scaffold(
          backgroundColor: Colors.black,
          body: Center(
            child: Text('Park JS',
            style: TextStyle(
            color: Colors.white,
              fontSize: 20.0,
              ),
            ),
          ),
        ),
    ),
  );
}
