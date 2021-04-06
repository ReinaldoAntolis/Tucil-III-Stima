from flask import Flask

@app.route("/")
def index():
	return redirect("/web_scraping")