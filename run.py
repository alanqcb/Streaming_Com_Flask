from streaming_service import app

app.env = 'development'
app.debug = True
app.run(host="0.0.0.0")


