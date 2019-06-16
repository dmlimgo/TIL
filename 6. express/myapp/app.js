let express = require("express")
let app = express()

app.get('/', function(req, res){
    res.send('welcome back!')
})

app.listen(3000)