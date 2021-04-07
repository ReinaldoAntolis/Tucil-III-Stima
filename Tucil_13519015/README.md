# Tucil-III-Stima
-----------------
Implementasi algoritma A* untuk menentukan lintasan terpendek antara dua tempat pada peta

## General Info
-------------
Program menggunakan algoritma A* untuk menentukan lintasan terpendek antara dua tempat pada peta. 

Penjelasan directory :
* Folder src berisi source code
* Folder test berisi kasus uji
* Folder doc berisi laporan

## Setup
------
* Python : https://www.python.org/downloads/
* Flask : 'pip install flask'
* Folium : 'pip install folium'

## Features
* Menampilkan peta/graf 
* Mencari dan menampilkan lintasan terpendek beserta jaraknya antara dua tempat pada peta

## Cara menjalankan program
clone github
Command Prompt  -> change directory ke folder hasil clone github
                -> change directory ke src
                -> python Main.py
                -> input file kasus uji (terdapat pada folder test)
                -> input simpul asal
                -> input simpul tujuan
                -> jarak lintasan terpendek akan ditampilkan pada CLI
                -> copy url web lokal dan jalankan pada browser untuk menampilkan peta/graf dan lintasan terpendek

Web lokal       -> warna sisi   : biru = lintasan terpendek dari simpul asal menuju simpul tujuan
                                : abu-abu = sisi dari simpul-simpul yang bertetangga
                -> zoom in dan zoom out pada peta menggunakan scroll mouse
                -> click + drag untuk menggeser peta
                -> click simpul untuk menampilkan info nama dan koordinat simpul
                
## Status
Project is: _Complete_

## Author
Reinaldo Antolis
13519015

Rehagana Kevin Christian Sembiring
13519117