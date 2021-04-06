from flask import Flask
import folium
from Main import *

app = Flask(__name__)

@app.route("/")
def index():
	# Mencari rata-rata posisi simpul
	avgLat = sum(node[0] for node in simpul)/len(simpul)
	avgLon = sum(node[1] for node in simpul)/len(simpul)

	# Membuka peta dengan titik tengah sesuai 
	# rata-rata posisi simpul
	map = folium.Map(
		location = [avgLat, avgLon], zoom_start = 10
	)

	# Menambahkan simpul pada peta
	for node in simpul :
		folium.Marker(tuple([node[0],node[1]])).add_to(map)

	for i in range (nodeCount) :
		for j in range(i, nodeCount) :
			tetangga = []
			if (matrix[i][j] != 0) :
				tetangga.append(tuple([simpul[i][0], simpul[i][1]]))
				tetangga.append(tuple([simpul[j][0], simpul[j][1]]))
				folium.PolyLine(tetangga, color="grey", weight=4, opacity=1).add_to(map)

	# koordinat = []
	# for node in simpul :
	# 	koordinat.append(tuple([node[0], node[1]])
	koordinat = []
	for node in shortestPath :
		koordinat.append(tuple([simpul[searchPos(node)][0], simpul[searchPos(node)][1]]))

	# Menampilkan lintasan terpendek
	folium.PolyLine(koordinat, color="blue", weight=4, opacity=1).add_to(map)

	return map._repr_html_()
	

if __name__ == '__main__':
   app.run()