let express = require("express")
let app = express()

let index = require("./routers/index/index.js")

app.use ('/', index)

app.set('view engine', 'ejs')
app.set('views', './views')

app.listen(3000)