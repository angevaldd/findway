import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:syncfusion_flutter_maps/maps.dart';
import "package:latlong2/latlong.dart" as latlong;

class markerpage1 extends StatelessWidget {
  const markerpage1({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Map Project',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const markerpage(title: 'Findway'),
    );
  }
}

class markerpage extends StatefulWidget {
  const markerpage({super.key, required this.title});

  final String title;

  @override
  State<markerpage> createState() => _markerpageState();
}

class _markerpageState extends State<markerpage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        elevation: 5,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'add marker',
        child: const Icon(Icons.add),
      ),
      // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
