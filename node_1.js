let express = require("express")
let bodyParser = require("body-parser")
let app = express()

let index = require("./views/routers/index/index.js")

app.use('/', index)

app.use(bodyParser.urlencoded())
app.use(bodyParser.json())

app.set('view engine', 'ejs')
app.set('views', './views')

app.listen(8080)