let express = require("express")
let bodyParser = require("body-parser")
let router = express.Router()

router.use(bodyParser.urlencoded())
router.use(bodyParser.json())

router.get('/', function(req, res){
    res.render('index')
})

router.post('/', function(req, res){
    let context = {}
    let email = req.body.email
    let password = req.body.password

    context.email = email
    context.password = password

    res.render('index2', context)
    console.log(email, password)
})

module.exports = router